# Kelsea Flores
#
# Classic Ciphers Assignment: 
#
# A Python command-line program that encrypts or decrypts a file based 
# on the flag passed in at the command line and writes the encrypted/
# decrypted text to an output file.

import sys 

def clean_text(text):
	"""
	Cleans all punctuation from a text file.

	Parameters
	----------
	text : str
		Text read in from the file passed in at the command line

	Returns
	-------
	text : str
		Clean text without punctuation
	"""
	for c in text:
		if c in ".,'?!/:;-_+=@#$%^&*~`<>()[]1234567890":
			text = text.replace(c, '')
	return text


# Resource for Caesar cipher:
# https://learncryptography.com/classical-encryption/caesar-cipher
def caesar_encrypt(text, output_file):
	"""
    Encrypts the text passed in (using Ceasar cipher) as an argument and 
    writes the encrypted code to the given output file. 

    Iterates through the plain text character by character, gets the character's
    ASCII value, adds 2 to the value, and converts it back into a character. 
    The function only encrypts letters of the alphabet (a-z,A-Z), so it checks
    if the character to be encrypted is a edge case. If it is, it wraps around to the
    front. 

    Parameters
    ----------
    text : str 
        Plain text that was read in from the input file

    output_file : str
    	File where encrypted text will be written

    """
	f = open(output_file, "w")
	for c in text:
		a_val = ord(c)
		if (a_val > 64 and a_val < 91) or (a_val > 96 and a_val < 123):
			if a_val == 90:
				a_val = 63
			elif a_val == 89:
				a_val = 65
			elif a_val == 122:
				a_val = 96
			elif a_val == 121:
				a_val = 97
			f.write(chr(a_val + 2))
		if a_val == 32:
			f.write(" ")
		elif a_val == 10:
			f.write("\n")

def caesar_decrypt(cipher_text, output_file):
	"""
    Decrypts the cipher text that is passed in back to plain text and writes
    the decrypted text to the given output file.

    Iterates through the cipher text character by character, gets the character's
    ASCII value, subtracts 2 from the value, and converts it back into a character. 
    The function only encrypts letters of the alphabet (a-z,A-Z), so it checks
    if the character to be encrypted is a edge case. If it is, it wraps around back
    around to the end.

    Parameters
    ----------
    cipher_text : str
        Cipher text passed in at the command line

    output_file : str
    	File where decrypted text will be written

    """

	f = open(output_file, "w")
	for c in cipher_text:
		a_val = ord(c)
		if (a_val > 64 and a_val < 91) or (a_val > 96 and a_val < 123):
			if a_val == 65:
				a_val = 91
			elif a_val == 66:
				a_val = 92
			elif a_val == 97:
				a_val = 123
			elif a_val == 98:
				a_val = 124
			f.write(chr(a_val - 2))
		if a_val == 32:
			f.write(" ")
		elif a_val == 10: 
			f.write("\n")

# Resource for simple substitution cipher: 
# http://practicalcryptography.com/ciphers/simple-substitution-cipher/
def simple_sub_encrypt(text, output_file):
	"""
	Encrypts the text passed in (using a simple substitution cipher) as an argument 
	and writes the encrypted code to the given output file. 

    Iterates through the plain text character by character, determines the ASCII value, and 
    depending on whether the character is upper case or lower case, subtracts 65 or 97,
    respectively to find the index of the character in the plain alphabet array. 

    There are also two cipher alphabet arrays (one for upper case, one for lower case). Once 
    index of the plain text character is found, the function replaces that character with 
    its cipher equivalent. 

    Parameters
    ----------
    text : str
        Plain text read in from the file passed in at the commmand line

    output_file : str
    	File where encrypted text is written 

    """

	f = open(output_file, "w")
	plain_alphabet_lower = ['a','b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 
		'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 
		'w', 'x', 'y', 'z']
	cipher_alphabet_lower = ['d', 'p', 'v', 'e', 'm', 's', 'l', 'r', 'z', 'a',
		'x', 'b', 'h', 'c', 't', 'u', 'y', 'g', 'n', 'i', 'f', 'j', 'k', 
		'w', 'q', 'o']
	plain_alphabet_upper = ['A','B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 
		'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 
		'W', 'X', 'Y', 'Z']
	cipher_alphabet_upper = ['D', 'P', 'V', 'E', 'M', 'S', 'L', 'R', 'Z', 'A',
		'X', 'B', 'H', 'C', 'T', 'U', 'Y', 'G', 'N', 'I', 'F', 'J', 'K', 
		'W', 'Q', 'O']

	for c in text: 
		a_val = ord(c)
		if a_val == 32:
			f.write(" ")
		elif a_val == 10:
			f.write("\n")
		elif a_val > 64 and a_val < 91:
			f.write(cipher_alphabet_upper[a_val - 65])
		elif a_val > 96 and a_val < 123:
			f.write(cipher_alphabet_lower[a_val - 97])

