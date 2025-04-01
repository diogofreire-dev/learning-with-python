def main():
    dollars = dollars_to_float(input("How much was the meal? "))
    percent = percent_to_float(input("What percentage would you like to tip? "))
    tip = dollars * percent
    print(f"Leave ${tip:.2f}")


def dollars_to_float(d):
    # Remove the leading '$' and convert to float
    return float(d.removeprefix('$'))


def percent_to_float(p):
    # Remove the trailing '%' and convert to float, then divide by 100
    return float(p.removesuffix('%')) / 100


main()