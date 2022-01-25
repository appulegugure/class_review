class Customer:
    def __init__(self, first_name, family_name, age):
        self.age = age
        self.fullname = first_name + " " + family_name

    def full_name(self):
        return self.fullname

    def entry_fee(self):
        if self.age < 20:
            result = 1000
        elif self.age < 65:
            result = 1500
        else:
            result = 1200
        return result


ken = Customer(first_name="Ken", family_name="Tanaka", age=15)
print(ken.entry_fee())  # 1000 という値を返す

tom = Customer(first_name="Tom", family_name="Ford", age=57)
print(tom.entry_fee())  # 1500 という値を返す

ieyasu = Customer(first_name="Ieyasu", family_name="Tokugawa", age=73)
print(ieyasu.entry_fee())  # 1200 という値を返す
