
tree_to_json = """If (feature 1 <= 3.6600000858307)
 If (feature 0 <= 4.7199997901917)
  Predict: 0.0
 Else (feature 0 > 4.7199997901917)
  If (feature 2 <= 3.6500000953674)
   If (feature 2 <= 1.6299999952316)
    Predict: 1.0
   Else (feature 2 > 1.6299999952316)
    If (feature 0 <= 5.0999999046326)
     Predict: 1.0
    Else (feature 0 > 5.0999999046326)
     Predict: 0.0
  Else (feature 2 > 3.6500000953674)
   Predict: 0.0
Else (feature 1 > 3.6600000858307)
 Predict: 1.0
"""

import json



def parse(lines):
	block = []
	while lines :
		
		if lines[0].startswith('If'):
			bl = ' '.join(lines.pop(0).split()[1:]).replace('(', '').replace(')', '')
			block.append({'name':bl, 'children':parse(lines)})
			
			
			if lines[0].startswith('Else'):
				be = ' '.join(lines.pop(0).split()[1:]).replace('(', '').replace(')', '')
				block.append({'name':be, 'children':parse(lines)})
		elif not lines[0].startswith(('If','Else')):
			block2 = lines.pop(0)
			block.append({'name':block2})
		else:
			break	
	return block
	
# Convert Tree to JSON
def tree_json(tree):
	data = []
	for line in tree.splitlines() : 
		if line.strip():
			line = line.strip()
			data.append(line)
		else : break
		if not line : break
	res = []
	res.append({'name':'Root', 'children':parse(data[1:])})
	with open('data/structure.json', 'w') as outfile:
		json.dump(res[0], outfile)
	print ('Conversion Success !')
	
tree_json(tree_to_json)


