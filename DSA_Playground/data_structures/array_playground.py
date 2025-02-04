
def main():
    # Array

    numbers = [1, 2, 3, 4, 5]

    # Default Array Operations
    
    numbers.append(6)
    print("This Operation adds the Number 6 to our Array", numbers)

    numbers.insert(2, 10)
    print("This Operation adds the Number 10 to the third Position", numbers)

    numbers.remove(3)
    print("This Operation removes the fourth Position in our Array", numbers)

    numbers.pop(1)
    print(numbers)

    index = numbers.index(4)
    print(f"{index}")

    numbers.sort()
    print("Sorted Array", numbers)

    numbers.reverse()
    print("Reversed Array", numbers)

if __name__ == "__main__":
    main()



