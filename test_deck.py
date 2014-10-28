import pytest
from Deck import *

## Empty deck
## Number comparable
## Suit comparable
## Number of cards/ number of each suit



def test_empty():
	with pytest.raises(Exception):
		newdeck = Deck()
		for numcards in len(xrange(53)):
			newdeck.deal()

def test_size():
	newdeck = Deck()
	decksize = 0
	for card in newdeck:
		decksize +=1
	assert decksize == 52
	assert newdeck.size == 52

def test_shuffle():
	newdeck = Deck()
	beforeshuffle = []
	for card in newdeck:
		beforeshuffle.append(card)
	newdeck.shuffle()

	sameplace = 0
	index = 0
	for card in newdeck:
		if card.card_value == beforeshuffle[index].card_value:
			sameplace += 1
		index += 1
	assert sameplace < newdeck.size/3

def test_deal():
	newdeck = Deck()
	newdeck.shuffle()
	first_player = []
	second_player = []
	third_player = []
	card_per_hand = 7
	for card in range(card_per_hand):
		first_player.append(newdeck.deal())
		second_player.append(newdeck.deal())
		third_player.append(newdeck.deal())
	assert len(first_player) == 7
	assert len(second_player) == 7
	assert len(third_player) == 7





