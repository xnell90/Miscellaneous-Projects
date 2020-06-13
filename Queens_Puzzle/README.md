# The Eight Queens Puzzle

<p align = 'justify'>
Last summer, I was working as a STEM instructor at the Boys and Girls Club at Hudson County where I had to prepare lesson plans for the upcoming days. To be honest, it was pretty difficult to create engaging lesson plans and often times my classes where not very engaging to my middle school students. However, I came up with the idea of teaching the game of chess to my students for one week. As a result, I decided to teach the basic rules of chess to my students and let play against one another at the first day of the week. 
</p>

<p align = 'center'>
They loved the game! 
</p>

<p align = 'justify'>
All of my students where eager to play the game with their friends, so much so, by the time they moved to their next class, they were interested in playing the game rather than pay attention to their teacher. Given that my class ran successfully for the first time, I decided to introduce an old chesss puzzle the next day. It is as follows:
</p>

---

### Problem

Suppose that you have 8 chess queens and an 8 by 8 chess board. Is it possible to place 8 qeens on the board so that no two quens attack each other? In other words, can you place 8 queens on the board so that no two queens are on the same *row*, the same *column*, or same *diagonal*?

---

<p align = 'justify'>
When I first introduced this puzzle to my collegue, he tried to solve it on his own but failed in the attempt. I tried to solve it as well and it turns out I failed as well. It turns out that the problem itself seemed impossible to do, but I was able to come up with a solution by writing a simple python script.
</p>

### How to run the script?

If you are interested in seeing the solution to the 8 queens puzzle, you can simply download my python script and run it on your computer. For Macs:
 * Open terminal,
 * Go to the directory where 8_Queens_Solution.py is located,
 * Type python3 8_Queens_Solution.py.

### Solution
<p align = 'justify'>
Now back to how I solved the puzzle using python. After thinking about it for a while, I noticed that there is a bijective map between the placement of the 8 queens on the board, where no row has two queens, and all eight digit numbers where each digit is a number from 1 to 8. For example, let us suppose that you have the number 11118888, that corresponds to a board where on the first 4 rows there are 4 queens on the first column, and 4 queens on the eight column. Likewise, if I give you the following arrangement,
</p>

<p align="center">
  <img src="http://www.aiai.ed.ac.uk/~gwickler/images/8-queens-config.png"/>
</p>

<p align = 'justify'>
that board corresponds to the number 15263748 (row 1 has queen on the col 1, row 2 has queen on col 5,...). Naturally, we can try every 8 digit number, where each digit being a number from 1 to 8, and see which one will correspond to a solution. This brute force method is not efficient at all because you would have to look over 8^8 possible arrangements, so we need to find a better way to solve this problem. Let us look at the above picture and notice that it is a solution to the queens' puzzle. If you convert that to a number (as described before), that will correspond to an 8 digit number where each digit is pairwise unique. In other words, it is a permutation of all the integers from 1 to 8. By using this obersvation, we can try to look for every permuation of the numbers from 1 to 8 and check if it corresponds to a solution of the 8 queens puzzle. That way, you need to look over 8! possible arrangements, instead of 8^8 possible arrangements.
</p>

<p align = 'justify'>
By using this observation, I was able to write out the solution in python and give 92 possible ways of placing 8 queens on the board so that no two queens attack each other. Of course there are better ways to solve this problem, but I'll leave it at another time.
</p>
