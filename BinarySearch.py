import os   # To Interact with Os

os.system("cls")  # Clear the terminal

print('''Search Algorithms 🔍
    1.Binary earch
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

else:  # runs only when the key is in the array

    l = 0   # starting index of array
    r = len(array) - 1     # last index of the array

    while True:  # there is no need for l <= r

        m = int((r-l)/2+l)  # middle index of arrat
        #print(array[m])

        if(array[m] == key):  
            print(key,"Is At Index : ",m)  # Print the index of the Key
            break
        elif(array[m] < key) :  # upto array[m] , key is not there
            l = m + 1

        elif(key < array[m]):  # key is present between the l and m-1
            r = m - 1
        
        #print(f"l = {l} r = {r}")
    
print("\nThank You ✌️")
