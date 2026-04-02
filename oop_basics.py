class Person:
    body_count = 0

    def __init__(self, name, age, height):
        self.name = name
        self.age = age
        self.height = height
        Person.body_count += 1

p = Person("Owen", 22, 180.9)
p1 = Person("Gayle", 21, 188.9)

print("{} is {} years old. ".format(p.name, p.age))
print("{} is {} years old. ".format(p1.name, p1.age))
print("You have created {} people".format(Person.body_count))

class Worker(Person):
    def __init__(self, name, age, height, salary):
        super().__init__(name, age, height)
        self.salary = salary

worker = Worker("Owen", 22, 222, 22222)
print("{} gets paid ${} ".format (worker.name, worker.salary))

class Musician(Person):
    def __init__(self, name, age, height, instrument):
        super().__init__(name, age, height)
        self.instrument = instrument
musician = Musician("Bob", 33, 190, "Guitar")
print("{} plays the {}.".format(musician.name, musician.instrument))

print("You have created {} people".format(Person.body_count))


class Backpack:

    number_of_backpacks = 0

    def __init__(self):
        self.number_of_backpacks = Backpack.number_of_backpacks

        Backpack.number_of_backpacks +=1

backpack = Backpack()
print(backpack.number_of_backpacks)
backpack1 = Backpack()
print(backpack1.number_of_backpacks)
backpack2 = Backpack()
print(backpack2.number_of_backpacks)


class Circle:
    def __init__(self, radius):
        self._radius = radius

    def get_radius(self):
        return self._radius

    def set_radius(self, new_radius):
        if isinstance(new_radius, float) and new_radius > 0:
            self._radius = new_radius
        else:
            print("Must be a float", new_radius)

    # Property******
    radius = property(get_radius, set_radius)


circle = Circle(2.90)
print(circle.get_radius())

# circle.set_radius(5.90)
print("New radius is ", circle.get_radius())

print("Radius: " , circle.radius)

#  @property() as getters and setter ****
class Movie:
    def __init__(self, title, rating):
        self.title = title
        self._rating = rating

    @property
    def rating(self):
        return self._rating

    @rating.setter
    def rating(self, new_rating):
        if isinstance(new_rating, int) and (new_rating == 15 or new_rating == 18):
            self._rating = new_rating
        else:
            print("Not a valid age")

movie = Movie("Jaws", 15)
print("Rating: ", movie.rating)

print("Update rating")
movie.rating = 18
print("New rating: ", movie.rating)

class Backpack1:
    def __init__(self):
        self._items = []

    @property
    def items(self):
        return self._items

    @items.setter
    def items(self, new_items):
        if isinstance(new_items, list):
            self._items = new_items
        else:
            print("Must be a list")


    # Call a method from inside a method******
    def add_multiple_items(self, items):
        for item in items:
            self.add_items(item)
        return self


    def add_items(self, item):
        if isinstance(item, str):
            self._items.append(item)
        else:
            print("Must provide an item")
        return self


    def show_items(self, sorted_list=False):
        if sorted_list:
            print(sorted(self._items))
        else:
            print(self._items)
        return self

    def delete_items(self, item):
        if isinstance(item, list):
            for i in item:
                if i in self._items:
                    self._items.remove(i)
        else:
            print("Must provide an item")
        return self

backpack1 = Backpack1()
backpack1.items = ["cup", "food"]

backpack1.add_items("torch")
backpack1.add_items("bag")
backpack1.show_items()
backpack1.show_items(True)


print(backpack1.items)
backpack1.show_items(True)

# chain methods by returning self in the method
backpack1.add_multiple_items(["money", "phone", "wallet"]).show_items(True)

backpack1.delete_items(["money", "phone", "wallet"])
#  OR
(
    backpack1.add_multiple_items(["money", "phone", "wallet"])
    .show_items(True)
)


# Class Aggregation *****
class Vehicle:

    def __init__(self, colour, plate, is_electric):
        self.colour = colour
        self.plate = plate
        self.is_electric = is_electric

    def show_plate(self):
        print(self.plate)

    def show_info(self):
        print("My Vehicle:")
        print(f"Color: {self.colour}")
        print(f"Plate: {self.plate}")
        print(f"Electric: {self.is_electric}")


class Employee:

    def __init__(self, name, vehicle):
        self.name = name
        self.vehicle = vehicle

    def show_vehicle_info(self):
        self.vehicle.show_info()

black_vehicle = Vehicle("Black", "ABC-123", is_electric=False)
black_vehicle.show_info()
employee = Employee("Alex", black_vehicle)
employee.show_vehicle_info()
print(employee.vehicle.is_electric)
employee.vehicle.show_plate()


