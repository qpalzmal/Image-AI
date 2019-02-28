import urllib.request


def DownloadImages():
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
    # print("DECIMALCOUNT: ", decimal_count)  # returns the n value of 10^n for formatted file count - ex 00005.png format
    # we get 4 so xxxx amount of images

    format_number = "1"  # number that the file will be named
    iter_format_number = 1
    for url in range(url_count):
        place_zero = decimal_count - len(str(format_number))  # gets the amount of zeros to be added to front
        # print("PLACEZERO: ", place_zero)
        for i in range(place_zero):
            format_number = "0" + format_number
            # print(format_number)
        image_name = file_name + "_" + format_number + ".jpg"
        print("IMAGENAME: ", image_name)

        # urllib.request.urlretrieve(url, format_number + ".jpg")
        iter_format_number += 1
        format_number = str(iter_format_number)


def main():
    DownloadImages()


if __name__ == "__main__":
    main()
