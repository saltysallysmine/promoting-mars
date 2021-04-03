from sys import stdin
from pprint import pprint

qw = []
for line in stdin:
    qw.append(f"<h4>{line.capitalize()}</h4>")
[print(el, end='') for el in qw]
