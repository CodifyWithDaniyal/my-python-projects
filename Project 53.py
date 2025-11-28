# This program defines a function `word_in_line(word)` that searches for a word in a file named "practice.txt".
# - It reads the file line by line, checking if the word is present in each line.
# - If found, it prints the line number(s) where the word appears.
# - If the word is not found in the file, it prints "Not found".
def word_in_line(word):
    with open("practice.txt") as f:
        line_no = 1
        found = False
        
        for line in f:
            if word in line:
                print(f"Found in line {line_no}")
                found = True
            line_no += 1
        
        if not found:
            print("Not found")
