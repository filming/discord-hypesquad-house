from colorama import init, Fore
from random import choice
from sys import exit
import requests
import json

init(convert = True)

def initial_visual():
	sign = "Made By Filming#6252"
	bad_colors = ['BLACK', 'WHITE', 'LIGHTBLACK_EX', 'RESET']
	codes = vars(Fore)
	colors = [codes[color] for color in codes if color not in bad_colors]
	colored_chars = [choice(colors) + char for char in sign]
	print(''.join(colored_chars))

	print(Fore.LIGHTBLUE_EX + "\nType one of the following numbers to choose a HypeSquad!" + Fore.WHITE)
	print(Fore.LIGHTYELLOW_EX + "	+========-HypeSquad Houses-=========+")
	print("		1 : House of Bravery")
	print("		2 : House of Brilliance")
	print("		3 : House of Balance" + Fore.WHITE)

	print(Fore.LIGHTBLUE_EX + "Select a house: " + Fore.WHITE, end='')
	house_choice = int(input())

	if not(1 <= house_choice <= 3):
		print (Fore.RED + "Invalid house choice!" + Fore.WHITE)
		exit()

	print ( )
	print(Fore.LIGHTBLUE_EX + "Enter your discord token: " + Fore.WHITE, end='')
	discord_token = input()

	return house_choice, discord_token
	
	
def hypesquad_changer(token, house):
	r = requests.post("https://discord.com/api/v8/hypesquad/online", data = json.dumps({"house_id":f"{house}"}), headers = {"Authorization":token,"User-Agent":"Mozilla/5.0 (Linux; Android 6.0; Nexus 5 Build/MRA58N) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/88.0.4324.96 Mobile Safari/537.36","Content-Type":"application/json"})
	return (r)

def main():
	house_choice, discord_token = initial_visual()

	houses = lambda c : "House of Bravery" if c == 1 else ("House of Brilliance" if c == 2 else "House of Balance")

	r = hypesquad_changer(discord_token, house_choice)

	if (r.status_code == 204):
		print (Fore.GREEN + f"\nYou have successfully changed your HypeSquad house to '{houses(house_choice)}'" + Fore.WHITE) 
	
	else:
		print (Fore.RED + f"\nThe attempt to change your HypeSquad house to '{houses(house_choice)}' has failed! (Reason: {json.loads(r.text)['message']})")

if __name__ == "__main__":
	main()
