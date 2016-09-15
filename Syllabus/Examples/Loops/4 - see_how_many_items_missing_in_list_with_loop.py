print("Here we are testing to see how many books does not exist in the full list of books but does exist in the list of books to check.")

def how_many_books_are_missing(full_list_of_books, list_of_books_to_check):
    books_found = 0

    for book_to_check in list_of_books_to_check:
        for current_book_to_compare in full_list_of_books:
            if book_to_check == current_book_to_compare:
                books_found += 1
                break

    return len(list_of_books_to_check) - books_found

books_to_check = ["Python for Kids", "Pragmatic thinking and Learning"]

missing_books_count = how_many_books_are_missing(books_in_library, books_to_check)

print("There are %s book(s) missing" % missing_books_count)
