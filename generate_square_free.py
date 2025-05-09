"""
Author: Alex Ma
This version: May 08, 2025
A suite of functions for generating and testing square-free words
"""

import random
import math

"""
Naive algorithm to test square-free-ness of a word. (Not the O(log log n) algorithm)
    Inv - any square in the word must only be at the very end. E.g. abb is OK, but abbc is NOT OK.
    @param word - the word to test for square-freeness
    @return (bool, int) - tuple containing
        [0] True if the string is square-free, False otherwise.
        [1] The number of characters at the end that are part of the ending square,
            possibly 0. (Remember that you can't string-slice str[:-0])
"""
def is_square_free(word):
    n = len(word)
    
    for r in range(n//2 + 1): # recall that range excludes the top!
        r += 1              # get it to start at 1 and end at n/2
        # Compare last r characters with last r to 2r characters.
        # Recall that the second index is exclusive
        if word[-r:] == word[-(2 * r):-r]:
            # print("r:", r, "n:", n, "\t MATCH")
            return (False, r) # use tuple, more efficient
        # else: # debug statement
            # print("r:", r, "n:", n, "\t not match")
    
    # We have passed all tests, can use all n elements
    return (True, 0)

'''
Function to generate a square free word of length n given a specific source word as a "seed"
For example, we might use "313213123" to generate a square free word by iterating over it
    @param seed the source "random" word
    @param n the length we need the string to be. NOTE THAT WE STOP AFTER 100,000 CYCLES
'''
def get_square_free_word_seeded(seed, n):
    max_length, longest_result = 0, "" # save the longest length word we've seen so far
    
    square_free_result = "" # empty word
    i = 0 # number of iterations
    ptr = 0 # ptr to the part of the seed we're using
    while (len(square_free_result) < n) and i < 2 * len(seed) and i < 100000:
        square_free_result += seed[ptr]
        i, ptr = i + 1, (ptr + 1) % len(seed) # increment iteration count and ptr (cyclic)
        #print(square_free_result)
        # dismiss any squares on right hand side of word
        (square_free, r) = is_square_free(square_free_result)
        
        # check if square-free
        if square_free == False:
            # if not then we have an r-square, delete the last r elements
            square_free_result = square_free_result[:-r]
        
        print(square_free_result)
        
        # if this is longer than longest known result, save it
        if len(square_free_result) > max_length:
            max_length, longest_result = len(square_free_result), square_free_result
    
    # iteration limit message
    if i >= 100000:
        print()
        print("You've reached the hardcoded 100,000 iteration limit. Contact me if you need it higher.")
    elif i >= 2 * len(seed):
        print()
        print("We used all characters in your seed string twice.")
        print("Appending %c to the output word"%(square_free_result[-1]),\
              "would make the word repeat %s."%square_free_result)

    return longest_result # the above is verified to return the longest

""" 
Function to get a square free word using a random letter/number generator from
alphabet of fixed size k.
    @param k the size of the alphabet we want
    @param n the length of the desired string
    @param alphabet_start can be any char, but suggested either "0" or "1" or "a" or "A"
        digits_0 starts ASCII indexing at 0
        digits_1 starts ASCII indexing at 1
        letters_a starts ASCII indexing at a
        letters_A starts ASCII indexing at A
"""
def get_square_free_word_unseeded(k, n, alphabet_start):
    max_length, longest_result = 0, "" # save the longest length word we've seen so far
    square_free_result = "" # empty word
    i = 0 # number of iterations

    # Append random characters
    while (len(square_free_result) < n) and i < 100000:
        # Append a random character from the correct range. Note that randint is INCLUSIVE
        square_free_result += str(chr(random.randint(alphabet_start, alphabet_start + k - 1)))
        i += 1
        #print(square_free_result)
        # dismiss any squares on right hand side of word
        (square_free, r) = is_square_free(square_free_result)
        
        # check if square-free
        if square_free == False:
            # if not then we have an r-square, delete the last r elements
            square_free_result = square_free_result[:-r]
        
        print(square_free_result)
        
        # if this is longer than longest known result, save it
        if len(square_free_result) > max_length:
            max_length, longest_result = len(square_free_result), square_free_result
    
    # iteration limit message
    if i >= 100000:
        print()
        print("You've reached the hardcoded 100,000 iteration limit.")

    return longest_result # the above is verified to return the longest

""" 
Function to check if square-freeness even exists
"""
def check_feasible(k, n):
    # Check if it's feasible to generate a length-n square-free word over alphabet of size k
    if (k < 1 or n < 1) or (k == 1 and n >= 2) or (k == 2 and n >= 4):
        print("Error: It is impossible to generate a square-free word longer than n=%d characters"%n,\
            "using only k=%d distinct source characters Either increase k, decrease n, or both."%k)
        quit()

# Code to count distinct charactes from GeeksForGeeks
# https://www.geeksforgeeks.org/count-the-number-of-unique-characters-in-a-given-string/
def cntDistinct(str):
    # created a empty dictionary over here
    count = {}
    for i in range(len(str)):
        # we are checking that if element already exist
        # we will be incrementing the count of element by 1
        if str[i] in count:
            count[str[i]] += 1
        # if exist in count then insert that element 
        # and initialize its count by 1
        else:
            count[str[i]] = 1
    return len(count)
 
# The source from which we generate a square free word
source ="1553454345452127135434312713245311165" # this is the pitch sequence for the Epitaph of Seikilos
try:
    source = str(input(">> Input a seed string, then press enter: "))
except(Exception):
    print("Error: Input error with seed string. Possible cause - must be a single line, no newlines within,"\
          "don't copy-paste text with multiple lines.")
    quit()
try:
    n = int(input(">> How long should the string be? Input a whole number, then press enter: "))
except(Exception):
    print("Error: Length of string needs to be a whole number. Or, you may have pasted in input with multiple lines for the seed string. Use one line only.")
    quit()

    
# If "random" was inputed for source, use random algorithm
if source.lower() != "random" and source.lower() != "rand":
    k = cntDistinct(source)

    # Check if it's feasible to generate a length-n square-free word over alphabet of size k
    check_feasible(k, n)
    
    # If feasible, proceed
    final_string = get_square_free_word_seeded(source, n)
else:
    # Get alphabet size and alphabet start character
    try:
        k = int(input(">> You indicated random. What size k should your alphabet be? "))
    except(Exception):
        print("Error: Please input a whole number >= 1.")
        quit()
    try:
        start = input(">> What character do you want the alphabet to start at? Press enter for default, 1. ")
        # Check if user wanted default, convert to a number
        if start == "":
            start = ord('1')
        else:
            start = ord(start)
    except(Exception):
        print("Error: Please enter a single character for alphabet start point.")
        quit()
    
    # Check if it's feasible to generate a length-n square-free word over alphabet of size k
    check_feasible(k, n)
    final_string = get_square_free_word_unseeded(k, n, start)

k_actual = cntDistinct(final_string)
print()
print("With seed", source)
print("The square-free string of max length was of length", len(final_string),\
      "with", k_actual, "distinct notes out of", k, "possible notes: ")
print(final_string)
