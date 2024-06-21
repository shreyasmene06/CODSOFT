import random
def pass_gen(l):                        #used to generate random password
    upper="ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    lower=upper.lower()
    special="!@#$%^&*()_+"
    digit="1234567890"
    password=""
    character="".join(upper+lower+special+digit+special)        #characters adds all different types of values
        
    for i in range(l):    
        password=password+random.choice(character)                #chooses password from the combination of characters
        if len(password)>l:
            break
    return password

def main():
    l=eval(input("Enter length of Password : "))                #main body which acts as a user interface for user and connects all functions while making sure length is within range
    if type(l)==int and l>0:
        print(pass_gen(l))
    else:
        print("Invalid ")
main()

