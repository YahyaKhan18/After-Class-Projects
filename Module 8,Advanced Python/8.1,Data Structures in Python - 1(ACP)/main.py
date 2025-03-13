def te(lst):
    output = {}
    for item in lst:
        output[item[0]] = item[1:]
    return output

fruits = [[1,'Banana','5'],[2,'Orange','6'],[3,'Pomegranate','8'],[4,'Lychee','10'],[5,'Kiwi','15']]

print("\nOriginal list of lists:")
print(fruits)
print("\nConverted lists to Dictionary:")
print(te(fruits))