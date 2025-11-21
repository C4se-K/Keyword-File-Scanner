import os
import argparse

def count_num_files(root_dir):
    count = 0
    for _, _, files in os.walk(root_dir):
        count += len(files)
    return count

def list_all_files(root_dir):
    global matched_file_names, matched_file_content, total_occurrences, occurrence_time

    count = 0
    for current_path, dirs, files in os.walk(root_dir):
        for file in files:
            count += 1
            found = False

            if keyword.lower() in file.lower():
                found = True
                matched_file_names += 1

            occurrences = check_file(os.path.join(current_path, file))
            if occurrences != 0:
                found = True
                matched_file_content += 1
                total_occurrences += occurrences
                occurrence_time.append(total_occurrences)

            if found:
                display_graph(count)

def check_file(file):
    occurrences = 0
    with open(file, "r", errors="ignore") as f:
        for i, line in enumerate(f, start=1):
            occurrences += line.lower().count(keyword)
            if i > 250:
                break
    return occurrences

def display_graph(count=1):
    os.system('cls' if os.name == 'nt' else 'clear')
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

    quarter = count // 4
    print(f"L{'_'*39}")
    print(f"0{' '*9}{quarter}{' '*9}{quarter*2}{' '*9}{count}")
    print(f"files scanned: {count} / {total}")
    print()
    print(f"keyword: {keyword} occurrences so far: {total_occurrences}")

def main():
    global keyword, total, matched_file_names, matched_file_content
    global total_occurrences, occurrence_time

    parser = argparse.ArgumentParser(description="Search files for keyword occurrences.")
    parser.add_argument("--path", required=True, help="Root directory to scan")
    parser.add_argument("--keyword", required=True, help="Keyword to search for")
    args = parser.parse_args()

    keyword = args.keyword.lower()
    matched_file_names = 0
    matched_file_content = 0
    total_occurrences = 0
    occurrence_time = []

    total_files = count_num_files(args.path)
    globals()["total"] = total_files

    list_all_files(args.path)

    print(total_files, matched_file_names, matched_file_content)

if __name__ == "__main__":
    main()