def simple_sub_decrypt(cipher_text, output_file):
	"""
   	Decrypts the text passed in as an argument and writes the decrypted code to 
   	the given output file. 

    Iterates through the cipher text character by character, determines the ASCII value, and 
    depending on whether the character is upper case or lower case, subtracts 65 or 97,
    respectively to find the index of the character in the cipher alphabet array. 

    The function will then use that index to get the character at that index in the 
    plain alphabet (either upper or lower, depending on the ASCII value of the cipher character).
    The function replaces that character with its plain alphabet equivalent. 

    Parameters
    ----------
    cipher_text : str
        Cipher text read in from the file passed in at the command line

    output_file : str
    	File where decrypted text is written

    """
	plain_alphabet_lower = ['a','b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 
		'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 
		'w', 'x', 'y', 'z']
	cipher_alphabet_lower = ['d', 'p', 'v', 'e', 'm', 's', 'l', 'r', 'z', 'a',
		'x', 'b', 'h', 'c', 't', 'u', 'y', 'g', 'n', 'i', 'f', 'j', 'k', 
		'w', 'q', 'o']
	plain_alphabet_upper = ['A','B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 
		'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 
		'W', 'X', 'Y', 'Z']
	cipher_alphabet_upper = ['D', 'P', 'V', 'E', 'M', 'S', 'L', 'R', 'Z', 'A',
		'X', 'B', 'H', 'C', 'T', 'U', 'Y', 'G', 'N', 'I', 'F', 'J', 'K', 
		'W', 'Q', 'O']

	f = open(output_file, "w")
	for c in cipher_text:
		a_val = ord(c)
		if a_val == 32:
			f.write(" ")
		elif a_val == 10:
			f.write("\n")
		elif a_val > 64 and a_val < 91:
			i = cipher_alphabet_upper.index(plain_alphabet_upper[a_val - 65])
			f.write(plain_alphabet_upper[i])		
		elif a_val > 96 and a_val < 123:
			i = cipher_alphabet_lower.index(plain_alphabet_lower[a_val - 97])
			f.write(plain_alphabet_lower[i])

# Resource for Atbash Cipher:
# http://practicalcryptography.com/ciphers/classical-era/atbash-cipher/
def atbash_encrypt(text, output_file):
	"""
   	Encrypts the text passed in as an argument and writes the encrypted code to 
   	the given output file. 

    Iterates through the cipher text character by character, determines the ASCII value, and 
    depending on whether the character is upper case or lower case, subtracts 65 or 97,
    respectively to find the index of the character in the cipher alphabet array. 

    The function will then use that index to get the character at that index in the 
    plain alphabet (either upper or lower, depending on the ASCII value of the cipher character).
    The function replaces that character with its plain alphabet equivalent. 

    Parameters
    ----------
    text : str
        Cipher text read in from the file passed in at the command line

    output_file : str
    	File where decrypted text is written

    """
	plain_alphabet_lower = ['a','b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 
		'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 
		'w', 'x', 'y', 'z']
	cipher_alphabet_lower = ['z', 'y', 'x', 'w', 'v', 'u', 't', 's', 'r', 'q',
		'p', 'o', 'n', 'm', 'l', 'k', 'j', 'i', 'h', 'g', 'f', 'e', 'd', 
		'c', 'b', 'a']
	plain_alphabet_upper = ['A','B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 
		'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 
		'W', 'X', 'Y', 'Z']
	cipher_alphabet_upper = ['Z', 'Y', 'X', 'W', 'V', 'U', 'T', 'S', 'R', 'Q',
		'P', 'O', 'N', 'M', 'L', 'K', 'J', 'I', 'H', 'G', 'F', 'E', 'D', 
		'C', 'B', 'A']

	f = open(output_file, "w")
	for c in text: 
		a_val = ord(c)
		if a_val == 32:
			f.write(" ")
		elif a_val == 10:
			f.write("\n")
		elif a_val > 64 and a_val < 91:
			f.write(cipher_alphabet_upper[a_val - 65])
		elif a_val > 96 and a_val < 123:
			f.write(cipher_alphabet_lower[a_val - 97])

