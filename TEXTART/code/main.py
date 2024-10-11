import art
import time
text = input('Write a word in English for drawing output: ')
font = input('Write the font of the text as in the example (block, rnd, rnd-small, rnd-medium, rnd-large, rnd-xlarge, wizard): ')
print('')
print(art.text2art(text, font=font))
print('(Fonts such as rnd, rnd-small, rnd-medium, rnd-large, rnd-xlarge choose any font with different sizes)')
print('(Made using the ART library in Python)')
print('The window will close automatically in a minute!')
time.sleep(60)
