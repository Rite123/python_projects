import os
#HINT: You can call clear() to clear the output in the console.
logo = '''
                         ___________
                         \         /
                          )_______(
                          |"""""""|_.-._,.---------.,_.-._
                          |       | | |               | | ''-.
                          |       |_| |_             _| |_..-'
                          |_______| '-' `'---------'` '-'
                          )"""""""(
                         /_________\\
                       .-------------.
                      /_______________\\
'''

print(logo)
print("Welcome to The secret Auction Programme")

players={}

while(True):
  name=input("What is your name:")
  bid=input("What's Your Bid:$")

  players[name]=bid

  condition=input("Are there any bidders? Type 'yes' or 'no'")
  if condition=="no":
    break
  os.system("cls")

os.system("cls")
max_value=max(players,key=players.get)
print(f"The winner is {max_value} having value of {players[max_value]}")
    
