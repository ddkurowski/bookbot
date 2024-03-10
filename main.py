def main():
    with open("books/frankenstein.txt") as f:
        book = f.read()
        word_count = book_to_string(book)
        letter_dict = character_count(book)
        dict_list = convert_to_list(letter_dict)
        final_report = sorted_report(dict_list)
        print(f"--- Begin report ---")  
        print(f"{word_count} words found in the document")
        print(final_report)
        print(f"---End of Report---")
        

def book_to_string(book):
    words = book.split()
    return len(words)

def character_count(book):
    words = book.lower()
    letter_dict = {}
    for letter in words:
        #checks if the character is a letter and if it is, proceeds to update the counts, if it's a special character (%, &, etc.) then it's skipped.
        if letter.isalpha() == True: 
            if letter in letter_dict:
                letter_dict[letter] += 1
            else:
                letter_dict[letter] = 1
    return letter_dict

def convert_to_list(letter_dict):
    dict_list = []
    for key, value in letter_dict.items():
        dict_list.append({"char": key,"count": value})
    return dict_list

def sort_list(item):
    return item["count"]

def sorted_report(dict_list):
    dict_list.sort(reverse=True, key=sort_list)
    report = ""
    for i in range(len(dict_list)):
        report += (f"The {dict_list[i]['char']} character was found {dict_list[i]['count']} times \n")
    return report
        
    


    

main()