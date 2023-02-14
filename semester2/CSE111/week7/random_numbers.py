import random

def main():

    numbers=[16.2,75.1,52.3]
    
    print(f"Before changes : { numbers}")

    append_random_numbers(numbers)
    print(f"After add one number : {numbers}")

    append_random_numbers(numbers,3)
    print(f"After add three numbers : {numbers}")


def append_random_numbers(numbers_list, quantity=1):

    for i in range(quantity):
        number=round(random.uniform(1.0,99.9),1)
        numbers_list.append(number)
    
if __name__=="__main__":
    main()