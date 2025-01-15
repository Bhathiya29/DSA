string = "Hello"

hashed_value = hash(string)

print(f"Hash value of {string}:{hashed_value}")


# Example of hashing in a dict

my_dict ={}

my_dict["apple"]=1
my_dict["orange"] = 2

print(my_dict["apple"])


# hash maps often has a time complexity of O(1)
# collisions are avoided through techniques like chaining(linkedlist) or open addressing(linear probing)