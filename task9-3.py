#using lambda function create fibonacci series 1-50 elments
from functools import reduce
fib=lambda n: reduce(lambda x,_:x+[x[-1]+x[-2]],range(n-2),[1,2])
print(fib(8))