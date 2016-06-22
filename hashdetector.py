import sys

from hashid import HashID
from terminaltables import AsciiTable

def HashDetector(hash):
	table  = [
		['Hash Name', 'Hashcat', 'John', 'Extended'],
	]
	out = [] 
	h = HashID()
	for i in  HashID().identifyHash(hash):
		if i.hashcat != None or i.john!= None:
			temp = [i.name, i.hashcat, i.john, i.extended]
			table.append(temp)
			out.append(i.name)

	pretty_table = AsciiTable(table)
	return pretty_table.table, out

if __name__=='__main__':
	if len(sys.argv) < 2:
		print 'Usage: ./HashDetector.py hash_in_hex'
		sys.exit() 

	table, out = HashDetector(sys.argv[1])
	print "Useless Guess:", ' '.join(out)
	print table