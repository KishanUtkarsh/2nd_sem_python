adj=['red','big','tasty']
fruits=['apple','banana','cherry']
for x in adj:
    for y in fruits:
        if y=="banana" and x=='red':
            continue
        print(x,y)