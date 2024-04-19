def create_profile():
    # Function to create user profile dictionary
    profile = {}  # Initialize an empty dictionary to store user profile
    print("Enter your personal details:")
    profile["Name"] = input("Name: ")  # Get user's name and store it in the dictionary
    profile["Age"] = input("Age: ")  # Get user's age and store it in the dictionary
    profile["Date of Birth"] = input("Date of Birth (YYYY-MM-DD): ")  # Get user's date of birth and store it in the dictionary
    profile["Aadhar Number"] = input("Aadhar Number: ")  # Get user's Aadhar number and store it in the dictionary
    profile["Phone Number"] = input("Phone Number: ")  # Get user's phone number and store it in the dictionary
    profile["Debit Card Number"] = input("Debit Card Number: ")  # Get user's debit card number and store it in the dictionary
    profile["PIN Code"] = input("PIN Code: ")  # Get user's PIN code and store it in the dictionary
    profile["Tax Percent"] = input("Tax Percent: ")  # Get user's tax percentage and store it in the dictionary
    return profile  # Return the user profile dictionary

def main():
    user_profile = create_profile()  # Call the create_profile function to create user profile
    print("\nUser Profile:")  
    for key, value in user_profile.items():  # Iterate through the items (key-value pairs) in the user profile dictionary
        print(f"{key}# {value}",end=',') # Print each key-value pair in the user profile dictionary
    print(user_profile.items())

if __name__ == "__main__":
    main()  # Call the main function to start the program
