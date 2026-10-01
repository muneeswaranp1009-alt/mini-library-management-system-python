Books = []

def add_book():
    print('\nAdd a New Book!')
    
    isbn = input("\nEnter Book ISBN Number:").strip()
    
    for book in Books:
        if book['isbn'] == isbn:
            print(f"The Book({isbn}) is already Exisits! ")
            return
        
    title = input("Enter Book Name:")
    author = input("Enter Author Name:")
        
    new_book ={
        'isbn' : isbn,
        'title' : title,
        'author' : author,
        'borrowed' : False
    }
    
    Books.append(new_book)
    print(f"\nThe Book {title} was Added Succesfully!")
    
def view_book():
    print("\nLibrary Books List....")
    
    if not Books:
        print("\nThe Library is Empty!")
        return
    
    print(f"\n{'Isbn':<15} {'Title':<30} {'Author':<25} {'Status':<12}")
    
    for book in Books:
        Status = "Borrowed" if book['borrowed'] else "Available"
        print(f"\n{book['isbn']:<15} {book['title']:<30} {book['author']:<25} {Status:<12}")
        
def borrow():
    print("\n Borrow a Book...")
    
    isbn = input("\nEnter Book ISBN Number to Borrow:").strip()
    
    for book in Books:
        if book['isbn'] == isbn:
            if book['borrowed']:
                print(f"Sorry, The Book '{book['title']}' is already Borrowed by Someone...!")
            
            else:
                book['borrowed'] = True
                print(f"\n The Book is Available,You Borrowed '{book['title']}'")
                return
    print("\nError: Book with that ISBN not found.")
            
def returned():
    print("\n Return a Book...")
    
    isbn = input("\nEnter the Returning Book ISBN Number:").strip()
    
    for book in Books:
        if book['isbn'] == isbn:
            if not book['borrowed']:
                print(f"\nThe Book '{book['title']}' was not borrowed!")
                
            else:
                book['borrowed'] = False
                print(f"\n The Book '{book['title']}' was Returned Succesfully..!")
                return
    print("\nError: Book with that ISBN not found.")

def menu():
    print("\n----------Mini Library Management System-----------------\n")
    print("1.Add Books")
    print("2.View Books")
    print("3.Borrow Books")
    print("4.Return Books")
    print("5.Exit")
    
def main():
    while True:
        menu()
        user_input = input("\nEnter Your Choice(1 to 5):")
        if user_input == "1":
            add_book()
            
        elif user_input == "2":
            view_book()
            
        elif user_input == "3":
            borrow()
            
        elif user_input == "4":
            returned()
            
        elif user_input == "5":
            print("\nThanks for visiting Mini Library...^__^")
            break
            
        else:
            print("\nPlease CHoose a Number Between(1 to 5)")
            
            
if __name__ == '__main__':
    main()