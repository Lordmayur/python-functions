# arguements
#positional
def person(name, age):
    print("my name is",name)
    print("my age is",age)
person("mayur",17)

#default
def human(name, age=17):
    print("my name is",name)
    print("my age is",age)
human("john")
human("joey",18)

#keyword 
def livingbeing(name,age,mobile):
    print(name)
    print(age)
    print(mobile)
livingbeing(mobile=208348084,age=19,name="Gary")

#variable-length

# def man(**information):
#     print(information["firstname"])
# man(firstname="john",lastname="wick",bloodgroup=O+,mobile=23434583485)