def main():
    i = 1
    while i <= 4:
        j = 0
        while j <= 3:
            print(f"{i}x{j}= {i*j}")
            j += 1
        print()
        i += 1

if __name__ == "__main__":
    main()