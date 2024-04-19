"""def print_v_pattern(name):
#n=int(input('enter name'))
    n=len(name)
    for i in range(n):
        for j in range(n*2):
            if i==j or j==n*2-1-i:
                print(name[i],end=' ')
            else:
                print(' ',end=' ')
        print()
name="sneha"
print_v_pattern(name)"""

'''import datetime #This line imports the datetime module, which provides classes for manipulating dates and times.
today_date=datetime.date.today() #This line gets today's date using the today() function of the date class in the datetime module. It returns a date object representing the current date.
current_time=datetime.datetime.now().time() #his line gets the current time using the now() function of the datetime class in the datetime module. It returns a datetime object representing the current date and time. Then .time() is used to extract only the time part.
today_day=today_date.strftime("%A") #This line formats the today_date using the strftime() method to get the name of the day (like Monday, Tuesday, etc.). %A is the format code for the full name of the day of the week.
print("today date",today_date)
print("current time",current_time)
print("today day",today_day)'''



'''name=str(input("enter name:"))
length=len(name)
for i in range(length):
    for j in range(length):
        if i==0 or i==length or i == length-1 or i+j==length-1:
            print(name[j],end=" ")
        else:
            print(" ",end=" ")
    print()'''


