# Base class: Smartphone
class Smartphone:
    def _init_(self, brand, model, price):
        self.brand = brand
        self.model = model
        self.price = price
    
    def make_call(self, number):
        return f"{self.brand} {self.model} is calling {number}..."
    
    def send_message(self, number, message):
        return f"Sending message to {number}: {message}"
    
    def browse_internet(self):
        return f"Browsing internet on {self.brand} {self.model}."

# Subclass: GamingSmartphone
class GamingSmartphone(Smartphone):
    def _init_(self, brand, model, price, gaming_mode):
        super()._init_(brand, model, price)
        self.gaming_mode = gaming_mode

    def play_game(self, game):
        mode = "High Performance" if self.gaming_mode else "Normal"
        return f"Playing {game} in {mode} mode."
    
    def enable_gaming_mode(self):
        self.gaming_mode = True
        return "Gaming mode enabled."

# Demonstrating functionality
phone = Smartphone("Samsung", "Galaxy S21", 799)
gaming_phone = GamingSmartphone("Asus", "ROG Phone 5", 999, False)

print(phone.make_call("1234567890"))
print(phone.send_message("9876543210", "Hello, how are you?"))
print(gaming_phone.browse_internet())
print(gaming_phone.play_game("PUBG"))
print(gaming_phone.enable_gaming_mode())
print(gaming_phone.play_game("Fortnite"))
