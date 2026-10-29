def main():
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

    sum_stars = {}
    reviews_amount = {}
    reviews_count = 0

    for review in reviews:
        review["product"] = review["product"].lower()
        product_id = review["id"]

        if product_id not in sum_stars:
            sum_stars[product_id] = 0
            reviews_amount[product_id] = 0

        sum_stars[product_id] += review["stars"]
        reviews_amount[product_id] += 1

        if review["stars"] == 1 or review["stars"] == 2:
            reviews_count += 1

    avg_estim = {}

    for product_id in sum_stars:
        avg_estim[product_id] = (
            sum_stars[product_id] / reviews_amount[product_id]
            )

    print("Average estimation:", avg_estim)

    worst_avg = 10
    worst_id = 0

    for product_id in avg_estim:
        if reviews_amount[product_id] >= 2:
            if avg_estim[product_id] < worst_avg:
                worst_avg = avg_estim[product_id]
                worst_id = product_id

    print("Worst product:", worst_id)
    print("Reviews for 1 or 2 stars:", reviews_count)
    print("Share of 1 or 2 star reviews:", reviews_count / len(reviews))


if __name__ == "__main__":
    main()
