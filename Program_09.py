def remove_odd_numbers(numbers):
 
    even_numbers = []


    i = 0
    while i < len(numbers):

        if numbers[i] % 2 == 0:
            
            even_numbers.append(numbers[i])
        i += 1


    return even_numbers


numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9]
print(remove_odd_numbers(numbers)) 