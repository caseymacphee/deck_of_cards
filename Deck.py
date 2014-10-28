import random

class Card(object):
	def __init__(self, card_value, suit):
		if card_value == 1:
			card_value = "Ace"
		if card_value == 11:
			card_value = "Jack"
		if card_value == 12:
			card_value = "Queen"
		if card_value == 13:
			card_value = "King"
		self.card_value = card_value
		self.suit = suit
		self.next = None

	def __str__(self):
		return "({}, {})".format(self.card_value, self.suit)

	def __cmp__(self, other):
		""" 
		Note that in most card games there is no suit order, 
		instead the pot is generally split
		"""
		first_card = self.card_value
		second_card = other.card_value
		if first_card == 'Ace':
			first_card = 1
		if first_card == 'Jack':
			first_card = 11
		if first_card == 'Queen':
			first_card = 12
		if first_card == 'King':
			first_card = 13
		if second_card == 'Ace':
			second_card = 1
		if second_card == 'Jack':
			second_card = 11
		if second_card == 'Queen':
			second_card = 12
		if second_card == 'King':
			second_card = 13
		if first_card > second_card:
			return 1
		if first_card < second_card:
			return -1
		else:
			return 0

class Deck(object):
	def __init__(self):
		self.top = None
		self.size = 0
		for card in xrange(1, 14):
			newcard = Card(card, 'Clubs')
			newcard.next = self.top
			self.top = newcard
			self.size += 1
		for card in xrange(1, 14):
			newcard = Card(card, 'Hearts')
			newcard.next = self.top
			self.top = newcard
			self.size += 1
		for card in xrange(1, 14):
			newcard = Card(card, 'Diamonds')
			newcard.next = self.top
			self.top = newcard
			self.size += 1
		for card in xrange(1, 14):
			newcard = Card(card, 'Spades')
			newcard.next = self.top
			self.top = newcard
			self.size += 1

	def deal(self):
		if self.top is None:
			raise Exception('There are no cards left in the deck!')
		self.size -= 1
		temp = self.top
		self.top = self.top.next
		return temp

	def __iter__(self):
		self.current = self.top
		return self

	def next(self):
		if self.current is None:
			raise StopIteration('There are no more cards in the deck!')
		else:
			temp = self.current
			self.current = self.current.next
			return temp

	def size(self):
		return self.size

	def shuffle(self):
		unshuffled_pile = []
		temp_deck_pile = []
		current = self.top
		while current is not None:
			unshuffled_pile.append(current)
			current = current.next
		while len(unshuffled_pile) > 0:
			nextcardnum = random.randint(0, len(unshuffled_pile)-1)
			temp_deck_pile.append(unshuffled_pile.pop(nextcardnum))
		# for index, card in enumerate(temp_deck_pile):
			# if index + 1 < len(temp_deck_pile):
			# 	card.next = temp_deck_pile[index + 1]
		self.top = temp_deck_pile.pop(0)
		current = self.top
		while len(temp_deck_pile) > 0:
			current.next = temp_deck_pile.pop(0)
			current = current.next
		current.next = None






