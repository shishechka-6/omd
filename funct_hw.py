import csv

input_file = "Corp_Summary.csv"


def read_data(input_file):
    employees = []
    with open(input_file, "r", encoding="utf-8", newline="") as f:
        data = csv.DictReader(f, delimiter=";")
        for i in data:
            i["Оценка"] = float(i["Оценка"])
            i["Оклад"] = int(i["Оклад"])
            employees.append(i)
    return employees


def hierarchy(employees):
    departments = {}

    for member in employees:
        department = member["Департамент"]
        team = member["Отдел"]
        if department not in departments:
            departments[department] = set()
        departments[department].add(team)

    for department in departments:
        print(department)
        for team in departments[department]:
            print("  -", team)


def svodka(employees):
    departments = {}

    for member in employees:
        department = member["Департамент"]
        oklad = member["Оклад"]
        if department not in departments:
            departments[department] = []
        departments[department].append(oklad)

    for i in departments:
        print(i)
        print("Сотрудников:", len(departments[i]))
        print("Минимальный оклад:", min(departments[i]))
        print("Максимальный оклад:", max(departments[i]))
        print("Средний оклад:",
              round(sum(departments[i])/len(departments[i]), 2))
        print()


def svodka_csv(employees, output_file="svodka.csv"):
    departments = {}

    for member in employees:
        department = member["Департамент"]
        oklad = member["Оклад"]
        if department not in departments:
            departments[department] = []
        departments[department].append(oklad)

    with open(output_file, "w", encoding="utf-8", newline="") as f:
        writer = csv.writer(f, delimiter=";")
        writer.writerow([
            "Название", "Кол-во сотрудников", "Минимальный оклад",
            "Максимальный оклад", "Средний оклад"
        ])
        for i in departments:
            writer.writerow([
                i,
                len(departments[i]),
                min(departments[i]),
                max(departments[i]),
                round(sum(departments[i])/len(departments[i]), 2)
            ])


def variant(variant):
    employees = read_data(input_file)
    if variant == 1:
        hierarchy(employees)
    elif variant == 2:
        svodka(employees)
    elif variant == 3:
        svodka_csv(employees)
    else:
        print("Input correct variant number (1/2/3)")


if __name__ == "__main__":
    variant(3)
