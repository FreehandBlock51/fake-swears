fname = ''
wcount = 100
mins = 4
maxs = 8
contu = True
print('''
welcome to:



                                                    $$$$$                              
                                                    $:::$                              
                                                $$$$$:::$$$$$$      &&&&&&&&&&     !!! 
     @@@@@@@@@          ######    ######      $$::::::::::::::$    &::::::::::&   !!:!!
   @@:::::::::@@        #::::#    #::::#     $:::::$$$$$$$::::$   &::::&&&:::::&  !:::!
 @@:::::::::::::@@      #::::#    #::::#     $::::$       $$$$$  &::::&   &::::&  !:::!
@:::::::@@@:::::::@######::::######::::######$::::$              &::::&   &::::&  !:::!
@::::::@   @::::::@#::::::::::::::::::::::::#$::::$               &::::&&&::::&   !:::!
@:::::@  @@@@:::::@######::::######::::######$:::::$$$$$$$$$      &::::::::::&    !:::!
@:::::@  @::::::::@     #::::#    #::::#      $$::::::::::::$$     &:::::::&&     !:::!
@:::::@  @::::::::@     #::::#    #::::#        $$$$$$$$$:::::$  &::::::::&   &&&&!:::!
@:::::@  @:::::::@@######::::######::::######            $::::$ &:::::&&::&  &:::&!:::!
@:::::@  @@@@@@@@  #::::::::::::::::::::::::#            $::::$&:::::&  &::&&:::&&!!:!!
@::::::@           ######::::######::::######$$$$$       $::::$&:::::&   &:::::&   !!! 
@:::::::@@@@@@@@        #::::#    #::::#     $::::$$$$$$$:::::$&:::::&    &::::&       
 @@:::::::::::::@       #::::#    #::::#     $::::::::::::::$$ &::::::&&&&::::::&& !!! 
   @@:::::::::::@       ######    ######      $$$$$$:::$$$$$    &&::::::::&&&::::&!!:!!
     @@@@@@@@@@@                                   $:::$          &&&&&&&&   &&&&& !!! 
                                                   $$$$$                               
                                                                                       
                                          
                                          ''')
worder = True
print("For when you can't use real swears")
print('')
fname = str(input("what is the .txt file name: "))
print("type help for help")

while True:
  while worder:
    if fname[-4:] != '.txt':
      print('that file name is not usable please input the correct one below')
      fname = str(input("what is the .txt file name: "))
    else:
      worder = False
  inpu = str(input("@#$&!> "))
  if inpu == "help":
    print("""
  this is some simple code that uses fictionary to generate random words in this
  case based on and fine tuned for swears but will work with any text document
  to setup put your text document name on the commented line about the txt file
  and make sure they are both in the same folder
  
  command = 'run' run the code with set params 
  command = 'min' this changes min size of the words outputed
  command = 'max' this changes max size of the words outputed
  command = 'count' this changes how many words are generated
  command = 'credits' for code credits
  command = 'file' to print out the file before you run
  command = 'exit' to exit the program 
  """)
  elif inpu == "min":
    mins = int(input("set min word length: "))
  elif inpu == "max":
    maxs = int(input("set maxium word length: "))
  elif inpu == "count":
    wcount = int(input("how many words should i gen"))
  elif inpu  == "credits":
    print("""
 thanks to creators of fictionary for doing the heavy lifting
 most of the code was writen by me 'superpotato9'
 naming creds go to 'bricked pixel'
 some adivce and coding help from 'blue_595'
 coding help and the swear list from 'czoky mylk '
 """)
  elif inpu == "run":
    break
  elif inpu == "file":
    a_file = open(fname)

    lines = a_file.readlines()
    for line in lines:
      print(line)
  elif inpu == 'exit':
    contu = False
    break
  
  else:
    print("error cmd does not exist")
  
 
                    




import fictionary
if contu:
  #this block of code feeds the txt line by line into the file converter and defines a few vars
  m = fictionary.Model()
  final_list = []
  words = open(fname, 'r').read()
  for word in words.splitlines():
    m.feed(word)

  #this converts the file 
  with open('words.json', 'w', encoding='utf-8') as json:
    m.write(json)
  with open("words.txt", 'r') as file_handle:
    lines = file_handle.read().splitlines()

  #train it!
  new_model = fictionary.Model(words = ["a"])
  with open('words.json', 'r', encoding='utf-8') as fp:
      new_model.read(fp)
  word = ""
  #get a bunch of random words but make sure it does not print any repeats
  print("running...")
  for i in range(1, wcount):#change this to have it make more words but does raise your On by a lot
    word = m.random_word(mins, maxs)#change words length
    final_list.append(word)
    

  print("""


  """)
  final_list = set(final_list)
  final_list = list(final_list)
  for x in final_list:
    print(x)

  input("press enter to exit")





