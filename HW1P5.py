#Problem 5: Dictionaries. Create a dictionary for the months of the year that can be called by the number of months (i.e. 1, 2, ..., 12) or the name of months (i.e. January, February, ..., December). Write a statement that prints ‘The sixth month is June.’ and another statement that prints ‘February is month 2.’
month_dict={"1":"January","2":"Feburary","3":"March","4":"April","5":"May","6":"June","7":"July","8":"August","9":"September","10":"October","11":"November","12":"December"}
month_dict.keys()
month_dict["2"]

print("The sixth month is "+ month_dict["6"]+".")
print(month_dict["2"]+" is month 2.")