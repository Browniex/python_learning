y = "Brownie from Delhi"
print(y[::-1]) #reverse slicing 

a = input("Enter Your Xyz: ")
b = int(input("Enter Your number: "))
ta = input("Enter your task left and Right")
l = len(a)

if ta == "Right":
  print(a[l-b::]) #right to left
elif ta == "Left":
   if b > l:
     print("Enter less number if characters ")
   else:
     print(a[b])
else:
  print("You Noob")
