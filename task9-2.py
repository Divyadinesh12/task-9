#check every element of a list is an integer or string
lst=list(input().split())
result=list(map(lambda x: "integer" if x.isdigit() else"string",lst))
print (result)



                  

