def main():
    book_path = "books/frankenstein.txt"
    text = get_book_text(book_path)
    num_words = word_count(text)
    num_chars = char_count(text)
    #print(f"{num_chars} words found in the document")
    #print(num_chars)
    sorted_char_list = chars_to_sorted(num_chars)

    print(f"--- Begin report of {book_path} ---")
    print(f"{num_words} words found in the document")
    print()

    for item in sorted_char_list:
        if not item["char"].isalpha():
            continue
        print(f"The '{item['char']}' character was found {item['num']} times")
    
    print("--- End report ---")

#get text of book
def get_book_text(path):
    with open(path) as f:
        return f.read()
    
#count the words
def word_count(text):
    words = text.split()
    return len(words)

#count each char
def char_count(text):
    my_dict = {}

    for char in text:
        lowered = char.lower()
        if lowered in my_dict:
            my_dict[lowered] += 1
        else:
            my_dict[lowered] = 1
    return my_dict


def sort_on(d):
    return d["num"]


#convert char count to a sorted list
def chars_to_sorted(num_chars_dict):
    sorted_list = []
    for char in num_chars_dict:
        sorted_list.append({"char": char, "num": num_chars_dict[char]})
    sorted_list.sort(reverse=True, key=sort_on)
    return sorted_list

main()