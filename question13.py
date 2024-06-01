#Write a Python program to sort a dictionary (ascending /descending) by value.

d={"a":1,"b":4,"c":3,"d":2,"e":5}

def get_value(item):
    return item[1]

#sort the d by value in ascending order
sorted_item_asc=sorted(d.items(),key=get_value)
sorted_dict_asc=dict(sorted_item_asc)

#sort the d by value in descending order
sorted_item_des=sorted(d.items(),key=get_value, reverse =True)
sorted_dict_des=dict(sorted_item_des)

#here print the ascending and decending
print("Ascending order:",sorted_dict_asc)
print("descending order:",sorted_dict_des)