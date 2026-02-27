programming_dictionary={
    "name": "Uday Raj is my full name",
    "age": "t25 is my age"
}
#print(programming_dictionary["age"])
programming_dictionary["place"]="I came from Narsampet a town in India."  #adding keys and values to the dictionary
#print(programming_dictionary)
programming_dictionary={}
programming_dictionary["name"]="Uday Raj"
programming_dictionary["age"]="t25"
programming_dictionary["place"]="I came from Narsampe a town in India."

for keys in programming_dictionary:
    print(keys)
    print(programming_dictionary[keys])
d1=dict(a="geeks",b="for",c="geeks")  #this function can be used to create a dictionary
print(d1)
print(programming_dictionary.get("name")) #this dictionary_name.get("key") can be used to get the value of that key

del programming_dictionary["name"] #delete key and value
print(programming_dictionary)

programming_dictionary={
    "name": "Uday Raj is my full name",
    "age": "t25 is my age",
    "place": "I came from Narsampet a town in India."
}

val=programming_dictionary.pop("place") #it will contain the value of popped key i mean removed key
print(val)
print(programming_dictionary)