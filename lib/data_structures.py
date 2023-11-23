spicy_foods = [
    {
        "name": "Green Curry",
        "cuisine": "Thai",
        "heat_level": 9,
    },
    {
        "name": "Buffalo Wings",
        "cuisine": "American",
        "heat_level": 3,
    },
    {
        "name": "Mapo Tofu",
        "cuisine": "Sichuan",
        "heat_level": 6,
    },
]

def get_names(spicy_foods):
    return [food["name"] for food in spicy_foods]

def get_spiciest_foods(spicy_foods):
    return [food for food in spicy_foods if food["heat_level"] > 5]

def print_spicy_foods(spicy_foods):
    for food in spicy_foods:
        heat_level_emojis = "🌶" * food["heat_level"]
        print(f"{food['name']} ({food['cuisine']}) | Heat Level: {heat_level_emojis}")

def get_spicy_food_by_cuisine(spicy_foods, cuisine):
    for food in spicy_foods:
        if food["cuisine"] == cuisine:
            return food
    return None

def print_spiciest_foods(spicy_foods):
    spiciest_foods = get_spiciest_foods(spicy_foods)
    print_spicy_foods(spiciest_foods)

def get_average_heat_level(spicy_foods):
    total_heat_level = sum(food["heat_level"] for food in spicy_foods)
    num_foods = len(spicy_foods)
    if num_foods > 0:
        return total_heat_level // num_foods
    else:
        return 0

def create_spicy_food(spicy_foods, spicy_food):
    updated_spicy_foods = spicy_foods.copy()
    updated_spicy_foods.append(spicy_food)
    return updated_spicy_foods

# Example usage
new_spicy_food = {
    "name": "Spicy Ramen",
    "cuisine": "Japanese",
    "heat_level": 8,
}

updated_spicy_foods = create_spicy_food(spicy_foods, new_spicy_food)

print("Names of Spicy Foods:", get_names(spicy_foods))
print("Spiciest Foods:", get_spiciest_foods(spicy_foods))
print("Print Spicy Foods:")
print_spicy_foods(spicy_foods)
print("Spicy Food by Cuisine (American):", get_spicy_food_by_cuisine(spicy_foods, "American"))
print("Spicy Food by Cuisine (Thai):", get_spicy_food_by_cuisine(spicy_foods, "Thai"))
print("Print Spiciest Foods:")
print_spiciest_foods(spicy_foods)
print("Average Heat Level:", get_average_heat_level(spicy_foods))
print("Original Spicy Foods:", spicy_foods)
print("Updated Spicy Foods:", updated_spicy_foods)
