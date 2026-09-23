person = {
    "name": "Coralie",
    "age": 25,
    "city": "Mauritius"
}

print(person["name"])
print(person["age"])
print(person["city"])

person["job"] = "Test Automation Engineer"

print(person)

print(person["country"])

print(person.get("country", "Not specified"))