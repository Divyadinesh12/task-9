#validate bangladesh mobile number
#Bangladesh country code +880 and national number 6-10 digits 
#Allowed mobile number sample +8801812598624,01812598624
import re
def main():
  mobile_number=input()
  reg="^([+]{1}[8]{2}|0088)?(01){1}[3-9]{1}\d{8}$"
  pat=re.compile(reg)
  mat=re.search(pat,mobile_number)
  if mat:
    print("mobile number is valid")
  else:
    print("mobile number invalid")
if __name__=='__main__': 
  main()

