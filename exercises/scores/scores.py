import csv
import statistics
import sys

def main():
    try:
        with open("scores.csv") as f:
            reader = csv.DictReader(f)
            rows = list(reader)
    except FileNotFoundError:
        sys.exit("scores.csv not found")
    scores = []
    for row in rows:
        try:
            scores.append((row["name"], int(row["score"])))
        except ValueError:
            continue
    vals = [s for _, s in scores]
    print(f"Students: {len(vals)}")
    print(f"Mean: {statistics.mean(vals)}")
    print(f"Median: {statistics.median(vals)}")
    top = max(scores, key=lambda x: x[1])
    bottom = min(scores, key=lambda x: x[1])
    print(f"Highest: {top[0]} ({top[1]})")
    print(f"Lowest: {bottom[0]} ({bottom[1]})")

if __name__ == "__main__":
    main()
