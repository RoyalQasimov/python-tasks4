import os


def delete_file(file_name):
    if os.path.exists(file_name):
        os.remove(file_name)
        print(f"{file_name} silindi.")
    else:
        print(f"{file_name} movcud deyil.")


def add_information(database_file, new_info):
    with open(database_file, 'a') as f:
        if new_info not in f.read():
            f.write(new_info + '\n')
            print(f"yeni melumat elde olundu: {new_info}")
        else:
            print(f"tekrar melumat: {new_info} baza movcuddur.")

# Function to show the number of lines in the database
def show_database_info(database_file):
    with open(database_file, 'r') as f:
        lines = f.readlines()
        print(f"bazada setirlerin sayi: {len(lines)}")


database_file = 'database.txt'

while True:
    print("\n(1) Sil TXT File")
    print("(2) melumat elave et")
    print("(3) bazani goster")
    print("(4) Cixin")

    choice = input("secimi daxil edin: ")

    if choice == '1':
        file_to_delete = input("falin adin daxil edin (e.g., file.txt): ")
        delete_file(file_to_delete)
    elif choice == '2':
        new_info = input("bazaya melumat elave edin: ")
        add_information(database_file, new_info)
    elif choice == '3':
        show_database_info(database_file)
    elif choice == '4':
        break
    else:
        print("sehv secim. yeniden secin 1, 2, 3, 4.")

