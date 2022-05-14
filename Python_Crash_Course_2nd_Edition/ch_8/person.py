def build_person(first_name, last_name):
    person = {"first": first_name, "last":last_name}
    return person

musician = build_person('jimi', 'hendrix')
print(musician)
print(musician['last'])

def build_person(first_name, last_name, age=None):
    person = {"first": first_name, "last":last_name}
    print(person)
    if age:
        print("요기로 들어왔습니다.")
        person['age'] = age
        print(person)
    return person

musician = build_person('jimi', 'hendrix', age=13)
print(musician)