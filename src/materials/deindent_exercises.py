#!/usr/bin/env python

import re
import sys

with open(sys.argv[1], "r") as input:
    lines = input.readlines()

i = 0
while i < len(lines):
    if lines[i].startswith("> **Exercise"):
        while i < len(lines) and lines[i].startswith("> "):
            lines[i] = lines[i][2:]
            if not lines[i].startswith("> "):
                if lines[i].strip() == "```":
                    lines.insert(i + 1, "\n")
                    i += 2
                elif lines[i].startswith("```"):
                    lines.insert(i, "\n")
                    i += 2
                else:
                    i += 1
    else: i += 1


with open(sys.argv[2], "w") as output:
    for line in lines:
        output.write(line)
