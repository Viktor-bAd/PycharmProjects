# task 1
n1 = int(input("Enter number1: "))
n2 = int(input("Enter number2: "))
n3 = int(input("Enter number3: "))
print(f"{n1}+{n2}+{n3}={n1+n2+n3}")
print(f"{n1}*{n2}*{n3}={n1*n2*n3}")

# task 2
d1 = int(input("Enter diagonal1: "))
d2 = int(input("Enter diagonal2: "))
print(f"{d1}*{d2}/{2}={d1*d2/2}")

# task 3
n1 = int(input("зарплата: "))
n2 = int(input("Кредит: "))
n3 = int(input("комуналка: "))
print(f"{n1}-{n2}-{n3}={n1-n2-n3}uah")

# task 4
n1 = int(input("Distance/km: "))
n2 = int(input("Fuel rate/l: "))
n3 = int(input("Gas price/uah: "))
print(f"{n1/100*n2*n3}uah")

# task 5
n1 = int(input("Total price: "))
n2 = int(input("Number of people: "))
print("tip=" f"{n1 * 0.15}uah")
print("Price+tip=" f"{n1 + n1 * 0.15}uah")
print("Total price per person=" f"{(n1 + n1 * 0.15) / n2}uah")

# task 6

n1 = int(input("Rental cost/day: "))
n2 = int(input("The number of rental days: "))
n3 = int(input("The deposit: "))
print("The total cost:" f"{n1*n2+n3}uah")
print("Tototal cost - deposite: " f"{n1*n2-n3}uah")
print("Daily total cost: " f"{(n1*n2-n3)/n2}uah")
