def password_check(password):
    length=8
    l=False
    u=False
    d=False
    s=False
    if len(password)>=length:
        for i in password:
            if i.isupper():
                u=True
            elif i.islower():
                l=True
            elif i.isdigit():
                d=True
            else:
                s=True
    else:
        print("Please Enter more than 8 characters")
    
    if u and l and d and s and len(password)>=length:
        print("Strong Password")
    elif u or l and d and len(password)>=length:
        print("Moderate Password")
    else:
        print("Weak Password")


pas=input("Enter Your Password: ")
password_check(pas)