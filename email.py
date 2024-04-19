'''uemail="sneha2@gamil.com"
upwd=1234
emailid=str(input("enter emailid"))
password=int(input("enter password"))
if(emailid==uemail and password==upwd):
    print("login sucess")
else:
    print("loin failed")'''

'''email="sneha2@gmail.com"
pwd=1235
uemail=str(input("enter the email"))
upwd=int(input("enter the pwd"))
if(email==uemail):
    if(pwd==upwd):
        print("login suce")
    else:
        print("login failed due to incorrect pwd")
else:
    print("login failed due to incoreect email")'''

email="sneha2@gmail.com"
pwd=1235
otp=345
uemail=str(input("enter the email"))
upwd=int(input("enter the pwd"))
uotp=int(input("rnter the otp"))
if(email==uemail):
    if(pwd==upwd):
        print("login suce")
        uotp=int(input("rnter the otp"))
        if(otp!=uotp):
           print("trassaction failed due to wrong otp")
        else:
            print("trassaction successfull")
    else:
        print("login failed due to incorrect pwd")
else:
    print("login failed due to incoreect email")





