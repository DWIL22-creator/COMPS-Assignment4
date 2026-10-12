# Pick one question from timed_challenge.txt
# Paste the question as a comment below
#15. Reverse Characters
#Reverse a string using custom logic, not slicing or built-in methods.
#Input: "hello"
#Output: "olleh"
# Set a timer for 30 minutes and complete the question!

class Node: #Initializing with the stack class.
    def __init__(self, value):
        self.value = value
        self.next = None
class Stack:
    def __init__(self):
        self.items = []

    def push_char(self, char):
       self.items.append(char)

    def pop_char(self):
        if self.items:
            return self.items.pop()
        return None

    def is_empty(self):
        return len(self.items) == 0
    

def reverse_string():
    print("#15. Reverse Characters")
    answer = input("Do you want to reverse a string? Type 'Yes' or 'No': ").capitalize() #I learned about the capitalize() method to make the first character uppercase. I realized there was an issue when I typed the response in lowercase.
    print("")
    while answer == "Yes":
        user_String = input("Enter a custom string: ")
        print("You picked: " + user_String)

        myString = Stack()
        for char in user_String:
            myString.push_char(char)

        reversed_String = ""
        while not myString.is_empty():
            reversed_String += myString.pop_char()
        print("Reversed string: " + reversed_String)
        
        print("")

        answer = input("Do you want to reverse another string? Type 'Yes' or 'No': ").capitalize()
        print("")
    if answer == "No":
        print("Okay, no problem!")
        print("Thank you for using the string reversal tool!")

reverse_string()
