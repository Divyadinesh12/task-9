import re
def validate_emailaddress(email):
    pattern='^[a-zA-Z0-9]+@[a-zA-Z0-9]+.[a-zA-Z]{2,4}'
    result= re.search(pattern,email)
    if result is not None:
        print("valid")
    else:
        print("invalid")
e_address=input()
validate_emailaddress(e_address)
    

