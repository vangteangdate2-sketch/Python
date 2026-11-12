even_numbers = []

for num in range(21):
    if num % 2 == 1:
        even_numbers.append(num)

print(even_numbers)

#list comprehension
even_numbers = [num1 for num1 in range(21) if num1 % 2 == 0]
print(even_numbers)

#using conditional expression lists in list comprehension
numbers = [1, 2, 3, 4, 5]
result = [(num, 'Even') if num % 2 == 0 else (num, 'Odd') for num in numbers]
print(result)

# filtering 
words = ['tree', 'sky', 'mountain', 'river', 'cloud', 'sun']

def is_long_word(word):
    return len(word) <= 5

long_words = list(filter(is_long_word, words))
print(long_words) 

# mapping function
celsius = [0, 10, 20, 30, 40]

def to_fahrenheit(temp):
    return (temp * 9/5) + 32

fahrenheit = list(map(to_fahrenheit, celsius))
print(fahrenheit)
