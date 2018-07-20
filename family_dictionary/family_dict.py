# Instructions
# Define a dictionary that contains information about several members of your family. Use the following example as a template.

my_family = {
    'mother': {
        'name': 'Tonna',
        'age': '55'
    },
    'father': {
        'name': 'Jack',
        'age': '57'
    },
    'cousin': {
        'name': 'Renee',
        'age': '36'
    }
}
# Using a dictionary comprehension, produce output that looks like the following example.
# my_family = {'my ' + k + ' is ' + v for (k,v) in family.items()}

# heath_fam = []
# for key, value in my_family.items():
#     print({' is my ' + key + ' and is ' + ' years old.'})
#     print(key, value)

family_stuff = set()
for family_member, member_values in my_family.items():
        family_stuff.add(f'{member_values["name"]} is my {family_member} and is {str(member_values["age"])} years old')
print("My family!", family_stuff)
# Krista is my sister and is 42 years old
# Helpful hint: To convert an integer into a string in Python, it's str(integer_value)

#With comprehension instead
family_stuff = {
    f'{member_values["name"]} is my {family_member} and is {str(member_values["age"])} years old.'
    for (family_member, member_values) in my_family.items()
}
print("My family!", family_stuff)