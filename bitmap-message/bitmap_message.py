"""
Bitmap Message
> Displays A Text Message According to the Provided Bitmap Image.
"""

import os


def read_bitmap(filename: str) -> str:
    with open(filename, "r", encoding="utf-8") as bitmap:
        return bitmap.read()


def bitmap_message_application() -> None:
    application_name = "Bitmap Message Application"
    print(application_name)
    print("-" * len(application_name))

    print("Please Enter The Name of The Bitmap Text File")
    while True:
        filename = input("> ")
        if os.path.isfile(filename):
            break
        print("File Does Not Exist. Try Again!")

    bitmap = read_bitmap(filename)

    print("Enter The Message To Display with The Bitmap")
    message = input("> ")
    if message == "":
        return

    new_bitmap = ""
    for line in bitmap.splitlines():
        modified_line = ""
        for index, char in enumerate(line):
            if char == " ":
                modified_line += " "
            else:
                modified_line += message[index % len(message)]
        new_bitmap += modified_line + "\n"

    print(new_bitmap)


if __name__ == "__main__":
    bitmap_message_application()
