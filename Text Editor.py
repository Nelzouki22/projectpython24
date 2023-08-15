def display_menu():
    print("Text Editor Menu")
    print("1. Create new file")
    print("2. Open existing file")
    print("3. Edit file")
    print("4. Save file")
    print("5. Exit")

def create_new_file():
    file_name = input("Enter the name of the new file: ")
    return file_name

def open_file(file_name):
    try:
        with open(file_name, "r") as file:
            content = file.read()
            print("\nFile content:")
            print(content)
            return content
    except FileNotFoundError:
        print("File not found.")

def edit_file(content):
    print("\nEditing mode. Press Ctrl+C to exit.")
    new_content = []
    try:
        while True:
            line = input()
            new_content.append(line)
    except KeyboardInterrupt:
        return "\n".join(new_content)

def save_file(file_name, content):
    with open(file_name, "w") as file:
        file.write(content)
        print("File saved.")

def main():
    current_file = None
    content = ""

    while True:
        display_menu()
        choice = input("Enter your choice: ")

        if choice == "1":
            current_file = create_new_file()
            content = ""
        
        elif choice == "2":
            if current_file:
                content = open_file(current_file)
            else:
                print("No file currently open.")

        elif choice == "3":
            if current_file:
                content = edit_file(content)
            else:
                print("No file currently open.")

        elif choice == "4":
            if current_file:
                save_file(current_file, content)
            else:
                print("No file currently open.")

        elif choice == "5":
            print("Exiting the text editor.")
            break

        else:
            print("Invalid choice. Please select a valid option.")

if __name__ == "__main__":
    main()
