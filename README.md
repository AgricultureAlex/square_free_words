# Purpose
Here, a **word** is a finite string of characters, such as _abc_ or _123_. In this sense it's equivalent to a **string**. (In some texts, the concept of a *word* is only defined in relation to a *language*, which is a set of rules specifying which strings are valid, by analogy with "word" but not "wrod" in English.)

This repository contains a program to generate or manipulate square-free words. There are other, more useful projects, but this fills one use case -- if you want to transform a *specific* string with $$k$$ characters into a *square-free* string with *k* characters.

The algorithm used is the simple one by Rampersad described [in this paper](url), under "Preliminaries and the algorithm." I did not use the modified algorithm provided as the main contribution in that paper because it requires a string with $$k - 1$$ characters to transform into $$k$$, and I needed to preserve cardinality of the alphabet. In particular, I needed to transform strings of musical pitches on some pitch class set (scale/key) into different strings of musical pitches on the same pitch class set (scale/key).

Here is the algorithm in full

>In his WORDS'2013 lecture, Rampersad described the following algorithm to construct k-ary square-free words (the same algorithm was used in [1] to build words avoiding approximate squares). Starting with an empty word, one appends to its end one letter per round; the letter is given by a uniform random source. If the current word ends with an r-square, then one dismisses the right half of this square. The algorithm works until the constructed word reaches the required length n.

# How To Use (I code)
Download the .py file and run it.

# How To Use (I do not code)
1. Go to onlinegdb.org
2. Click the dropdown menu on the top-right to select Python 3
3. Delete the placeholder code
4. Copy the text of the .py file into your clipboard and paste it into the code field
5. Click the green "Run" button at the top left.
6. Follow the prompts as given in the black command field at the bottom, entering text and pressing enter as requested.
