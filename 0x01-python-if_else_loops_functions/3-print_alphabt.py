#!/usr/bin/python3
for c in range(97, 123):
    if (c == 101) | (c == 113):
        continue
    print("{}".format(chr(c)), end="")
