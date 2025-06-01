# Step 1: prompt user for words
adjective = input("Enter an adjective: ")
noun = input("Enter a noun: ")
verb = input("Enter a verb: ")
favorite_animal = input("What's your favourite animal?: ")

# Step 2: Build story with condition
story = f"On a {adjective} day, I saw a {noun} that was {verb}ing. "

if favorite_animal.lower() == "lion":
    story += " It was a majectic lion!"
else:
    story += f" It was a {favorite_animal}."

# Step 3: Print the story
print(story)