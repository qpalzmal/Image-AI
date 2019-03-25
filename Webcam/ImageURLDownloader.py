import urllib.request


def DownloadImages():
    file_name = input(
        str("Enter the name of the text file that contains the urls of images: "))  # user inputs name of file
    # print(file_name)
    try:
        # print(file_name + ".txt")
        # appends the file type ".txt" to end of name and reads the file
        file = open("test\\" + file_name + "\\" + file_name + ".txt", "r")  # opens the file at its designated path
        print(file.name)
    except FileNotFoundError:
        print("The file can not be found")
        print("Exiting the program now")
        exit()

    url_count = 0  # gets the line count for the file
    url_list = []  # list that will contain all the urls from the file
    for url in file:  # returns the n value of 10^n for formatted file count - ex 00005.png format
        url_count += 1
        url_list.append(url)
    decimal_count = len(str(url_count))  # value n of 10^n
    # print("DECIMALCOUNT: ", decimal_count)

    # 0 - 333 \\\ 1824 - urlcount --- numbers that need to be downloaded for computer, light, paper, phone, person
    for count in range(1496, 1824):
        format_number = str(count + 1)  # gets the number the file will be named and its a string
        place_zero = decimal_count - len(format_number)  # gets the amount of zeros to be added to front
        # print("PLACEZERO: ", place_zero)

        # adds the needed amount of zero to the beginning of the number
        for i in range(place_zero):
            format_number = "0" + format_number
            # print(format_number)

        # adds together the passed name, the number its assigned, and the file type
        image_name = file_name + "_" + format_number + ".jpg"
        img_url = url_list[count]  # gets the url associated with the line number from the list of urls

        print("URL {}: ".format(count) + img_url)
        # print("IMAGENAME: ", image_name)

        # does the downloading of the image and saves and the given name
        try:
            urllib.request.urlretrieve(img_url, "test\\" + file_name + "\\" + image_name)
        except TypeError:
            print("DOWNLOAD FAILED")
            print("")
        except urllib.request.HTTPError as e:
            if e == 403:
                print("HTTP ERROR")
                print("")
        except urllib.request.URLError as e:
            print("URL ERROR")
            print("")
        except TimeoutError:
            print("TIMEOUT ERROR")
            print("")
    print("DOWNLOAD COMPLETE")
    file.close()


def main():
    DownloadImages()


if __name__ == "__main__":
    main()
