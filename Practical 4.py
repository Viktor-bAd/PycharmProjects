# Є текстовий файл. Виведіть кількість рядків та кількість
# символів в ньому

with open("input.txt", encoding="utf-8") as file:
    lines = file.readlines()

line_count = len(lines)
char_count = sum(len(line) for line in lines)

print("Кількість рядків:", line_count)
print("Кількість символів:", char_count)


# Користувач вводить ім’я та вік. Запишіть їх у файл. Назву
# файлу також вводить користувач(без розширення .txt)

name = input("Введіть імя")
age = int(input("Enter age:"))
filename = input("Enter file name:")
age_str = str(age)

with open(filename + ".txt", "w", encoding="utf-8") as f:
    f.write(name)
    f.write("\n")
    f.write(age_str)


# Є текстовий файл. Запишіть його рядки в інший файл.

with open("input.txt", encoding="utf-8") as f1:
    with open("output.txt", "w", encoding="utf-8") as f2:
        for line in f1:
            f2.write(line)


# Користувач вводить літеру та назву файлу. Виведіть усі
# слова з файлу, які починаються на цю літеру.

letter = input("Введіть літеру: ").lower()
filename = input("Введіть назву файлу (з .txt): ")

with open(filename, encoding="utf-8") as file:
    text = file.read()

words = text.split()

for word in words:
    if word.lower().startswith(letter):
        print(word)

# Є текстовий файл. Замініть у ньому усі символи * на &, та
# навпаки.
