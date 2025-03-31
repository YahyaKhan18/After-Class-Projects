def test(tpl):
    result = {}
    for item in tpl:
        result[item[0]] = item[1:]
    return result

students = ([1,'Jean Castro','V'],[2,'Lula Powell','V'],[3,'Brian Howell','VI'],[4,'Lynne Foster','VI'],[5,'Zachary Simon','VII'])

print("\nOriginal list of Tuples:")
print(students)
print("\nConverted lists to Dictionary:")
print(test(students))