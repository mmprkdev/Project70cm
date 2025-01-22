import numpy as np
import os

'''
The dots are always 1
The symbol spaces are always 2
The dashes are always 4
The letter spaces are always 5

Logic:
When there is a transition from high to low or low to high, count the number of 1s or 0s between the current transition and the previous transition. Based on this, build the morse code.

lets start by going through the entire array of samples, create an entire array of symbols, go through the entire array of symbols, create a list of decoded letters/numbers
'''

if os.path.isfile("decoded_output"):
  os.remove("decoded_output")
  print('removed exsisting decoded_output file')

samples = np.fromfile('test_output', np.float32) # Read in file

print('Starting decode...')
f = open('decoded_output', 'a')
f.write(f"Number of samples: {len(samples)}\n\n")

index = 0 # keeping track of the current samples array index
change_index = 0 # this keeps track of the previous index where a change occured
t = 0.0
for s in samples:
  if s != t:  # check if value has changed
    ### value changed, see what symbol it is ###
    '''
    symbol = samples[change_index:index]
    for i in symbol:
      # match the pattern to the symbol
    #f.write('changed value\n')
    '''
    if change_index == 6:
      symbol = samples[change_index:index]
      for i in symbol:
        f.write(f'{i}\n')
    #f.write(f'previous change_index: {change_index}\n') 
    change_index = index
  #f.write(f'Current index: {index}, value: {s}\n')
  index += 1  
  t = s

f.close()

print('Decode complete')

 



