class Hero:
    def __init__(self, name: str, lvl: int, hp: int):
        self.name = name
        self.lvl = lvl
        self.hp = hp

    def action(self) -> str:
        return f"{self.name} готов к бою!"


class MageHero(Hero):
    def __init__(self, name: str, lvl: int, hp: int, mp: int):
        super().__init__(name, lvl, hp)
        self.mp = mp

    def action(self) -> str:
        return f"Маг {self.name} кастует заклинание! MP: {self.mp}"


class WarriorHero(MageHero):
    def __init__(self, name: str, lvl: int, hp: int, mp: int = 0):
        super().__init__(name, lvl, hp, mp)

    def action(self) -> str:
        return f"Воин {self.name} рубит мечом! Уровень: {self.lvl}"


class BankAccount:
    def __init__(self, hero: Hero, balance: float, password: str, bank_name: str = "Simba"):
        self.hero = hero
        self._balance = balance
        self.__password = password
        self.bank_name = bank_name

    def login(self, password: str) -> bool:
        return self.__password == password

    @property
    def full_info(self) -> str:
        return f"Герой: {self.hero.name} | Уровень: {self.hero.lvl} | Баланс: {self._balance} SOM"

    def get_bank_name(self) -> str:
        return self.bank_name

    def bonus_for_level(self) -> int:
        return self.hero.lvl * 10

    def __str__(self) -> str:
        return f"{self.hero.name} | Баланс: {self._balance} SOM"

    def __add__(self, other):
        if not isinstance(other, BankAccount):
            return NotImplemented
        
        if type(self.hero) is type(other.hero):
            return self._balance + other._balance
        
        print("Ошибка: Нельзя сложить счета героев разных классов!")
        return ""

    def __eq__(self, other) -> bool:
        if not isinstance(other, BankAccount):
            return False
            
        return (type(self.hero) is type(other.hero)) and (self.hero.lvl == other.hero.lvl)


mage1 = MageHero("Merlin", 50, 100, 150)
warrior = WarriorHero("Conan", 50, 200)
mage2 = MageHero("Merlin", 50, 100, 150)

print(mage1.action())
print(warrior.action())

acc1 = BankAccount(mage1, 5000, "pass123")
acc2 = BankAccount(mage2, 3000, "pass123")
acc3 = BankAccount(warrior, 4000, "pass123")

print(acc1)
print(acc2)

print("Банк:", acc1.get_bank_name())
print("Бонус за уровень:", acc1.bonus_for_level(), "SOM")

print("\n=== Проверка __add__ ===")
print("Сумма счетов двух магов:", acc1 + acc2)

acc1 + acc3

print("\n=== Проверка __eq__ ===")
print("Mage1 == Mage2 ?", acc1 == acc2)
print("Mage1 == Warrior ?", acc1 == acc3)