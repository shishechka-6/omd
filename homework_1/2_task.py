queries = [
    "чехол",
    "iphone",
    "чехол",
    "наушники",
    "iphone",
    "iphone",
    "кабель",
    "чехол",
    "iphone",
]

print("In total:", len(queries))

count = {}
for i in queries:
    if i in count:
        count[i] += 1
    else:
        count[i] = 1
print("Number of times each query was entered:", count)

max_count = max(count, key=count.get)
print("Most frequent query:", max_count)

print("Share of all:", count[max_count] / len(queries))

once_ans = []
for i in count:
    if count[i] == 1:
        once_ans.append(i)
print("Met once:", once_ans)
