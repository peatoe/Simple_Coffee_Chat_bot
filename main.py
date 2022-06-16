import time

# Define functions

#define bot
def coffee_bot():
  print("Welcome to the cafe!")

  size = get_size()
  drink_type = get_drink_type()
  print('Alright, that\'s a {} {}!'.format(size, drink_type))
  time.sleep(1.5)

  name = input('Can I get your name please?\n')
  print('Thanks, ' + name + '! Your drink will be ready shortly.')

#message prints if an unexpected input is recieved
def print_message():
  print('I\'m sorry, I did not understand your selection. Please enter the corresponding letter for your response.')

#ask what size drink and return input
def get_size():
  res = input('What size drink can I get for you? \n[a] Small \n[b] Medium \n[c] Large \n> ')

  if res == 'a':
    return 'small'
  elif res == 'b':
    return 'medium'
  elif res == 'c':
    return 'large'
  else:
    print_message()
    time.sleep(1.5)
    return get_size()

#ask what drink type and return input
def get_drink_type():
  res = input('What type of drink would you like? \n[a] Brewed Coffee \n[b] Mocha \n[c] Latte \n> ')
  if res == "a":
    return 'brewed coffee'
  elif res == 'b':
    return 'mocha'
  elif res == 'c':
    return order_latte()
  else:
    print_message()
    return get_drink_type()

#If customer wants a latte, then this will as what kind of milk they want and return input
def order_latte():
  res = input('And what kind of milk for your latte? \n[a] 2% milk \n[b] Non-fat milk \n[c] Soy milk \n> ')
  if res == 'a':
    return 'latte'
  elif res == 'b':
    return 'non-fat latte'
  elif res == 'c':
    return 'soy latte'
  else:
    print_message()
    return order_latte()

#Initialize bot
coffee_bot()
