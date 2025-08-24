x=int(input('Please enter the amount of electricity units you have used in the last 1 month.\n'))
if x<50:
    amount=x*2.60
    surcharge=25
elif x<=100:
    amount=130+((x-50)*3.25)
    surcharge=35
elif x<=200:
    amount=130+162.5((x-100)*5.26)
    surcharge=45
else:
    amount=132+162.50+526+((x-200)*8.45)
    surcharge=75
total=amount+surcharge
print('Your total electricity bill is',total,'.')