# Step 1 : Ask the user for the current weather condition
weather = input("What's the weather like today? (sunny/rainy/cold): ").lower()

# Step 2: Provide clothing recommendations based on input
if weather == "sunny":
    print("wear a t-shirt and sunglasses.")
elif weather == "rainy":
    print("Don't forget your umbrella and a raincoat.")
elif weather == "cold":
    print("Make sure to wear a warm coat and a scarf. ")
else:
    print("Sorry, I don't have recommendations for this weather.")
    