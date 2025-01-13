def main():
    text_file = "books/frankenstein.txt"

    # Check appereance of each letter
    def check_char(file_contents):
        char_dict = {}
        for char in file_contents.lower():
            if char not in char_dict:
                char_dict[char] = 1
            else:
                char_dict[char] += 1
        return char_dict

    # Return the total amount of words
    def return_num_words(file_contents):
        words_split = file_contents.split()
        return len(words_split)

    def sort_on(dict):
        return dict["count"]

    def sorting_words(char_dict):
        char_list = []
        for char, count in char_dict.items():
            char_list.append({"char": char, "count": count})
        char_list.sort(reverse=True, key=sort_on)
        return char_list

    def read_file():
        with open(text_file) as f:
            file_contents = f.read()
        return file_contents

    def final_report(word_count, sorted_chars):
        print("--- Begin report of books/frankenstein.txt ---")
        print(f"{word_count} words found in the document\n")
        
        for char_dict in sorted_chars:
            if char_dict["char"].isalpha():  # only print alphabetic characters
                print(f"The '{char_dict['char']}' character was found {char_dict['count']} times")
        
        print("--- End report ---")

    file_contents = read_file()
    words = return_num_words(file_contents)
    check_dict = check_char(file_contents)
    sorted_words = sorting_words(check_dict)
    final_report(words, sorted_words)

main()