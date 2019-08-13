# KaiwenZhu_DIDI_HomeTest
HomeTest_DIDI Word Anagram
## Word Anagram

### Requirements

1.Input: a set of input characters, ranging from a-z, case-insensitive.
2.Output: all the possible English words from the dictionary that could be composed of these characters, case-insensitive.
3.The possible English words could be fetched from, for example,  https://raw.githubusercontent.com/lad/words/master/words which is a copy of /usr/share/dict/words.
4.Ensure the main program can be run in https://coderpad.io/

### Deliverable

1.Submit your code to github.com and email us the link of your code repo, where the repo contains the following.
2.One source code file for the main program.
3.One runme.sh bash script to (compile and) run the program on Linux or Mac terminal.
[Optional] one README file with additional instructions, if needed.
[Bonus] one additional file with test cases.

## Algorithm

1. The program first reads the word.txt, and creates <b>Word Search Tree</b>.
2. Load the testdata.txt. Each line is input data set.
3. Use DFS to search relative words.
4. Print the answer

<b>This Algorithm is better than Force Burst.</b>


## Files Description

### WordAnagram.py

This is the main program.
There are two classes in this file.
<b>TreeNode</b> is the data structure for storing the dictionary.
<b>Anagram</b> is the main class for getting anwser.

There are fives methods in Anagram class.
#### CreateSearchTree
Load the words.txt and read each line. Add eah word into <b>Word Search Tree</b> with TreeNode class. The Word Search Tree will be saved in self.WordsTree.

#### GetPossibleWords
For solving the question. The input is char array. This function calls <b>TraverseTree</b>.

#### TraverseTree
This function is for traversing the tree and finding the subtree that is made up with input characters. When finding out a subtree that contains all characters, it will call SearchWords method.

#### SearchWords
This function is for add all words from subtree into self.words. Self.words is the result.

#### TestWordAnagram
Loard the testdata.txt and print all anwser.


## testdata.txt
It is the test file for saving test data.
each line is one test input.




