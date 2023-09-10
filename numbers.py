def main():
    name = input("Whats your name?")
    age = int(input("Whats your age?"))
    year = int(input("What year is it ?"))
    current_year = year - age
    print(f"{name} you were born in the year {current_year} ")

if __name__ == "__main__":
    main()