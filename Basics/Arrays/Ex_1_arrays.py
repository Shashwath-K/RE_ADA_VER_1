import sys
if __name__ == "__main__":
    int_array = [0] * 5 # Create a Statically allocated array of integers
    print(int_array)
    int_array_dynamic =[] # Create a Dynamically allocated array of integers
    for i in range(5):
        int_array_dynamic.append(i)
    print(int_array_dynamic)
    # This can be done for other data types as well
    # now for the Command line arguments
    n=int(input("Enter the number of elements: "))
    cmd_array = [0] * n
    for i in range(n):
        cmd_array[i] = int(input(f"Enter element {i+1}: "))
    print("The command line array is:", cmd_array)
    # To get the size of the array
    print("Size of statically allocated array:", sys.getsizeof(int_array), "bytes")
