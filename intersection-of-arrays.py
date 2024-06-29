A = [1,2,3,4,5]
B = [4,5,6,7,8]
C = [x for x in A if x in B]

print("Intersection of arrays: ")
print(f"A: {A}")
print(f"B: {B}")
print(f"A ∩ B: {set(C)}")