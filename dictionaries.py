#Dictionaries in python
my_dict={
    "book":"Dynamics",
    "publisher":"longhorn",
    "year":2001,
    "authors":["John","mike"]
}

#accessing item
x=my_dict["year"]
print(x)

#Accessing using get
y=my_dict.get("book")
print(y)

#All keys
x=my_dict.keys()
print(x)

#All values
x=my_dict.values()
print(x)

#printing all items in a dictionary
x=my_dict.items()
print(x)

#checking if key exists
if "publisher"in my_dict:
    print("publisher is one of the keys")


