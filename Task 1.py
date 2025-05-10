try:
    file = open("sample.txt", "r")
    print("Reading file content:")
    line_num = 1
    for line in file:
        print("Line", line_num, ":", line.strip())
        line_num += 1
    file.close()
except FileNotFoundError:
    print("Error: The file 'sample.txt' does not exist.")
