import os


def delete_file(file_name):
    if os.path.exists(file_name):
        os.remove(file_name)
        print(f"{file_name} silindi")
    else:
        print(f"{file_name} movcud deyil.")


def add_information(database_file, new_info):
    with open(database_file, 'a') as f:
        if new_info not in f.read():
            f.write(new_info + '\n')
            print(f"melumat elave edin: {new_info}")
        else:
            print(f"tekrar melumat elave edin: {new_info} bazada movcud deyil.")


def show_database_info(database_file):
    with open(database_file, 'r') as f:
        lines = f.readlines()
        print(f"Number of lines in the database: {len(lines)}")

# Function to find the first and last index of elements in the file
def find_first_and_last_index(database_file, element):
    with open(database_file, 'r') as f:
        lines = f.readlines()
        first_index = None
        last_index = None

        for i, line in enumerate(lines):
            if element in line:
                if first_index is None:
                    first_index = i
                last_index = i

        if first_index is not None:
            print(f"First index of '{element}' in the database: {first_index}")
            print(f"Last index of '{element}' in the database: {last_index}")
        else:
            print(f"'{element}' not found in the database.")


database_file = 'database.txt'

while True:
    print("\n(1) sil TXT File")
    print("(2) melumat elave edin")
    print("(3) bazani goster")
    print("(4) birinci ve sonuncu indeksi tap")
    print("(5) Quit")

    choice = input("secim elave edin: ")

    if choice == '1':
        file_to_delete = input("file adin elave edin (e.g., file.txt): ")
        delete_file(file_to_delete)
    elif choice == '2':
        new_info = input("bazaya yeni melumat elave edin: ")
        add_information(database_file, new_info)
    elif choice == '3':
        show_database_info(database_file)
    elif choice == '4':
        element_to_find = input("elementlari tap: ")
        find_first_and_last_index(database_file, element_to_find)
    elif choice == '5':
        break
    else:
        print("sehv secim: 1, 2, 3, 4, 5.")
