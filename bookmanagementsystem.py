# Module name: Sleigh Squad Book Management System
# Date created: 20 November 2023
# Purpose: To develop a personal book management system to keep track of all the books in collection

# text file: books.txt


# Import modules
import os
import datetime


# Function that read existing book data from text file
def read_books_data():
    try:
        # List to store book data
        books_data = []
        file_path = "books.txt"
        with open(file_path, "r") as file:
            # Loop through each line in the file and create a dictionary for each book
            for line in file:
                # Unpack values from the text file line into variables by seperating using (,)
                isbn, author, title, publisher, genre, year_published, date_purchased, status = line.strip().split(",")
                # Creating a dictionary for each book and adding it to the list
                book_info = {
                    "isbn": isbn,
                    "author": author,
                    "title": title,
                    "publisher": publisher,
                    "genre": genre,
                    "year_published": year_published,
                    "date_purchased": date_purchased,
                    "status": status
                }
                books_data.append(book_info)
        return books_data
    except FileNotFoundError:
        print("File not found or unable to read.\n")
        return []


# Function that allow editing/writing book data to the text file
def write_books_data(books_data):
    try:
        file_path = "books.txt"
        with open(file_path, "w") as file:
            # Writing each book's information to the file
            for book_info in books_data:
                file.write(",".join(str(book_info[key]) for key in book_info) + "\n")
    except FileNotFoundError:
        print("File not found or unable to write.\n")


# Current year to be used for various date validations
current_year = datetime.datetime.now().year


# Function to add a new book to the list
def add_book(books_data):
    try:
        current_year = datetime.datetime.now().year

        while True:
            # Gather information of new book
            isbn = getISBN(books_data)
            author = getAuthor()
            title = getTitle()
            publisher = getPublisher()
            genre = getGenre()
            year_published = getYearPublished(current_year)
            date_purchased = getDatePurchased(year_published)
            status = getStatus()

            # Create a dictionary for the new book
            new_book = {
                "isbn": isbn,
                "author": author,
                "title": title,
                "publisher": publisher,
                "genre": genre,
                "year_published": year_published,
                "date_purchased": date_purchased,
                "status": status
            }

            while True:
                print("\nNew Book Information:")
                book_information(new_book)

                confirm = input("Are all the information correct? (Yes: Enter '1', No: Enter any other key): ")
                # Prompt user to enter '1' as confirmation to add new book
                if confirm == '1':
                    books_data.append(new_book)

                    print("\nBook added successfully!\n")
                    break
                elif confirm.strip() == '':
                    print("Please enter a valid choice.")
                else:
                    # Ask for which part to be edit
                    print("\nWhich part would you like to edit?")
                    print(
                        "1. ISBN\n2. Author\n3. Title\n4. Publisher\n5. Genre\n6. Year Published\n7. Date Purchased\n8. Status")
                    edit_choice = input("Enter the number of the part to edit: ")
                    if edit_choice == '1':
                        editISBN(new_book)
                    elif edit_choice == '2':
                        editAuthor(new_book)
                    elif edit_choice == '3':
                        editTitle(new_book)
                    elif edit_choice == '4':
                        editPublisher(new_book)
                    elif edit_choice == '5':
                        editGenre(new_book)
                    elif edit_choice == '6':
                        editYearPublished(new_book, current_year)
                    elif edit_choice == '7':
                        editDatePurchased(new_book, year_published)
                    elif edit_choice == '8':
                        editStatus(new_book)

            # Ask if user want to add more book
            while True:
                # Prompt to add another book
                prompt = input("Do you want to add another book? 'Y' or 'N': ").lower()
                if prompt not in ['y', 'n']:
                    print("ERROR: Invalid input! Please enter 'Y' or 'N' only !")
                    continue
                elif prompt == 'n':
                    # Asking the user whether to clear the screen or not
                    confirm_clear = input(
                        "Do you want to clear the screen? Yes: Enter '1',No: Enter any other key: ").lower()
                    if confirm_clear == '1':
                        clear()
                    return  # Exit the inner loop, continue the outer loop

                elif prompt == 'y':
                    break  # Exit the inner loop, continue the outer loop


    except Exception as e:
        print(f"Error: {e}")


