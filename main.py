
def main():
    book_path = 'books/frankenstein.txt'
    text = get_book_text(book_path)
    num_words = count_words(text)
    letter_count_dict = letter_count(text)
    print('--- Begin report of books/frankenstein.txt ---')
    print(f'{num_words} words found in the document')
    list = create_report_list(letter_count_dict);
    print_report_list(list)
    print('--- End report ---')

def print_report_list(list):
    for item in list:
        print(f'The "{item['name']}" character was found {item['num']} times')

def create_report_list(dictlist):
    list = []
    for key in dictlist:
        dict = {}
        if key.isalpha():
            dict['name'] = key
            dict['num'] = dictlist[key]
        if (len(dict) > 0):
            list.append(dict)
    list.sort(reverse=True, key=sort_on)
    return list

def sort_on(dict):
    return dict['num']

def count_words(str):
    words = str.split()
    return len(words)

def get_book_text(path):
    with open(path) as f:
        file_contents = f.read()
        return file_contents

def letter_count(text):
    dict = {}
    for char in text:
        lowered = char.lower()
        if lowered in dict:
            dict[lowered] += 1
        else:
            dict[lowered] = 1
    return dict

main()