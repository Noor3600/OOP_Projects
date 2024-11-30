# Python OOP Assignment  

This repository contains the completed tasks for the Python Object-Oriented Programming (OOP) assignment. The assignment demonstrates the use of classes, constructors, inheritance, encapsulation, and polymorphism in Python.

---

## *Assignment 1: Design Your Own Class*  

### Description:  
In this task, we create a class to represent a *Smartphone* and a subclass *GamingSmartphone*.  
The implementation includes:  
- Attributes like brand, model, price, and methods such as make_call(), send_message(), and browse_internet().
- A constructor (__init__) to initialize objects with specific values.
- Inheritance: The GamingSmartphone class inherits from Smartphone and adds additional functionality like play_game() and enable_gaming_mode().

### Example Usage:  
```python
phone = Smartphone("Samsung", "Galaxy S21", 799)
print(phone.make_call("1234567890"))

gaming_phone = GamingSmartphone("Asus", "ROG Phone 5", 999, False)
print(gaming_phone.play_game("PUBG"))