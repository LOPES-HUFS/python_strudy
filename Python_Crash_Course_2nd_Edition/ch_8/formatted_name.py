def get_formatted_name(first_name, last_name):
    full_name = f"{first_name} {last_name}"
    return full_name

musician = get_formatted_name('jimi', 'hendrix')
print(musician)

def get_formatted_name(first_name, last_name, middle_name=''):
    if middle_name:
        print("요기로 들어왔습니다.")
        full_name = f"{first_name} {middle_name} {last_name}"
    else:
        full_name = f"{first_name} {last_name}"
    return full_name.title()

# 여기는 middle_name의 값이 없기 때문에 else 쪽으로 간다.
musician = get_formatted_name('jimi', 'hendrix')
print(musician)

musician = get_formatted_name('john', 'hooker', 'lee')
print(musician)
