#For this assignment use the numbers.txt file.
#A different numbers.txt will be used for grading.
#Read in all the numbers. Display the following information:
#How many numbers in the file
#Total of all the number
#Average
#Highest number
#Lowest number
#Correct answers for the included file:

def process_numbers(file_path):
    try:
        with open(file_path, 'r') as file:
            numbers = [int(line.strip()) for line in file if line.strip().isdigit()]
        
        count = len(numbers)
        total = sum(numbers)
        average = total / count if count > 0 else 0
        highest = max(numbers) if count > 0 else None
        lowest = min(numbers) if count > 0 else None

        print(f"Number of numbers: {count}")
        print(f"Total of all numbers: {total}")
        print(f"Average: {average:.2f}")
        print(f"Highest number: {highest}")
        print(f"Lowest number: {lowest}")
    except FileNotFoundError:
        print(f"Error: The file '{file_path}' was not found.")
    except ValueError:
        print("Error: The file contains invalid data.")

if __name__ == "__main__":
    file_path = "numbers.txt"
    process_numbers(file_path)