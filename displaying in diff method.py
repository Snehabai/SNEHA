Employee={"name":"rizwan","age":70,"date_of_birth":"10/09/2002","Debit_card_no":98542125823,"tax_persentage": 12.5,"Hight":5.6,
          "Adhar_no":973838927426,"Ph_no":9740608412,"pin_no":583101}
print(type(Employee))
print("printing Employee data .... ")        
print(Employee)        
print("Enter the details of the new employee....");        
Employee["Name"] = input("Name: ");        
Employee["age"] = int(input("age: "));        
Employee["date_of_birth"] = str(input("date_of_birth: "));        
Employee["Adhar_no"] = int(input("Adhar_no:"));
Employee["Debit_card_no"] = int(input("Debit_card_no:"));
Employee["pin_no"] = int(input("pin_no:"));
Employee["Hight"] = float(input("Hight:"));
Employee["tax_persentage"] = float(input("tax_persentage:"));
Employee["Ph_no"] = int(input("Ph_no:"));
print("printing the new data",end=' ');        
#print(Employee)
print("*********************************************")
#values
#print("printing  all values one by one
print(Employee)
print("printing  all values")
for x in Employee:        
    print(Employee[x])
    
print("*********************************************")    
# display value in single line
print("print all value in single line")
print(Employee.values())
print("*********************************************")
#keys
print(Employee)
print("printing all the keys")
for x in Employee:        
        print(x)                    
        
print("*********************************************")
#items
print("printging all the items in single lines")
print(Employee)
for x in Employee.items():
    print(x)
    
print("*********************************************")
# key segrated by #
print("all the keys segrated by #")
print(Employee)
values='   #  '.join([f"{key}" for key,value in Employee.items()])
print(values)
print("*********************************************")
#all key and value segragted by ,
print("all the key and value segrated by ,")
print(Employee)
values=" , ".join(["{key}:{value}"for key,value in Employee.items()])
print(values)




      