from collections import defaultdict

#1

persons = [
    {"name": "Ваня", "age": 12},
    {"name": "Марго", "age": 19},
    {"name": "Анастасія", "age": 18},
    {"name": "Паша", "age": 12}
]
age_by_names = defaultdict(list)
len_name_by_names = defaultdict(list)
ages = []
for p in persons:
    name = p['name']
    age = p['age']
    age_by_names[age].append(name)
    len_name_by_names[len(name)].append(name)
    ages.append(age)
min_age = min(age_by_names)
print('Мінімальний вік:', *age_by_names[min_age])
max_len_name = max(len_name_by_names)
print('Саме довге імя:', *len_name_by_names[max_len_name])
print('Середній вік:', sum(ages) // len(ages))

#2

y_dict_1 = {"Імя": "Ваня",
             "Вік": 12,
             "Скорочено": "Ва"}
my_dict_2 = {"Імя": "Микола",
             "Професія": "байкер"}

res = dict(item for item in y_dict_1.items() if item[0] not in my_dict_2)

for item in y_dict_1.items():
    if item[0] not in my_dict_2:
        res[item[0]] = item[1]
    else:
        res[item[0]] = [item[1], my_dict_2[item[0]]]

print(res)



