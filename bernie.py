import numpy as np 

adlibs = ['skrt skrt', 'swag swag', 'trap trap', 
		  'gang gang', 'wrist game', 'dick game', 'get cash', 'flow like', 'big boss']

endlines = ['(YUH!)', '(QUAVO!)', '(SKRRRT!)', '(UGHH!)', '(BANG BANG!)']

def bernie(num_lines): 
	for _ in range(num_lines): 
		index = np.random.randint(low=0, high=len(adlibs))
		line = adlibs[index] + ' bernie sanders '
		line = line.title()
		if (np.random.randint(20) % 3 == 0):
			endline_index = np.random.randint(low=0, high=len(endlines))
			line += endlines[endline_index]
		print(line)
