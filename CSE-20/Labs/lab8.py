#Lab 8
# 1)Write a code snippet that asks the user to enter a name and a major one
# at a time and creates a dictionary with keys corresponding to names
# and values corresponding to majors.

d = {}

numtime = int(input("how many users: "))


for i in range(0, numtime):

    key = input("enter your name: ")
    d[key] = input("enter your major: ")

print(d)

# 2)Write a code snippet that creates a dictionary (records) using keys from a
# frozenset of numbers (ids) and values from a list of names (students).

students = ["alice", "bob", "carol"]

ids = frozenset([123, 124, 125])

records = {}

zipped = zip(ids,students)

records = dict(zipped)

print(records)