# To get ISBN from user
def getISBN(books_data):
    while True:
        isbn = input("Enter ISBN (13 digits): ")
        # Prompt user to enter valid ISBN
        if len(isbn) == 0:
            print("ISBN cannot be empty. Please enter a 13-digit numeric ISBN.")
        elif len(isbn) == 13 and isbn.isdigit():
            isbn_unique = True
            for book in books_data:
                if book['isbn'] == isbn:
                    isbn_unique = False
                    break
            if isbn_unique:
                return isbn  # Return the ISBN if it's unique
            else:
                print("ISBN already exists. Please enter a different ISBN.")
        else:
            print("Invalid ISBN. Please enter a 13-digit numeric ISBN.")


# To get author from user
def getAuthor():
    while True:
        author = input("Enter Author: ")
        if author.strip() == '':
            print("Author cannot be empty.")
        elif any(char.isdigit() for char in author):
            print("Invalid author. Please enter a valid name without numbers or special characters.")
        else:
            return author


# To get title from user
def getTitle():
    while True:
        title = input("Enter Title: ")
        if title.strip() == '':
            print("Title cannot be empty.")
        else:
            return title  # Return the validated title


# To get publisher from user
def getPublisher():
    while True:
        publisher = input("Enter Publisher: ")
        if publisher.strip() == '':
            print("Publisher cannot be empty.")
        else:
            return publisher  # Return the validated publisher


# To get genre from user
def getGenre():
    while True:
        genre = input("Enter Genre: ")
        if genre.strip() == '':
            print("Genre cannot be empty.")
        elif any(char.isdigit() for char in genre):
            print("Invalid genre. Please enter a valid genre without numbers or special characters.")
        else:
            return genre  # Return the validated genre


# To get year published from user
def getYearPublished(current_year):
    while True:
        year_input = input("Enter Year Published: ")
        if year_input.strip() == '':
            print("Year published cannot be empty.")
        elif len(year_input) == 4 and year_input.isdigit():
            year_published = int(year_input)
            if year_published < 5:
                print("The earliest printed book was created in 0005 CE.")
            elif year_published > current_year:
                print(f"Year cannot exceed the current year ({current_year}).")
            else:
                return year_published  # Return the validated year_published
        else:
            print("Invalid year published. Please enter a valid 4-digit year.")


# To get date purchased from user
def getDatePurchased(year_published):
    while True:
        date_purchased = input("Enter Date Purchased (dd-mm-yyyy): ")
        if date_purchased.strip() == '':
            print("Date purchased cannot be empty.")
        else:
            try:
                purchase_date = datetime.datetime.strptime(date_purchased, "%d-%m-%Y")
                current_date = datetime.datetime.now()
                if purchase_date > current_date:
                    print("Date purchased cannot be a future date.")
                elif purchase_date.year < year_published:
                    print("Date purchased cannot be earlier than the year published.")
                else:
                    return date_purchased  # Return the validated date_purchased
            except ValueError:
                print("Invalid date format. Please enter the date in the format dd-mm-yyyy.")


# To get status from user
def getStatus():
    while True:
        status = input("Enter Status (read/to-read): ").lower()
        if status.strip() == '':
            print("Status cannot be empty.")
        elif status in ['read', 'to-read']:
            return status  # Return the validated status
        else:
            print("Invalid status. Please enter 'read' or 'to-read'.")


# To edit isbn
def editISBN(new_book):
    while True:
        isbn = input("Enter ISBN (13 digits): ")
        if len(isbn) == 0:
            print("ISBN cannot be empty. Please enter a 13-digit numeric ISBN.")
            continue
        elif len(isbn) == 13 and isbn.isdigit():
            new_book["isbn"] = isbn
            break
        else:
            print("Invalid ISBN. Please enter a 13-digit numeric ISBN.")


