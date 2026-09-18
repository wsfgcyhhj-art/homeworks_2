from faker import Faker

fake = Faker('ru_RU')

print(f"Случайное имя: {fake.name()}")
print(f"Случайный адрес: {fake.address()}")