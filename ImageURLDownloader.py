import urllib.request


def reeee():
    file_name = input(
        str("Enter the name of the text file that contains the urls of images: "))  # user inputs name of file
    try:
        file = open(file_name + ".txt", "r")  # appends the file type ".txt" to end of name and reads the file
    except FileNotFoundError:
        print("The file can not be found")
        print("Fix the problem before running the program again")
        exit()

    url_count = 0  # gets the line count for the file
    for url in file:
        url_count += 1
    decimal_count = len(str(url_count))
    print(decimal_count)  # returns the n value of 10^n for formatted file count - ex 00005.png format
    # we get 4 so xxxx amount of images

    format_number = 1
    # for img in file:
    place_zero = decimal_count - len(str(format_number))  # gets the amount of zeros to be added to front
    print(str(format_number) + ".jpg")
    # urllib.request.urlretrieve(url, "{}str(format_number) + ".jpg")
    # format_number += 1



def main():
    reeee()


if __name__ == "__main__":
    main()
