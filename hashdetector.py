import io
import os
import sys
from argparse import ArgumentParser

from hashid import HashID
from terminaltables import AsciiTable

def HashDetector(hash, mode, john, extended):
	table = [	['Hash Name']	]

	if mode:
		table[0].append( 'Hashcat' )
	if john:
		table[0].append( 'John' )
	if extended:
		table[0].append( 'Salted' )
	
	out = [] 
	
	for i in  HashID().identifyHash(hash):
		
		temp = [i.name]

		if john & mode :
			if i.hashcat == None and i.john == None:
				out.append(i.name)
			else:
				temp.append(i.hashcat)
				temp.append(i.john)
		
		elif mode:
			if i.hashcat != None:
				temp.append(i.hashcat)
			else:
				out.append(i.name)

		elif john:
			if i.john != None: 
				temp.append(i.john)
			else:
				out.append(i.name)

		if len(temp) < 2:
			continue

		if extended:
			temp.append(i.extended)

		table.append(temp)
		
	if len(table) < 2:
		return None, set(out)
	pretty_table = AsciiTable(table)
	return pretty_table.table, set(out)

def writeResult(string, mode, john, extended, verbose):
	if mode == False and john == False and extended == False:
		mode = john = extended = True 

	table, out = HashDetector(string, mode, john, extended)
	print '[+] {}'.format(string)
	print table
	if verbose:
		print "Useless Guess:", ' | '.join(out)	


if __name__=='__main__':
	print 
	parser = ArgumentParser(
		description="Identify the different types of hashes used to encrypt data",
		add_help=False,
	)
	parser.add_argument("strings",
						metavar="INPUT", type=str, nargs="*",
						help="input to analyze (default: STDIN)")

	group = parser.add_argument_group('optional')

	group.add_argument("-e", "--extended",
						action="store_true",
						help="list all possible hash algorithms including salted passwords")
	group.add_argument("-m", "--mode",
						action="store_true",
						help="show corresponding Hashcat mode in output")
	group.add_argument("-j", "--john",
						action="store_true",
						help="show corresponding JohnTheRipper format in output")
	group.add_argument("-h", "--help",
						action="help",
						help="show this help message and exit")
	group.add_argument('-v', '--verbose',
						action="store_true",
						help="show useless guesses, which don't work in both Hashcat and Jtr")
	

	args = parser.parse_args()
	
	if not args.strings or args.strings[0] == "-":
		while True:
			print ' >>> ',
			line = sys.stdin.readline()
			if not line:
				break
			writeResult(line, args.mode, args.john, args.extended, args.verbose)
			sys.stdout.flush()
	else:
		for string in args.strings:
					if os.path.isfile(string):
						try:
							with io.open(string, "r", encoding="utf-8") as infile:
								for line in infile:
									if line.strip():
										writeResult(line, args.mode, args.john, args.extended, args.verbose)
						except (EnvironmentError, UnicodeDecodeError):
							print("--File '{0}' - could not open--".format(string))
						else:
							print("--End of file '{0}'--".format(string))
					else:
						writeResult(string, args.mode, args.john, args.extended, args.verbose)



	
