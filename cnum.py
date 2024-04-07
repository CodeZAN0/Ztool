import os
import random
from colorama import Back, Fore, Style

def random_number() -> None:
  namefile = input(Fore.LIGHTYELLOW_EX + 'input file name: ')
  print('=========================')
  code= input(Fore.MAGENTA + '750,770,751,771,44,\nchoice code:')
  for x in range(10000):
     ne=str(int(random.randint(1000000 ,9999999)))
     open(f'{namefile}.txt', 'a').write('0'+code+ne+':'+'0'+code+ne+'\n')
  print('=======================')
  print(Fore.GREEN + 'You\'ve been successful')
if __name__ == '__main__':
   random_number()
