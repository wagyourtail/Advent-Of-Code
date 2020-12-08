# this is cancer, why oh god why
import re

bagTypes = {}

def createBagType(name):
    bagTypes[name] = {"parents": [], "children": []}

def addParent(name, parent):
    if name not in bagTypes:
        createBagType(name)
    bagTypes[name]["parents"].append(parent)

def addChild(name, child, count):
    if name not in bagTypes:
        createBagType(name)
    bagTypes[name]["children"].append((count, child))

def traverseParents(startBag, bags = []):
    for parent in bagTypes[startBag]["parents"]:
        if parent not in bags:
            bags.append(parent)
            traverseParents(parent, bags)
    return bags

def traverseChildren(startBag):
    children = bagTypes[startBag]["children"]
    if len(children) == 0:
        return 0
    count = 0
    for child in children:
        count += child[0] * (traverseChildren(child[1]) + 1)
    return count

def main():
    # load lines
    with open('input1.txt', 'r') as f:
        for line in f:
            match = re.match(r'(.+)\sbags? contain((?:\s*\d+\s.+?bags?[,\.])+|(?:\s*no other bags.))', line)
            if match.group(1).strip() not in bagTypes:
                createBagType(match.group(1).strip())
            if match.group(2).strip() != "no other bags.":
                for name in re.finditer(r'(\d+)\s+(.+?)bags?[,\.]', match.group(2)):
                    addParent(name.group(2).strip(), match.group(1).strip())
                    addChild(match.group(1).strip(), name.group(2).strip(), int(name.group(1).strip()))

    print(bagTypes)
    p1 = len(traverseParents("shiny gold"))
    print(f"part1: {p1}")
    print(traverseChildren("shiny gold"))


if __name__ == "__main__":
    main()