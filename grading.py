python=int(input('enter python marks:'))
saad=int(input('enter saad marks:'))
calculus=int(input('enter calculus marks:'))
research=int(input('enter research marks:'))
#if statement to deal with invalid marks entered
if (python<0 or python>100 or saad< 0 or saad>100 or calculus < 0 or saad >100 or calculus<0 or calculus>100 or research<0 or research>100):
    print('Invalid marks entered.')
else:
  average=(python+saad+calculus+research)/4
print(average)
if(average>=70 and average<=100):
    print ('A')
elif(average>=60 and average<=69):
    print ('B')
elif(average>=50 and average<=59):
    print ('C')
elif(average>=40 and average<=49):
    print ('D')
else:
    print('fail')
