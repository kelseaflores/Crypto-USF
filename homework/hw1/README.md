## HW 1: Classic Ciphers<br>

A Python command-line program that encrypts or decrypts a file. Users must specify whether they would like to encrypt or decrypt a file. They must also specify which cipher they want to use to encrypt/decrypt their text file.


**Feature(s):**<br>
The user can enter the "-h" flag on the command line: $ python cipher.py -h<br>
This will give the user a list of all possible command line arguments in the proper format with a brief description of each.


**Python version:**<br>
Python version 2.7.10


**Imported libraries:** <br>
sys - Imported sys library to be able to access command line args.


**All possible command line options:**

-h flag will list all possible command line options and brief descriptions of each <br>
$ python cipher.py -h

$ python cipher.py -f input_filename> -c -o output_filename<br><br>
Possible options for -f flag:
<br>    -e: encrypt file
<br>    -d: decrypt file
<br><br>
input_filename:<br>file to be encrypted or decrypted
<br><br>
Possible options for -c flag:
<br>-c: Caesar Cipher
<br>-s: Simple Substitution Cipher
<br>-a: Atbash Cipher
<br>-v: Vigenere Cipher
<br>-r: Rail Fence Cipher
<br><br>
-o output_filename:
<br>file name where encrypted/decrypted text will be written
<br><br>"NOTE: If -o flag and filename are not provided, encrypted/decrypted text will be written to 'encrypted' or 'decrypted', respectively.


**References:**<br>
Caesar Cipher: <br>
https://learncryptography.com/classical-encryption/caesar-cipher

Simple Substitution Cipher: <br>
http://practicalcryptography.com/ciphers/simple-substitution-cipher/

Atbash Cipher:<br>
http://practicalcryptography.com/ciphers/classical-era/atbash-cipher/

Vigenere Cipher (polyalphabetic cipher):<br>
https://www.dcode.fr/vigenere-cipher

Rail Fence Cipher (transposition cipher): <br>
https://www.britannica.com/topic/transposition-cipher <br>
https://en.wikipedia.org/wiki/Transposition_cipher
