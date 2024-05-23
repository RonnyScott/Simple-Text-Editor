def display_file(filename):
    try:
        with open(filename, 'r') as file:
            print(file.read())
    except FileNotFoundError:
        print(f"The file {filename} does not exist.")
    except IOError:
        print(f"An error occurred while reading the file {filename}.")

def append_to_file(filename):
    try:
        with open(filename, 'a') as file:
            print("Enter text to append (type 'EXIT' on a new line to stop):")
            while True:
                line = input()
                if line == 'EXIT':
                    break
                file.write(line + '\n')
    except IOError:
        print(f"An error occurred while writing to the file {filename}.")

def main():
    filename = input("Enter the filename: ")

    while True:
        print("\nText Editor")
        print("1. Display file")
        print("2. Append to file")
        print("3. Exit")
        choice = input("Enter your choice: ")

        if choice == '1':
            display_file(filename)
        elif choice == '2':
            append_to_file(filename)
        elif choice == '3':
            print("Exiting...")
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()
