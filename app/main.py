class Person:
    people = {}

    def __init__(self, name, age):
        self.name = name
        self.age = age
        Person.people[name] = self

    def set_spouse(self, role, spouse_name):
        if spouse_name in Person.people:
            spouse = Person.people[spouse_name]
            setattr(self, role, spouse)
            reverse_role = "husband" if role == "wife" else "wife"
            setattr(spouse, reverse_role, self)


def create_person_list(people):
    [Person(p["name"], p["age"]) for p in people]

    person_list = []
    for person_dict in people:
        person = Person.people[person_dict["name"]]

        if person_dict.get("wife"):
            person.set_spouse("wife", person_dict["wife"])
        elif person_dict.get("husband"):
            person.set_spouse("husband", person_dict["husband"])

        person_list.append(person)

    return person_list
