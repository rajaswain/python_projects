import json
import difflib
from difflib import SequenceMatcher

data = json.load(open("data.json"))

def meaning(word):
	word = word.lower()		
	word_match = difflib.get_close_matches(word, data.keys())[0]	
	ratio1     = difflib.SequenceMatcher(None, word, word_match)

	if word in data.keys():
		return data[word]
	elif SequenceMatcher.ratio(ratio1) > 0.8:
		print(f"The matching ratio is {SequenceMatcher.ratio(ratio1)}")
		user1 = input(f"you mean {word_match}\n Press Y for yes and N for No.\n)")
		print(user1)
		if user1 == "Y":
			print(f"\nYou entered Yes \nThe meaning of {word_match} is \n")
			return data[word_match]
		elif user1 == "N":
			return "You entered No\nThe word doesnt exist"
	else:
		return "\n The word doesn\'t exist in this Dictionary.\n Please check once again"
		
print("Dictionary")
while True:	
	word = input("\nInput : ")
	output = meaning(word)
	if type(output) == list:
		for x in output:
			print(x)
	else:
		print(output)