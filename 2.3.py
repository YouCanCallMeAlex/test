s = str(input('придумайте пароль:'))
while len(s) != 0:
  if len(s)<9:
    print('слишком короткий')
    break
    
  elif s.isupper() == 0 and s.islower() == 0:
    print('принято!')
    break
  else:
    print('пароль должен сожердать хотябы по одной букве каждого регистра')
    break