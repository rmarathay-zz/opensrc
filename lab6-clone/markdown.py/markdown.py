"""
 Markdown.py
 0. just print whatever is passed in to stdin
 0. if filename passed in as a command line parameter,
    then print file instead of stdin
 1. wrap input in paragraph tags
 2. convert single asterisk or underscore pairs to em tags
 3. convert double asterisk or underscore pairs to strong tags

"""

import fileinput
import re

def convertStrong(line):
  line = re.sub(r'\*\*(.*)\*\*', r'<strong>\1</strong>', line)
  line = re.sub(r'__(.*)__', r'<strong>\1</strong>', line)
  return line

def convertEm(line):
  line = re.sub(r'\*(.*)\*', r'<em>\1</em>', line)
  line = re.sub(r'_(.*)_', r'<em>\1</em>', line)
  return line

def convert1(line):
    line = re.sub(r'\#(.*)', r'<h1>\1</h1>',line)
    line = re.sub(r'_(.*)', r'<h1>\1</h1>', line)
    return line

def convert2(line):
    line = re.sub(r'\#\#(.*)', r'<h2>\1</h2>',line)
    line = re.sub(r'_(.*)', r'<h2>\1</h2>', line)
    return line

def convert3(line):
    line = re.sub(r'\#\#\#(.*)', r'<h3>\1</h3>',line)
    line = re.sub(r'_(.*)', r'<h3>\1</h3>', line)
    return line

def convert4(line):
    line = re.sub(r'>(.*)', r'<blockquote>\1</blockquote>',line)
    line = re.sub(r'__(.*)__', r'<blockquote>\1</blockquote>>', line)
    return line

for line in fileinput.input():
  line = line.rstrip()
  line = convert4(line)
  line = convertStrong(line)
  line = convertEm(line)
  line = convert3(line)
  line = convert2(line)
  line = convert1(line)
  # line = convert2(line)
  print '<p>' + line + '</p>',
