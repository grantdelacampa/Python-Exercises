pyg = 'ay'

#the user input
original = raw_input('Enter a word:')

#connvert the word to lowercase to prevent
#odd capitalization
word = original.lower()

#first letter in the word
first = word[0]

#compounds the word with the first letter
#and the ending
new_word = word + first + pyg

#strips the last n-1 characters from the #word
new_word = new_word[1:len(new_word)]

#ensures the word is not null,
#and there are no numbers
if len(original) > 0 and original.isalpha():
  print new_word
else:
  print 'empty'