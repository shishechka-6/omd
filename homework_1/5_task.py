reviews = [
    {"id": 1, "product": "Чехол", "stars": 5},
    {"id": 1, "product": "Чехол", "stars": 3},
    {"id": 1, "product": "Чехол", "stars": 4},
    {"id": 2, "product": "Наушники", "stars": 2},
    {"id": 2, "product": "наушники", "stars": 2},
    {"id": 2, "product": "НАУШНИКИ", "stars": 5},
    {"id": 3, "product": "Планшет", "stars": 5},
    {"id": 4, "product": "Колонка", "stars": 4},
    {"id": 4, "product": "Колонка", "stars": 4},
    {"id": 5, "product": "Кабель", "stars": 1},
]

for i in reviews:
    i["product"] = i["product"].lower()


product = set()
for i in reviews:
    product.add(i["id"])


avg_estim = []
for i in product:
    sum_stars = 0
    count = 0
    for j in reviews:
        if j["id"] == i:
            sum_stars += j["stars"]
            count += 1
    avg_estim.append(sum_stars / count)
print("Average estimation:", avg_estim)


worst_avg = 10
worst_id = None
for i in product:
    sum_stars = 0
    count = 0
    for j in reviews:
        if j["id"] == i:
            sum_stars += j["stars"]
            count += 1
    if count >= 2:
        avg = sum_stars / count
        if avg < worst_avg:
            worst_avg = avg
            worst_id = i

print("Worst product:", worst_id)


reviews_count = 0
for i in reviews:
    if i["stars"] == 1 or i["stars"] == 2:
        reviews_count += 1
print("Reviews for 1 or 2 stars:", reviews_count)


print("Share of 1 or 2 star reviews:", reviews_count / len(reviews))
