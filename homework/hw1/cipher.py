# Kelsea Flores
#
# Classic Ciphers Assignment: 
#
# A Python command-line program that encrypts or decrypts a file based 
# on the flag passed in at the command line. 

import sys 

# Resource for Caesar cipher:
# https://learncryptography.com/classical-encryption/caesar-cipher
def caesar_encrypt(text):
	"""
    Encrypts the text passed in (using Ceasar cipher) as an argument and 
    writes the encrypted code to an output file. 

    Iterates through the plain text character by character, gets the character's
    ASCII value, adds 2 to the value, and converts it back into a character. 
    The function only encrypts letters of the alphabet (a-z,A-Z), so it checks
    if the character to be encrypted is a edge case. If it is, it wraps around to the
    front. 

    Parameters
    ----------
    text : str 
        Plain text that was read in from the input file

    Returns
    -------
    null
    	No return value

    """

	cipher_text = ""
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
			cipher_text = cipher_text + chr(a_val + 2)
		if a_val == 32:
			cipher_text = cipher_text + " "
	return cipher_text

def caesar_decrypt(cipher_text):
	"""
    Decrypts the cipher text that is passed in back to plain text.

    Iterates through the cipher text character by character, gets the character's
    ASCII value, subtracts 2 from the value, and converts it back into a character. 
    The function only encrypts letters of the alphabet (a-z,A-Z), so it checks
    if the character to be encrypted is a edge case. If it is, it wraps around back
    around to the end.

    Parameters
    ----------
    cipher_text : str
        Cipher text passed in at the command line.

    Returns
    -------
    null
        No return value

    """

	decrypted_text = ""
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
			decrypted_text = decrypted_text + chr(a_val - 2)
		if a_val == 32:
			decrypted_text = decrypted_text + " "
	return decrypted_text

# Resource for simple substitution cipher: 
# http://practicalcryptography.com/ciphers/simple-substitution-cipher/
def simple_sub_encrypt(text):
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

	cipher_text = ""
	for c in text: 
		a_val = ord(c)
		if a_val == 32:
			cipher_text = cipher_text + " "
		elif a_val == 10: 
			cipher_text = cipher_text + "\n"
		elif a_val > 64 and a_val < 91:
			cipher_text = cipher_text + cipher_alphabet_upper[a_val - 65]
		elif a_val > 96 and a_val < 123:
			cipher_text = cipher_text + cipher_alphabet_lower[a_val - 97]
	return cipher_text

def simple_sub_decrypt(cipher_text):
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

	plain_text = ""
	for c in cipher_text:
		a_val = ord(c)
		if a_val == 32:
			plain_text = plain_text + " "
		elif a_val == 10:
			plain_text = plain_text + "\n"
		elif a_val > 64 and a_val < 91:
			i = cipher_alphabet_upper.index(plain_alphabet_upper[a_val - 65])
			plain_text = plain_text + plain_alphabet_upper[i]			
		elif a_val > 96 and a_val < 123:
			i = cipher_alphabet_lower.index(plain_alphabet_lower[a_val - 97])
			plain_text = plain_text + plain_alphabet_lower[i]
	return plain_text

# Resource for polyalphabetic cipher (Vigenere cipher):
# https://www.dcode.fr/vigenere-cipher
def vigenere_encrypt(text):
	key = "kota"
	cipher_text = ""
	key_index = 0
	key_val = 0
	for c in text:
		a_val = ord(c)
		if a_val == 32: 
			cipher_text = cipher_text + " "
		else:
			if key_index == len(key):
				key_index = 0

			a_val -= 97
			key_val = ord(key[key_index]) - 97
			new_index = (a_val + key_val) % 26
			cipher_text = cipher_text + chr(new_index + 97)
			key_index += 1
	return cipher_text

def vigenere_decrypt(cipher_text):
	key = "kota"
	plain_text = ""
	key_index = 0
	key_val = 0
	for c in cipher_text:
		a_val = ord(c)
		if a_val == 32:
			plain_text = plain_text + " "
		else: 
			a_val -= 97
			if key_index == len(key):
				key_index = 0
			key_val = ord(key[key_index]) - 97
			new_index = (a_val - key_val) % 26
			plain_text = plain_text + chr(new_index + 97)
			key_index += 1
	return plain_text

