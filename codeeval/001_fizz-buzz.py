#!/usr/bin/env python

"""
Fizz Buzz

Challenge Description:

Players generally sit in a circle. The player designated to go first says the number "1", and each player thenceforth counts one number in turn. However, any number divisible by 'A' e.g. three is replaced by the word fizz and any divisible by 'B' e.g. five by the word buzz. Numbers divisible by both become fizz buzz. A player who hesitates or makes a mistake is either eliminated.

Write a program that prints out the the pattern generated by such a scenario given the values of 'A'/'B' and 'N' which are read from an input text file. The input text file contains three space delimited numbers i.e. A, B, N. The program should then print out the final series of numbers using 'F' for fizz, 'B' for 'buzz' and 'FB' for fizz buzz.

Input sample:

Your program should read an input file (provided on the command line) which contains multiple newline separated lines. Each line will contain 3 numbers which are space delimited. The first number is first number to divide by ('A' in this example), the second number is the second number to divide by ('B' in this example) and the third number is where you should count till ('N' in this example). You may assume that the input file is formatted correctly and is the numbers are valid positive integers.e.g.

    3 5 10
    2 7 15
Output sample:

Print out the series 1 through N replacing numbers divisible by 'A' by F, numbers divisible by 'B' by B and numbers divisible by both as 'FB'. Since the input file contains multiple sets of values, your output will print out one line per set. Ensure that there are no trailing empty spaces on each line you print.e.g.

    1 2 F 4 B F 7 8 F B
    1 F 3 F 5 F B F 9 F 11 F 13 FB 15
"""

import sys


if __name__ == '__main__':
    with open(sys.argv[1]) as f:
        for line in f:
            A, B, N = list(map(int, line.split()))
            output = []
            
            for i in range(1, N + 1):
                if i % (A * B) == 0:
                    output.append('FB')
                elif i % A == 0:
                    output.append('F')
                elif i % B == 0:
                    output.append('B')
                else:
                    output.append(str(i))
            
            print(' '.join(output))
