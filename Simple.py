import time

ppl = {
	"bar keeper": {
		"text": "add text for bar keeper",
	},
	"waitress": {
		"text": "add text for waitress",
	},
	"hooded man": {
		"text": "add text for hooded man",
	},
	"weapons shop": {
		"text": "add text for weapons",
		"options": {
		"1": "short sword",
		"2": "long sword",
		"3": "mace",
		"4": "staff",
		"5": "bow & arrow",
		"6": "exit the shop"
		}
	},
	"item shop": {
		"text": "add text for items",
		"options": {
		"1": "potions",
		"2": "revives",
		"3": "amulet",
		"4": "exit the shop",
		}
	},
	"tavernpeople": {
		"options": {
		"1": "bar keeper",
		"2": "waitress",
		"3": "hooded man"
	}},
	"tavernpeople1": {
		"options": {
		"1": "waitress",
		"2": "hooded man"
	}},
	"tavernpeople2": {
		"options": {
		"1": "hooded man"
	}},
	"tavernpeople3": {
		"options": {
		"1": "waitress"
	}},
	"tavernpeople4": {
		"options": {
		"1": "bar keeper",
		"2": "hooded man"
	}},
	"places": {
		"options": {
		"1": "weapons shop",
		"2": "item shop"
	}},
	"places1": {
		"options": {
		"1": "weapons shop"
	}},
	"places2": {
		"options": {
		"1": "item shop"
	}},
	"tavernpeople5": {
		"options": {
		"1": "bar keeper"
	}},
	"tavernpeople6": {
		"options": {
		"1": "waitress",
		"2": "bar keeper"
	}}
}


playerName = input("What is your name? ")
print("Welcome, to the Taverna {}!".format(playerName)) 



def start_tavern():
	print("There are some people who may talk to you. Who do you want to try talking to?")
	print(ppl["tavernpeople"]["options"])

def go_places():
	print("I think we got enough information here. Let's head out")
	print(ppl["places"]["options"])
	check = input(">>> ")
	if check == "1":
		print(ppl["weapons shop"]["text"])
		print(ppl["places2"]["options"])
		check = input(">>> ")
		if check == "1":
			print(ppl["item shop"]["text"])
	if check == "2":
		print(ppl["item shop"]["text"])
		print(ppl["places1"]["options"])
		check = input(">>> ")
		if check == "1":
			print(ppl["weapons shop"]["text"])



start_tavern()



talkto = input(">>> ")
while talkto != "1" and talkto != "2" and talkto != "3":
	talkto = input("Select a person(1, 2, 3): ")
if talkto == "1":
	print(ppl["bar keeper"]["text"])
	print(ppl["tavernpeople1"]["options"])
	talkto = input(">>> ")
	if talkto == "1":
		print(ppl["waitress"]["text"])
		print(ppl["tavernpeople2"]["options"])
		talkto = input(">>> ")
		if talkto == "1":
			print(ppl["hooded man"]["text"])
			go_places()
	if talkto == "2":
		print(ppl["hooded man"]["text"])
		print(ppl["tavernpeople3"]["options"])
		talkto = input(">>> ")
		if talkto == "1":
			print(ppl["waitress"]["text"])
			go_places()
if  talkto == "2":
	print(ppl["waitress"]["text"])
	print(ppl["tavernpeople4"]["options"])
	talkto = input(">>> ")
	if talkto == "1":
		print(ppl["bar keeper"]["text"])
		print(ppl["tavernpeople2"]["options"])
		talkto = input(">>> ")
		if talkto == "1":
			print(ppl["hooded man"]["text"])
			go_places()
	if talkto == "2":
		print(ppl["hooded man"]["text"])
		print(ppl["tavernpeople3"]["options"])
		talkto = input(">>> ")
		if talkto == "1":
			print(ppl["waitress"]["text"])
			go_places()
if talkto == "3":
	print(ppl["hooded man"]["text"])
	print(ppl["tavernpeople6"]["options"])
	talkto = input(">>> ")
	if talkto == "1":
		print(ppl["waitress"]["text"])
		print(ppl["tavernpeople5"]["options"])
		talkto = input(">>> ")
		if talkto == "1":
			print(ppl["bar keeper"]["text"])
			go_places()
	if talkto == "2":
		print(ppl["bar keeper"]["text"])
		print(ppl["tavernpeople3"]["options"])
		talkto = input(">>> ")
		if talkto == "1":
			print(ppl["waitress"]["text"])
			go_places()
else:
	goplaces()


	
