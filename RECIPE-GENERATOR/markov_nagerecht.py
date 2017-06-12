#!/usr/bin/env python

import markovify

with open("NAGERECHT.txt") as f:
    text = f.read()

text_model = markovify.Text(text)

for i in range(8):
    print(text_model.make_sentence())
