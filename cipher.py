# Nick attempted to aid in fixing the main problem
# Medina help solved the creation of blank pages by seperating the two open statements 
# Main code is from tutorial
from Crypto.Cipher import ARC4 #from tutorial

msg = raw_input("Input a series of numbers for a key. Otherwise, default key. >> ")
try:    #If the input is an interger
    key = str(int(msg) + 0)    #test for an interger and make it into a string
    key1 = ARC4.new('\'' + key + '\'')    #create a encrypt key
    key2 = ARC4.new('\'' + key + '\'')    #create a decrypt key
except:   #If it was not a interger
    key1 = ARC4.new('Hello')    #default encryptors
    key2 = ARC4.new('Hello')    #just default decryptors



text = raw_input("Filename or string. >> ")
#text = 'm.txt' #My test code

####################
####MAIN PROBLEM####
####################
try: #Run if there is a file
    ###FIRST OPEN STATEMENT###
    a = open(text, 'r')   #checks for the file, does not exist, this fails
    string = a.read()    #record the information from 'a'
    a.close()    #close function 'a'

    ###SECOND OPEN STATEMENT###
    d = open(text, 'w')   #Needed to clean out the old file
    cipher_text = key1.encrypt(string);    #encrypt the file using the key
    d.write(cipher_text);    #write the result into a file
    d.close()    #close function 'd'

    w = open(text, 'r')   #Needed to clean out the old file
    s = open('temp.txt', 'w')    #Shows that the decrypting works
    string = w.read()    #record the information from 'a'
    decypher = key2.decrypt(cipher_text)    #shows that this is decrpyted
    s.write(decypher)   #write everthing
    s.close();w.close()    #close EVERYTHING!!!
################################
except:   #If the code cannot find a file
    cipher_text = key1.encrypt(text)    #encrypt the string
    print cipher_text    #print the ecrypted stuff
    print key2.decrypt(cipher_text)    #decrypt the string and print
