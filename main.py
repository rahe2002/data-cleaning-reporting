import csv

def read_data(filename):
    rows = []
    with open(filename, newline='', encoding="utf-8") as file:
        reader = csv.DictReader(file)
        for row in reader:
            rows.append(row)
    return rows

def clean_data(rows):
    cleaned = []
    removed = []

    for row in rows:
        if row["name"] and row["email"] and row["age"] and row["city"]:
            cleaned.append(row)
        else:
            removed.append(row)

    return cleaned, removed

def generate_report(cleaned, removed):
    total_records = len(cleaned) + len(removed)
    percentage = (len(cleaned) / total_records) * 100 if total_records > 0 else 0

    with open("report.txt", "w") as file:
        file.write(f"Valid records: {len(cleaned)}\n")
        file.write(f"Removed records: {len(removed)}\n")
        file.write(f"Clean data percentage: {percentage:.2f}%\n")

def main():
    data = read_data("data.csv")
    cleaned, removed = clean_data(data)
    generate_report(cleaned, removed)

if __name__ == "__main__":
    main()
