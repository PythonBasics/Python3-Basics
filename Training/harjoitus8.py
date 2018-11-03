

for letter in "Apina Mafia":
    print(letter)

def raise_to_power(base_num, pow_num):
    result=1
    for index in range(pow_num):
        result = result * base_num
    return result

def raise2(eka,toka):
    print(eka**toka)

print(raise_to_power(3,4))
raise2(3,4)


#2D lists
number_grid = [
    [1,2,3],
    [4,5,6],
    [7,8,9],
    [0]
]

print(number_grid[0][0])

for row in number_grid:
    for col in row:
        print(col)

#translate
#rules
#vowels are g

def translate(phrase):
    translation= ""
    for letter in phrase:
        if letter in "AEIOUYaeiouy":
            translation = translation + "g"
        else:
            translation = translation + letter
    return translation

print(translate("Eläimet ei syö kebabbia"))