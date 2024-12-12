import random



def scoreing():
   score = 30
   shoot = random.randint(1,2)
   #two point
   if shoot == 1:
      two = random.randint(1,100)
      if two >= 48:
         score += 2
      elif two < 48:
         print ('two point miss')
   if shoot == 2:
      three = random.randint(1,100)
      if three >= 36:
         score += 3
      elif three < 36:
         print('three point miss')
   

# testing code
"""user = input('r = run and q = quit: ')
while not user == 'q':
   if user == "r":
      scoreing()
      print(f'{input('r for run and q for quit: ')}')
   elif user == 'q':
      print('thank you for playing')
      break"""
