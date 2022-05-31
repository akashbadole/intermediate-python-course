import random 

def main():
  # print('You rolled a die')
  # roll = 5
  # dice_roll = 2
  dice_rolls = int(input('how many dice would you like to roll!'))
  dice_size = int(input('how many sides are the dice!'))
  dice_sum = 0
  for i in range(0, dice_rolls):
    roll = random.randint(1,6)
    dice_sum = dice_sum + roll
    if roll == 1:
      print(f'you rolled a {roll}! critical fail')
    elif roll==6:
      print(f'you rolled a {roll}! Critical Success')
    else:
      print(f'You rolled a {roll}')
    # print(f'You rolled a {roll}')
  print(f'You have a total of {dice_sum}')

if __name__== "__main__":
  main()