def atbash_decrypt(cipher_text, output_file):
	"""
   	Decrypts the text passed in as an argument and writes the decrypted code to 
   	the given output file. 

    Iterates through the cipher text character by character, determines the ASCII value, and 
    depending on whether the character is upper case or lower case, subtracts 65 or 97,
    respectively to find the index of the character in the cipher alphabet array. 

    The function will then use that index to get the character at that index in the 
    plain alphabet (either upper or lower, depending on the ASCII value of the cipher character).
    The function replaces that character with its plain alphabet equivalent. 

    Parameters
    ----------
    cipher_text : str
        Cipher text read in from the file passed in at the command line

    output_file : str
    	File where decrypted text is written

    """

	plain_alphabet_lower = ['a','b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 
		'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 
		'w', 'x', 'y', 'z']
	cipher_alphabet_lower = ['z', 'y', 'x', 'w', 'v', 'u', 't', 's', 'r', 'q',
		'p', 'o', 'n', 'm', 'l', 'k', 'j', 'i', 'h', 'g', 'f', 'e', 'd', 
		'c', 'b', 'a']
	plain_alphabet_upper = ['A','B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 
		'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 
		'W', 'X', 'Y', 'Z']
	cipher_alphabet_upper = ['Z', 'Y', 'X', 'W', 'V', 'U', 'T', 'S', 'R', 'Q',
		'P', 'O', 'N', 'M', 'L', 'K', 'J', 'I', 'H', 'G', 'F', 'E', 'D', 
		'C', 'B', 'A']

	f = open(output_file, "w")
	for c in cipher_text:
		a_val = ord(c)
		if a_val == 32:
			f.write(" ")
		elif a_val == 10:
			f.write("\n")
		elif a_val > 64 and a_val < 91:
			i = cipher_alphabet_upper.index(plain_alphabet_upper[a_val - 65])
			f.write(plain_alphabet_upper[i])
		elif a_val > 96 and a_val < 123:
			i = cipher_alphabet_lower.index(plain_alphabet_lower[a_val - 97])
			f.write(plain_alphabet_lower[i])

# Resource for polyalphabetic cipher (Vigenere cipher):
# https://www.dcode.fr/vigenere-cipher
def vigenere_encrypt(text, output_file):
	"""
	Encrypts the text passed in (using Vigenere cipher) as an argument 
	and writes the encrypted code to the given output file. 

    Using a key and the alphabet, take the first letter of the key, convert it to
    its ASCII value, and depending on whether its upper or lower case, is subtracted by
    65 or 97, respectively. The same is done for the first letter in the text file. 
    Both values are added and modulated by 26 to get the index of the letter 
    replacing the first letter of the text file. This is done to each character, but 
    once the function reaches the end of the key, it wraps around to the beginning.

    Parameters
    ----------
    text : str
        Text read in from the file passed in at the command line
    output_file : str
        File where encrypted text will be written

    """

	f = open(output_file, "w")
	key = "kota"
	key_index = 0
	key_val = 0
	for c in text:
		a_val = ord(c)
		if a_val == 32: 
			f.write(" ")
		elif a_val == 10:
			f.write("\n")
		else:
			if a_val > 64 and a_val < 91:
				a_val -= 65
				key_val = ord(key[key_index]) - 65
				new_index = (a_val + key_val) % 26
				f.write(chr(new_index + 65))
			elif a_val > 96 and a_val < 123:  
				a_val -= 97
				key_val = ord(key[key_index]) - 97
				new_index = (a_val + key_val) % 26
				f.write(chr(new_index + 97))
			key_index += 1
			if key_index == len(key):
				key_index = 0

