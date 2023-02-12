from replit import clear
from art import logo
import random

def compare(total_player, total_computer):
  if total_player > 21 and total_computer > 21:
    return "You went to far. You lost"
  
  if total_player == total_computer:
    return "Same score"
  elif total_computer == 0:
    return " You lost. Computer won blackjack"
  elif total_player == 0:
    return " You oin. You won the blackjack"
  elif total_player >21 :
     return "You went to far. You lost"
  elif total_computer >21 :
     return "Computer went to far. You won"
  elif total_player >total_computer :
     return "You won!"
  else:
    return "You lost"
     
def card_random ():
   cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
   return random.choice(cards)

def sum_total(cards):
  if(sum(cards) == 21 and len(cards)== 2):
    return 0
  if 11 in cards and sum (cards) == 2:
    cards.remove(11)
    cards.append(1)
  return sum(cards)

def play_game():
  print(logo)
  player_cards = []
  computer_cards = []
  end_game = False
  
  for card in range (2):
    player_cards.append(card_random())
    computer_cards.append(card_random())

  while not end_game:
    total_player = sum_total(player_cards)
    total_computer= sum_total(computer_cards)
    print(f"     You hand is {player_cards} and score is : {total_player} ")
    print(f"     Computer first card is {computer_cards[0]} ")
    
    if total_player == 0 or total_computer == 0 or total_player > 21:
      end_game = True
    else:
      new_card_message= "Press 'y' if you want another card or 'n' for pass "
      bet_user = input(new_card_message)
      if bet_user == "y":
        player_cards.append(card_random())
      else:
        end_game = True
  while total_computer != 0 and total_computer < 17:
    computer_cards.append(card_random())
    total_computer = sum_total(computer_cards) 
  print(f"     You final hand is {player_cards} and score is : {total_player}")
  print(f"     Computer final hand is {computer_cards} and score is :{total_computer}")
  print(compare(total_player, total_computer))
  

start_note = ("Do you want to play balckjack? y/n : ")

while (input(start_note))== "y":
  clear()
  play_game()
 

