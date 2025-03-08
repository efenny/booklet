def get_book_text(b):
    file_contents = ''
    with open(b) as f:
        file_contents = f.read()

    return file_contents