def vigenere_decrypt(cipher_text, output_file):
	"""
	Decrypts the text passed in (using Vigenere cipher) as an argument 
	and writes the decrypted code to the given output file. 

    Using a key and the alphabet, take the first letter of the key, convert it to
    its ASCII value, and depending on whether its upper or lower case, is subtracted by
    65 or 97, respectively. The same is done for the first letter in the text file. 
    Both values are added and modulated by 26 to get the index of the letter 
    replacing the first letter of the text file. This is done to each character, but 
    once the function reaches the end of the key, it wraps around to the beginning.

    Parameters
    ----------
    cipher_text : str
        Text read in from the file passed in at the command line
    output_file : str
        File where encrypted text will be written

    """

	f = open(output_file, "w")
	key = "kota"
	key_index = 0
	key_val = 0
	for c in cipher_text:
		a_val = ord(c)
		if a_val == 32:
			f.write(" ")
		elif a_val == 10:
			f.write("\n")
		else: 
			if a_val > 64 and a_val < 91:
				a_val -= 65
				key_val = ord(key[key_index]) - 65
				new_index = (a_val - key_val) % 26
				f.write(chr(new_index + 65))
			else:
				a_val -= 97
				key_val = ord(key[key_index]) - 97
				new_index = (a_val - key_val) % 26
				f.write(chr(new_index + 97))
			key_index += 1
			if key_index == len(key):
				key_index = 0

# Resources for Rail Fence cipher: 
# https://www.britannica.com/topic/transposition-cipher
# https://en.wikipedia.org/wiki/Transposition_cipher
def rail_fence_encrypt(text, output_file):
	"""
	Encrypts the text passed in (using rail fence cipher) as an argument 
	and writes the encrypted code to the given output file. 

    There are three rows, or strings. The function reads the file character by character
    and, starting at row1, appends the character onto the string. The function will keep 
    jumping to each row with every iteration, looping around to the front when it reaches
    the last row. Once the function reaches the end of the file, the rows are concatenated
    into one long string, separated by a space. 

    Parameters
    ----------
    text : str
        Text read in from the file passed in at the command line
    output_file : str
        File where encrypted text will be written

    """

	f = open(output_file, "w")
	row_num = 1
	row1 = ""
	row2 = ""
	row3 = ""
	for c in text:
		if row_num == 1:
			if c == " ":
				row1 = row1 + "/"
			elif c == "\n":
				row1 = row1 + "-"
			else:
				row1 = row1 + c
		elif row_num == 2:
			if c == " ":
				row2 = row2 + "/"
			elif c == "\n":
				row2 = row2 + "-"
			else:
				row2 = row2 + c
		elif row_num == 3:
			if c == " ":
				row3 = row3 + "/"
			elif c == "\n":
				row3 = row3 + "-"
			else:
				row3 = row3 + c
		row_num += 1
		if row_num == 4:
			row_num = 1

	f.write("\n" + row1 + " " + row2 + " " + row3)

def rail_fence_decrypt(cipher_text, output_file):
	"""
	Decrypts the text passed in as an argument and writes the encrypted 
	code to the given output file. 

	The function makes n number of iterations total, where n = number of characters
	in the cipher_text passed in. The function iterates through each chunk of text, 
	getting the first character of each, then the second, and so on and so forth, 
	writing each character to the output_file.

    Parameters
    ----------
    text : str
        Text read in from the file passed in at the command line
    output_file : str
        File where encrypted text will be written

    """

	f = open(output_file, "w")
	index_of_word = 0
	index_of_char = 0
	i = 0
	text_array = cipher_text.split()
	num_char = len(cipher_text)

	while i < num_char:
		word = text_array[index_of_word]
		c = word[index_of_char]
		if c == "/":
			f.write(" ")
		elif c == "-":
			f.write("\n")
		else:
			f.write(c)
		index_of_word += 1
		if index_of_word == len(text_array):
			index_of_word = 0
			index_of_char += 1
			if index_of_char == len(word):
				break
		i += 1


