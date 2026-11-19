file =open(r'c:\Users\ASUS\Downloads\Telegram Desktop\example.txt')
content = file.read()
print(content)
file.close()
print('')

file =open(r'c:\Users\ASUS\Downloads\Telegram Desktop\example.txt')
content = file.readlines()
for line in content:
    print(line.strip())

with open(r'C:\Users\ASUS\Downloads\Telegram Desktop\example.txt') as file:
    chunk = file.read(100)
    print(chunk)

