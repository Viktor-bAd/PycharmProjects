# Завдання 1

text = "привіт! як твої справи? мені 37 років. я навчаюся в шаге ! це круто!!!"

sentences = text.split(". ")

new_text = []

for s in sentences:
    s = s.strip()
    if s:
        s = s[0].upper() + s[1:]
        new_text.append(s)

new_text = ". ".join(new_text)

digits_count = 0
for ch in text:
    if ch.isdigit():
        digits_count += 1

punctuation = ".,!?;:"
punct_count = 0

for ch in text:
    if ch in punctuation:
        punct_count += 1

exclam_count = text.count("!")

print(new_text)

print("Кількість цифр:", digits_count)
print("Кількість розділових знаків:", punct_count)
print("Кількість знаків оклику:", exclam_count)


# Завдання 2

nums = list(map(int, input("Введіть числа через пробіл: ").split()))

unique = []

for n in nums:
    if n not in unique:
        unique.append(n)

print("Унікальні числа:", unique)