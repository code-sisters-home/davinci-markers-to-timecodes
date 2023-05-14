import os
import re

directory_path = 'edls'


def print_hi(directory):
    for filename in os.listdir(directory):
        if filename.endswith(".edl"):
            file_path = os.path.join(directory, filename)
            try:
                with open(file_path, 'r', encoding='utf-8') as file:
                    lines = file.readlines()
                    result = []
                    for i in range(len(lines) - 1):
                        line1 = lines[i].strip()
                        line2 = lines[i + 1].strip()

                        match1 = re.search(r'\d{2}:\d{2}:\d{2}:\d{2}', line1)
                        match2 = re.search(r'\|M:(.*?)\|D:1', line2)

                        if match1 and match2:
                            group1 = match1.group(0)[:-3]
                            group2 = match2.group(1)
                            joined = f'{group1} {group2}'
                            result.append(joined)

                    output = '\n'.join(result)
                    print(output)
                    output_file_path = file_path.rsplit('.', 1)[0] + '.txt'
                    with open(output_file_path, 'w', encoding='utf-8') as output_file:
                        output_file.write(output)

                    file.close()
                    output_file.close()
            except FileNotFoundError:
                print(f"File '{file_path}' not found.")
            except IOError:
                print(f"Error reading file '{file_path}'.")


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    print_hi(directory_path)

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
