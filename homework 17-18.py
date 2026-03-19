# Завдання 1
# Є деякий текст. Порахуйте в цьому тексті кількість речень і виведіть на екран отриманий результат.

text = "Привіт! Як справи? Сьогодні гарна погода."

sentences = text.count('.') + text.count('!') + text.count('?')

print(sentences)

# Завдання 2
# Користувач вводить з клавіатури рядок. Перевірте чи є введений рядок паліндромом.
# Паліндром — слово або текст, що читається однаково зліва направо і справа наліво. Наприклад:
# Кок;
# Козак з казок;
# Радар;
# А мене нема.

text = input("Введіть рядок: ")

clean_text = text.lower()
clean_text = clean_text.replace(" ", "")
clean_text = clean_text.replace(".", "")
clean_text = clean_text.replace(",", "")
clean_text = clean_text.replace("!", "")
clean_text = clean_text.replace("?", "")

reversed_text = ""
i = len(clean_text) - 1

while i >= 0:
    reversed_text += clean_text[i]
    i -= 1

if clean_text == reversed_text:
    print("Рядок є паліндромом")
else:
    print("Рядок не є паліндромом")


# Завдання 3
# Користувач вводить рядок і два символи. Видаліть із рядка всі символи між першим входженням
# першого символу і першим входженням другого символу, включаючи самі символи. Виведіть результат.

text = input("Введіть рядок: ")
char1 = input("Введіть перший символ: ")
char2 = input("Введіть другий символ: ")

index1 = text.find(char1)
index2 = text.find(char2)
if index1 != -1 and index2 != -1 and index1 < index2:
    result = text[:index1] + text[index2 + 1:]
else:
    result = text
print("Результат:", result)
