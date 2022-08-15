import hashlib
import colorama
from hashlib import *
colorama.init(autoreset=True)
style = '''\033[34m
                          __
                            .d$$b
                          .' TO$;\
                         /  : TP._;
                        / _.;  :Tb|
                       /   /   ;j$j
                   _.-"       d$$$$
                 .' ..       d$$$$;
                /  /P'      d$$$$P. |\
               /   "      .d$$$P' |\^"l
             .'           `T$P^"""""  :
         ._.'      _.'                ;
      `-.-".-'-' ._.       _.-"    .-"
    `.-" _____  ._              .-"
   -(.g$$$$$$$b.              .'
     ""^^T$$$P^)            .(:
       _/  -"  /.'         /:/;
    ._.'-'`-'  ")/         /;/;
 `-.-"..--""   " /         /  ;
.-" ..--""        -'          :
..--""--.-"         (\      .-(\
  ..--""              `-\(\/;`
    _.                      :
                            ;`-                           
                           :\  
                           {by

=================================================|
            [ + ] by kivani                      |
=================================================|
            [ + ] Instagram : 2knn10             |                   
=================================================|
'''                                                                              
print(style)
style = '''\033[33m
================================================
 -Hash chacker [1]\n -Hash length  [2]\n -Hash type    [3] 
 -MD5 Encrypt  [4]\n -md5 Decrypt  [5] 
================================================
'''
print(style)
choose = input("please choose option : ") 
if choose == '1':
        print("This option is to match the hash type")
        hash1 = input("Enter hash [1] : ")
        hash2 = input("Enter hash [2] : ")
        if hash1 == hash2 : 
                print("the hash is clean")
        else:
                print("the hash is virus")
if choose == '2' :
        print("This optin For length hash")
        length = input("Enter your Hash : ")
        print("Length Hash is : ", len(length))
if choose == '3':
       print("This option For know Hash Type")
       hash = input("Enter the hash : ")
       length = len(hash)
       if length == 32 :
               print("The hash is [ MD5 ]")
       if length == 40 :
               print("The hash is [ sha1 ]")
       if length == 64 :
               print("The hash is [ sha256 ]")       
if choose == '4' :
        print("Put the text you want to encrypt")       
        word = input("Enter your text :")
        md5  = hashlib.md5(word.encode())
        print(md5.hexdigest())
if choose == '5':
        print("This option For decryption")
        hash = input ("Enter your hash : ")
        file = input ("Write file name : ")
        with open(file , mode='r') as f :
                for line in f :
                        line = line.strip()
                        if md5(line.encode()).hexdigest() == hash :
                                print("[-] hash Found :" +line)
        
