"""
User Class
A simple class to represent a user with name and family name.

"""

class User:
    
    def __init__(self, first_name, last_name):
        
        self.first_name = first_name
        self.last_name = last_name
    
    def get_full_name(self):
        return f"{self.first_name} {self.last_name}"
    
    def get_initial(self):
        return self.first_name[0].upper()
    
    def __str__(self):
        return f"User: {self.get_full_name()}"



# Test


if __name__ == "__main__":
    # Method 1: Get from user input
    print("Enter user information:")
    name = input("First name: ")
    family = input("Last name: ")
    user1 = User(name, family)
    
    # Method 2: Direct assignment
    user2 = User("asal", "nasiri")
    
    # Display results
    print("\n" + "-" * 30)
    print(f"User 1: {user1.get_full_name()}")
    print(f"User 2: {user2.get_full_name()}")
    print(f"User 2 initial: {user2.get_initial()}")
    print(f"User 2 string: {user2}")