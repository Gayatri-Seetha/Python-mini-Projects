from abc import ABC, abstractmethod

class Pinterest(ABC):
    def __init__(self, username):
        self.username = username  # Encapsulation
    
    def display_username(self):
        print(f"Username: {self.username}")

    def display_features(self):
        print("Features: Pinning, Boards, Following, Discovering Ideas")
    
    @abstractmethod
    def display_specific_pins(self):
        pass


class Photography(Pinterest):
    def display_specific_pins(self):  # Override the abstract method
        print(f"{self.username}'s Photography Pins: Nature, Portraits, Landscapes")

    def photography_tips(self):
        print("Photography Tips: Use natural light, Focus on composition, Experiment with angles.")


class DIY(Pinterest):
    def display_specific_pins(self):  # Override the abstract method
        print(f"{self.username}'s DIY Pins: Home Decor, Crafts, Projects")
    
    def DIY_tips(self):
        print("DIY Tips: Plan your projects, use quality materials, Have fun!")


class Travel(Pinterest):
    def display_specific_pins(self):  # Override the abstract method
        print(f"{self.username}'s Travel Pins: Destinations, Travel Tips, Adventures")

    def Travel_tips(self):
        print("Travel Tips: Research your destination, Plan your next day, Stay safe, Pack smart!")


# Creating objects
photography_user = Photography("PhotoLover")
diy_user = DIY("CraftyGirl")
travel_user = Travel("Traveler123")

# Photography user information
print("=== Photography User ===")
photography_user.display_username()  
photography_user.display_features()    
photography_user.display_specific_pins()        # Photography subclass 
photography_user.photography_tips()  
print()  

# DIY user information
print("=== DIY User ===")
diy_user.display_username()
diy_user.display_features()
diy_user.display_specific_pins()   # Subclass
diy_user.DIY_tips()
print()

# Travel user information
print("=== Travel User ===")
travel_user.display_username()
travel_user.display_features()
travel_user.display_specific_pins()  # Subclass
travel_user.Travel_tips()
