import re
def main():
  password=input()
  reg="^(?=.*[a-z])(?=.*[A-Z])(?=.*\d)(?=.*[@#%&*!?])[a-zA-Z\d@#$%&*?]{16}$"
  pat=re.compile(reg)
  mat=re.search(pat,password)
  if mat:
    print("password is valid")
  else:
    print("password invalid")
if __name__=='__main__': 
  main()


