dict1 = {"Name": "Ahmed", "Age": 23}
dict2 = {"City": "Gaza", "Gender": "Male"}

concatenated_dict = {
    "Name": "Ahmed",
    "Age": dict1[23],
    "City": "Gaza",
    "Gender": dict2["Male"]
}
print(concatenated_dict)
