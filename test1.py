text = 'm.txt'

a = open(text, 'r')
d = open ('temp.txt', 'w')
string = a.read()
print string
d.write(string)
a.close();d.close()
