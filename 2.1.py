a = int(input('первое число:'))
b = int(input('второе число:'))
c = int(input('третье число:'))
if a == b == c:
  print(3)
elif a==b or a==c or c==b:
  print(2)
else:
  print(0)