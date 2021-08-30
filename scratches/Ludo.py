list_of_objects = [{"name": "Deepak", "age": 28}, {"name": "Prakash", "age": 28}, {"name": "Nachos", "age": 24}]
dict_of_objects ={}
for obj in list_of_objects:
    for obj_ind in range(len(obj)):
        if list(obj.keys())[obj_ind] in dict_of_objects:
            dict_of_objects[list(obj.keys())[obj_ind]].append(list(obj.values())[obj_ind])
        else:
            dict_of_objects[list(obj.keys())[obj_ind]] = [list(obj.values())[obj_ind]]

print(dict_of_objects)