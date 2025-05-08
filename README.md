# How To Use (I do not code)
1. Click here and follow the instructions: [Python Trinket](https://trinket.io/python3/3196758d83ba?outputOnly=true&runOption=run)
2. If the program terminates, press Run (top-left) again. (Trinket stops running on super large inputs — if you need that, you'll need to run this code somewhere else.)

# How To Use (I code)
Download the .py file and run it.

# Suggested Inputs
1. Enter seed `12341234` and length `14` to demonstrate the program.
2. Enter seed `1553454345452127135434312713245311165` with any length. This is the [Epitaph of Seikilos](https://en.wikipedia.org/wiki/Seikilos_epitaph) in scale degrees.
3. Enter seed `rand` or `random` and follow the instructions to get truly random square-free strings.

# Purpose
Here, a **word** is a finite[^***] string of characters, such as _abc_ or _123_. In this sense it's interchangeable with **string**.[^*]

A **[square-free word](https://en.wikipedia.org/wiki/Square-free_word)** is one that does not repeat patterns contiguously. For example, *aba* is OK because the *a*s are separated, but *abab* is not because the *ab*s are contiguous. Also, the square need not use up the entire word. For example, *caac* has a square *aa*, but neither *c* is part of it. The term **square** comes from algebra: one can write $$xx = x^2$$.

The program in this repository transforms a *specific* input string that uses $$k$$ characters (e.g. *abcbac* uses 3 characters — *a*, *b*, and *c*) into a *square-free* string of a length specified by the user (e.g. *abcbac* is 6 characters long).

The algorithm used is described by Rampersad, as paraphrased [in this paper](url), under "Preliminaries and the algorithm."[^**]

Here is the algorithm in full.

>In his WORDS'2013 lecture, Rampersad described the following algorithm to construct k-ary square-free words (the same algorithm was used in [1] to build words avoiding approximate squares). Starting with an empty word, one appends to its end one letter per round; the letter is given by a uniform random source. If the current word ends with an r-square, then one dismisses the right half of this square. The algorithm works until the constructed word reaches the required length n.

[^***]: Depending on the topic, words can also be infinite, like *3.1415926535...*. Let's focus on finite words.
[^*]: In some texts, the concept of a *word* is only defined in relation to a *language*. Loosely speaking, a language has rules to specify strings that are "in" or "out" of the language. A good example: "hello" is a word in English, but "hllelo" is not.
[^**]: I did not use Shur's algorithm, the main contribution in the paper. One would need to input a string with only *k - 1* characters to yield a string with *k* characters, but I needed to preserve cardinality of the alphabet. In particular, I needed to transform strings of musical pitches on some pitch class set (scale/key) into different strings of musical pitches on the very same pitch class set (scale/key). You probably could finagle a way to use Shur's algorithm if you wanted — let me know.
