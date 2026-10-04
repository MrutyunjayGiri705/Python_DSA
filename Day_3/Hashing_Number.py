n=[5,3,2,2,1,5,5,7,5,10]
m=[10,111,1,9,5,67,2]

# for num in m:
#     count = 0
#     for x in n:
#         if x == num:
#             count += 1
#     print(f"{num} occurs {count} times")


# hash_list=[0]*11
# # print(hash_list)
# for num in n:
#     hash_list[num]+=1
# # print(hash_list)
# for num in m:
#     if  num <0 or num >10:
#         print(0)

#     else:
#         print(f"{num}={hash_list[num]}")

hash_map = dict()
for num in n:
    hash_map[num] = hash_map.get(num, 0) + 1

for num in m:
    if num < 0 or num > 10:
        print(f"{num}=0")
    else:
        print(f"{num}={hash_map.get(num, 0)}")
