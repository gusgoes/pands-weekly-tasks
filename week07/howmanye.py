filename = "text.txt"

def count_letter_e(filename):
    try:
        with open(filename, 'r') as file:
            content = file.read()
            count = content.count('e')
            return count
    except FileNotFoundError:
        print("Error: File not found.")
    except:
        print("An error occurred while reading the file.")

count = count_letter_e(filename)
if count is not None:
    print(f"The file '{filename}' contains {count} occurrences of the letter 'e'.")
