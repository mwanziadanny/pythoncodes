salary=int(input('Enter salary:'))
years_of_service=int(input('Enter years of service:'))
if(years_of_service>10) :
    bonus=salary*0.1
    print(bonus)
if(years_of_service>=6 and years_of_service<=10):
    bonus=salary*0.08
    print(bonus)
else:
    bonus=salary*0.05
    print(bonus)