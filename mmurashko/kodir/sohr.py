import sys
fr=sys.argv[1]
fw=sys.argv[2]

with open(fr,'r') as f_read:
	with open(fw,'w') as f_w:
		for x in f_read:
			f_w.write(x)
