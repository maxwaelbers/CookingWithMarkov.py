#!/usr/bin/env python

import markovify

with open("VOORGERECHT.txt") as f:
    text = f.read()

text_model = markovify.Text(text)

for i in range(7):
    print(text_model.make_sentence())
