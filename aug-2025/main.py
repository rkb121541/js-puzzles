import string

alphabet = list(string.ascii_lowercase)

ranks = ["A", "2", "3", "4", "5", "6", "7", "8", "9", "10", "J", "Q", "K"]
suits = ["C", "D", "H", "S"]
deck = [f"{rank}{suit}" for rank in ranks for suit in suits]

class Dog:
    def __init__(self, card1, chips1, card2, chips2, emoji, breed):
        self.card1 = card1
        self.chips1 = chips1
        self.card2 = card2
        self.chips2 = chips2
        self.emoji = emoji
        self.breed = breed

    def __str__(self):
        return (f"Dog(\n"
            f"card1 = {self.card1},\n"
            f"chips1 = {self.chips1},\n"
            f"card2 = {self.card2},\n"
            f"chips2 = {self.chips2},\n"
            f"emoji = {self.emoji},\n"
            f"breed = {self.breed}\n"
            f")"
        )

dogCards = [["4C", "5H"], ["6D", "9S"], ["9H", "4H"], ["5D", "8D"], ["7C", "5S"], ["AH", "8H"], ["5C", "6C"], ["8C", "6H"]]
dogChips = [[1, 0], [22, 23], [7, 12], [10, 11], [23, 6], [16, 0], [23, 0], [14, 25]]
dogEmojis = ["flushedface", "droolingface", "cowboyhatface", "woozyface", "anguishedface", "poutingcat", "confoundedface", "squintingface"]
dogBreeds = ["doberman", "bernesemountaindog", "labrador", "bulldog", "cockerspaniel", "britishshorthair", "germanshepherd", "goldenretriever"] 
dogs = []

allCards = set(deck)
usedCards = set()
for card1, card2 in dogCards:
    usedCards.add(card1)
    usedCards.add(card2)
remainingCards = allCards.difference(usedCards)

numDogs = 8 # excluding the doodle
for i in range(numDogs):
    dog = Dog(
        card1 = dogCards[i][0],
        chips1 = dogChips[i][0],
        card2 = dogCards[i][1],
        chips2 = dogChips[i][1],
        emoji = dogEmojis[i],
        breed = dogBreeds[i]
    )
    dogs.append(dog)

s = ""
for dog in dogs:
    if dog.card1[0] == 'A':
        s += dog.emoji[0]
    else:
        s += dog.emoji[int(dog.card1[0])-1]
    if dog.card2[0] == 'A':
        s += dog.emoji[0]
    else:
        s += dog.emoji[int(dog.card2[0])-1]
print(s)

s = ""
for dog in dogs:
    if dog.card1[0] == 'A':
        index = (alphabet.index(dog.emoji[0]) + dog.chips1) % len(alphabet)
    else:
        index = (alphabet.index(dog.emoji[int(dog.card1[0])-1]) + dog.chips1) % len(alphabet)
    s += alphabet[index]
    if dog.card2[0] == 'A':
        index = (alphabet.index(dog.emoji[0]) + dog.chips2) % len(alphabet)
    else:
        index = (alphabet.index(dog.emoji[int(dog.card2[0])-1]) + dog.chips2) % len(alphabet)
    s += alphabet[index]
print(s)
