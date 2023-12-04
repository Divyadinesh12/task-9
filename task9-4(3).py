#validate telephone numbers of USA
#the standard american telephone number is ten digits such as (123)123-1234.the first three digits are the "area code" 
import re
def main():
  number=input()
  reg="^([+]{1}[1]{1})\([0-9]{3}\)[0-9]{3}-[0-9]{4}$"
  pat=re.compile(reg)
  mat=re.search(pat,number)
  if mat:
    print("mobilenumber is valid")
  else:
    print("mobilenumber invalid")
if __name__=='__main__': 
  main()
