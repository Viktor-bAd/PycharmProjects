# Завдання 1:
# Користувач вводить:
# час відправлення: години h (0–23) і хвилини m (0–59)
# тривалість дороги: t хвилин (може бути більше 60 і навіть більше 1440)
# Потрібно вивести:
# час прибуття у форматі HH:MM
# скільки повних діб пройде під час дороги (0, 1, 2, …)
# Приклад
#
# Ввід: 23 50 і 125
# Прибуття: 01:55
# Діб пройшло: 0 (бо менше 24 год)

h=int(input("Enter Hours:"))
m=int(input("Enter Minutes:"))
t=int(input("Enter Times:"))
start_minutes = h * 60 + m
total = start_minutes + t

days = total // 1440
arrival = total % 1440

hh = arrival // 6010
mm = arrival % 60

print("arrival: " f"{hh:02d}:{mm:02d}")
print("days:",days)


# Завдання 2:
# Умова:
# Користувач вводить 4-значне число (наприклад, 5831). Потрібно:
# вивести окремо кожну цифру (по одній в рядок)
# знайти суму цифр
# сформувати число навпаки (5831 → 1385)
# сформувати число з перших двох цифр і останніх двох цифр (наприклад 58 і 31

n = int(input("Number:"))
a = n // 1000
b = (n // 100) % 10
c = (n // 10) % 10
d = n % 10
print(a)
print(b)
print(c)
print(d)
print("Sum:", a + b + c + d)
print("Revers:",d * 1000 + c * 100 + b * 10 + a )
print("first two=", a * 10 + b)
print("last_two=", c * 10 + d)


# Завдання 3:
# Користувач вводить суму в гривнях (може бути дробова, наприклад 763.28). Треба:
# перевести суму в копійки (ціле число)
# порахувати, скільки потрібно купюр/монет, щоб видати цю суму мінімальною кількістю для номіналів:
# грн: 200, 100, 50, 20, 10, 5, 2, 1
# коп: 50, 25, 10, 5, 2, 1
# Вивести кількість кожного номіналу та підсумкову кількість усіх купюр/монет.


amount = float(input("input amount: "))
coins = round(amount * 100)

print("Total coins:", coins)

n200 = coins // 20000
coins -= n200 * 20000

n100 = coins // 10000
coins -= n100 * 10000

n50 = coins // 5000
coins -= n50 * 5000

n20 = coins // 2000
coins -= n20 * 2000

n10 = coins // 1000
coins -= n10 * 1000

n5 = coins // 500
coins -= n5 * 500

n2 = coins // 200
coins -= n2 * 200

n1 = coins // 100
coins -= n1 * 100

c50 = coins // 50
coins -= c50 * 50

c25 = coins // 25
coins -= c25 * 25

c10 = coins // 10
coins -= c10 * 10

c5 = coins // 5
coins -= c5 * 5

c2 = coins // 2
coins -= c2 * 2

c1 = coins // 1
coins -= c1 * 1

total = n200 + n100 + n50 + n20 + n10 + n5 + n2 + n1 + c50 + c25 + c10 + c5 + c2 + c1

print(f"200 грн: {n200}")
print(f"100 грн: {n100}")
print(f"50 грн: {n50}")
print(f"20 грн: {n20}")
print(f"10 грн: {n10}")
print(f"5 грн: {n5}")
print(f"2 грн: {n2}")
print(f"1 грн: {n1}")
print(f"50 коп: {c50}")
print(f"25 коп: {c25}")
print(f"10 коп: {c10}")
print(f"5 коп: {c5}")
print(f"2 коп: {c2}")
print(f"1 коп: {c1}")
print("Total nominals: ", total)