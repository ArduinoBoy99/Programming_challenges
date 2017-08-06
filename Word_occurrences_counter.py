# Word_occurrences_counter
# Counts the number of occurrences for specified word in specified text file


def term_seracher(search_term, f_name):

    occ_counter = 0  # sets counter
    f_handle = open(str(f_name) + ".txt")  # opens file handle on file name + .txt at the end

    for line in f_handle:  # opens every line in file in each iteration
        line = (line.strip()).split(" ")  # splits the words and makes a list from a stripped line
        lst_counter = line.count(search_term)  # counts the search term occurrences in the list
        occ_counter += lst_counter  # adds the list results to file results

    f_handle.close()  # closes the file handle
    print(str(occ_counter) + " occurrences found in " + str(file) + " file.")  # prints results


def main():
    term = str(input("Enter word to search for: "))
    file = input("Enter name of the file to search: ")
    term_seracher(term, file)

if __name__ == "__main__":
    main()
