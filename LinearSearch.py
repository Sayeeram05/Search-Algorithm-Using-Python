import os   # To Interact with Os

os.system("cls")  # Clear the terminal

print('''Search Algorithms 🔍
    1.Linear Search
        ⭐ First Sorted Array will Printed
        ⭐ Then, You Have to Enter the Number To Search
        ⭐ Program will search and Give the Output\n''')

print("\nLets Start 👍")
array = [2,5,9,10,13,16,19,21,26,27,29,30,35,37,39,40,45,49,50]  # Sorted List

print("\nList = ",end="")
print(*array,sep=", ")  # Print the list with comma seperated

while True:  # Runs until Get the correct Value

    try:  # To Handel the Run Time Errors 
        key = int(input("\nEnter The Number To Search : "))  # Stores the Integer value
        if(key >= 0):
            break  # Loop Will stop 
        else:
            print("❌ Enter Positive Value (Greater Than 0)")
    except ValueError: # if the user entered other than integer 
        print("❌ Invalid Number")

if(key not in array):   # Checks Wether the key is in the array
    print(key,"Is Not In The List")
else:
    print(key,"Is At Index : ",(array.index(key)))  # Print the index of the Key

print("\nThank You ✌️")