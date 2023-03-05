import pandas as pd

players ={}

number_of_players= input("Tell me how many players do you wanna list: ")

for i in range(int(number_of_players)):
    last_name= input("Enter player's last name: ")
    if last_name == "END":
        break
    pl_score= int(input("Enter player's score: "))
    players[last_name]= pl_score

print(players)
print(min(players, key=players.get))