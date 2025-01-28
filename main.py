def main():
    with open("books/frankenstein.txt") as file_to_read:
        content = file_to_read.read()
    print(content)

main()
