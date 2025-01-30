#nevermind this is a cooking thing now
baked_things = 0
baking_stuff = ["crepe", "bread", "pie", "pancakes", "croissant", "icecream cake"]
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