# To edit author
def editAuthor(new_book):
    while True:
        author = input("Enter Author: ")
        if author.strip() == '':
            print("Author cannot be empty.")
        elif any(char.isdigit() for char in author):
            print("Invalid author. Please enter a valid name without numbers or special characters.")
        else:
            new_book["author"] = author
            print("Author updated successfully!")
            break


# To edit title
def editTitle(new_book):
    while True:
        title = input("Enter Title: ")
        if title.strip() == '':
            print("Title cannot be empty.")
        else:
            new_book["title"] = title
            print("Title updated successfully!")
            break


# To edit publisher
def editPublisher(new_book):
    while True:
        publisher = input("Enter Publisher: ")
        if publisher.strip() == '':
            print("Publisher cannot be empty.")
        else:
            new_book["publisher"] = publisher
            print("Publisher updated successfully!")
            break


# To edit genre
def editGenre(new_book):
    while True:
        genre = input("Enter Genre: ")
        if genre.strip() == '':
            print("Genre cannot be empty.")
        elif any(char.isdigit() for char in genre):
            print("Invalid genre. Please enter a valid genre without numbers or special characters.")
        else:
            new_book["genre"] = genre
            print("Genre updated successfully!")
            break


# To edit year publised
def editYearPublished(new_book, current_year):
    date_purchased = new_book['date_purchased']  # Retrieve date purchased from new_book
    while True:
        year_input = input("Enter Year Published (4 digits): ")
        if year_input.strip() == '':
            print("Year published cannot be empty.")
        elif len(year_input) == 4 and year_input.isdigit():
            year_published = int(year_input)
            if year_published < 5:
                print("The earliest printed book was created in 0005 CE.")
            elif year_published > current_year:
                print(f"Year cannot exceed the current year ({current_year}).")
            elif datetime.datetime(year_published, 1, 1) > datetime.datetime.strptime(date_purchased, "%d-%m-%Y"):
                print("Year published cannot be later than the date purchased.")
            else:
                new_book["year_published"] = year_published
                print("Year Published updated successfully!")
                break
        else:
            print("Invalid year published. Please enter a valid 4-digit year.")


# To edit date purchased
def editDatePurchased(new_book, year_published):
    while True:
        date_purchased = input("Enter Date Purchased (dd-mm-yyyy): ")
        if date_purchased.strip() == '':
            print("Date purchased cannot be empty.")
        else:
            try:
                purchase_date = datetime.datetime.strptime(date_purchased, "%d-%m-%Y")
                if purchase_date < datetime.datetime(year_published, 1, 1):
                    print("Date purchased cannot be earlier than the year published.")
                elif purchase_date > datetime.datetime.now():
                    print("Date purchased cannot be a future date.")
                else:
                    new_book["date_purchased"] = date_purchased
                    print("Date Purchased updated successfully!")
                    break
            except ValueError:
                print("Invalid date format. Please enter the date in the format dd-mm-yyyy.")


# To edit status
def editStatus(new_book):
    while True:
        status = input("Enter Status (read/to-read): ").lower()
        if status.strip() == '':
            print("Status cannot be empty.")
        elif status in ['read', 'to-read']:
            new_book["status"] = status
            print("Status updated successfully!")
            break
        else:
            print("Invalid status. Please enter 'read' or 'to-read'.")


# Print new book information
def book_information(new_book):
    print("{:<20}{:<30}{:<50}{:<45}{:<30}{:<20}{:<25}{:<10}".format(
        "ISBN", "Author", "Title", "Publisher", "Genre", "Year Published", "Date Purchased", "Status"))
    print('-' * 230)
    print(
        "{isbn:<20}{author:<30}{title:<50}{publisher:<45}{genre:<30}{year_published:<20}{date_purchased:<25}{status:<10}".format(
            **new_book))


