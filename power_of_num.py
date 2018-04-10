nm=input("enter the num\n")
pw=input("enter the power of number\n")
if nm.isdigit() and pw.isdigit(): 
  res=int(nm) ** int(pw)
  print(res)
else:
  print("input error!")
