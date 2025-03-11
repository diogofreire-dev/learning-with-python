with open("names.txt", "r") as file:
    for line in file:
        print("hello,", line.rstrip())


"""    
    lines = file.readlines()

    for line in lines:
        print("hello,", line.rstrip())
"""