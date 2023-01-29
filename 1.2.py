v = int(input('скорость:'))
t = int(input('время:'))
s = v * t 
if s > 109:
  s = (v * t)%109
print(s)