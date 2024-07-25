class car:

    def __init__(self, color, model, brand, age, motorPower):

        self.color = color
        self.model = model
        self.brand = brand
        self.age = age
        self.motorPower = motorPower
    
    def yearManufactured(self):

        print("The " + self.color + " " + self.brand + " " + self.model + " was manufactured in the year " + str(2024 - self.age) + ".")

    def tax(self):
        
        if self.age <= 10:

            tax = (self.motorPower ** 2 * 30) - 20
            print("The " + self.color + " " + self.brand + " " + self.model + " has a tax of $" + str(tax) + " per year.")
        
        elif self.age > 10 and self.age < 20:

            tax = (self.motorPower ** 2 * 20) - 20
            print("The " + self.color + " " + self.brand + " " + self.model + " has a tax of $" + str(tax) + " per year.")
        
        else:
            tax = (self.motorPower ** 2 * 10) - 40
            print("The " + self.color + " " + self.brand + " " + self.model + " has a tax of $" + str(tax) + " per year.")

car1 = car(color = "blue", model = "Mustang", brand = "Ford", age = 0, motorPower = 500)

car.yearManufactured(car1)
car.tax(car1)