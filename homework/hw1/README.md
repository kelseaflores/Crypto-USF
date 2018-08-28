## HW 1: Classic Ciphers<br>

A Python command-line program that encrypts or decrypts a file. Users must specify whether they would like to encrypt or decrypt a file. They must also specify which cipher they want to use to encrypt/decrypt their text file.


The user can enter the "-h" flag on the command line: <br><br>
    $ python cipher.py -h<br><br>
This will give the user a list of all possible command line arguments in the proper format with a brief description of each.


Python version 2.7.10


Imported libraries: <br>
sys - Imported sys library to be able to access command line args.


All possible command line options:

-h flag will list all possible command line options and brief descriptions of each <br>
$ python cipher.py -h

Encrypt the file using Caesar Cipher and write the encrypted text to given output file <br>
$ python cipher.py -e filename -c -o encrypted_filename

Encrypt the file using simple substitution cipher and write the encrypted text to given output file <br>
$ python cipher.py -e filename -s -o encrypted_filename

Encrypt the file using Atbash Cipher and write the encrypted text to given output file <br>
$ python cipher.py -e filename -a -o encrypted_filename

Encrypt the file using Vigenere Cipher and write the encrypted text to given output file <br>
$ python cipher.py -e filename -v -o encrypted_filename

Encrypt the file using rail fence cipher and write the encrypted text to given output file <br>
$ python cipher.py -e filename -r -o encrypted_filename

Decrypt the file using Caesar Cipher and write the decrypted text to given output file <br>
$ python cipher.py -d filename -c -o decrypted_filename

Decrypt the file using simple substitution cipher and write the decrypted text to given output file <br>
$ python cipher.py -d filename -s -o decrypted_filename

Decrypt the file using Atbash Cipher and write the decrypted text to given output file <br>
$ python cipher.py -d filename -a -o decrypted_filename

Decrypt the file using Vigenere Cipher and write the decrypted text to given output file <br>
$ python cipher.py -d filename -v -o decrypted_filename

Decrypt the file using rail fence cipher and write the decrypted text to given output file <br>
$ python cipher.py -d filename -r -o decrypted_filename

Encrypt the file using Caesar Cipher and write the encrypted text to default output file <br>
$ python cipher.py -e filename -c 

Encrypt the file using simple substitution cipher and write the encrypted text to default output file <br>
$ python cipher.py -e filename -s 

Encrypt the file using Atbash Cipher and write the encrypted text to default output file <br>
$ python cipher.py -e filename -a 

Encrypt the file using Vigenere Cipher and write the encrypted text to default output file <br>
$ python cipher.py -e filename -v 

Encrypt the file using rail fence cipher and write the encrypted text to default output file <br>
$ python cipher.py -e filename -r 

Decrypt the file using Caesar Cipher and write the decrypted text to default output file <br>
$ python cipher.py -d filename -c 

Decrypt the file using simple substitution cipher and write the decrypted text to default output file <br>
$ python cipher.py -d filename -s 

Decrypt the file using Atbash Cipher and write the decrypted text to default output file <br>
$ python cipher.py -d filename -a

Decrypt the file using Vigenere Cipher and write the decrypted text to default output file <br>
$ python cipher.py -d filename -v 

Decrypt the file using rail fence cipher and write the decrypted text to default output file <br>
$ python cipher.py -d filename -r 


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
