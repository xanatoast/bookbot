def get_word_count(book_content):
    return len(book_content.split())

def get_character_count(book_content):
    letter_dict = {}
    for each in book_content:
        letter = each.lower()
        if letter not in letter_dict:
            letter_dict[letter] = 1
        else:
            letter_dict[letter] += 1
    return character_sort(letter_dict)

def character_sort(character_dict):
    letter_list = []
    for each in character_dict:
        if str.isalpha(each) == True:
            letter_list.append({"char": each, "num": character_dict[each]})
    letter_list.sort(reverse=True, key=sort_on)
    return letter_list

def sort_on(items):
    return items["num"]