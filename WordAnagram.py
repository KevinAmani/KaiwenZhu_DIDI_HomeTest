#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Aug 12 14:14:47 2019

@author: kaiwen

Word Anagram
Requirements

Input: a set of input characters, ranging from a-z, case-insensitive.
Output: all the possible English words from the dictionary that could be composed of these characters, case-insensitive.
The possible English words could be fetched from, for example,  https://raw.githubusercontent.com/lad/words/master/words which is a copy of /usr/share/dict/words.
Ensure the main program can be run in https://coderpad.io/

"""

## Tree Node Class
class TreeNode:
    def __init__(self, end):
        self.end = end
        self.next = [None for _ in range(26)]


## Write the data from the file

class Anagram:
    
    def __init__(self):
        self.words = []
        self.WordsTree = self.CreateSearchTree()
    ## Create Search Tree to Save Words
    def CreateSearchTree(self):
        ## Create Search Tree
        WordsTree = TreeNode(False)
        ## Read File
        with open('words.txt','rt') as file:
            for line in file:
                ## Read lines
                line = line.lower().strip()
                temp_tree = WordsTree
                for n in range(len(line)):
                    position = ord(line[n])-97
                    if position>25 or position<0:
                        continue
                    end = False
                    if n == len(line)-1:
                        end = True
                    try:
                        if temp_tree.next[position] is None:
                            temp_tree.next[position] = TreeNode(end)
                        else:
                            if n== len(line)-1:
                                temp_tree = temp_tree.next[position]
                                temp_tree.end = end
                                break
                        temp_tree = temp_tree.next[position]
                    except:
                        print(line)
                        print(position)
                    
        return WordsTree
                    
    ## Input
    def GetPossibleWords(self,characters):
        ## case-insensitive
        characters = [letter.lower() for letter in characters]
        ## Create Tree
        
        pre = ""
        temp_tree = self.WordsTree
        self.TraverseTree(temp_tree,characters,pre)
    
    def TraverseTree(self,tree,characters,pre):
        if not characters:
            self.SearchWords(tree,pre)
        for node in range(len(tree.next)):
            if not tree.next[node]:
                continue
            if chr(node+97) in characters:
                temp_ch = list(characters)
                temp_ch.remove(chr(node+97))
            else:
                temp_ch = list(characters)
            temp_pre = str(pre)+chr(node+97)
            self.TraverseTree(tree.next[node],temp_ch,temp_pre)
            
                
    
    ## Append all possible words into result
    def SearchWords(self,tree,pre):
        if tree.end == True:
            self.words.append(pre)
        for node in range(len(tree.next)):
            if tree.next[node]:
                self.SearchWords(tree.next[node],pre+chr(97+node))
                
    def SetTree(self,tree):
        self.WordsTree = tree
        
    ## Test data
    def TestWordAnagram(self):
        self.words = []
        with open('testdata.txt','rt') as file:
            for line in file:
                line = line.strip()
                inputdata = line.split(' ')
                self.GetPossibleWords(inputdata)
                print(self.words)
                self.words = []
            
test = Anagram()
test.GetPossibleWords(['a','b','c','d','e'])
print(test.words)
test.TestWordAnagram()