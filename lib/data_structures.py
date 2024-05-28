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
# print([item for item in spicy_foods])
    return [food['name'] for food in spicy_foods]

get_names(spicy_foods)
def get_spiciest_foods(spicy_foods):
    return [food for food in spicy_foods if food["heat_level"]>5]

def print_spicy_foods(spicy_foods):
    for food in spicy_foods:
        print(f'{food["name"]} ({food["cuisine"]}) | Heat Level: {food["heat_level"]*"🌶"}') 

print_spicy_foods(spicy_foods)

def get_spicy_food_by_cuisine(spicy_foods,cuisine="American"):
    for food in spicy_foods:
        if food["cuisine"]==cuisine:
            print(food)
            return food
    return None

get_spicy_food_by_cuisine(spicy_foods ,cuisine="American")

def print_spiciest_foods(spicy_foods):
    for food in spicy_foods :
        if food["heat_level"]>5:
            print(f'{food["name"]} ({food["cuisine"]}) | Heat Level: {food["heat_level"]*"🌶"}' )

print_spiciest_foods(spicy_foods)
def get_average_heat_level(spicy_foods):
    add=sum(food["heat_level"] for food in spicy_foods)
    avg=add/len(spicy_foods)
    print(avg)
    return avg
get_average_heat_level(spicy_foods)

new_food = {"name": "Spicy Ramen", "cuisine": "Japanese", "heat_level": 8}
def create_spicy_food(spicy_foods, spicy_food=new_food):
    spicy_foods.append(spicy_food)
    return spicy_foods
