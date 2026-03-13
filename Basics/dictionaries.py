# Loops for "Dictionaries" :
# It's a data structure that allows us to gather somnthing with something else
def main():
    print("===dict specailties===\n")

    dict_specialties()
    dict_comprehension()

    print("\n\n=== Examples ===\n")
    airplane = {
        "name": "Boeing 747-8",
        # "nick_name": "Queen Of The Skies",  (commented to test the late\
        #                                      declaration and assignement)
        "typee": "Medium",  # (Giving a wrong value tp test the .update method)
        # "weight": "447.700kg", (I cpmmented to test the .get\
        #                        method : dictionary.get(key, the value to
        #                        uotput if it's not
        #                        initialized or even specified when
        #                        declaring the dictionary))
        # "max_speed": "533 knots"
    }

    airplane["nick_name"] = "Queen Of The Skies"
    airplane.update({"typee": "Heavy"})
    print(aircraft(airplane))

    airplanes()


def dict_specialties():
    my_dict = {
        'a': 36,
        'b': 74,
        'c': 74,
        'a': 59
    }
    print(my_dict)
    # Here we find that dicts save the ORDER, But don't allow DUPLICATES
    # while it's possible to assign the value to different keys

    # Dictionaries are not indexed, but we can access values using KEYS
    print(my_dict['c'])

    # Dictionaries are mutable:
    my_dict['c'] = 18
    print(my_dict['c'])

    # Dictionaries methods :
    my_dict = {
        'id': 1,
        'age': 26,
        'city': "Chicago"
    }
    # to access a value we need to use the exact key, if we're not
    # sure about the key the to avoid KeyError, we have to use this method :
    print(my_dict.get('name', 'unknown'), my_dict.get('age', 'unknown'))

    # we can check if a key is in my dict or not using :
    print('name' in my_dict, 'age' in my_dict)

    # We can get all the keys or the values or the pairs k:v of our dict using:
    print('keys: ', my_dict.keys())
    print('values: ', my_dict.values())
    print('pairs (key:value)', my_dict.items())
    # All these are iteratable lists that we can iterate on in loops:
    for key, value in my_dict.items():
        print(f"the key: {key}, and the value: {value}")

    # To add a new pair key:value to th dict use :
    my_dict['new'] = True
    my_dict['new'] = "already"
    print(my_dict)
    my_dict.update({'name': 'Joe', 'Height': 178, 'city': 'New York'})
    print(my_dict)

    # Now to delete a key:value pair, use:
    removed = my_dict.pop('new')
    print(my_dict.get('new', 'deleted'), removed)
    # If u're not sure if that key exists or not, use :
    unfound = my_dict.pop('new', 'Not Found')
    print(my_dict.get('new', 'no key!'), unfound)
    # if we just want to delete the last item without specifying the key, use:
    deleted = my_dict.popitem()
    print(my_dict, deleted)

    # Dictionaries creation:
    # If we want to create a dict but we still don't know about the values
    # or we ant to set a default value for all keys we can use :
    my_dict = dict.fromkeys(['name', 'job', 'company'], None)
    print(my_dict)


def dict_comprehension():
    user = {
        'id': 1, 'name': 'joe', 'job': 'engineer', 'age': 28, 'city': 'chicago'
    }

    new = {}
    for key, value in user.items():
        if type(value) is str:
            new.update({key: value})
    print(new)
    new = {
        k.upper(): v.title()
        for k, v in user.items()
        if isinstance(v, str)
    }
    print(new)


def ft_gpas():
    gpas = {
        "med    ": 3.7,
        "amir   ": 3.4,
        "Jeremy ": 3.1,
        "Steve  ": 3.5,
        "Alma   ": 2.9,
    }
    print(gpas["med    "])

    for student in gpas:
        print(student, gpas[student])


def students_info():
    students = [
        {"name": "Mohamed", "major": "Maths", "gpa": 3.7},
        {"name": "Alison", "major": "Chimistry", "gpa": 3.1},
        {"name": "Christian", "major": "Arts", "gpa": 2.8},
        {"name": "Jeremy", "major": "Mecanics", "gpa": 3.4}
    ]

    for student in students:
        print(student["name"], student["major"], student["gpa"], sep=", ")


def airplanes():
    aircrafts = {
        "first": "Airbus A380-800",
        "second": "Boeing 777-300ER",
        "third": "Airbus A320 neo",
    }

    # loop over keys
    for name in aircrafts.keys():
        print(name, ":", aircrafts[name])
    print()
    # Thos two loops have the same behavior even if we \
    # remove the .keys method (that returns all the keys \
    # we have in our dictionary) nothing changes
    for nam in aircrafts:
        print(f"{nam} : {aircrafts[nam]}")
    print()
    # loop over values
    for names in aircrafts.values():
        print(names)


def aircraft(airplane):
    return f"""
    =========================================
          Name      : {airplane["name"]}
          Nickname  : {airplane["nick_name"]}
          Type      : {airplane["typee"]}
          Weight    : {airplane.get("weight", "Not Specified")}
          Max Speed : {airplane.get("max_speed")}
    =========================================
    """


main()
