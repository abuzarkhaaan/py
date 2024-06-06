key_location="chair"
locations=["garage","living room","chair","closet"]
for i in locations:
    if i==key_location:
        print("key found",i)
        break
    else:
        print("key not found")