list1 = [1,5,2,3,6,4,8,9,7,10]
list1.sort()
print(f"Original list:{list1}")
new_list = list1[:5]
print(f"Extrected first five element: {new_list}")

new_list.reverse()
print(f"Reverse extracted element:{new_list}")