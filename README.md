[![Build Status](https://travis-ci.org/Layto888/Words-Analysis.svg?branch=master)](https://travis-ci.org/Layto888/Words-Analysis/)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
# words
Words analysis by Amardjia Amine.

https://github.com/Layto888/Words-Analysis

Free software utility which allows you to find the most frequent phrases
and frequencies of words. French and English language texts are supported.
It also counts number of words, characters, the lexical density,
sentences...etc.

Usage in command line:
```dos
>>> python words.py -f [filename.txt] -d [True/False]
>>> -h : for help.
```
Usage example:
```dos
>>> python words.py -f test.txt -d True
```
Output:
```dos
Number of different words: 101
Total number of characters: 842
Number of characters without spaces: 703
Number of spaces: 139
Sentence count: 8
Average sentence length (Words): 18.12
Max sentence length (Characters): 177
Min sentence length (Characters): 30
Lexical density: 27.59 %
Language: English

Top 10 recurring words:

# Ref                         Occurrence                    Perc
the                           11                            7.59 %
a                             6                             4.14 %
is                            5                             3.45 %
of                            5                             3.45 %
that                          4                             2.76 %
one                           3                             2.07 %
was                           3                             2.07 %
in                            3                             2.07 %
with                          3                             2.07 %
it                            2                             1.38 %

Elapsed time: 0.0144 [sec]
CPU process time: 0.0000 [sec]
Done.
```
