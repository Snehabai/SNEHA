# File: example.py

def hello():
    print("Hello from module_script.py!")

if __name__ == "__main__":
    #hello()
    print("This script is being run directly.")
else:
    print("This script is being imported as a module.")


'''Purpose:In Python, the __name__ default parameter serves as a built-in
variable that holds the name of the current module or script.
It's a very useful feature that allows you to determine
whether a script is being run directly or being imported as a module into another script '''










# File: example.py

