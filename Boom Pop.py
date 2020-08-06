def boomPop(userEntry):
    if userEntry % 10 == 0:
        print("boompop")
    elif userEntry % 5 == 0:
        print("pop")
    elif userEntry % 2 == 0:
        print("boom")

user = int(input("Please enter an integer. If it is divisble by 2, 5, or 10, you will see ""boom"", ""pop"", or ""boompop"" repsectively"))
boomPop(user)
