# for testing functionality without the discord bot
strr = ''

from chatbot import Morty
x = Morty()

while True:
	strr = input('Enter text: ')
	if strr == 'q':
		break
	print(x.predict(strr))

