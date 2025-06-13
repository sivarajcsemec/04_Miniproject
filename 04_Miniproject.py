import numpy as np
import json

# Reading the json file
with open("prize.json","r",encoding="utf-8") as file:
    data = json.load(file)

prizes = data["prizes"]


# Total years present :
years = np.array([prize["year"] for prize in prizes])
unique_years, years_count = np.unique(years, return_counts= True )
a = len(unique_years)
print(f" {'Total years present ':<25}  : {a:<15}")

# Total prizes awarded:
no_of_prizes = np.array([prize["year"]+prize["category"] for prize in prizes])
a = len(np.unique(no_of_prizes))
print(f" {'Total prizes awarded ':<25}  : {a:<15}")

# Total laureates honoured:
all_laureaes1 = np.array([b["id"] for prize in prizes if "laureates" in prize for b in prize["laureates"]])
a =len(all_laureaes1)
print(f" {'Total laureates Honoured ':<25}  : {a:<15}")

# Total unique categories:
all_categories = np.array([prize["category"] for prize in prizes])
unique_cat1 = np.unique(all_categories)
a = len(unique_cat1)
print(f" {'Total unique categories ':<25}  : {a:<15}")

# The same logic without numpy libary 

print(f" {'Same output without using numpy concept'}")

# Total years present :

all2 = {} 
all2 = set() 
all2.clear() 
for prize in prizes: 
    all2.add(prize["year"])
a = len(all2)
print(f" {'Total years present ':<25}  : {a:<15}")

# Total prizes awarded:

all2.clear() 
for prize in prizes:
    a = prize["year"]+prize["category"]
    all2.add(a)
a =len(all2)
print(f" {'Total prizes awarded ':<25}  : {a:<15}")

# Total laureates honoured:

all1=[] 
count1 = 0 
for prize in prizes:
    if "laureates" in prize: 
        for l in prize["laureates"]:
            all1.append(l["id"])
            count1 = count1 + 1

print(f" {'Total laureates honoured ':<25}  : {count1:<15}")


# Total unique categories:

all2.clear() 
for prize in prizes: 
    all2.add(prize["category"])
a = len(all2)
print(f" {'Total unique categories ':<25}  : {a:<15}")