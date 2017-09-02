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
		# if not match then return this:
		# return "Sorry I don't understand that yet."

	def predict(self, test):
		predictions = []
		for msg in test:
			reply = self.find_string_in_test(msg)
			predictions.append(reply)
		return predictions


import pandas

# url = './chat.data'
# names = ['content', 'reply']
# dataset = pandas.read_csv(url, names=names).values

# features = dataset[:, 0]
# replies = dataset[:, 1]

# clf = MyClassifier()
# clf.fit(features, replies)
# key = clf.predict(['hi how are YoU', 'BYE BYE CYA', 'lol', 'fuck whats up my man'])
# print (key)

# key = 1;
# #TODO next step is implement randomness for message which is to be returned

# maps = []
# maps.append(Maps(0, ['Yooooo!', 'Hello!', 'Hello there!', 'What\'s up?']))
# maps.append(Maps(1, ['Byeee!', 'See ya in another life brother!', 'Goodbye!']))

# for obj in maps:
# 	if obj.is_key(key):
# 		print(obj.get_msg())

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

	def predict(self, msg):
		blah = []
		blah.append(msg)
		key = self.clf.predict(blah)
		if key[0] is None:
			return "Sorry I don't understand that yet."
		for obj in self.maps:
			if obj.is_key(key[0]):
				return obj.get_msg()

# x = Morty()
# print(x.predict('hi how are you'))
# print(x.predict('asdasd'))