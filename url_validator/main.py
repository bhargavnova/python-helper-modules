import url_validator

if __name__ == "__main__":
    url = input("Enter a URL: ")

    is_valid, is_accessible = url_validator.validate(url)

    if is_valid:
        print("The URL is valid.")

        if is_accessible:
            print("The URL is accessible.")
        else:
            print("The URL is not accessible.")
    else:
        print("The URL is not valid.")
