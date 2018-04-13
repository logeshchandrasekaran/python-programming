def exploder(x,n):
     return x * n 
def my_fun(fun1,aa, stri):
     a=fun1(stri,aa)
     print(a)
stri=input("enter the string")
num=int(input("enter the number of times"))
my_fun(exploder,num,stri)
