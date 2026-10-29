days = [
    {"day": "пн", "orders": 20, "revenue": 40_000, "returns": 2},
    {"day": "вт", "orders": 16, "revenue": 19_200, "returns": 4},
    {"day": "ср", "orders": 25, "revenue": 55_000, "returns": 1},
    {"day": "чт", "orders": 10, "revenue": 12_000, "returns": 3},
    {"day": "пт", "orders": 30, "revenue": 48_000, "returns": 3},
]

week_revenue = 0
for i in days:
    week_revenue += i["revenue"]
print("Week revenue:", week_revenue)


max_revenue = 0
max_day = ""
for i in days:
    if i["revenue"] > max_revenue:
        max_revenue = i["revenue"]
        max_day = i["day"]
print("Max day revenue:", max_day)


avg_revenue = []
for i in days:
    avg_revenue.append((i["day"], i["revenue"] / i["orders"]))
print("Average revenue:", avg_revenue)


ret_ord_20 = []
for i in days:
    if i["returns"] / i["orders"] > 0.2:
        ret_ord_20.append(i["day"])
print("Days when returned > 20 %:", ret_ord_20)
