# ▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄.
# 		 ███████╗███╗   ██╗███╗   ██╗███████╗███████╗██╗    ██╗      .
# 		 ██╔════╝████╗  ██║████╗  ██║██╔════╝██╔════╝╚██╗  ██╔╝      .
# 		 █████╗  ██╔██╗ ██║██╔██╗ ██║█████╗  █████╗    ╚███╔╝        .
# 		 ██╔══╝  ██║╚██╗██║██║╚██╗██║██╔══╝  ██╔══╝   ██╔  ██╗       .
# 		 ███████╗██║ ╚████║██║ ╚████║███████╗███████╗██╔╝   ██╗      .
# ▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄.
# ╔═════════════════════════════════════════════════════════════════╗.
# ║  ⚡ ENNEEX         ▸		AERO-DATA SYSTEMS ENGINEER		⚡     ║.
# ║  ⚡ Mohamed ENNIH  ▸			enneex0113@gmail.com		⚡     ║.
# ║  ⟡ File	 	: dictionaries.py									║.
# ║  ⟡ Created		: 2026-02-06	                                ║.
# ║  ⟡ Updated		: 2026-02-06	                                ║.
# ╚═════════════════════════════════════════════════════════════════╝.
# ▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄.


# Loops for "Dictionaries" :
# It's a data structure that allows us to gather somnthing with something else
def main():
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
