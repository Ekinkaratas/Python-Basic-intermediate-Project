## **Part 3** 

### *Chapter 1*

- **numbers.py**  
  The program prints out all integer numbers greater than zero but smaller than the input.

- **powers_OF_N.py**  
  Modify powers_OF_Two so that the user can also enter the multiplied base (in powers_OF_Two the base is always 2).

- **powers_OF_Two**  
  I wrote a program that asks the user for an upper limit and prints the powers of 2 starting from 1 and doubling each time. The program stops before or when it reaches the limit.

- **print_Numbers**  
  I wrote a program that prints all even numbers from 2 to 30 using a loop. Each number will be printed on a separate line.

- **The_Sum_OF_Consecutive_Numbers**  
  I wrote a program that asked the user to type in a limit, calculated the sum of consecutive numbers (1 + 2 + 3 + ...) until the sum was at least equal to the limit, and printed both the result and the calculation performed.

### *Chapter 2*

- **A_Framed_Word**  
  I wrote a program that asks the user for a string and prints it out inside a frame of * characters. The width of the frame is 30 characters.

- **A_Line_OF_Hashes**  
  I wrote a program that asks the user for a width and then prints out a line of hash (#) characters with the specified width.

- **A_Rectangle_OF_Hashes**  
  I modified the A_Line_OF_Hashes program to ask for both the width and height. It will then print a rectangle of hash (#) characters with the specified dimensions. 

- **Does_It_Contain_Vowels**  
  I wrote a program that asks the user to input a string and then checks if the string contains any of the vowels a, e, or o. Depending on whether any of these vowels are found, it prints out different messages.

- **End_TO_Beginning**  
  I wrote a program that asked the user for a string and then printed out the string in reversed order, with each character on a separate line.

- **Find_All_The_Substrings**  
  I wrote a program that asks for a string and a character. It then prints all substrings that are at least three characters long and start with the specified character.

- **Right_Aligned**  
  I wrote a program that asks the user for a string and then prints it out so that exactly 20 characters are displayed. If the input is shorter than 20 characters, the beginning of the string is filled with * characters.

- **Second_AND_Second_To_Last_Characters**  
  I wrote a program that asked the user for a string and then printed out a message based on whether the second character and the second-to-last character are the same or not.

- **String_Multiplied**  
  I wrote a program that asked the user for a string and an amount, then printed the string as many times as specified by the amount, all on one line without any extra spaces or symbols.

- **Substrings_Part_1**  
  I wrote a program that asks the user to type a string and then prints all substrings starting from the first character to the last character.

- **Substrings_Part_2**  
  I wrote a program that asks for a string and then prints all substrings from the last character to the first character.

- **The_Longer_String**  
  I wrote a program that asked the user for two strings of characters and printed the longer one. If the strings were of equal length, the program printed “Strings of equal length”.

- **The_Second_Occurrence**  
  I wrote a program that finds the second occurrence of a substring in a given string. If there is no second occurrence, it prints a message indicating so. The program ensures that the occurrences don't overlap.

- **Underlining**  
  I wrote a program that repeatedly asks the user for strings using a loop, printing each string with an underline. The program stops when the user enters an empty string.

### *Chapter 3*

- **Factorial**  
  I wrote a program that asks the user for an integer. If the number is 0 or negative, the program terminates. Otherwise, it prints the factorial of the number (the product of all positive integers up to that number). For example, 5! = 1 × 2 × 3 × 4 × 5 = 120.

- **First_Letters_OF_Words**  
  The program then prints out the first letter of each word in the sentence, each letter on a separate line.

- **Flip_THE_Pairs**  
  The program prints out all the positive integer values from 1 up to the number. However, the order of the numbers is changed so that each pair of numbers is flipped. That is, 2 comes before 1, 4 before 3 and so forth.

- **Multiplication**  
  The program prints out a list of multiplication operations until both operands reach the number given by the user.

- **Taking_Turns**  
  The program prints out the positive integers between 1 and the number itself, alternating between the two ends of the range.

### *Chapter 4*

- **The first character**  

  The exercise summarizes the first_character function. I make it print the first character of the string it receives.  

- **Mean**  

  I wrote a function called mean, which takes three integer arguments. Then, I calculated the arithmetic mean by dividing the sum of these three numbers by three. Finally, I printed the result on the screen.  

- **Print many times**  

  I wrote a function called print_many_times which takes a text and a number. Then, I printed the text on the screen for the given number of times.  

  Then, I created an infinite loop. I asked the user to enter a text. If the user entered “1”, I exited the loop. Otherwise, I took a repeat number from the user and tried to convert it to an integer. If I succeeded, I called the print_many_times function and printed the text on the screen for the specified number of times. If the user entered an invalid input, I printed the message “Please try again.” on the screen.  

- **Chessboard**  

  When writing this code, I asked the user for a number and generated a chessboard pattern accordingly. If the number was less than 1, I terminated the program. If it was equal to 1 or the input was not valid, I asked the user to try again.  

  In the first solution, I created the rows by setting the start value according to the row number. In the alternative solution, I used a while loop to print both rows in sequence.  

- **A word squared**  

  I wrote a function called chessboard, which takes a text and a length value. First, I calculated the length of the text. Then, I created as many rows as the given length. In each row, I printed a repeating square pattern, taking the characters of the text in order. When writing each character in the row, I was careful not to exceed the length of the text and I cyclically changed the indices.  

  Then, I created an infinite loop. I asked the user to enter a text. If the user typed “1”, I exited the loop. Otherwise, I took a square size input from the user and tried to convert it to an integer. If I succeeded, I called the chessboard function and printed the pattern on the screen. If the user entered an invalid input, I printed the message “Please try again.”  

## **Part 4**

### **Chapter 1**

- **A Square**

  While writing this code, I aimed to create a square pattern with a word entered by the user.

  I defined the square function, repeated the word for the specified length and printed it on the screen. I took input from the user with a while True loop. If the user entered “1”, I ended the loop with break.

  I converted the length entered by the user to int. In case of incorrect input, I caught ValueError and gave a warning, if correct, I called the square function and printed the square on the screen.

- **A Triangle**

  While writing this code, I aimed to create a triangle shape with a word entered by the user.

  In the triangle function, I used a loop to create the triangle. I put “ ” at the beginning of each line and centered the shape by adding a space with *(length - i). Then I repeated the word up to (2 * i - 1) to expand the triangle.

  I created the main loop with while True and took input from the user. If the user entered “1” I ended the loop with break. I converted the length to int, if the input was wrong I caught ValueError and gave a warning, if it was correct I called the triangle function and printed the triangle on the screen.

- **Shape**

  While writing this code, I aimed to create a shape with two words and two numbers specified by the user.

  In the shape function, I used the first number to print the word as a triangle on the screen. For i in range(1, number_1+1, 1) loop, I created a pattern by increasing the number of repetitions of the word in each line.

  I created the main loop with while True and received input from the user. For y in range(number_2) I added lines repeating the second word as many times as number_1.

  I took two numbers and two words input from the user and called the shape function. If the input was incorrect, I caught ValueError and gave a warning.

- **A Spruce**

  When writing this code, I aimed to create a spruce tree shape with the length specified by the user.

  First, I defined the spruce function and printed the message “a spruce!” to the screen before drawing the tree. Then, I created the trunk of the tree by looping for i in range(1, length+1, 1). I centered the shape by adding a space at the beginning of the line and repeated the stars until (2*i - 1).

  For the trunk of the tree, I placed a star at the bottom using print(“ ‘ * (length-2), ’*”).
  I set up the main loop with while True and take the length input from the user. If the user enters zero or a negative number, I end the loop with break. In case of incorrect input, I catch ValueError and give a warning.

- **The Greatest Number**

  When writing this code, I aimed to find the largest of the three numbers entered by the user.

  In The_Greatest_Number function, I first set the variable max and compare it with the other numbers to find the largest value. If all numbers are equal, I print the message “All numbers equal”, otherwise I print the message “Largest number {max}”.

  In the main loop, I exit if the user enters a zero or negative number, otherwise I get three numbers and call the function. I give a warning for incorrect input.

- **Same characters**

  When writing this code, I wanted to check if the two indexes specified by the user have the same letter.
  In the same_chars function, I compare the characters in the given index_1 and index_2 and print the message “indexes have the same letter” if they have the same letter, or “indexes haven't the same letter” if they are different.

  In the main loop, I exit if the user enters '1'. I get a word and two indexes from the user and call the same_chars function. In case of incorrect input, I catch ValueError and give a warning.

- **First, second and last words**