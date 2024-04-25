my_dict={'balaji':10,'banana':20,'mango':30,'baskar':40}
for key,value in my_dict.items():
    if key[2].lower()=='l':
        print(f"the value of '{key}' is {value}")
     