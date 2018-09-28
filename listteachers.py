#!/usr/bin/env python
import sys
from bs4 import BeautifulSoup

if(len(sys.argv) < 2) :
  print('USAGE:',sys.argv[0],'[FILE]','[PARSER]')
  exit();
f = open(sys.argv[1], 'r')
html = f.read();
parser = 'html.parser' if len(sys.argv) < 3 else sys.argv[2]

soup = BeautifulSoup(html, parser)
tables = soup.findAll('table')

classes = []
for c in range(0, len(tables)):
  classes.append(tables[c].text.strip().split('\n'))

names = []
periods = []
teachers = []

for c in range(1, len(classes)):
  names.append(classes[c][0])
  periods.append(classes[c][1])
  teachers.append(classes[c][2])

print(names)
print(periods)
print(teachers)
