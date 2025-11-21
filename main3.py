user_level=int(input("Enter your level: "))
passcode=(input("Enter the passcode"))
if user_level>=5:
    print("Level check passed")
    if passcode==passcode:
        print("Welcome to the meeting!!")
    else:
        print("Correct level,wrong passcode:")
else:
    print("user level too low")