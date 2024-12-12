import random

# points system
def scoreing():
   shoot = random.randint(1,99)
   #two point
   if shoot <= 33:
      two = random.randint(1,100)
      if two >= 48:
         team += str(2)
         print(f'current score: {'team'}')
      elif two < 48:
         print ('two point miss')
   rebound = random.randint(1,2)
   if rebound == 1:
      ball()
      clock - 5
   elif rebound == 2:
      scoreing()
# three point shot
   if shoot >= 34:
      three = random.randint(1,100)
      if three >= 36:
         team += str(3)
         print(f'current score: {'team'}')
      elif three < 36:
         print('three point miss')
   rebound = random.randint(1,2)
   if rebound == 1:
      ball()
      clock - 5
   elif rebound == 2:
      scoreing()

def foul():
   
#who has the ball
def ball():
    home_team = 2   
    away_team = 1
    ball_1 = random.randint(1,2)
    if ball_1 != 1:
       team = away_team
       team = 32
       print('away has ball')
    elif ball_1 != 2:
        team = home_team
        team = 30
        print('home has ball')


   # main
user = input('r = run and q = quit: ')
while not user == 'q':
   clock = 30
   if user == "r":
    while clock > 1:
      ball()
      scoreing()
      time_left = clock - 1
      print(f'time reamining, {time_left}')
      print(f'{input('r for run and q for quit: ')}')
   elif user == 'q':
      print('thank you for playing')
      break
   elif user != '':
      print("something went wrong: r to run q to quit: ")
      break