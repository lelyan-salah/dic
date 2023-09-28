dict1 = {"Name": "Ahmed", "Age": 23}
dict2 = {"City": "Gaza", "Gender": "Male"}

concatenated_dict = {
    "Name": "Ram",
    "Age": dict1["Age"],
    "City": "Salem",
    "Gender": dict2["Gender"]
}
print(concatenated_dict)