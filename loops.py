#qs1
numbers = [12, 7, 5, 18, 24, 3, 9]
Even_count = 0
Odd_count = 0
for num in numbers:
    if num % 2 == 0:
        Even_count += 1
    else:
        Odd_count += 1
print(f"Even count: {Even_count}")
 print(f"Odd count: {Odd_count}")


# # #qs2

# # text = "python"
# # reversed_text = ""
# # for char in text:
# #     reversed_text = char + reversed_text
# # print(reversed_text)

# # #qs3


# print("Enter number: ")
# number = int(input())
# for i in range(1, 11):
#     result = number * i
#     print(f"{number} x {i} = {result}")


# #Qs4

# numbers = [4, 15, 2, 89, 23]
# largest = numbers[0]
# for num in numbers:
#     if num > largest:
#         largest = num
# print(f"Largest number: {largest}")


#Qs5

print ("Enter a number: ")
number = int(input())
is_prime = True
if number <= 1:
    is_prime = False
else:
    for i in range(2, int(number**0.5) + 1):
        if number % i == 0:
            is_prime = False
            break
if is_prime:
    print(f"{number} is a prime number")
else:
    print(f"{number} is not a prime number")

#Qs6

for i in range(1, 6):
    for j in range(i):
        print("*", end="")
    print()


#Qs7


attempts = 3
while attempts > 0:
    print("Enter PIN: ")
    input_pin = int(input())
    if input_pin == correct_pin:
        print("Access granted")
        break
    else:
        attempts -= 1
        print("Wrong PIN")
        if attempts == 0:
            print("Card blocked")
