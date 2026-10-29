def main():
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

    for query in queries:
        if query in count:
            count[query] += 1
        else:
            count[query] = 1

    print("Number of times each query was entered:", count)

    max_count = max(count, key=count.get)
    print("Most frequent query:", max_count)

    print("Share of all:", count[max_count] / len(queries))

    once_ans = []

    for query in count:
        if count[query] == 1:
            once_ans.append(query)

    print("Met once:", once_ans)


if __name__ == "__main__":
    main()
