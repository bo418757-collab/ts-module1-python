def main():
    while True:
        try:
            frac = input("Fraction: ")
            num, den = frac.split("/")
            x = int(num)
            y = int(den)
            if y == 0 or x > y:
                raise ValueError
            pct = round(x / y * 100)
            break
        except (ValueError, ZeroDivisionError):
            continue
    if pct <= 1:
        print("E")
    elif pct >= 99:
        print("F")
    else:
        print(f"{pct}%")

if __name__ == "__main__":
    main()
