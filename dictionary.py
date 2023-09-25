month_conversion = {
    # key : value (key should be unique
    "Jan" : "January",
    "Feb" : "feburary",
    "Mar" : "March",
    4: "Hey"
}

print(month_conversion["Feb"])
print(month_conversion.get("mar", "Not a valid key"))
print(month_conversion.get(4))
