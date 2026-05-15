from functions.get_file_content import get_file_content

print(get_file_content("calculator", "main.py"))
print('\n')
print(get_file_content("calculator", "pkg/calculator.py"))
print('\n')
print(get_file_content("calculator", "/bin/cat"))
print('\n')
print(get_file_content("calculator", "pkg/does_not_exist.py"))
print('\n')

content = get_file_content("calculator", "lorem.txt")
is_truncated = '[...File "lorem.txt" truncated at' in content
print(f"lorem.txt truncated: {is_truncated}")