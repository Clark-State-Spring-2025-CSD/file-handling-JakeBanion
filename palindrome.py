#For this assignment use the words.txt file.
#Read in all the words. Count how many are palindromes, or words that are spelled the same forwads and backwards.
#For example, wow is a paldindrome.
#A different file wile be used for grading.
#Correct answer for this file: 15 Palindromes.

def is_palindrome(word):
    return word == word[::-1]

def count_palindromes(file_path):
    with open(file_path, 'r') as file:
        words = file.read().splitlines()
    palindromes = [word for word in words if is_palindrome(word)]
    return len(palindromes), palindromes

if __name__ == "__main__":
    file_path = "words.txt"
    count, palindromes = count_palindromes(file_path)
    print(f"Number of palindromes: {count}")
    print("Palindromes:", palindromes)