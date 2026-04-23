class Recipe:
    def __init__(self, name, ingredients, text, time):
        self._name = name
        self._ingredients = ingredients
        self._text = text
        self._time = time

    def __str__(self):
        return self._name

    def __contains__(self, item):
        return item in self._ingredients

    def __gt__(self, other):
        return self._time > other._time

    def display_info(self):
        print(f"Назва: {self._name}")
        print(f"Інгредієнти: {', '.join(self._ingredients)}")
        print(f"Рецепт: {self._text}")
        print(f"Час приготування: {self._time} хв\n")



recipes = [
    Recipe(
        "Піца",
        ["борошно", "вода", "дріжджі", "томат", "сир"],
        "Готуємо тісто, додаємо інгредієнти та запікаємо",
        30
    ),
    Recipe(
        "Салат",
        ["томат", "огірок", "зелень", "олія"],
        "Нарізаємо овочі, додаємо зелень та поливаємо олією",
        10
    ),
    Recipe(
        "Суп",
        ["вода", "картопля", "морква", "м'ясо"],
        "Варимо всі інгредієнти до готовності",
        45
    )
]


print("Рецепти з інгредієнтом 'томат':")
for r in recipes:
    if "томат" in r:
        print(r)


fastest = min(recipes, key=lambda r: r._time)

print("\nНайшвидший рецепт:")
fastest.display_info()
