
from art import logo

print(logo)

bids = {}
isTrue = True


def find_highest_bidder():
  highest = 0
  winner = ''
  for key in bids:
    val = int(bids[key])
    if highest < val:
      highest = val
      winner = key
  print(f"The winner for is bid is {winner} by bidding ${highest}. ")


while isTrue:
  name = input("What is your name?\n")
  price = input("What is your bidding price?\n$")
  bids[name] = price
  ask = input(
      "Is there anyone else willing to bet? type 'yes' if there is or else 'no'\n"
  )

  if ask == 'yes':
    clear()
    isTrue = True
  elif ask == 'no':
    isTrue = False
    find_highest_bidder()



#                          ___________
#                          \         /
#                           )_______(
#                           |"""""""|_.-._,.---------.,_.-._
#                           |       | | |               | | ''-.
#                           |       |_| |_             _| |_..-'
#                           |_______| '-' `'---------'` '-'
#                           )"""""""(
#                          /_________\
#                        .-------------.
#                       /_______________\
# What is your name?
# kai
# What is your bidding price?
# $4
# Is there anyone else willing to bet? type 'yes' if there is or else 'no'
# no
# The winner for is bid is kai by bidding $4. 
 