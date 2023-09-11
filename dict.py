def main():
    programming_books = {

        "form_one" :34,
        "form_two" :78,
        "form_three"  :66,
        "form_four" :29
    }

    for key in programming_books.keys():
        print(key)
    for value in programming_books.values():
        print(value)

if __name__ == "__main__":
    main()