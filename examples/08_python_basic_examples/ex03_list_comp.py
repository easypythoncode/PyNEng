from pprint import pprint

numbers = [1, 2, 3, 10, 20, 100]
result = []

for num in numbers:
    result.append(f"vlan {num}")

pprint(result)

# list comp
numbers = [1, 2, 3, 10, 20, 100]
result = [f"vlan {num}" for num in numbers]
pprint(result)
