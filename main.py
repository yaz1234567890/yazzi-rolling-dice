
import random


#nevermind this is a cooking thing now
baked_things = 0
baking_stuff = ["crepe", "bread", "pie", "pancakes", "croissant", "icecream cake", "cake"]
flav = ["chocolate", "vanilla", "strawberry", "mint", "caramel"]
ingreds = ["flour", "fruits", "eggs", "icecream", "butter", "water"]

print("this is a baking help thing, need some help?")

flavour = input("enter a flavour you want to use: ")
if flavour in flav:
    print("ok")
else:
    print("i dont know what that is")

ingredient = input ("enter an ingredient you have: ")
if ingredient in ingreds:
    print("ok")
else:
    print("idk what that is")

print(f"you want to use {flavour}, and have {ingredient} in your baked good.")

#eggs
if (flavour == "strawberry") and (ingredient == "eggs"):
    print("you made a crepe from",flavour, "and ", ingredient,)
    baked_things += 1
elif (flavour == "chocolate") and (ingredient == "eggs"):
    print("you made a crepe from",flavour, "and ", ingredient,)
    baked_things += 1
elif (flavour == "vanilla") and (ingredient == "eggs"):
    print("you made a nothing")
elif (flavour == "mint") and (ingredient == "eggs"):
    print("you made an icecream cake from",flavour, "and ", ingredient,)
    baked_things += 1
elif (flavour == "caramel") and (ingredient == "eggs"):
    print("you made a pie from",flavour, "and ", ingredient,)
    baked_things += 1

#flour
if (flavour == "strawberry") and (ingredient == "flour"):
    print("you made a crepe from",flavour, "and ", ingredient,)
    baked_things += 1
elif (flavour == "chocolate") and (ingredient == "flour"):
    print("you made a cake from",flavour, "and ", ingredient,)
    baked_things += 1
elif (flavour == "vanilla") and (ingredient == "flour"):
    print("you made a nothing")
elif (flavour == "mint") and (ingredient == "flour"):
    print("you made a nothing!")
elif (flavour == "caramel") and (ingredient == "flour"):
    print("you made a pie from",flavour, "and ", ingredient,)
    baked_things += 1

#fruits
if (flavour == "strawberry") and (ingredient == "fruits"):
    print("you made a pie from",flavour, "and ", ingredient,)
    baked_things += 1
elif (flavour == "chocolate") and (ingredient == "fruits"):
    print("you made a nothjing!")
    baked_things += 1
elif (flavour == "vanilla") and (ingredient == "fruits"):
    print("you made an icecream cake from",flavour, "and", ingredient)
    baked_things += 1
elif (flavour == "mint") and (ingredient == "fruits"):
    print("you made an icecream cake from",flavour, "and ", ingredient,)
    baked_things += 1
elif (flavour == "caramel") and (ingredient == "fruits"):
    print("you made a pie from",flavour, "and ", ingredient,)
    baked_things += 1

#icecream
if (flavour == "strawberry") and (ingredient == "icecream"):
    print("you made a icecream cake from",flavour, "and ", ingredient,)
    baked_things += 1
elif (flavour == "chocolate") and (ingredient == "icecream"):
    print("you made a crepe from",flavour, "and ", ingredient,)
    baked_things += 1
elif (flavour == "vanilla") and (ingredient == "icecream"):
    print("you made a nothing")
elif (flavour == "mint") and (ingredient == "icecream"):
    print("you made an icecream cake from",flavour, "and ", ingredient,)
    baked_things += 1
elif (flavour == "caramel") and (ingredient == "icecream"):
    print("you made a pancake from",flavour, "and ", ingredient,)
    baked_things += 1

#butter
if (flavour == "strawberry") and (ingredient == "butter"):
    print("you made a crepe from",flavour, "and ", ingredient,)
    baked_things += 1
elif (flavour == "chocolate") and (ingredient == "butter"):
    print("you made a cake from",flavour, "and ", ingredient,)
    baked_things += 1
elif (flavour == "vanilla") and (ingredient == "butter"):
    print("you made croissant")
    baked_things += 1
elif (flavour == "mint") and (ingredient == "butter"):
    print("you made a nothing!")
    baked_things += 1
elif (flavour == "caramel") and (ingredient == "butter"):
    print("you made a croissant from",flavour, "and ", ingredient,)
    baked_things += 1

#water
if (flavour == "strawberry") and (ingredient == "water"):
    print("you made a nothing")
elif (flavour == "chocolate") and (ingredient == "water"):
    print("you made a nothing")
elif (flavour == "vanilla") and (ingredient == "water"):
    print("you made a nothing")
elif (flavour == "mint") and (ingredient == "water"):
    print("you made a nothing")
elif (flavour == "caramel") and (ingredient == "water"):
    print("you made a pie from",flavour, "and ", ingredient,)
    baked_things += 1

print("you have baked", baked_things, " thing, are you proud of yourself?")

import random

baking_stuff = random.randint(0,7)
print(random recipie to make:", baking_stuff)