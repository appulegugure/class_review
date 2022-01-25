class Customer:
    def __init__(self, first_name, family_name):
        self.fullname = first_name + " " + family_name

    def full_name(self):
        print(self.fullname)


ken = Customer(first_name="Ken", family_name="Tanaka")
ken.full_name()  # "Ken Tanaka" という値を返す

tom = Customer(first_name="Tom", family_name="Ford")
tom.full_name()  # "Tom Ford" という値を返す
