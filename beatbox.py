#!/usr/bin/python3
# bytebox.py

t = 0
while True:
    print(chr(int( t) % 256 ), end='')
    t += 1
