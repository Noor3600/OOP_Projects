Python OOP Assignment

This repository contains the completed tasks for the Python Object-Oriented Programming (OOP) assignment. The assignment demonstrates the use of classes, constructors, inheritance, encapsulation, and polymorphism in Python.


---

Assignment 1: Design Your Own Class

Description:

In this task, we create a class to represent a Smartphone and a subclass GamingSmartphone.
The implementation includes:

Attributes like brand, model, price, and methods such as make_call(), send_message(), and browse_internet().

A constructor (_init_) to initialize objects with specific values.

Inheritance: The GamingSmartphone class inherits from Smartphone and adds additional functionality like play_game() and enable_gaming_mode().


Example Usage:

phone = Smartphone("Samsung", "Galaxy S21", 799)
print(phone.make_call("1234567890"))

gaming_phone = GamingSmartphone("Asus", "ROG Phone 5", 999, False)
print(gaming_phone.play_game("PUBG"))


---

Activity 2: Polymorphism Challenge

Description:

This task demonstrates polymorphism by creating a base class Vehicle with a method move() and multiple subclasses (Car, Plane, Boat). Each subclass overrides the move() method to provide specific behavior.

Example Usage:

vehicles = [Car(), Plane(), Boat()]

for vehicle in vehicles:
    print(vehicle.move())


---

How to Run

1. Clone the repository:

git clone https://github.com/Noor3600/OOP_Projects.git


2. Navigate to the project directory:

cd Python-OOP-Assignment


3. Run the files:

For Assignment 1:

python assignment1.py

For Activity 2:

python activity2.py





---

Technologies Used

Python 3.x



---

License

This project is licensed under the MIT License. Feel free to use or modify the code as needed.
