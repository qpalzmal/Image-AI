import urllib.request


def DownloadImages():
    file_name = input(
        str("Enter the name of the text file that contains the urls of images: "))  # user inputs name of file
    print(file_name)
    try:
        print(file_name + ".txt")
        file = open(file_name + ".txt", "r")  # appends the file type ".txt" to end of name and reads the file
    except FileNotFoundError:
        print("The file can not be found")
        print("Exiting the program now")
        exit()

    url_count = 0  # gets the line count for the file
    for url in file:  # returns the n value of 10^n for formatted file count - ex 00005.png format
        url_count += 1
    decimal_count = len(str(url_count))
    # print("DECIMALCOUNT: ", decimal_count)

    for count in range(url_count):
        format_number = str(count + 1)
        place_zero = decimal_count - len(format_number)  # gets the amount of zeros to be added to front
        # print("PLACEZERO: ", place_zero)
        # adds the needed amount of zero to the beginning of the number
        for i in range(place_zero):
            format_number = "0" + format_number
            # print(format_number)
        # adds together the passed name, the number its assigned, and the file
        image_name = file_name + "_" + format_number + ".jpg"
        reader = file.readlines()
        print("URL: ", reader[count - 1])
        print("IMAGENAME: ", image_name)

        # does the downloading of the image and saves and the given name
        try:
            urllib.request.urlretrieve(reader[count - 1], image_name)
        except TypeError:
            print("DOWNLOAD FAILED")
            print("")


def main():
    DownloadImages()


if __name__ == "__main__":
    main()
