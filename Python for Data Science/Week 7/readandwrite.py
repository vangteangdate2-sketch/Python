with open('data.txt', 'r+') as file:
    content = file.read()
    file.write('\nNew data added')

with open('image.jpg','rb') as file:
    binary_data = file.read()

try:
    with open('new_file.txt','x') as file:
        file.write('This is a brand new file')
except FileExistsError:
    print('File already exist!')

    