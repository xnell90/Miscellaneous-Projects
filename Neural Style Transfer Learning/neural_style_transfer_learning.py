# # Neural style transfer

# ## Import Necessary Libraries

import argparse
import numpy as np
import tensorflow as tf
import time

from tensorflow.keras import Model
from tensorflow.keras.applications import VGG19
from tensorflow.keras.applications.vgg19 import preprocess_input
from tqdm import tqdm
from PIL.Image import fromarray

# ## Define Content Image and Style Image Paths
parser = argparse.ArgumentParser(description = 'Neural Style Transfer with TF 2.0')

parser.add_argument("c_image_path", type = str, metavar = "base_image_path",  help = "Path to Content Image.")
parser.add_argument("s_image_path", type = str, metavar = "style_image_path", help = "Path to Style Image.")
parser.add_argument("--new_image", type = str, default = 'stylized', required = False, help = "New Image Name.")

parser.add_argument("--iterations", type = int, default = 40, required = False, help = 'Iterations.')
parser.add_argument("--c_weight", type = float, default = 1e4, required = False, help = "Content Weight.")
parser.add_argument("--s_weight", type = float, default = 1e-2, required = False, help = "Style Weight.")
parser.add_argument("--tv_weight", type = float, default = 20.0, required = False, help = 'Total Variation Weight.')

args = parser.parse_args()
c_path = args.c_image_path #c = content
s_path = args.s_image_path #s = style

# ## Define Functions That Convert Images <-> Tensors

def image_to_tensor(image_path):
    max_dim = 1024
    image_tensor = tf.io.read_file(image_path)
    image_tensor = tf.image.decode_image(image_tensor, channels = 3)
    image_tensor = tf.image.convert_image_dtype(image_tensor, tf.float32)

    shape = tf.cast(tf.shape(image_tensor)[:-1], tf.float32)
    scale = max_dim / max(shape)

    new_shape = tf.cast(shape * scale, tf.int32)
    image_tensor = tf.image.resize(image_tensor, new_shape)
    image_tensor = image_tensor[tf.newaxis, :]

    return image_tensor

c_image = image_to_tensor(c_path) #c = content
s_image = image_to_tensor(s_path) #s = style

def tensor_to_image(tensor):
    tensor = tensor * 255
    tensor = np.array(tensor, dtype = np.uint8)

    if np.ndim(tensor) > 3:
        assert tensor.shape[0] == 1
        tensor = tensor[0]

    return fromarray(tensor)

# ## Define NST Model That Extracts Outputs From The Intermediate Layers (VGG19)

C_LAYERS = ['block5_conv2']
S_LAYERS = ['block1_conv1', 'block2_conv1', 'block3_conv1', 'block4_conv1', 'block5_conv1']

NUM_C_LAYERS = len(C_LAYERS)
NUM_S_LAYERS = len(S_LAYERS)

def vgg_layers(layer_names):
    vgg = VGG19(include_top = False, weights = 'imagenet')
    vgg.trainable = False

    outputs = [vgg.get_layer(name).output for name in layer_names]
    model = Model([vgg.input], outputs)

    return model

def gram_matrix(tensor):
    shape_tensor = tf.shape(tensor)
    num_of_terms = tf.cast(shape_tensor[1] * shape_tensor[2], tf.float32)
    result = tf.linalg.einsum('bijc,bijd->bcd', tensor, tensor)

    return result / num_of_terms

class StyleContentModel(tf.keras.models.Model):
    def __init__(self, s_layers, c_layers):
        super(StyleContentModel, self).__init__()

        self.vgg = vgg_layers(s_layers + c_layers)

        self.s_layers = s_layers
        self.c_layers = c_layers

        self.num_s_layers  = len(s_layers)
        self.vgg.trainable = False

    def call(self, inputs):
        #Expects float input in [0,1]
        outputs = self.vgg(preprocess_input(inputs * 255))

        s_outputs, c_outputs = (
            outputs[:self.num_s_layers],
            outputs[self.num_s_layers:]
        )

        s_outputs = [gram_matrix(s_output) for s_output in s_outputs]

        c_dict = {c_name:value for c_name, value in zip(self.c_layers, c_outputs)}
        s_dict = {s_name:value for s_name, value in zip(self.s_layers, s_outputs)}

        return {'c':c_dict, 's':s_dict}

extractor = StyleContentModel(S_LAYERS, C_LAYERS)
s_targets = extractor(s_image)['s']
c_targets = extractor(c_image)['c']
print("1) Loaded VGG19 Model ...")

# ## Define Style Loss, Content Loss, and Total Variation Loss

c_weight  = args.c_weight
s_weight  = args.s_weight
tv_weight = args.tv_weight # tv = total_variation

def content_loss(outputs):
    c_outputs = outputs['c']
    c_loss = tf.add_n(
        [
            tf.reduce_mean((c_outputs[name] - c_targets[name]) ** 2)
            for name in c_outputs.keys()
        ]
    )
    c_loss *= c_weight / NUM_C_LAYERS

    return c_loss


def style_loss(outputs):
    s_outputs = outputs['s']
    s_loss = tf.add_n(
        [
            tf.reduce_mean((s_outputs[name] - s_targets[name]) ** 2)
            for name in s_outputs.keys()
        ]
    )
    s_loss *= s_weight / NUM_S_LAYERS

    return s_loss

def total_variation_loss(image_tensor):
    return tv_weight * tf.image.total_variation(image_tensor)

# ## Define Training Step

image_tensor = tf.Variable(c_image)
parameters = {'learning_rate': 0.02, 'beta_1': 0.99, 'epsilon': 1e-1}
optimizer  = tf.keras.optimizers.Adam(**parameters)

def clip_0_1(image_tensor):
    return tf.clip_by_value(image_tensor, 0.0, 1.0)

@tf.function()
def train_step(image_tensor):
    with tf.GradientTape() as tape:
        outputs = extractor(image_tensor)
        loss  = content_loss(outputs)
        loss += style_loss(outputs)
        loss += total_variation_loss(image_tensor)

    gradients = tape.gradient(loss, image_tensor)
    optimizer.apply_gradients([(gradients, image_tensor)])
    image_tensor.assign(clip_0_1(image_tensor))

# ## Train And Display New Image
iterations = args.iterations
for _ in tqdm(range(iterations), desc = '2) Generating Stylized Image'):
    train_step(image_tensor)

new_image = args.new_image

print("3) Displaying Stylized Image ...")
stylized_image = tensor_to_image(image_tensor)
stylized_image.save(new_image + '.png')
stylized_image.show()