# Tests:-------------------------------------------------------------

if "-h" in sys.argv:
	print ("\n$ python cipher.py -f <input filename> -c -o <encrypted/decrypted output filename>")
	print
	print ("Possible options for -f flag:\n\t-e: encrypt file\n\t-d: decrypt file")
	print ("<input filename>:\n\tfile to be encrypted or decrypted")
	print ("Possible options for -c flag:")
	print ("\t-c: Caesar Cipher")
	print ("\t-s: Simple Substitution Cipher")
	print ("\t-a: Atbash Cipher")
	print ("\t-v: Vigenere Cipher")
	print ("\t-r: Rail Fence Cipher")
	print ("-o <encrypted/decrypted output filename>:")
	print ("\tfile name where encrypted/decrypted text will be written")
	print ("NOTE: If -o flag and filename are not provided, encrypted/decrypted text will be written to 'encrypted' or 'decrypted', respectively.\n")
	exit()
elif len(sys.argv) != 4 and len(sys.argv) != 6:
	print ("\nERROR: You have not entered the correct number of arguments in the command line.\n")
	print ("Please run the program again with the '-h' flag in the command line to see all possible command line arguments.")
	print ("\t$ python cipher.py -h\n")
	exit()
else: 
	ed_flag = sys.argv[1]
	input_filename = sys.argv[2]
	cipher_flag = sys.argv[3]
	if len(sys.argv) == 6:
		output_file = sys.argv[5]
	else:
		if ed_flag == "-e":
			output_file = "encrypted"
		else:
			output_file = "decrypted"

	f = open(input_filename, "r")
	text = f.read()
	clean_text = clean_text(text)

	if ed_flag == "-e":
		if cipher_flag == "-c":
			print("Running Caesar cipher encryption..\n..Output is in '" + output_file + "'")
			caesar_encrypt(clean_text, output_file)
		elif cipher_flag == "-s":
			print ("Running a simple substitution cipher encryption..\n..Output is in '" + output_file + "'")
			simple_sub_encrypt(clean_text, output_file)
		elif cipher_flag == "-a":
			print ("Running Atbash Cipher encryption..\n..Output is in '" + output_file + "'")
			atbash_encrypt(clean_text, output_file)
		elif cipher_flag == "-v":
			print ("Running Vigenere Cipher encryption..\n..Output is in '" + output_file + "'")
			vigenere_encrypt(clean_text, output_file)
		elif cipher_flag == "-r":
			print ("Running Rail Fence Cipher encryption..\n..Output is in '" + output_file + "'")
			rail_fence_encrypt(clean_text, output_file)
	else:
		if cipher_flag == "-c":
			print("Running Caesar cipher decryption..\n..Output is in '" + output_file + "'")
			caesar_decrypt(clean_text, output_file)
		elif cipher_flag == "-s":
			print ("Running a simple substitution cipher decryption..\n..Output is in '" + output_file + "'")
			simple_sub_decrypt(clean_text, output_file)
		elif cipher_flag == "-a":
			print ("Running Atbash Cipher decryption..\n..Output is in '" + output_file + "'")
			atbash_decrypt(clean_text, output_file)
		elif cipher_flag == "-v":
			print ("Running Vigenere Cipher decryption..\n..Output is in '" + output_file + "'")
			vigenere_decrypt(clean_text, output_file)
		elif cipher_flag == "-r":
			print ("Running Rail Fence Cipher decryption..\n..Output is in '" + output_file + "'")
			print(rail_fence_decrypt(clean_text, output_file))
