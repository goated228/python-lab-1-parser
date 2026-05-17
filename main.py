from prettytable import PrettyTable
from parser import get_page, parse_birth_data

html = get_page()

if html:
    data = parse_birth_data(html)

    table = PrettyTable()

    table.field_names = ["index", "value"]

    for item in data:
        table.add_row([item["title"], item["value"]])

    print(table)

    with open("result.txt", "w", encoding="utf-8") as file:
        file.write(str(table))

else:
    print("error occurred")