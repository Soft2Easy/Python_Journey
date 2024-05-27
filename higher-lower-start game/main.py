import art
import game_data
import random
from replit import clear

print(art.logo+"\n")

#declare our list
data = []

#copying our list data into "data" variable
data = game_data.data

#getting the list size
data_length = len(data)


runner_ = True
score_ = 0

while runner_ :

  #Make sure our code don't generate the same random numbers
  a_rand = random.randint(0,data_length-1)
  b_rand = random.randint(0,data_length-1)

  while a_rand == b_rand:
    b_rand = random.randint(0,data_length-1)

  #Choosing items to compare randomly from the list
  a_data = data[a_rand]
  b_data = data[random.randint(0,data_length-1)]

  #declare and asign values to our dictioneries
  a_dict ={}
  a_dict = a_data

  b_dict = {}
  b_dict = b_data


  print(f"Compare A : {a_dict['name']}, a {a_dict['description']} ,from {a_dict['country']} {a_dict['follower_count']}")

  print(art.vs)

  print(f"Compare B : {b_dict['name']}, a {b_dict['description']} ,from {b_dict['country']} {b_dict['follower_count']}")

  followers_ = input("Who has more followers? Type 'A' or 'B': ").lower()

  if followers_ == "a" :
    if a_dict['follower_count'] > b_dict['follower_count'] :
      score_ +=1 
      clear()
      print(art.logo+"\n")
      print(f"You are right! Current score: {score_}")
    elif a_dict['follower_count'] < b_dict['follower_count'] :
      runner_ = False
      clear()
      print(art.logo+"\n")
      print(f"Sorry, that's wrong.Final Score : {score_}")

  elif followers_ == "b" :
    if b_dict['follower_count'] > a_dict['follower_count'] :
      score_ +=1
      clear()
      print(art.logo+"\n")
      print(f"You are right! Current score: {score_}")
    elif b_dict['follower_count'] < a_dict['follower_count'] :
      runner_ = False
      clear()
      print(art.logo+"\n")
      print(f"Sorry, that's wrong.Final Score : {score_}")



