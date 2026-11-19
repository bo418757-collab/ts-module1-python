import csv
import statistics
import sys

def letter(score):
    if score >= 90:
        return "A"
    elif score >= 80:
        return "B"
    elif score >= 70:
        return "C"
    elif score >= 60:
        return "D"
    else:
        return "F"

def load_students(filename):
    students = []
    try:
        with open(filename) as f:
            reader = csv.DictReader(f)
            for row in reader:
                name = row["name"]
                raw = row["score"]
                try:
                    score = int(raw)
                except ValueError:
                    print(f'Skipping {name}: score "{raw}" is not a number')
                    continue
                students.append({"name": name, "score": score})
    except FileNotFoundError:
        sys.exit(f"File {filename} not found")
    return students

def write_report(students):
    ordered = sorted(students, key=lambda s: s["score"], reverse=True)
    with open("report.txt", "w") as f:
        for s in ordered:
            f.write(f'{s["name"]},{s["score"]},{letter(s["score"])}\n')
    return ordered

def main():
    if len(sys.argv) < 2:
        sys.exit("Usage: python gradebook.py students.csv")
    if len(sys.argv) > 2:
        sys.exit("Too many arguments")
    filename = sys.argv[1]
    if not filename.endswith(".csv"):
        sys.exit("File must end with .csv")
    students = load_students(filename)
    if not students:
        sys.exit("No valid students found")
    vals = [s["score"] for s in students]
    ordered = write_report(students)
    top = ordered[0]
    bottom = ordered[-1]
    print(f"Students: {len(vals)}")
    print(f"Mean: {statistics.mean(vals)}")
    print(f"Median: {statistics.median(vals)}")
    print(f"Highest: {top['name']} ({top['score']})")
    print(f"Lowest: {bottom['name']} ({bottom['score']})")

if __name__ == "__main__":
    main()
