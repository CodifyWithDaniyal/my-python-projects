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
