# Number_reverser
# Small Python programm for reversing number
# Notice: This outputs the number as str


def num_reverser(n):

    size = len(str(n))  # getting the size of num by converting it to str then len
    cntr = size - 1  # counter for the loop has to be smaller by 1
    reversed_number = ""  # empty string to which we will append digits

    while cntr >= 0:  # smaller or equals to 0 because we need 10 on power of 0 to extract last digit

        digit = n // (10 ** cntr)   # digit on the left is extracted using floor division
        n = int(n) % (10 ** cntr)  # preparing number for the next loop iteration, the remainder
        reversed_number = "" + str(digit) + reversed_number  # appending digit on the front
        cntr -= 1  # and update counter

    return reversed_number  # returns reversed number as str

if __name__ == "__main__":
    number_input = input("Enter a number to be reversed: ")
    result = int(number_input)
    print(num_reverser(result))
