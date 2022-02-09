card_list=[
    {"a1":1,"a2":2,"a3":3},
    {"b1":"b1","b2":"b2"}
]

for item in card_list:
    print("max is "+max(item))
    for k in item:
        print("%f is"+item[k],% k)
        if item[k]==1:
            del item[k]
