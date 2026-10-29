def main():
    moscow = {201, 202, 203, 204}
    kazan = {203, 204, 205, 206}

    print("Can pick it up in either of two cities:", moscow | kazan)
    print("Only in Moscow:", moscow - kazan)
    print("Only in Kazan:", kazan - moscow)
    together = moscow | kazan
    print("Number of different items:", len(together))


if __name__ == "__main__":
    main()
