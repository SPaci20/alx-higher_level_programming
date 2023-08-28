def safe_print_list(my_list=[], x=0):
    try:
        count = 0
        for i in range(x):
            print(my_list[i], end="")
            count += 1
        print()  # Print a newline after printing elements
        return count
    except IndexError:  # Handle the case when x is larger than the list length
        print()  # Print a newline if the list is exhausted before x elements
        return count
