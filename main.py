
print("Welcome to The Data Analyzer and Transformer Program")

data = []



def input_data():
    """Get input from user and store in 1D or 2D Array"""
    global data

    print("Select an Option:")
    print("1. 1D Array")
    print("2. 2D Array")

    choice = int(input("Enter Your Choice: "))

   

    if choice == 1:
        """Get input from user and store in 1D Array"""
       

        entered_values = input("Enter data for a 1D array (Separated By Spaces): ").split()

        data = list(map(int, entered_values))
        

        print("Data has been stored successfully!")

    elif choice == 2:
        """Get input from user and store in 2D Array"""
        

        rows = int(input("Enter Number Of Rows: "))
        cols = int(input("Enter Number Of Columns: "))

        for i in range(rows):
            row = []

            for j in range(cols):
                num = int(input("Enter The Number: "))
                row.append(num)

            data.append(row)

        
def converter(data):
    """Flatten nested row data into a 1D list when needed."""
    if len(data)>0 and isinstance(data[0],list):
        flat_values=[]
        for i in data:
            flat_values.extend(i)
        return flat_values
    else:
        return data

def data_summary():
    """Display a summary of the current dataset."""

    values=converter(data)
   
    print("Data Summary:")
    print(f"- Total Elements: {len(values)}")
    print(f"- Minimum Value: {min(values)}")
    print(f"- Maximum Value: {max(values)}")
    print(f"- Sum of all values: {sum(values)}")
    print(f"- Average Value: {sum(values) / len(values):.2f}")
    print()


def fact(n):
    """Calculate Factorial"""

    if n < 0:
        return None

    if n == 0 or n == 1:
        return 1

    return n * fact(n - 1)


def Fact_data():
    """Calculate Factorial of a number using recursion."""
    num = int(input("Enter Your Number for Factorial: "))

    if num < 0:
        print("Factorial is not defined for negative numbers.")
        return

    res = fact(num)
    print(f"Factorial of {num} is: {res}")


def Thresold_data():
    """Filter and display values greater than the threshold."""
    values=converter(data)
    

    value = int(input("Enter a threshold value: "))

    ans = filter(lambda x: x > value, values)
    print(*ans,sep=", ")
    
    print("Values greater than threshold:")
    


def sort_data():
    """Sort the dataset in ascending or descending order."""

    values=converter(data)

    print("Select An Option (1-2):")
    print("1. Ascending")
    print("2. Descending")

    choice = int(input("Enter Your Choice: "))

    if choice == 1:
        values.sort()
        print("Sorted data in Ascending order:")
        print(values)

    elif choice == 2:
        values.sort(reverse=True)
        print("Sorted data in Descending order:")
        print(values)

    else:
        print("Invalid Choice!!")


def data_statistics(*value):
    """Return minimum, maximum, total, and average values."""
    print("Data Statistics : ")
    minimum = min(value)
    maximum = max(value)
    total = sum(value)
    average = sum(value) / len(value) 

    return minimum, maximum, total, average
    




while True:

    print()
    print("Main Menu:")
    print("1. Input Data")
    print("2. Data Summary (Built-in Functions)")
    print("3. Calculate Factorial (Recursion)")
    print("4. Filter Data By Threshold (Lambda Function)")
    print("5. Sort Data")
    print("6. Display Data Set Statistics (Return Multiple Values)")
    print("7. Exit Program")
    print()

    choice = int(input("Please Enter Your Choice: "))
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
        values=converter(data)
        minimum, maximum, total, average = data_statistics(*values)
        print(f"- Minimum Value: {minimum}")
        print(f"- Maximum Value: {maximum}")
        print(f"- Sum of all values: {total}")
        print(f"- Average Value: {average:.2f}")
    elif choice == 7:
        print("Thank you for using The Data Analyzer and Transformer Program.")
        break

    else:
        print("Invalid Choice!!")
