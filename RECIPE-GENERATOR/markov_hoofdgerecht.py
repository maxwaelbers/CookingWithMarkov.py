#!/usr/bin/env python

import markovify

with open("HOOFDGERECHT.txt") as f:
    text = f.read()

text_model = markovify.Text(text)

for i in range(12):
    print(text_model.make_sentence())
