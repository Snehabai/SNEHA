months=['january','february','march','april','may','june','july','august','september','october','november','december']
month=input('enter month:')
if month.lower() in months:
    if month in ['february']:
        print(month," has 28/29 days")
    elif month in ['january','march','may','july','august','october','december']:
        print(month,'has 31 days')
    else:
        print(month,'has 30 days')
else:
    print('invalid input')