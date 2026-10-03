#d["key"]
student = {
    "name":"kamlesh",
    "age": 30
}
print(student["name"])
print("...........................................")

#Missing key:
d = {
    "name": "Patil",
    "age": 25
}
#print(d["city"])           #remove # for missing key program
print("...........................................")


#d.get("key")
print(d.get("name"))

#Missing key:
print(d.get("city"))