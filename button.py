# button.py

class Button:
    def __init__(self, label, color="grey", width=100, height=50):
        self.label = label
        self.color = color
        self.width = width
        self.height = height
    
    def click(self):
        return f"Button '{self.label}' clicked!"

    def display(self):
        return f"Displaying a {self.color} button with label '{self.label}' of size {self.width}x{self.height}."

# Example usage:
if __name__ == "__main__":
    # Create a new button
    my_button = Button(label="Submit", color="blue", width=150, height=50)
    
    # Display the button
    print(my_button.display())
    
    # Simulate a button click
    print(my_button.click())
