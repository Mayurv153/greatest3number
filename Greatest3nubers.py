#This is the method 1
#Largest among three numbers
a=float(input("1st no is:"))
b=float(input("2nd no is:"))
c=float(input("3rd no is:"))
if(a>b and a>c):
  print(a," is the greatest.")
elif(b>a and b>c):
  print(b," is the greatest.")
elif(c>a and c>b):
  print(c," is the greatest.")
else:
  print("Numbers are same.")


#This is the method 2 which uses nested if else statements
a=float(input("1st no:"))
b=float(input("2nd no:"))
c=float(input("3rd no:"))
if(a>=b):
  if(a>c):
    print(a," is greatest.")
  else:
    print(c," is greatest.")
else:
  if(b>c):
    print(b," is greatest.")
  else:
    print(c," is greatest.")
       
                          
    
