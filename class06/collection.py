collection = {1,2,3,4,5,5,6}
print(collection)
collection.add(7)
print(collection)
collection.discard(2)
print(collection)

collection_one = {1,3,5,7,9}
collection_two = {2,4,6,8,10}
collection_union = collection_one.union(collection_two)
print("União das collections: ",collection_union)

print("Intersection da collection com a collection_one ",
      collection.intersection(collection_one))

print("Intersection da collection com a collection_two ",
      collection.intersection(collection_two))



