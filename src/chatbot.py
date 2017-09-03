import random

class Maps():
	def __init__(self, i, list):
		self.i = i
		self.list = list

	def is_key(self, i):
		return self.i == i

	def get_msg(self):
		return random.choice(self.list)


class MyClassifier():
	def fit(self, features, replies):
		self.features = features
		self.replies = replies

	def find_string_in_test(self, msg):
		# print ("Current msg: {0}".format(msg))
		maxMatch = 0
		maxLength = 0
		for i in range(0, len(self.features)):
			strr = self.features[i].lower()
			if strr in msg.lower():
				# if bad word set it as reply and exit from loop
				if self.replies[i] == -1:
					maxMatch = i
					maxLength = len(strr)
					break

				if len(strr) > maxLength:
					# print ("strr: " + strr)
					maxMatch = i
					maxLength = len(strr)
		if maxLength > 0:
			return self.replies[maxMatch]

	def predict(self, test):
		predictions = []
		for msg in test:
			reply = self.find_string_in_test(msg)
			predictions.append(reply)
		return predictions


import pandas

class Morty():
	def __init__(self):
		url = './chat.data'
		names = ['content', 'reply']
		dataset = pandas.read_csv(url, names=names).values
		features = dataset[:, 0]
		replies = dataset[:, 1]
		self.clf = MyClassifier()
		self.clf.fit(features, replies)

		self.maps = []
		self.maps.append(Maps(0, ['Yooooo!', 'Hello!', 'Hello there!', 'What\'s up?']))
		self.maps.append(Maps(1, ['Byeee!', 'See ya in another life brother!', 'Goodbye!']))
		self.maps.append(Maps(-1, [':eyes:', 'Language!', 'You don\'t have to swear!', 'Don\'t talk like that!', 'Stop that!', 'Stop swearing!'])
		self.maps.append(Maps(2, ['I\'m fine, thanks!', 'I\'m feeling great!', 'I\'m a bit bored :pensive: ', 'Everything\'s good!']))

	def predict(self, msg):
		blah = []
		blah.append(msg)
		key = self.clf.predict(blah)
		if key[0] is None:
			return "Sorry I don't understand that yet."
		for obj in self.maps:
			if obj.is_key(key[0]):
				return obj.get_msg()