def read_content(filename):
    with open(filename, 'r') as file:
        content = file.read()
    return content

def write_content(filename, content):
    with open(filename, 'w') as file:
        file.write(content)

def convert_to_uppercase(content):
    return content.upper()

if __name__ == "__main__":
    first_file_content = "Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat. Duis aute irure dolor in reprehenderit in voluptate velit esse cillum dolore eu fugiat nulla pariatur. Excepteur sint occaecat cupidatat non proident, sunt in culpa qui officia deserunt mollit anim id est laborum."
    first_file_name = "my_first_file.txt"
    write_content(first_file_name, first_file_content)

    
    content_from_first_file = read_content(first_file_name)

   
    uppercased_content = convert_to_uppercase(content_from_first_file)

    second_file_name = "my_second_file.txt"
    write_content(second_file_name, uppercased_content)

    print(f"Content of {first_file_name}:\n{content_from_first_file}\n")
    print(f"Content of {second_file_name} (in uppercase):\n{uppercased_content}")
