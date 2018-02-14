import sys

def binary_error(message):
	print(message)
	sys.exit()

def binary_version():
	print('** Ascii Code **\nName: asciiToBinary.py\nVersion: 1.0.0')
	sys.exit()

def binary_help():
	print('*** Ascii Coding Help ***')
	print("usage asciiToBinary.py <\"<Ascii (letter, word, frase>\">")
	sys.exit(1)

def main(argv):
	multiples = [128, 64, 32, 16, 8, 4, 2, 1]
	asciiUpper = {"A":65, "B":66, "C":67, "D":68, "E":69, "F":70, "G":71, "H":72, "I":73, "J":74, "K":75, "L":76, "M":77, "N":78, "O":79, "P":80, "Q":81, "R":82, "S":83, "T":84, "U":85, "V":86, "W":87, "X":88, "Y":89, "Z":90}
	asciiLower = {"a":97, "b":66, "c":67, "d":68, "e":69, "f":70, "g":71, "h":72, "i":73, "j":74, "k":75, "l":76, "m":77, "n":78, "o":79, "p":80, "q":81, "r":82, "s":83, "t":84, "u":85, "v":86, "w":87, "x":88, "y":89, "z":90}

	asciii = argv.upper()
	binary = ""
	baseNumber = 0
	for letter in asciii:
		baseNumber = asciiUpper[letter]
		if str(binary) != "":
			binary = str(binary) + " "
		for multiple in multiples:
			if multiple <= baseNumber:
				if binary == "":
					binary = "1"
				else:
					binary = binary + "1"
				baseNumber = baseNumber - multiple
			else:
				if binary == "":
					binary = "0"
				else:
					binary = binary + "0"
	print ('The BINARY result to ASCII entered ' + str(asciii) + ' is: \n' + binary)

if __name__ == "__main__":
	if len(sys.argv) <= 1:
		binary_error('SyntaxError: Expected Argument.\nUse asciiToBinary.py -h for help')
		sys.exit()
	elif len(sys.argv) > 2:
		binary_error('SyntaxError: Invalid Number of Arguments.\nUse asciiToBinary.py -h for help')
		sys.exit()
	elif sys.argv[1] == "-h" or sys.argv[1] == "-H":
		binary_help()
	elif sys.argv[1] == "-v" or sys.argv[1] == "-V":
		binary_version()
	else:
		main(sys.argv[1])