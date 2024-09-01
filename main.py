def main():
  book_path = "books/frankenstein.txt"
  text = get_book_text(book_path)
  word_count = get_num_words(text)
  char_count = get_char_count(text)
  print(f"--- Begin report of {book_path} ---")
  print(f"{word_count} words found in the document\n")
  format_char_count_log(char_count)
  print(f"--- End report ---")

def format_char_count_log(char_count):
    # Sort the list in descending order based on the values
    char_count.sort(key=lambda x: list(x.values())[0], reverse=True)
    for dictionary in char_count:
        for key in dictionary:
            value = dictionary[key]
            print(f"The '{key}' character was found {value} times.")

def get_char_count(text):
    char_dict = {}
    for c in text:
        if c.isalpha():
          char = c.lower()
          if char in char_dict:
              char_dict[char] += 1
          else:
              char_dict[char] = 1
    return convert_dict_to_list(char_dict)

def convert_dict_to_list(dict):
    list_of_dicts = []
    for key in dict:
        value = dict[key]
        list_of_dicts.append({key: value})
    return list_of_dicts

def get_num_words(text):
    words = text.split()
    return len(words)

def get_book_text(path):
    with open(path) as f:
        return f.read()

main()