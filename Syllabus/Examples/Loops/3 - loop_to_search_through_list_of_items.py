
print("Here we write a function to search for a certain book in our library")

books_in_library = ["Extreme Programming","The Toyota Way", "Python for Kids", "Learn Python the hard way","Pragmatic Programmer"]

def is_book_in_library(book_name, books_to_search_through):
    for current_book in books_to_search_through:
        if book_name.lower() == current_book.lower():
            return True# we use this to quite the entire function because we found the book
    return False

book_is_in_library = is_book_in_library("The Toyota Way", books_in_library)
print("Is the Toyota Way in the library? %s" % book_is_in_library)

book_to_search_for = raw_input("Book to search for: ")

book_is_in_library = is_book_in_library(book_to_search_for, books_in_library)

if (book_is_in_library):
    print("%s is in the library" % book_to_search_for)
else:
    print("%s is not in the library" % book_to_search_for)

