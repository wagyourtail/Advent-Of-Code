import re

def validatePassport(passport):
    if 1920 <= int(passport['byr']) <= 2002:
        if 2010 <= int(passport['iyr']) <= 2020:
            if 2020 <= int(passport['eyr']) <= 2030:
                if (re.match(r"\d{3}cm", passport['hgt']) and 150 <= int(passport['hgt'][:-2]) <= 193) or (re.match(r"\d{2}in", passport['hgt']) and 59 <= int(passport['hgt'][:-2]) <= 76):
                    if re.fullmatch(r"#[a-fA-F\d]{6}", passport['hcl']):
                        if passport['ecl'] in ["amb", "blu", "brn", "gry", "grn", "hzl", "oth"]:
                            if re.fullmatch(r"\d{9}", passport['pid']):
                                return passport
    #                         else:
    #                             print(f"PID: {passport['pid']}")
    #                     else:
    #                         print(f"ECL: {passport['ecl']}")
    #                 else:
    #                     print(f"HCL: {passport['hcl']}")
    #             else:
    #                 print(f"HGT: {passport['hgt']}")
    #         else:
    #             print(f"EYR: {passport['eyr']}")
    #     else:
    #         print(f"IYR: {passport['iyr']}")
    # else:
    #     print(f"BYR: {passport['byr']}")


def createPassport(passport):
    fields = {}
    for field in passport:
        field = field.split(":")
        fields[field[0]] = field[1]
    if "byr" in fields and "iyr" in fields and "eyr" in fields and "hgt" in fields and "hcl" in fields and "ecl" in fields and "pid" in fields:
        return fields

def part1(passports):
    b = []
    for passport in passports:
        a = createPassport(passport)
        if a:
            b.append(a)
    return b

def part2(passports):
    return list(filter(validatePassport, passports))

def main():
    passports = []
    # load lines
    with open('input1.txt', 'r') as f:
        lines = re.finditer(r"([\s\S]+?)(?:\n\s*\n|\Z)", f.read(), re.MULTILINE)
        for match in lines:
            passports.append(match.group(1).split())
            # print(match.group(1))
            # print("-------------------")
    p = part1(passports)
    print(f"part1: {len(p)}")
    print(f"part2: {len(part2(p))}")


if __name__ == "__main__":
    main()