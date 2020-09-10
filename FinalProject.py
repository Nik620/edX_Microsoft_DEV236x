##### [ ] create, call and test the adding_report() function
# then PASTE THIS CODE into edX
total = 0
items = ""

def adding_report(report):
    counter = 0
    total = 0
    items = ""
    while True:
        string = input("Enter an integer or \"Q\": ")
        if string.isdigit():
            if counter >= 1:
                total = total + int(string)
                items = items + "\n" + string 
                counter += 1
            else:
                total = int(string)
                items = string
                counter += 1
        elif (string.upper()).startswith("Q"):
            if report == "A" and counter != 0:
                return print("\nItems\n"+items+"\n\nTotal\n",total)
                break
            elif report == "A" and counter == 0:
                return print("\nItems\n"+""+"\n\nTotal\n",total)
                break
            else:
                return print("\nTotal\n",total)
                break
        else:
            print(string,"is an invalid input")
        
print("Report Types include All Items (\"A\") or Total Only (\"T\")")
report = input("Choose Report Type (\"A\" or \"T\"): ").upper()

while True:
    if report == "A" or report == "T":
        break
    else:
        print(report,"is invalid input")
        report = input("Choose Report Type (\"A\" or \"T\"): ").upper()

print("\nInput an integer to add to the total or \"Q\" to quit")
adding_report(report)
