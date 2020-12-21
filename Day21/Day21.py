import re

ingredients = []
allergens = {}


def intersection(lst1, lst2):
    lst3 = [value for value in lst1 if value in lst2]
    return lst3


def part1(foods):
    global ingredients, allergens
    for food in [a for a in foods if len(a["allergens"]) == 1]:
        if food["allergens"][0] in allergens:
            allergens[food["allergens"][0]] = intersection(allergens[food["allergens"][0]], food["ingredients"])
        else:
            allergens[food["allergens"][0]] = food["ingredients"][:]
    for food in foods:
        for allergen in food["allergens"]:
            if allergen in allergens:
                allergens[allergen] = intersection(allergens[allergen], food["ingredients"])
            else:
                allergens[allergen] = food["ingredients"][:]
    ingredients = set(ingredients)
    safe = []
    for ing in ingredients:
        for allergen in allergens.values():
            if ing in allergen:
                break
        else:
            safe.append(ing)
    c = 0
    for ing in safe:
        for food in foods:
            if ing in food["ingredients"]:
                c += 1
    print(f"Part1: {c}")


def part2():
    solved = {}
    while len(allergens.keys()):
        for allergen in [a for a in allergens.keys()]:
            if len(allergens[allergen]) == 1:
                solved[allergen] = allergens[allergen][0]
                del allergens[allergen]
                for a2 in allergens.keys():
                    if solved[allergen] in allergens[a2]:
                        allergens[a2].remove(solved[allergen])
    s2 = []
    for i in sorted(solved.keys()):
        s2.append(solved[i])
    print("Part2: ",end="")
    print(*s2, sep=",")


def main():
    global ingredients
    foods = []
    with open("input1.txt", "r") as f:
        for line in f:
            m = re.match(r"(.+)\(contains (.+)\)", line)
            foods.append({"ingredients": m.group(1).split(), "allergens": m.group(2).split(", ")})
            ingredients += m.group(1).split()
    part1(foods)
    part2()


if __name__ == "__main__":
    main()
