#1.list[10,501,22,37,100,999,87,351] your task is to create two list one which have all the even numbers and another list which will have all the odd numbers in it?

# Given list
numbers = [10, 501, 22, 37, 100, 999, 87, 351]

# Separate even and odd numbers using list comprehensions
even_numbers = [num for num in numbers if num % 2 == 0]
odd_numbers = [num for num in numbers if num % 2 != 0]

# Output the results
print("Even numbers:", even_numbers)
print("Odd numbers:", odd_numbers)

#Output
Even numbers: [10, 22, 100]
Odd numbers: [501, 37, 999, 87, 351]


#2.python list [10,501,22,37,100,999,87,351] your task is to count all the prime numbers and create a new python list which will contain all the prime numbers in it

# Given list
numbers = [10, 501, 22, 37, 100, 999, 87, 351]

# Function to check if a number is prime
def is_prime(n):
    if n <= 1:  # Numbers less than or equal to 1 are not prime
        return False
    for i in range(2, int(n**0.5) + 1):  # Check divisors up to square root of n
        if n % i == 0:
            return False
    return True

# Filter prime numbers from the list
prime_numbers = [num for num in numbers if is_prime(num)]

# Count the number of prime numbers
prime_count = len(prime_numbers)

# Output the results
print("Prime numbers:", prime_numbers)
print("Count of prime numbers:", prime_count)

Prime numbers: [37]
Count of prime numbers: 1

#Output
This output shows that 37 is the only prime number in the given list.


#3.Python list [10,501,22,37,100,999,87,351] Find out how many numbers are there in the given Python list which are Happy Numbers

# Given list
numbers = [10, 501, 22, 37, 100, 999, 87, 351]

# Function to check if a number is Happy
def is_happy_number(n):
    seen = set()
    while n != 1 and n not in seen:
        seen.add(n)
        n = sum(int(digit) ** 2 for digit in str(n))  # Sum of squares of digits
    return n == 1

# Filter happy numbers from the list
happy_numbers = [num for num in numbers if is_happy_number(num)]

# Count the number of happy numbers
happy_count = len(happy_numbers)

# Output the results
print("Happy numbers:", happy_numbers)
print("Count of happy numbers:", happy_count)

#Output
Happy numbers: [10, 100]
Count of happy numbers: 2


#4.Write a python program to find the sum of the first and last digit of an integer

# Function to calculate the sum of the first and last digit
def sum_first_last_digit(number):
    # Convert the number to a string 
    num_str = str(abs(number))  # Use abs() to handle negative numbers
    first_digit = int(num_str[0])  # First digit
    last_digit = int(num_str[-1])  # Last digit
    return first_digit + last_digit

# Input from the user
number = int(input("Enter an integer: "))

# Calculate the sum of the first and last digit
result = sum_first_last_digit(number)

# Output the result
print(f"The sum of the first and last digit of {number} is: {result}")


#5.

def minimize_mango_difference(mango_bags, M):
    # Sort the list of mangoes
    mango_bags.sort()

    # Initialize the minimum difference
    min_difference = float('inf')

    # Iterate over the sorted list with a sliding window of size M
    for i in range(len(mango_bags) - M + 1):
        # Calculate the difference between max and min in the current window
        difference = mango_bags[i + M - 1] - mango_bags[i]
        # Update the minimum difference
        min_difference = min(min_difference, difference)

    return min_difference

# Example 
mango_bags = [10, 20, 30, 100, 200, 300, 1000]
M = 3  # Number of students
result = minimize_mango_difference(mango_bags, M)
print(f"The minimum difference is: {result}")


#6.You have been given three lists. Your task is to find the duplicates in the three lasts. Write a python for the same. You can use your own python lists

# lists
list1 = [1, 2, 3, 4, 5]
list2 = [3, 4, 5, 6, 7]
list3 = [5, 6, 7, 8, 9]

def find_duplicates(list1, list2, list3):
    # Combine all lists
    combined_list = list1 + list2 + list3
    
    # Use a dictionary to count occurrences
    element_count = {}
    for item in combined_list:
        element_count[item] = element_count.get(item, 0) + 1
    
    # Find elements that appear in at least two of the lists
    duplicates = [item for item, count in element_count.items() if count > 1]
    
    return duplicates

# Find and print duplicates
duplicates = find_duplicates(list1, list2, list3)
print("Duplicates across the three lists:", duplicates)

#Output
Duplicates across the three lists: [3, 4, 5, 6, 7]


#7.Write a python program to find the first non-repeating elements in a given list of integers

def first_non_repeating_element(nums):
    # Create a dictionary to count occurrences of each number
    count = {}
    for num in nums:
        count[num] = count.get(num, 0) + 1

    # Iterate through the list to find the first non-repeating element
    for num in nums:
        if count[num] == 1:
            return num

    # If no non-repeating element is found
    return None

# Example
nums = [9, 4, 9, 6, 7, 4]
result = first_non_repeating_element(nums)
if result is not None:
    print(f"The first non-repeating element is: {result}")
else:
    print("No non-repeating element found.")

#Output
The first non-repeating element is: 6

#8.Write a python to find the minimum element in a rated and sorted list

def find_min_in_rotated_sorted_list(nums):
    # If the list has only one element or is not rotated
    if len(nums) == 1 or nums[0] < nums[-1]:
        return nums[0]

    # Binary search to find the minimum element
    left, right = 0, len(nums) - 1
    while left < right:
        mid = (left + right) // 2

        # If the middle element is greater than the rightmost, the minimum is in the right half
        if nums[mid] > nums[right]:
            left = mid + 1
        else:
            # Otherwise, the minimum is in the left half
            right = mid

    return nums[left]  # or nums[right], as left == right

# Example 
rotated_sorted_list = [4, 5, 6, 7, 0, 1, 2]
min_element = find_min_in_rotated_sorted_list(rotated_sorted_list)
print(f"The minimum element is: {min_element}")

#Output
The minimum element is: 0


#9.You have been given a python list[10,20,30,9]and a value of 59. Write a python program to find the triplet in the list whose sum is equal to the given value?

def find_triplet_with_sum(nums, target):
    n = len(nums)
    for i in range(n - 2):
        for j in range(i + 1, n - 1):
            for k in range(j + 1, n):
                if nums[i] + nums[j] + nums[k] == target:
                    return nums[i], nums[j], nums[k]
    return None

# Example 
nums = [10, 20, 30, 9]
target = 59

triplet = find_triplet_with_sum(nums, target)
if triplet:
    print(f"Triplet found: {triplet}")
else:
    print("No triplet found.")

#Output
Triplet found: (10, 20, 9)














