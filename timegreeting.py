import time
gm = "Good Morning"
gf = "Good Afternoon"
ge = "Good Evening"
gn = "Good Night"


t = time.localtime()
fti = time.strftime("%H:%M:%S")
print(fti)
hu = time.strftime("%H")
m = time.strftime("%M")
s = time.strftime("%S")
h = int(hu)
tn = 24
te = 21
ta = 15
ts = 12


if h < ts:
  print(gm)
elif h < (ta):
  print(gf)
elif h < te:
  print(ge)
elif h < tn:
  print(gn)
else:
  print("You Noob")
