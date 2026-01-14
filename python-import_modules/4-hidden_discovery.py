#!/usr/bin/env python3
import hidden_4

if __name__ == "__main__":
    
    names = dir(hidden_4)
    names_alpha = sorted(names)
    for name in names_alpha:
        if name.startswith("__"):
            continue
        print(name)
