# [ ] create, call and test the str_analysis() function  
# then PASTE THIS CODE into edX  

# Created May 8, 2020

def str_analysis(string):
    if string.isdigit():
        string = int(string)
        if string > 99:
            return print(string,"is a pretty big number")
        else:
            return print(string,"is a smaller number than expected")
    elif string.isalpha():
        return print("\""+string+"\" is all alphabetical characters!")
    else:
        return print("Thats neither a digit nor an alpha")

msg = input("enter a word or integer: ")

while True:
    if msg:
        break
    else:
        msg = input("enter a word or integer: ")
        
str_analysis(msg)
