# Завдання 1
# Написати програму, яка за вибором користувача зводить введене ним число у ступінь від нульового до сьомого включно.

number = float(input("Введіть число: "))
exponent = int(input("Ваш вибір (0-7): "))
if 0 <= exponent <= 7:
    result = number**exponent
    print(f"Результат: {number} у ступені {exponent} = {result}")
else:
    print("Помилка: ви обрали ступінь поза межами дозволеного.")

# Завдання 2
# Написати програму підрахунку вартості розмови для різних мобільних операторів.
# Користувач вводить вартість розмови і вибирає з якого на який оператор він телефонує.
# Вивести вартість на екран.

minutes = float(input("Введіть тривалість розмови (у хвилинах): "))
print("1. Всередині мережі (на того ж оператора) — 0.50 грн/хв")
print("2. На іншого оператора по Україні — 1.50 грн/хв")
print("3. Міжнародний дзвінок — 5.00 грн/хв")
choice = input("Ваш вибір (1, 2 або 3): ")
if choice == "1":
    rate = 0.50
    direction = "всередині мережі"
elif choice == "2":
    rate = 1.50
    direction = "на іншого оператора"
elif choice == "3":
    rate = 5.00
    direction = "за кордон"
else:
    rate = 0
    print("Помилка: невірний вибір напрямку.")
if rate > 0:
    total_cost = minutes * rate
    print(f"Вартість розмови {direction}:")
    print(f"Тариф: {rate} грн/хв")
    print(f"Загальна сума: {total_cost:.2f} грн")

# # Завдання 2
# Користувач вводить із клавіатури число в діапазоні від 1 до 100.
# Якщо число кратне 3 (ділиться на 3 без залишку) потрібно вивести слово Fizz.
# Якщо число кратне 5 потрібно вивести слово Buzz. Якщо число кратне 3 і 5 потрібно вивести Fizz Buzz.
# Якщо число не кратне не 3 і 5 потрібно вивести саме число.
# Якщо користувач ввів значення не в діапазоні від 1 до 100 потрібно вивести повідомлення про помилку.

number = int(input("Введіть число від 1 до 100: "))
if number < 1 or number > 100:
    print("Помилка: число поза діапазоном від 1 до 100!")
else:
    if number % 3 == 0 and number % 5 == 0:
        print("Fizz Buzz")
    elif number % 3 == 0:
        print("Fizz")
    elif number % 5 == 0:
        print("Buzz")
    else:
        print(number)

# Завдання 4
# Зарплата менеджера становить 200$ + відсоток від продажів, продажі до 500$ – 3%, від 500 до 1000 – 5%, понад 1000 – 8%.
# Користувач вводить із клавіатури рівень продажів для трьох менеджерів.
# Визначити їхню зарплату, визначити найкращого менеджера, нарахувати йому премію 200$, вивести підсумки на екран.

base_salary = 200
sales1 = float(input("Введіть обсяг продажів менеджера 1: "))
sales2 = float(input("Введіть обсяг продажів менеджера 2: "))
sales3 = float(input("Введіть обсяг продажів менеджера 3: "))
if sales1 < 500:
    salary1 = base_salary + sales1 * 0.03
elif sales1 <= 1000:
    salary1 = base_salary + sales1 * 0.05
else:
    salary1 = base_salary + sales1 * 0.08
if sales2 < 500:
    salary2 = base_salary + sales2 * 0.03
elif sales2 <= 1000:
    salary2 = base_salary + sales2 * 0.05
else:
    salary2 = base_salary + sales2 * 0.08
if sales3 < 500:
    salary3 = base_salary + sales3 * 0.03
elif sales3 <= 1000:
    salary3 = base_salary + sales3 * 0.05
else:
    salary3 = base_salary + sales3 * 0.08
best_salary = salary1
best_manager = 1
if salary2 > best_salary:
    best_salary = salary2
    best_manager = 2
if salary3 > best_salary:
    best_salary = salary3
    best_manager = 3
if best_manager == 1:
    salary1 += 200
elif best_manager == 2:
    salary2 += 200
else:
    salary3 += 200
print("\nЗарплати менеджерів:")
print("Менеджер 1:", salary1)
print("Менеджер 2:", salary2)
print("Менеджер 3:", salary3)

