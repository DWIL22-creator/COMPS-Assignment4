# Pick one question from timed_challenge.txt
# Paste the question as a comment below
#15. Reverse Characters
#Reverse a string using custom logic, not slicing or built-in methods.
#Input: "hello"
#Output: "olleh"
# Set a timer for 30 minutes and complete the question!

print("#15. Reverse Characters")
answer = input("Do you want to reverse a string? Type 'Yes' or 'No': ").capitalize() #I learned about the capitalize() method to make the first character uppercase. I realized there was an issue when I typed the response in lowercase.
print("")
while answer == "Yes":
    user_String = input("Enter a custom string: ")
    print("You picked: " + user_String)
    sub_char = -1
    reverse_String = ""
    for i in range(len(user_String)):
        reverse_String += user_String[sub_char]
        sub_char -= 1
    print("Reversed string: " + reverse_String)
    print("")
    answer = input("Do you want to reverse another string? Type 'Yes' or 'No': ").capitalize()
    print("")
if answer == "No":
    print("Okay, no problem!")
    print("Thank you for using the string reversal tool!")