#!/usr/bin/env python3
for i in range(0, 10):
    for j in range(i + 1, 10):
        if(i == 8 and j == 9):
            print(f"{i:d}{j:d}")
        else:
            print(f"{i:d}{j:d}, ", end="")