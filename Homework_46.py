# Завдання 1

with open("input.txt", "r", encoding="utf-8") as f:
    text = f.read()

chars_count = len(text)
lines_count = text.count("\n") + 1 if text else 0
digits_count = sum(c.isdigit() for c in text)
vowels = "aeuioAEUIO"
vowels_count = sum(c in vowels for c in text)

with open("output.txt", "w", encoding="utf-8") as f:
    f.write(f"Кількість символів: {chars_count}\n")
    f.write(f"Кількість рядків: {lines_count}\n")
    f.write(f"Кількість цифр: {digits_count}\n")
    f.write(f"Кількість голосних: {vowels_count}\n")


# Завдання 2

word = input("Введіть слово: ")
filename = input("Введіть назву файлу: ")

with open(filename, "r", encoding="utf-8") as f:
    text = f.read()

words = text.split()

count = words.count(word)

print(f"Слово '{word}' зустрічається {count} разів")


# Завдання 3

with open("input.txt", "r", encoding="utf-8") as f:
    lines = f.readlines()

if lines:
    lines = lines[:-1]

with open("input.txt", "w", encoding="utf-8") as f:
    f.writelines(lines)
