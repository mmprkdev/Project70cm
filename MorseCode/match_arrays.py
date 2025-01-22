def decode_letter(t):
  match t:
    case [2, 0, 3]:
      letter_list.append('A')
    case [3, 0, 2, 0, 2, 0, 2]:
      letter_list.append('B')
    case [3, 0, 2, 0, 3, 0, 2]:
      letter_list.append('C')    
    case [3, 0, 2, 0, 2]:
      letter_list.append('D')
    case [2]:
      letter_list.append('E')
    case [2, 0, 2, 0, 3, 0, 2]:
      letter_list.append('F')
    case [3, 0, 3, 0, 2]:
      letter_list.append('G')
    case [2, 0, 2, 0, 2, 0, 2]:
      letter_list.append('H')
    case [2, 0, 2]:
      letter_list.append('I')
    case [2, 0, 3, 0, 3, 0, 3]:
      letter_list.append('J')
    case [3, 0, 2, 0, 3]:
      letter_list.append('K')
    case [2, 0, 3, 0, 2, 0, 2]:
      letter_list.append('L')
    case [3, 0, 3]:
      letter_list.append('M')
    case [3, 0, 2]:
      letter_list.append('N')
    case [3, 0, 3, 0, 3]:
      letter_list.append('0')
    case [2, 0, 3, 0, 3, 0, 2]:
      letter_list.append('P')
    case [3, 0, 3, 0, 2, 0, 3]:
      letter_list.append('Q')
    case [2, 0, 3, 0, 2]:
      letter_list.append('R')
    case [2, 0, 2, 0, 2]:
      letter_list.append('S')
    case [3]:
      letter_list.append('T')
    case [2, 0, 2, 0, 3]:
      letter_list.append('U')
    case [2, 0, 2, 0, 2, 0, 3]:
      letter_list.append('V')
    case [2, 0, 3, 0, 3]:
      letter_list.append('W')
    case [3, 0, 2, 0, 2, 0, 3]:
      letter_list.append('X')
    case [3, 0, 2, 0, 3, 0, 3]:
      letter_list.append('Y')
    case [3, 0, 3, 0, 2, 0, 2]:
      letter_list.append('Z')
    case [2, 0, 3, 0, 3, 0, 3, 0, 3]:
      letter_list.append('1')
    case [2, 0, 2, 0, 3, 0, 3, 0, 3]:
      letter_list.append('2')
    case [2, 0, 2, 0, 2, 0, 3, 0, 3]:
      letter_list.append('3')
    case [2, 0, 2, 0, 2, 0, 2, 0, 3]:
      letter_list.append('4')
    case [2, 0, 2, 0, 2, 0, 2, 0, 2]:
      letter_list.append('5')
    case [3, 0, 2, 0, 2, 0, 2, 0, 2]:
      letter_list.append('6')
    case [3, 0, 3, 0, 2, 0, 2, 0, 2]:
      letter_list.append('7') 
    case [3, 0, 3, 0, 3, 0, 2, 0, 2]:
      letter_list.append('8')
    case [3, 0, 3, 0, 3, 0, 3, 0, 2]:
      letter_list.append('9')
    case [3, 0, 3, 0, 3, 0, 3, 0, 3]:
      letter_list.append('0') 


# Create the letters K and F
a = [1, 1, 1, 1] # dash 3
b = [0, 0] # symbol space 0
c = [1, 1, 1, 1] # dash 3
d = [0, 0, 0, 0, 0] # letter space 1
e = [1] # dot 2
f = [0, 0] # symbol space 0
g = [1] # dot 2
h = [0, 0] # symbol space 0
i = [1, 1, 1, 1] # dash 3
j = [0, 0] # symbol space 0
k = [1] # dot 2
l = [0, 0, 0, 0, 0] # letter space 1

x = [a, b, c, d, e, f, g, h, i, j, k, l]
 
symbol_list = [] # list of ints representing the 4 different symbols

'''
symbol space: 0
letter space: 1
dot: 2
dash: 3
'''

for i in x:
  match i:
    case [0, 0]:
      symbol_list.append(0)
    case [0, 0, 0, 0, 0]:
      symbol_list.append(1)
    case [1]:
      symbol_list.append(2)
    case [1, 1, 1, 1]: 
      symbol_list.append(3)
      
change_index = 0
symbol_list_index = 0
tmp_letter = []
letter_list = []
for s in symbol_list:
  symbol_list_index += 1
  if symbol_list[s] == 1:
    tmp_letter = symbol_list[change_index:symbol_list_index]
    print(tmp_letter)
    letter_list.append(decode_letter(tmp_letter))

                   

'''
symbol space: 0
letter space: 1
dot: 2
dash: 3
'''

  
