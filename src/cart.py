cart = [
    {"name": "Розы", "price": 250, "quantity": 3},
    {"name": "Тюльпаны", "price": 150, "quantity": 5},
]

total = sum(
    item["price"] * item["quantity"]
    for item in cart
)

print(f"Стоимость корзины: {total} руб.")