# Function to delete a book from the list
def delete_book(books_data):
    try:
        while True:
            isbn_to_delete = input("Enter ISBN of the book to delete: ")
            found = False

            for book_info in books_data:
                if book_info["isbn"] == isbn_to_delete:
                    found = True

                    # Display book information for confirmation
                    print("{:<20}{:<30}{:<50}{:<45}{:<30}{:<20}{:<25}{:<10}".format(
                        "ISBN", "Author", "Title", "Publisher", "Genre", "Year Published", "Date Purchased", "Status"))
                    print('-' * 230)
                    print(
                        "{isbn:<20}{author:<30}{title:<50}{publisher:<45}{genre:<30}{year_published:<20}{date_purchased:<25}{status:<10}".format(
                            **book_info))

                    # Prompt for confirmation to delete the book
                    while True:
                        prompt = input("\nAre you sure to delete this book? 'Y' or 'N': ").lower()
                        if prompt == 'y':
                            # Remove the book from the list
                            books_data.remove(book_info)
                            print("\nBook deleted successfully!\n")
                            break
                        elif prompt == 'n':
                            break
                        else:
                            print("ERROR: Invalid input! Please enter 'Y' or 'N' only !")
                            continue

                    break  # Exit the loop after deleting the book

            if not found:
                print("Book with ISBN {} not found.\n".format(isbn_to_delete))

            while True:
                # Prompt to delete another book
                prompt = input("Do you want to delete another book? 'Y' or 'N': ").lower()
                if prompt not in ['y', 'n']:
                    print("ERROR: Invalid input! Please enter 'Y' or 'N' only !")
                    continue
                elif prompt == 'n':
                    # Asking the user whether to clear the screen or not
                    confirm_clear = input(
                        "Do you want to clear the screen? Yes: Enter '1', No: Enter any other key: ").lower()
                    if confirm_clear == '1':
                        clear()
                    return  # Exit the inner loop, continue the outer loop
                elif prompt == 'y':
                    break  # Exit the inner loop, continue the outer loop

    except Exception as e:
        print(f"Error: {e}")


# Function to update information of an existing book
def update_book(books_data):
    try:
        current_year = datetime.datetime.now().year
        # To find book with ISBN or author and title
        while True:
            isbn = input("Enter ISBN (press Enter to skip): ").strip().lower()

            if isbn:
                found_books = [book_info for book_info in books_data if isbn == book_info["isbn"].lower()]
            else:
                author = input("Enter Author: ").strip().lower()
                title = input("Enter Title: ").strip().lower()

                found_books = [book_info for book_info in books_data if
                               author == book_info["author"].lower() and title == book_info["title"].lower()]

            if not isbn and not author and not title:
                print("No search criteria provided. Please enter ISBN, Author, or Title.")
                continue

            if found_books:
                for book_info in found_books:
                    updateISBN(book_info)
                    updateAuthor(book_info)
                    updateTitle(book_info)
                    updatePublisher(book_info)
                    updateGenre(book_info)
                    updateYearPublished(book_info, current_year)
                    updateDatePurchased(book_info)
                    updateStatus(book_info)

                    new_book = book_info  # Assuming new_book has been updated with all the changes
                    print("\nNew Book Information:")
                    print("{:<20}{:<30}{:<50}{:<45}{:<30}{:<20}{:<25}{:<10}".format(
                        "ISBN", "Author", "Title", "Publisher", "Genre", "Year Published", "Date Purchased", "Status"))
                    print('-' * 230)
                    print(
                        "{isbn:<20}{author:<30}{title:<50}{publisher:<45}{genre:<30}{year_published:<20}{date_purchased:<25}{status:<10}".format(
                            **new_book))
                    print("\nUpdated Book Information:")
                    # Confirmation for update the book
                    confirmation = input("\nPress '1' to confirm the update, any other key to discard changes: ")
                    if confirmation == '1':
                        print("\nBook updated successfully!\n")
                        break
                    else:
                        print("\nChanges discarded.\n")
                    break  # Exit the loop after updating a book

            else:
                print("No books found matching the search criteria.")
            # Prompt tp update another book
            while True:
                prompt = input("Do you want to update another book? 'Y' or 'N': ").lower()
                if prompt not in ['y', 'n']:
                    print("ERROR: Invalid input! Please enter 'Y' or 'N' only !")
                    continue
                elif prompt == 'n':
                    # Asking the user whether to clear the screen or not
                    confirm_clear = input(
                        "Do you want to clear the screen? Yes: Enter '1',No: Enter any other key: ").lower()
                    if confirm_clear == '1':
                        clear()
                    return  # Exit the inner loop, continue the outer loop
                elif prompt == 'y':
                    break  # Exit the inner loop, continue the outer loop

    except Exception as e:
        print(f"Error: {e}\n")


