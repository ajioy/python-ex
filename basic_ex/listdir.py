import os

all_list = os.listdir('.')

with open('./all.txt', 'w') as f:
  #maps = map(lambda x: x+'\n', all_list)
  maps = [x+'\n' for x in os.listdir('.') if os.path.isdir(x)]
  for s in maps:
    f.write(s)
