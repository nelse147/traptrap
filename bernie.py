'''An approximation of Ugly God's 'Bernie Sanders.' 
Please excuse any profanity. '''

import numpy as np 

begin_lines = ['skrt skrt', 'swag swag', 'trap trap', 
		  'gang gang', 'wrist game', 'dick game', 'get cash', 'flow like', 'big boss']


adlibs = ['(YUH!)', '(QUAVO!)', '(SKRRRT!)', '(UGHH!)', '(BANG BANG!)']

def bernie(num_lines): 
	for _ in range(num_lines): 
		index = np.random.randint(low=0, high=len(begin_lines))
		line = begin_lines[index] + ' bernie sanders '
		line = line.title()
		if (np.random.randint(20) % 3 == 0):
			endline_index = np.random.randint(low=0, high=len(adlibs))
			line += adlibs[endline_index]
		print(line)
