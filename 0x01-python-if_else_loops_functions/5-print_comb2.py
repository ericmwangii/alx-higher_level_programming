#!/usr/bin/env python3
for i in range(0, 100):
    if i == 99:
        print(f"{i:d}")
    else:
        print(f"{i:02}", end=", ")
