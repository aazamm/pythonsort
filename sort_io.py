import json
#test sorting program with file input and manual input


def read_numbers_from_file(filename):
    """Read numbers from a text file"""
    try:
        with open(filename, 'r') as file:
            content = file.read()
            numbers = [float(x) for x in content.split()]
            return numbers
    except FileNotFoundError:
        print(f"File {filename} not found!")
        return None
    except ValueError:
        print("Invalid data in file!")
        return None

def save_results_to_file(original, ascending, descending, filename):
    """Save sorting results to a JSON file"""
    results = {
        "original": original,
        "ascending": ascending,
        "descending": descending
    }
    
    with open(filename, 'w') as file:
        json.dump(results, file, indent=2)
    print(f"Results saved to {filename}")

def advanced_sorting_program():
    print("=== Advanced Number Sorting Program ===")
    
    # Choose input method
    print("Choose input method:")
    print("1. Manual input")
    print("2. Read from file")
    
    choice = input("Enter choice (1 or 2): ")
    
    if choice == "1":
        numbers_input = input("Enter numbers separated by spaces: ")
        numbers = [float(x) for x in numbers_input.split()]
    elif choice == "2":
        filename = input("Enter filename: ")
        numbers = read_numbers_from_file(filename)
        if numbers is None:
            return
    else:
        print("Invalid choice!")
        return
    
    # Sort the numbers
    ascending = sorted(numbers)
    descending = sorted(numbers, reverse=True)
    
    # Display results
    print(f"\nOriginal numbers: {numbers}")
    print(f"Ascending order: {ascending}")
    print(f"Descending order: {descending}")
    
    # Ask if user wants to save results
    save_choice = input("\nDo you want to save results to file? (y/n): ")
    if save_choice.lower() == 'y':
        output_filename = input("Enter output filename (e.g., results.json): ")
        save_results_to_file(numbers, ascending, descending, output_filename)

if __name__ == "__main__":
    advanced_sorting_program()

