import random
def pass_gen(l):
    upper="ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    lower=upper.lower()
    special="!@#$%^&*()_+"
    digit="1234567890"
    password=""
    character="".join(upper+lower+special+digit+special)
        
    for i in range(l):
        password=password+random.choice(character)
        if len(password)>l:
            break
    return password

def main():
    l=eval(input("Enter length of Password : "))
    if type(l)==int and l>0:
        print(pass_gen(l))
    else:
        print("Invalid ")
main()

