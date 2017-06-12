# CookingWithMarkov.py

PROJECT:
  A generated cookbook/recipes with a script called Markov-Chain

  All the recipes that are to be found in the PDF File are generated by the python script Markov-Chain.
  I took the liberty to sometimes edit small pieces inside of the recipes to avoid repitition or 'unlogic' actions.

If you want to explore the markov chain further this is how it works:

EXPLANATION:
You can input texts of your choice inside the .txt file(s). The more texts the better, the .py script will then seek for relations between the sentences and words within the input it's given.
For this project it was necessary to create three different categories: 'VOORGERECHT' which is 'appetizer' in Dutch, 'HOOFDGERECHT' = main course and 'NAGERECHT' which is dessert.
The three different .txt files are filled with existing recipes from allrecipes.com. The python file then creates a new text with the amount of sentences you say it must produce.
This is editable in the line: for i in range(7): print(text_model.make_sentence()))
You can change the number in this line of code and this will determine how many sentences the script will give back

HOW TO RUN:
inside of your terminal go to the destinated folder like this
ex: cd /Users/maxwaelbers/Artez/Semester2/Digital-Media/RECIPE-GENERATOR 
ENTER

then run it like this: 
ex: python markov_nagerecht.py 



Max Waelbers
GD3A
ArtEZ Hogeschool voor de Kunsten,
Arnhem
