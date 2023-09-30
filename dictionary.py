dict1 = {"Name": "Ahmed", "Age": 23}
dict2 = {"City": "Gaza", "Gender": "Male"}

concatenated_dict = {}

concatenated_dict.update(dict1)
concatenated_dict.update(dict2)

concatenated_dict["Name"] = "Ram"
concatenated_dict["City"] = "Salem"

print(concatenated_dict)
