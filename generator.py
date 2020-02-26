#!/usr/bin/env python3

print(''.join(sorted([character.upper() if index % 2 == 0 else character.lower() for index, character in enumerate(input().lower())], reverse=True)))