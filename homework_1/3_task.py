orders = [
    {"id": 1, "buyer": "anya", "status": "delivered", "amount": 900},
    {"id": 2, "buyer": "boris", "status": "returned", "amount": 4_500},
    {"id": 3, "buyer": "anya", "status": "delivered", "amount": 1_500},
    {"id": 4, "buyer": "vera", "status": "delivered", "amount": 3_200},
    {"id": 5, "buyer": "boris", "status": "delivered", "amount": 700},
    {"id": 6, "buyer": "gleb", "status": "returned", "amount": 2_100},
]

ret_sum = 0
for i in orders:
    if i["status"] == "returned":
        ret_sum += i["amount"]
print("Sum of returned orders:", ret_sum)


ret_buyer = set()
for i in orders:
    if i["status"] == "returned":
        ret_buyer.add(i["buyer"])
print("Returned orders:", ret_buyer)


del_ord = 0
for i in orders:
    if i["status"] == "delivered":
        del_ord += 1
print("Delivered orders:", del_ord)


del_sum = 0
for i in orders:
    if i["status"] == "delivered":
        del_sum += i["amount"]
avg_bill = del_sum / del_ord
print("Average bill of delivered orders:", avg_bill)
