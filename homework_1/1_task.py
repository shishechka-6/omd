Moscow = {201, 202, 203, 204}
Kazan = {203, 204, 205, 206}

print("Can pick it up in either of two cities:", Moscow | Kazan)
print("Only in Moscow:", Moscow - Kazan)
print("Only in Kazan:", Kazan - Moscow)
together = Moscow | Kazan
print("Number of different items:", len(together))
