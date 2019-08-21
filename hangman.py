#Hangman

import random
words = ["tomato", "python", "dalmation", "delicious", "sandwich", "refrigerator", "computer", "television", "reality", "dystopia"]
words_length = len(words)
words_index = random.randint (0, words_length)
rand_word = words[words_index]
print (rand_word)
length_rand_word = len(rand_word)
print ("_ " * length_rand_word) #Sets up Hangman game


guess = input("First letter! ")
if guess