print("\nНайкращий менеджер: Менеджер", best_manager)
print("Йому нараховано премію 200$")

# Користувач вводить суму кредиту і термін (у роках).
# Програма визначає процентну ставку і розраховує загальну суму до виплати:
# Для кредиту до 10 000$ на строк до 3 років – ставка 8%.
# Для кредиту до 10 000$ на строк понад 3 роки – ставка 10%.
# Для кредиту від 10 001$ до 50 000$ на строк до 3 років – ставка 12%.
# Для кредиту від 10 001$ до 50 000$ на строк понад 3 роки – ставка 15%.
# Для кредиту понад 50 000$ на будь-який термін – ставка 20%.
# Програма виводить підсумкову суму до виплати і щомісячний платіж.

credit = float(input("Введіть суму кредиту ($): "))
years = int(input("Введіть термін кредиту (у роках): "))
if credit <= 10000 and years <= 3:
    rate = 0.08
elif credit <= 10000 and years > 3:
    rate = 0.10
elif credit <= 50000 and years <= 3:
    rate = 0.12
elif credit <= 50000 and years > 3:
    rate = 0.15
else:
    rate = 0.20
total_payment = credit + credit * rate
months = years * 12
monthly_payment = total_payment / months
print("Процентна ставка:", rate * 100, "%")
print("Загальна сума до виплати:", total_payment, "$")
print("Щомісячний платіж:", monthly_payment, "$")

# Ви розробляєте програму для розрахунку вартості комплексного обіду в ресторані.
# Меню складається з трьох категорій: закуска, основна страва і десерт.
# Залежно від вибору клієнта і його статусу програма повинна розрахувати підсумкову вартість
# з урахуванням можливих знижок і спеціальних пропозицій.
# Умови:
# Меню комплексного обіду.
# Закуски:
# Салат – 5$,
# Суп – 7$.
# Основні страви:
# Курка – 10$,
# Риба – 12$.
# Десерти:
# Морозиво – 3$,
# Фрукти – 4$.
# Знижки.
# Якщо клієнт замовляє всі три позиції (закуску, основну страву і десерт), надається знижка 10% на все замовлення.
# Якщо сума замовлення перевищує 20$, знижка збільшується до 15%.
# Для постійних клієнтів надається додаткова знижка 5%, яка підсумовується з іншими знижками.
# Спеціальні пропозиції.
# Якщо клієнт замовляє "Суп" і "Рибу", надається знижка 2$ на десерт.
# Якщо клієнт замовляє "Курку" і "Морозиво", до замовлення додається безкоштовний напій (наприклад, "Чай").
# Підсумкова вартість.
# Програма повинна коректно застосувати всі знижки та спеціальні пропозиції,
# а потім розрахувати підсумкову вартість замовлення.

# Ціни на страви
snack_price = 0
main_price = 0
dessert_price = 0
snack = input("Оберіть закуску (Салат / Суп / Нічого): ")
main = input("Оберіть основну страву (Курка / Риба / Нічого): ")
dessert = input("Оберіть десерт (Морозиво / Фрукти / Нічого): ")
regular = input("Чи є клієнт постійним? (так / ні): ")
if snack == "Салат":
    snack_price = 5
elif snack == "Суп":
    snack_price = 7
if main == "Курка":
    main_price = 10
elif main == "Риба":
    main_price = 12
if dessert == "Морозиво":
    dessert_price = 3
elif dessert == "Фрукти":
    dessert_price = 4
total = snack_price + main_price + dessert_price
discount_percent = 0
if snack_price > 0 and main_price > 0 and dessert_price > 0:
    discount_percent = 10
if total > 20:
    discount_percent = 15
if regular == "так":
    discount_percent = discount_percent + 5
if snack == "Суп" and main == "Риба" and dessert_price > 0:
    dessert_price = dessert_price - 2
    if dessert_price < 0:
        dessert_price = 0
total = snack_price + main_price + dessert_price
free_drink = False
if main == "Курка" and dessert == "Морозиво":
    free_drink = True
total = total - (total * discount_percent / 100)
print("\nПідсумок замовлення:")
print("Сума до оплати:", round(total, 2), "$")
print("Загальна знижка:", discount_percent, "%")
if free_drink:
    print("Бонус: безкоштовний напій (Чай)")
