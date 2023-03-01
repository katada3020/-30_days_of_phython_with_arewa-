def count_lines_words(filename):
    with open(filename, 'r') as file:
        text = file.read()
        lines = len(text.split('\n'))
        words = len(text.split())
    return lines, words
lines, words = count_lines_words('/storage/sdcard0/txtpad/obama.txt')
print(f"The file has {lines} lines and {words} words")
lines, words = count_lines_words('/storage/sdcard0/txtpad/mitchel.txt')
print(f"the file had {lines} lines and {words} words")
lines,words = count_lines_words('/storage/sdcard0/txtpad/melina.txt')
print(f"the file has {lines} lines and {words} words")
