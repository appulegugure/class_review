class Customer:
    def __init__(self, first_name, family_name, age):
        self.fullname = first_name + " " + family_name
        self.age = age
        if self.age < 20:
            self.entry_tree = 1000
        elif self.age < 65:
            self.entry_tree = 1500
        else:
            self.entry_tree = 1200

    def full_name(self):
        return self.fullname

    def info_csv(self):
        print(','.join([self.fullname, str(self.age), str(self.entry_tree)]))


ken = Customer(first_name="Ken", family_name="Tanaka", age=15)
ken.info_csv()  # "Ken Tanaka,15,1000" という値を返す

tom = Customer(first_name="Tom", family_name="Ford", age=57)
tom.info_csv()  # "Tom Ford,57,1500" という値を返す.

ieyasu = Customer(first_name="Ieyasu", family_name="Tokugawa", age=73)
ieyasu.info_csv()  # "Ieyasu Tokugawa,73,1200" という値を返す
