import json
## Open the JSON file of pokemon data
pokedex = open("./pokedex.json", encoding="utf8")
## create variable "data" that represents the enitre pokedex list
data = json.load(pokedex)

# Create a function that will take the data from the JSON file and you will iterate through the list of pokemon and print each pokemons name.
def pokedex(pokemon_list):


# Add a language choice feature and print the pokemons name based on the user input
#revisit
    lang=input("What language would you like? 1 for English, 2 for Japanese, 3 for Chinese, or 4 for French: ")
    for pokemon in data:
        if lang=="1":
            print(pokemon["name"]["english"])
        elif lang=="2":
            print(pokemon["name"]["japanese"])
        elif lang=="3":
            print(pokemon["name"]["chinese"])
        elif lang=="4":
            print(pokemon["name"]["french"])
        else:
            print("Invalid input")
            break
#pokedex(data)

# Develop a function that creates a new list of pokemon based on the type the user searched for. If no pokemon was found of that type inform the user
def pokemon_type(types_list):
    pokemon_history=[]
    for pokemon in data:
        x=input("What type?")          
        if x in pokemon["type"]:
            pokemon_history.append(pokemon["name"])
        else:
            print("No pokemon of that type.")
            break


for pokemon in data:
    print(pokemon["type"]["English"])

#Develop a function to find all pokemon matching the name the user searched for. Ex. if "Char" return Charmander, Charmeleon and Charizard. Make the user aware if no pokemon was found. 


#Based on user input, show all moves that a pokemon could learn based on their type. For example, if Charizard is fire/fyling, show all fire and flying moves. HINT import the moves.json file too!