# To update ISBN
def updateISBN(book_info):
    while True:
        isbn = input(f"Update new ISBN (13 digits, press Enter to keep current - {book_info['isbn']}): ").strip()
        if len(isbn) == 0:
            return book_info['isbn']
        elif len(isbn) == 13 and isbn.isdigit():
            book_info["isbn"] = isbn  # Update the ISBN directly in the book_info dictionary
            break
        else:
            print("Invalid ISBN. Please enter a 13-digit numeric ISBN or leave it empty to keep current.")


# To update author
def updateAuthor(book_info):
    while True:
        author = input(
            f"Update new Author (press Enter to keep current - {book_info['author']}): ").strip()
        if author == '':
            return book_info['author']
        elif any(char.isdigit() for char in author):
            print("Invalid author. Please enter a valid name without numbers or special characters.")
        else:
            book_info["author"] = author
            return author


# To update title
def updateTitle(book_info):
    while True:
        title = input(
            f"Update new Title (press Enter to keep current - {book_info['title']}): ").strip()
        if title == '':
            # If the input is empty, keep the current title
            return book_info['title']
        else:
            # Update the title and return the updated value
            book_info["title"] = title
            return title


# To update publisher
def updatePublisher(book_info):
    while True:
        publisher = input(
            f"Update new Publisher (press Enter to keep current - {book_info['publisher']}): ").strip()
        if publisher == '':
            return book_info['publisher']
        else:
            book_info["publisher"] = publisher
            return publisher


# To update genre
def updateGenre(book_info):
    while True:
        genre = input(
            f"Update new Genre (press Enter to keep current - {book_info['genre']}): ").strip()
        if genre == '':
            return book_info['genre']
        else:
            book_info["genre"] = genre
            return genre


# To update year published
def updateYearPublished(book_info, current_year):
    while True:
        year_input = input(
            f"Update new Year Published (press Enter to keep current - {book_info['year_published']}): ").strip()
        if year_input == '':
            return book_info['year_published']
        elif len(year_input) != 4 or not year_input.isdigit():
            print("Invalid year published. Please enter a valid 4-digit year.")
        else:
            year_published = int(year_input)
            if year_published < 5:
                print("The earliest printed book was created in 0005 CE.")
            elif year_published > current_year:
                print(f"Year cannot exceed the current year ({current_year}).")
            else:
                book_info["year_published"] = year_published
                return year_published


# To update date purchased
def updateDatePurchased(book_info):
    while True:
        date_purchased = input("Update new Date Purchased (dd-mm-yyyy) "
                               "(press Enter to keep current - {}): ".format(book_info['date_purchased'])).strip()
        if date_purchased == '':
            return book_info['date_purchased']
        else:
            try:
                purchase_date = datetime.datetime.strptime(date_purchased, "%d-%m-%Y")
                if purchase_date > datetime.datetime.now():
                    print("Date purchased cannot be a future date.")
                else:
                    book_year_published = int(book_info["year_published"])
                    if purchase_date.year < book_year_published:
                        print("Date purchased cannot be earlier than the year published.")
                    else:
                        book_info["date_purchased"] = date_purchased
                        return date_purchased
            except ValueError:
                print("Invalid date format. Please enter the date in the format dd-mm-yyyy.")


