import random

# safely make an int
# limit guesses
# too high
# too low
# play again

def game():
  # generate random number between 1 and 10
  secret_number = random.randint(1, 10)

  tries = []
  
  while len(guesses) < 5:
    try:
      # get a number guess from player
      guess = int(input("Guess a number betwee 1 and 10: "))
    except ValueError:
      print("{} is not a number!".format(guess))
    else:
      # compare guess to secret number
      if guess == secret_number:
        print("You got it! My number was {}".format(secret_number))
        break
      elif guess < secret_number:
        print("The number is higher than {}".format(guess))
      else:
        print("The number is less than {}.".format(guess))
      tries.append(guess)
  else:
    print("You didn't get it! My number was {}".format(secret_number))
  
  play_again = input("Play again? Y/n ")
  if play_again.lower() != 'n':
    game()
  else:
    print("Bye!")
  

  game()