class CreditCardPayment:
    def __init__(self, currency):
        self._currency = currency

    def pay(self, amount):
        print(f"Оплата карткою {amount}{self._currency}")


class PayPalPayment:
    def __init__(self, currency):
        self._currency = currency

    def pay(self, amount):
        print(f"Оплата PayPal {amount}{self._currency}")


class CryptoPayment:
    def __init__(self, currency):
        self._currency = currency

    def pay(self, amount):
        print(f"Оплата криптогаманцем {amount}{self._currency}")


def create_payment():
    payment_type = input("Введіть тип оплати (card/paypal/crypto): ").lower()
    currency = input("Введіть валюту (наприклад: грн, $, €): ")

    if payment_type == "card":
        return CreditCardPayment(currency)
    elif payment_type == "paypal":
        return PayPalPayment(currency)
    elif payment_type == "crypto":
        return CryptoPayment(currency)
    else:
        print("Невідомий тип оплати.")
        return None




payments = []

n = int(input("Скільки оплат створити? "))

for _ in range(n):
    payment = create_payment()
    if payment:
        payments.append(payment)

print("\n--- Виконання оплат ---")

for p in payments:
    amount = float(input("Введіть суму оплати: "))
    p.pay(amount)
