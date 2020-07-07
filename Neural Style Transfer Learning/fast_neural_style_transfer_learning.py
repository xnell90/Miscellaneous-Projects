# # Neural style transfer

# ## Import Necessary Libraries

import argparse
import numpy as np
import tensorflow as tf
import tensorflow_hub as hub
import time

from tqdm import tqdm
from PIL.Image import fromarray

# ## Define Content Image and Style Image Paths
parser = argparse.ArgumentParser(description = 'Fast Neural Style Transfer with TF 2.0')

parser.add_argument("c_image_path", type = str, metavar = "base_image_path",  help = "Path to Content Image.")
parser.add_argument("s_image_path", type = str, metavar = "style_image_path", help = "Path to Style Image.")
parser.add_argument("--new_image", type = str, default = 'stylized', required = False, help = "New Image Name.")

args = parser.parse_args()
c_path = args.c_image_path #c = content
s_path = args.s_image_path #s = style

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

hub_module = hub.load('https://tfhub.dev/google/magenta/arbitrary-image-stylization-v1-256/1')
image_tensor = hub_module(tf.constant(c_image), tf.constant(s_image))[0]

new_image = args.new_image

stylized_image = tensor_to_image(image_tensor)
stylized_image.save(new_image + '.png')
stylized_image.show()