# To update status
def updateStatus(book_info):
    while True:
        status = input(
            f"Update new Status (read/to-read) (press Enter to keep current - {book_info['status']}): ").strip()
        if status == '':
            return book_info['status']
        elif status not in ['read', 'to-read']:
            print("Invalid status. Please enter 'read' or 'to-read'.")
        else:
            book_info["status"] = status
            return status


# Function that display all existing books in text file
def display_book(books_data):
    # Displaying the header with column names
    print("{:<20}{:<30}{:<50}{:<45}{:<30}{:<20}{:<25}{:<10}".format(
        "ISBN", "Author", "Title", "Publisher", "Genre", "Year Published", "Date Purchased", "Status"))
    print('-' * 230)
    # Display all content in the text file
    for book_info in books_data:
        print(
            "{isbn:<20}{author:<30}{title:<50}{publisher:<45}{genre:<30}{year_published:<20}{date_purchased:<25}{status:<10}".format(
                **book_info))
        
    # Asking the user whether to clear the screen or not
    confirm_clear = input("\nDo you want to clear the screen? Yes: Enter '1',No: Enter any other key: ").lower()
    if confirm_clear == '1':
        clear()
        return


# Function to search for books based on user input
def search_book(books_data):
    try:
        while True:
            # Prompts for the ISBN, author, and title
            isbn = input("Enter ISBN: ").strip()
            author = input("Enter Author: ").strip().lower()
            title = input("Enter Title: ").strip().lower()

            if not isbn and not author and not title:
                print("No searching information provided! Please enter at least one criteria.")
                continue

            search_results = []
            for book_info in books_data:
                # Checking if the book matches the search criteria
                if book_info["isbn"] == isbn or book_info["author"].lower() == author or book_info[
                    "title"].lower() == title:
                    search_results.append(book_info)

            if search_results:
                display_book(search_results)
            else:
                print("No matching books found.\n")

            # Control statement to loop the search process
            while True:
                prompt = input("Do you want to search another book? 'Y' or 'N': ").lower()
                if prompt not in ['y', 'n']:
                    print("Invalid input! Please enter 'Y' or 'N' only! ")
                    continue
                elif prompt == 'y':
                    break
                elif prompt == 'n':
                    # Asking the user whether to clear the screen or not
                    confirm_clear = input(
                        "Do you want to clear the screen? Yes: Enter '1',No: Enter any other key: ").lower()
                    if confirm_clear == '1':
                        clear()
                    return

    except Exception as e:
        print(f"Error: {e}")


# Function to clear the screen based on differrent operating system
def clear():
    if os.name == 'nt':
        os.system('cls')  # For Windows
    else:
        os.system('clear')  # For macOS and Linux


# Main function to run the program
def main():
    print("\nWelcome to Sleigh Squad Book Management System!")
    try:
        # Reading existing book data from the file
        books_data = read_books_data()

        while True:
            # Displaying the program menu
            print("\n\nMenu:")
            print('-' * 40)
            print("1. Add Book Record(s)")
            print("2. Delete Book Record(s)")
            print("3. Update/Edit Book Record(s)")
            print("4. Display")
            print("5. Search for Book(s)")
            print("6. Exit")
            print("7. Clear screen")
            print('-' * 40)

            # User input as their choice
            choice = input("Enter your choice (1-7): ")
            print()

            match choice:

                case "1":
                    add_book(books_data)
                case "2":
                    delete_book(books_data)
                case "3":
                    update_book(books_data)
                case "4":
                    print("")
                    display_book(books_data)
                case "5":
                    search_book(books_data)
                case "6":
                    write_books_data(books_data)
                    # save the changes that made during program execution
                    print("Exiting program. Data saved.\n\n")
                    break
                case "7":
                    clear()
                case _:
                    print("Invalid input. Please enter a number between 1 and 7.")
    except Exception as e:
        print(f"Error: {e}")


# Call the main function when the script is executed
if __name__ == "__main__":
    main()
