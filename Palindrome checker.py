import time 
word = " "
rev = " " 
name = " "
again = " "
def next ():
    print ("Please enter a word")
    word = input ()
    time.sleep (0.5)
    print ("The word you entered is: %s " %(word))
    word = word.casefold()
    rev = word [::-1]
    time.sleep (1)
    print ("The word you entered written backwards is : %s" %(rev))
    time.sleep (0.5)
    if word == rev:
        print ("It is a palindrome")
    else:
        print ("It is not a palindrome")
    print ("Would you like another try?")
    time.sleep (1)
    print ("Please enter either Yes or No")
    again = input()
    again = again.casefold()
    if again == "yes":
        next()
    else:
        print ("Thanks for playing, %s" %(name))
 
print ("Welcome to my Palindrome checker")
time.sleep (1)
print ("Please enter your name")
name = input()
time.sleep (0.5)
print ("Hello, %s. Here is how it works" %(name))
print ("You enter a word, I check if it is a palindrome or not")
time.sleep (1)
next()
