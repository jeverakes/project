import crypt
import re

count = 0
m = open("hashpass.txt", "r")
password = open("passwords.txt", "r")
file_out = open("output_file.txt", "a+")
#passSet = set()
#hashSet = set()
passSet = []
hashSet = []

def a():
    for strpw in password:
        strpw = strpw.rstrip('\n')
        strpw = ''.join(strpw)
        passSet.append(str(strpw))
        #passSet.add(str(strpw))
        

a()

def b():
    for hashy in m:
	hashy = hashy.rstrip('\n')
	hashy = ''.join(hashy)
	hashSet.append(str(hashy))
	#hashSet.add(str(hashy))

b()


for pw in passSet:
    for hashy in hashSet:
	count += 1
	print count
	fullpw = ''.join(hashy)
	fullpw = fullpw.rstrip('\n')
	fullpw = re.findall(r'(\$\d*\$\w*\d*\S*)', fullpw)
	fullpw = ''.join(fullpw)
	fullpw = str(fullpw)
	hashy = hashy.rstrip('\n').split('$')
	user = str(hashy[0]).rstrip('\n')
	meth = str(hashy[1]).rstrip('\n')
	salt = str(hashy[2]).rstrip('\n')
	if meth == '6':
	    cmd = crypt.crypt(pw, '$6$' + salt)
	    cmd = cmd.rstrip('\n')
	    cmd = str(cmd)
	    fullpw = str(fullpw)
      	    if cmd == fullpw:
		print "match sha512"
		file_out.write(user)
		file_out.write("\n")
            	file_out.write(pw)
                file_out.write("\n")
                file_out.write(cmd)
	        file_out.write("\n")
	else:
            cmd = crypt.crypt(pw, '$1$' + salt)
	    cmd = cmd.rstrip('\n')
	    cmd = str(cmd)
	    fullpw = str(fullpw)
            if cmd == fullpw:
		print "match md5"
                file_out.write(user)
                file_out.write("\n")
		file_out.write(pw)
		file_out.write("\n")
		file_out.write(cmd)
		file_out.write("\n")

