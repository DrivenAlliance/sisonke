def get_value_at(index , list):
    #use the index to retrieve the value - very easy!
    return list[index]

def get_index_of_value(value, list):
	for index in range(0,len(list)):
		if (list[index] == value):
			get_index_of_value = index
	return get_index_of_value

def sisonke_length(my_list):
    sisonke_length = 0
    for element in my_list:
        sisonke_length = sisonke_length + 1
    return sisonke_length

candice_favourite_numbers = [13,42,26,37,12,31]

print("These are my favourite numbers: ", candice_favourite_numbers)
print()
print("The value at index 0 (should be 13): ", get_value_at(0,candice_favourite_numbers))
print("The value at index 5 (should be 31): ", get_value_at(5,candice_favourite_numbers))
print()
print("The index of value 13 (should be 0): ", get_index_of_value(13,candice_favourite_numbers))
print("The index of value 31 (should be 5): ", get_index_of_value(31,candice_favourite_numbers))
print()
print("The length of my list (should be 6): ", sisonke_length(candice_favourite_numbers))