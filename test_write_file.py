from functions.write_file import write_file

# The first call will overwrite the original lorem.txt
print(write_file("calculator", "lorem.txt", "wait, this isn't lorem ipsum"))

# The second call will create a new file inside the pkg directory
print(write_file("calculator", "pkg/morelorem.txt", "lorem ipsum dolor sit amet"))

# This call should be rejected because /tmp is outside the working directory
print(write_file("calculator", "/tmp/temp.txt", "this should not be allowed"))