# Develop the following code and refactor it using the Factory Design Pattern.
# Refer to the content on BB, slide 16, Week 7. Share your GitHub link with your description .
class RedCarMaker:
    def make_car(self, size):
        print(f"This is from red car, and size to make is {size}")


class BlueCarMaker:
    def make_car(self, size):
        print(f"This is from blue car, and size to make is {size}")


class BlackCarMaker:
    def make_car(self, size):
        print(f"This is from black car, and size to make is {size}")


def car_production_factory(car_color, size):
    if car_color is None:
        print("Can't create any car, please specify car color....")
    elif car_color == "red":
        maker = RedCarMaker()
    elif car_color == "blue":
        maker = BlueCarMaker()
    elif car_color == "black":
        maker = BlackCarMaker()
    else:
        print("Sorry, couldn't create any car...")

    maker.make_car(size)


if __name__ == "__main__":
    car_production_factory("blue", 200)
