from Crypto.Cipher import ARC4 #from tutorial


msg = raw_input("Input a series of numbers for a key. Otherwise, default key. >> ")
try:
    key = str(int(msg) + 0)    #test for an interger and make it into a string
    obj1 = ARC4.new('\'' + key + '\'')    #create a encrypt key
    obj2 = ARC4.new('\'' + key + '\'')    #create a decrypt key
except:
    obj1 = ARC4.new('Hello')    #default encryptors
    obj2 = ARC4.new('Hello')    #just default decryptors



text = raw_input("Filename or string. >> ")
try:
    a = open(text, 'r')   #checks for the file, does not exist, this fails
    d = open(text, 'w')   #Needed to clean out the old file
    s = open('temp.txt', 'w')    #Shows that the decrypting works
    string = a.read()    #record the information from 'a'
    print string
    cipher_text = obj1.encrypt(string);    #encrypt the file using the key
    print cipher_text
    decypher = obj2.decrypt(cipher_text)    #shows that this is decrpyted
    d.write(cipher_text);s.write(decypher)   #write everthing
    a.close();s.close();d.close()    #close EVERYTHING!!!
    
except:
    cipher_text = obj1.encrypt(text)    #encrypt the string
    print cipher_text    #print the ecrypted stuff
    print obj2.decrypt(cipher_text)    #decrypt the string and print
