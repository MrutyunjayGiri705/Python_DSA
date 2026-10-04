s="azyxyyzaaaa"
q=["a","d","y","x"]
hash_list=[0]*26
for ch in s:
    ascii_val=ord(ch)
    index=ascii_val-97
    hash_list[index]+=1

# print(hash_list)

for ch in q:
    ascii_val=ord(ch)
    index=ascii_val-97
    print(f"{ch}={hash_list[index]}")