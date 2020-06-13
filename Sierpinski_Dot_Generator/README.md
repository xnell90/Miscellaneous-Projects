# Sierpinski Dot Generator

<p align = 'justify'>
There is an interesting video that I saw from Youtube that talks about chaotic games. In that video,
it described the following algorithm to produce a drawing.
</p>

### The Algorithm of the Chaotic Game

1. Put three points on the plane so that it forms a triangle, and label the points A, B, and C.
2. Take a die and label two faces as A, two faces as B, and the remaining two faces as C.
3. Choose any point in the plane so that you have a seed point.
4. Roll the die.
5. Move the seed half the distance to the appropiately labeled vertex given by the die.
6. Repeat steps 4 and 5 as many times as you like.

<p align = 'justify'>
After watching the video, I decided to implement the above algorithm using Java. For my own exploration, I took three points 
so that it forms an equilateral triangle, place my seed point at the center of the triangle, and then repeated steps 4 and 5 
for more than 2000 iterations. By running the program, it produced an unusual shape. 
</p>

---
### How to run the script?

<p align = 'justify'>
If you are interested in running the code that I made, there are two files you need to download my java script.
</p>

 * Sierpinski.java 
 * and the StdDraw.java file. 

<p align = 'justify'>
Since the Sierpinski.java is dependent StdDraw.java, Sierpinski.java will not run if the StdDraw.java 
does not exist within the same directory as Sierpinski.java. For Macs:
</p>

 * Open terminal,
 * Go to the directory where both files are located,
 * Type javac Sierpinski.java to create a class file,
 * Then type java Sierpinksi to run the program.
---

### Result of The Construction

<p align="center">
  <img src="https://github.com/xnell90/Sierpinski_Dot_Generator/blob/master/Sierpinski.jpg"/>
</p>

<p align = 'justify'>
As you can see, this image represents the Sierpinski traingle. It is a fractal with the overall shape of an
equilateral traingle, subdivided recursively into smaller equilateral triangles. One thing interesting about
the Sierpinski triangle is that it is self similar. For example, if examine the lower right section of
the Sierpinski triangle, it looks similar to the entire Sierpinski triangle. One weird about the algorithm
which generated the image is that if you initialize your seed point anywhere in the plane, it still produces
the same image. I wonder why.
</p>
