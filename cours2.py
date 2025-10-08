def generate_value():
    k=1
    while True:
        yield 2**k
        k+=1

generator = generate_value()
nbr_element = 50
my_keys = [i for i in range(0,nbr_element)]
my_values = [next(generator) for _ in range(0,nbr_element)]

my_dico_1 = {}
#Medium method
for index in range(0,len(my_keys)):
    current_key = f"key_{my_keys[index]}"
    current_value = my_values[index]

    my_dico_1[current_key] = current_value

#Easy
my_dico_3 = zip(my_keys,my_values)

for key in my_dico_1.keys():
    pretty_sentence = f"key : {key}; my_dico_1[{key}] : {my_dico_1[key]}"
    print(pretty_sentence)