a brief description of what your program does


features of your program


Python version 2.7.10


Imported libraries: 
sys - Imported sys library to be able to access command line args.


All possible command line options:

-h flag will list all possible command line options and brief descriptions of each
$ python cipher.py -h

Will read and encrypt the text in given "filename" and write encrypted text to given 
"encryped filename"
$ python cipher.py -e <filename> -o <encrypted filename>

Will read and decrypt the text in given "filename" and write decrypted text to given
"decrypted filename"
$ python cipher.py -d <filename> -o <decrypted filename>

Will read and encrypt the text given in "filename" and write encrypted text to default
file "encrypted"
$ python cipher.py -e <filename> 

Will read and decrypt the text given in "filename" and write decrypted text to default
file "decrypted"
$ python cipher.py -d <filename>


References: 
Caesar Cipher: 
https://learncryptography.com/classical-encryption/caesar-cipher

Simple Substitution Cipher: 
http://practicalcryptography.com/ciphers/simple-substitution-cipher/

Vigenere Cipher (polyalphabetic cipher):
https://www.dcode.fr/vigenere-cipher

Rail Fence Cipher (transposition cipher): 
https://www.britannica.com/topic/transposition-cipher
https://en.wikipedia.org/wiki/Transposition_cipher