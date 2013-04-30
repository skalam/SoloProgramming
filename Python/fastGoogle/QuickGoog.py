"""
Goal: return URL of first result for a phrase in Google
1. intake user input
2. process (i.e. remove "and" "or" etc., make all lowercase)
3. input into Google
4. sort through HTML (or whatever Google uses)
5. find first URL that came back in the search
6. return it as a string
"""
# excuse the varying styles for naming etc., I'm practicing with them
import urllib
from sys import argv
import sys
import os

script, filename = argv
"""
iw stands for "ignore words" -- the list of words that search engines
omit from user input when conducting searches. The engine will omit them
anyways, but this sounded fun to code.
"""


# file object of iw to be passed around
iwTarget = open(filename, 'r')
# reading file
iwRawWords = iwTarget.read()
# converting string of words into an array/list (whatever they are)
iwList = iwRawWords.split("\n")

input_word = raw_input("Enter search term: ")
input_list = input_word.split(" ")

# probably a built-in function for this, but I want loop practice
for word in input_list:
	if word in iwList:
		input_list.remove(word)

print input_list
penultimate_input = ' '.join(input_list)
final_input = penultimate_input.replace(' ', '+')
rawURL = "http://www.google.com/search?q=%&pws=0"
inputURL = rawURL.replace('%', final_input)

os.execl("C:\Users\Max\AppData\Local\Google\Chrome\Application\chrome.exe", "--new-window", inputURL)