order = {
    "id": "FLOWER-001",
    "customer": "Анна",
    "recipient": "Мария",
    "product": "Букет роз",
    "price": 2500,
    "quantity": 1,
    "status": "Создан"
}

print("Заказ:", order["id"])
print("Покупатель:", order["customer"])
print("Получатель:", order["recipient"])
print("Товар:", order["product"])
print("Сумма:", order["price"] * order["quantity"], "руб.")
print("Статус:", order["status"])
