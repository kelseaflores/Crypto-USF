a brief description of what your program does


features of your program


Python version 2.7.10


Imported libraries: 
sys - Imported sys library to be able to access command line args.


All possible command line options:

-h flag will list all possible command line options and brief descriptions of each <br>
$ python cipher.py -h

Encrypt the file using Caesar Cipher and write the encrypted text to given output file <br>
$ python cipher.py -e filename -c -o encrypted_filename

Encrypt the file using simple substitution cipher and write the encrypted text to given output file <br>
$ python cipher.py -e <filename> -s -o <encrypted filename>

Encrypt the file using Atbash Cipher and write the encrypted text to given output file <br>
$ python cipher.py -e <filename> -a -o <encrypted filename>

Encrypt the file using Vigenere Cipher and write the encrypted text to given output file <br>
$ python cipher.py -e <filename> -v -o <encrypted filename>

Encrypt the file using rail fence cipher and write the encrypted text to given output file <br>
$ python cipher.py -e <filename> -r -o <encrypted filename>

Decrypt the file using Caesar Cipher and write the decrypted text to given output file <br>
$ python cipher.py -d <filename> -c -o <decrypted filename>

Decrypt the file using simple substitution cipher and write the decrypted text to given output file <br>
$ python cipher.py -d <filename> -s -o <decrypted filename>

Decrypt the file using Atbash Cipher and write the decrypted text to given output file <br>
$ python cipher.py -d <filename> -a -o <decrypted filename>

Decrypt the file using Vigenere Cipher and write the decrypted text to given output file <br>
$ python cipher.py -d <filename> -v -o <decrypted filename>

Decrypt the file using rail fence cipher and write the decrypted text to given output file <br>
$ python cipher.py -d <filename> -r -o <decrypted filename>

Encrypt the file using Caesar Cipher and write the encrypted text to default output file <br>
$ python cipher.py -e <filename> -c 

Encrypt the file using simple substitution cipher and write the encrypted text to default output file <br>
$ python cipher.py -e <filename> -s 

Encrypt the file using Atbash Cipher and write the encrypted text to default output file <br>
$ python cipher.py -e <filename> -a 

Encrypt the file using Vigenere Cipher and write the encrypted text to default output file <br>
$ python cipher.py -e <filename> -v 

Encrypt the file using rail fence cipher and write the encrypted text to default output file <br>
$ python cipher.py -e <filename> -r 

Decrypt the file using Caesar Cipher and write the decrypted text to default output file <br>
$ python cipher.py -d <filename> -c 

Decrypt the file using simple substitution cipher and write the decrypted text to default output file <br>
$ python cipher.py -d <filename> -s 

Decrypt the file using Atbash Cipher and write the decrypted text to default output file <br>
$ python cipher.py -d <filename> -a

Decrypt the file using Vigenere Cipher and write the decrypted text to default output file <br>
$ python cipher.py -d <filename> -v 

Decrypt the file using rail fence cipher and write the decrypted text to default output file <br>
$ python cipher.py -d <filename> -r 


References: 
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
