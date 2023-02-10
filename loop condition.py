first_name = input("Enter your first name")
last_name = input("Enter your last name")
if len(first_name)>0 and len(last_name)>0:
    print("Hye " + first_name +" "+ last_name)
elif len(first_name)>0:
    print("Hello "+ first_name)
elif len(last_name)>0:
    print("Hello "+ last_name)
else :
    print("Hello World")