import random

def generate_random_number():
    return random.randint(1, 100)

def generate_files():
    for char in range(ord('A'), ord('Z') + 1):
        filename = f"{chr(char)}.txt"
        with open(filename, 'a') as file:
            random_number = generate_random_number()
            file.write(str(random_number))
        print(f"{filename}: {random_number}")

def create_summary():
    with open("summary.txt", "w") as summary_file:
        for char in range(ord('A'), ord('Z') + 1):
            filename = f"{chr(char)}.txt"
            with open(filename, 'r') as file:
                number = file.read()
            summary_file.write(f"{filename}: {number} ")

if __name__ == "__main__":
    generate_files()
    create_summary()
