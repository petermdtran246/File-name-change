# Read the name of the input file
input_file = input().strip()

# Read file contents and modify file names
with open(input_file, 'r') as file:
    photo_names = file.readlines()

modified_names = [name.strip().replace('_photo.jpg', '_info.txt') for name in photo_names]

# Output modified file names
for name in modified_names:
    print(name)