def encrypt_spaces(c):
	if c == " ":
		return "/"
	if c == "\n":
		return "//"

# Resources for Rail Fence cipher: 
# https://www.britannica.com/topic/transposition-cipher
# https://en.wikipedia.org/wiki/Transposition_cipher
def rail_fence_encrypt(text):
	row_num = 1
	row1 = ""
	row2 = ""
	row3 = ""
	cipher_text = ""
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

	cipher_text = "\n" + row1 + " " + row2 + " " + row3
	return cipher_text

def rail_fence_decrypt(cipher_text):
	plain_text = ""
	index_of_word = 0
	index_of_char = 0
	c_text_array = cipher_text.split()
	c = c_text_array[index_of_word][index_of_char]

	while c != null:
		plain_text = plain_text + c
		index_of_word += 1
		c = c_text_array[index_of_word][index_of_char]

# Tests:

if "-h" in sys.argv:
	print ("$ python cipher.py -f <input filename> -o <encrypted/decrypted output filename>")
	print
	print ("Possible options for -f flag:\n\t-e: encrypt file\n\t-d: decrypt file")
	print ("<input filename>:\n\tfile to be encrypted or decrypted")
	print ("-o <encrypted/decrypted output filename>:")
	print ("\tfile name where encrypted/decrypted text will be written")
	print ("\t(If -o flag and filename are not provided, encrypted/decrypted text will be written to 'encrypted.txt' or 'decrypted.txt', respectively.")
	exit()
elif len(sys.argv) != 5 and len(sys.argv) != 3:
	print ("ERROR:\n")
	print ("$ python cipher.py -f <input filename> -o <encrypted/decrypted output filename>\n")
	print ("You have not entered the correct number of arguments in the command line.")
	print ("Example: python cipher.py -f <filename> -o <encrypted/decrypted filename>")
	print ("Please enter '-h' as your flag to list all possible flags and their descriptions.")
	print
	exit()
# elif len(sys.argv) == 3: 
# 	input_var = raw_input("ATTENTION:\n\nYou have not entered an output file name for the encrypted/decrypted text. Enter 'C' or 'c' to continue with default encrypted/decrypted output files. Enter 'Q' or'q' to exit.")
# 	if input_var == 'C' or 'c':
# 	elif input_var == 'Q' or 'q':
# 		exit()
else: 
	cipher_flag = sys.argv[1]
	input_filename = sys.argv[2]


	f = open(input_filename, "r")
	contents = f.read()

	# if flag == "-e":
	# 	print ("Plain text:\n" + contents)
	# 	print
	# 	print ("Caesar cipher encryption:\n" + caesar_encrypt(contents))
	# 	print 
	# 	print ("Simple substitution encryption:\n" + simple_sub_encrypt(contents))
	# 	print
	# 	print ("Vigenere cipher encryption:\n" + vigenere_encrypt(contents))
	# 	print
	# 	print ("Transposition cipher encryption:\n" + transposition_cipher(contents))
	# elif flag == "-d":

# print ("Plain text:\n" + contents)
# print
# contents = f.read()
# caesar_text = caesar_encrypt(contents)
# print ("Testing Caesar Cipher:")
# print ("Encrypted text: " + caesar_text)
# print ("Decrypted text: " + caesar_decrypt(caesar_text))
# print 
# print ("Testing Simple Substitution Cipher:")
# simple_sub_text = simple_sub_encrypt(contents)
# print ("Encrypted Text:\n" + simple_sub_text + "\n")
# print ("Decrypted Text:\n" + simple_sub_decrypt(simple_sub_text + "\n"))
# print
# print ("Testing polyalphabetic cipher:")
# vigenere_text = vigenere_encrypt(contents)
# print ("Encrypted Text: " + vigenere_text)
# print ("Decrypted Text: " + vigenere_decrypt(vigenere_text))
# print
print ("Testing transposition cipher:")
trans_text = rail_fence_encrypt(contents)
print ("Encrypted Text: " + trans_text)
# print ("Decrypted Text: " + transposition_cipher(trans_text))
