import os

def count_num_files(root_dir):
    count = 0
    for current_path, dirs, files in os.walk(root_dir):
        for file in files:
            count += 1

    return count

def list_all_files(root_dir):
    count = 0
    global matched_file_names
    global matched_file_content
    global total_occurrences
    for current_path, dirs, files in os.walk(root_dir):
        for file in files:
            count += 1
            found = False

            if keyword.lower() in file.lower():
                found = True
                matched_file_names += 1
                
                #print(f"file number {count} of {total}, {file}, has the keyword in its name!")

            occurrences = check_file(os.path.join(current_path, file))
            if occurrences != 0:
                found = True
                matched_file_content += 1
                total_occurrences += occurrences
                occurrence_time.append(total_occurrences)
                #print(f"file number {count} of {total}, {file}, has {occurrences} occurrences of the keyword in its content!")
            #print(f"{count} of {total}, names: {matched_file_names}, content: {matched_file_content}, occurrences: {total_occurrences}")

            if found:
                display_graph(count)



def check_file(file):
    occurrences = 0

    with open(file, "r", errors="ignore") as f:
        count = 0
        for line in f:
            count += 1

            low_line = line.lower()
            occurrences += low_line.count(keyword)

            if count > 250:
                return occurrences

    return occurrences

def display_graph(count=1):
    os.system('cls' if os.name == 'nt' else 'clear')

    height = 10
    width = 40
    """
    data = occurrence_time
    if len(data) >= width:
        step = len(data) // width
        sampled = [data[i] for i in range(0, len(data), step)][:width]
    else:
        sampled = data

    max_val = max(sampled) if sampled else 1
    scaled = [int((val / max_val) * (height - 1)) for val in sampled]

    grid = [[" " for _ in range(width)] for _ in range(height)]

    for x, y in enumerate(scaled):
        plot_y = height - 1 - y   # invert vertically
        grid[plot_y][x] = "*"

    for row in grid:
        print("|" + "".join(row))
    """
    quarter = count//4
    print(f"L{"_"*39}")
    print(f"0{" "*9}{quarter}{" "*9}{quarter*2}{" "*9}{count}")
    print(f"files scanned: {count} / {total}")
    print()
    print(f"keyword: {keyword} occurrences so far: {total_occurrences}")

    return 

keyword = "hello"
matched_file_extention = {}
matched_file_names = 0
matched_file_content = 0
total_occurrences = 0
occurrence_time = []
fast = False

path = "C:\\dev"

total = count_num_files(path)

list_all_files(path)

print(total, matched_file_names, matched_file_content)
