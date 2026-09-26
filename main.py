print("Welcome to The data Analyzer and Transformer Program")

data = []
array_type = 0
a=[]

def input_data():
    print("Select an Option :")
    print("1. 1D Array :")
    print("2. 2D Array :")

    choice = int(input("Enter Your Choice :"))

    if choice == 1:
        """Get Input From user And Store in 1D Array"""
        global data,array_type,a
        array_type=1
        arr = input("Enter data for a 1D array (Separated By Spaces) : ").split()

        for i in arr:
            data.append(i)
            data = list(map(int, arr))

    elif choice == 2:
        array_type=2
        """Get Input From user And Store in 2D Array"""
        rows = int(input("Enter Numbers Of Rows :"))
        cols = int(input("Enter Numbers Of Column :"))
     
        for i in range(rows):
            global l
            l = []
            for j in range(cols):
                num = int(input("Enter The Number :"))
                l.append(num)
            data.append(l)
            print("2D Array :")
            print(l)
            a = []
            
            for i in data:
                a.extend(i)
                    

    else:
        print("Invalid Choice !!")


print("data has been stored Successfully !!!")


def data_summary():
    """Display summary"""
    
    if array_type==1:
        print("data Summary : ")
        print(f"- Total Elements : {len(data)}")
        print(f"- Minimum Value : {min(data)}")
        print(f"- Maximum Value : {max(data)}")
        print(f"- Sum of all values: {sum(data)}")
        print(f"- Average Value : {len(data) / sum(data):.2f}")
        print()
    elif array_type==2:
        
        
        a=[]
        
        a=a.append(data)    
        for i in data:        
             a=list(map(int,i))

        print("data Summary : ")
        print(f"- Total Elements : {len(a)}")
        print(f"- Minimum Value : {min(a)}")
        print(f"- Maximum Value : {max(a)}")
        print(f"- Sum of all values: {sum(a)}")
        print(f"- Average Value : {len(a) / sum(a):.2f}")
        print()
 

def fact(n):
    """Calculate Factorial"""

    if n <= 0:
        return 1
    else:
        return n * fact(n - 1)


def Fact_data():
    num = int(input("Enter Your Number for Factorial: "))
    res = fact(num)
    print(f"Factorial of {num} is : {res}")


def Thresold_data():
    """Filter and display values greater than the threshold."""
    if array_type==1:
        value = int(input("Enter a threshold value:- "))
        res = filter(lambda x: x > value, data)
        print(*res, sep=", ")
    elif array_type==2:
        value1 = int(input("Enter a threshold value:- "))
        res1 = filter(lambda x: x > value1, a)
        print(*res1, sep=", ")



def sort_data():
    """Sort the dataset in ascending or descending order."""

    print("Select An Option (1-2) :")
    print("1. Ascending.")
    print("2. Descending.")

    choice = int(input("Enter Your Choice:-"))

    if choice == 1:
        print("Sorted data in Ascending order:")
        data.sort()
        print(data)

    elif choice == 2:
        print("Sorted data in Descending order:")
        data.sort(reverse=True)
        print(data)

    else:
        print("Invalid Choice!!")


def data_statistics():
    """For Returning minimum, maximum, total, and average values."""
    if array_type==1:

        total = sum(data)
        minimum = min(data)
        maximum = max(data)
        average = sum(data) / len(data)
    
        return minimum, maximum, total, average
    elif array_type==2:
        
        total = sum(a)
        minimum = min(a)
        maximum = max(a)
        average = sum(a) / len(a)
    
        return minimum, maximum, total, average



while True:
    print("")
    print("Main Menu: ")
    print("1. Input data")
    print("2. data Summary (Built-in-Functions)")
    print("3. Calculate Factorial (Recursion)")
    print("4. Filter data By Threshold (Lambda Function)")
    print("5. Sort data")
    print("6. Display data Set Statistics (Return Multiple Values)")
    print("7. Exit Program")
    print()

    choice = int(input("Please Enter Your Choice :- "))
    print()

    if choice == 1:    
        input_data()
    elif choice == 2:
        data_summary()

    elif choice == 3:
        Fact_data()

    elif choice == 4:
        Thresold_data()

    elif choice == 5:
        sort_data()

    elif choice == 6:
        total, minimum, maximum, average = data_statistics()

        print(f"- Minimum Value : {minimum}")
        print(f"- Maximum Value : {maximum}")
        print(f"- Sum of all values : {total}")
        print(f"- Average Value : {average:.2f}")

    elif choice == 7:
        print(
            "Thank you for using The Data Analyzer and Transformer Program."
        )
        break

    else:
        print("Invalid Choice !!")
