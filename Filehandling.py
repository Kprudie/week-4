def modify_content(content):
    # Example modification: convert text to uppercase
    return content.upper()

def main():
    try:
        filename = input("Enter the filename to read: ")

        # Try to open and read the file
        with open(filename, 'r') as file:
            content = file.read()

        # Modify the content
        modified_content = modify_content(content)

        # Save to new file
        new_filename = "modified_" + filename
        with open(new_filename, 'w') as new_file:
            new_file.write(modified_content)

        print(f"Modified content written to '{new_filename}' successfully.")

    except FileNotFoundError:
        print("Error: File not found. Please check the filename and try again.")
    except IOError:
        print("Error: Could not read or write the file.")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")

if __name__== "_main_":
    main()
