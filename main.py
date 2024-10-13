def main():
    with open("/home/roman/projects/github/romanschenk/bookbot/books/frankenstein.txt") as txt_file:
        txt = txt_file.read()
        word_count =count_words(txt)
        character_count_dict = count_characters(txt)
        report = format_report(word_count, character_count_dict)
        print(report)

def count_words(txt: str):
    lst_words = txt.split()
    return len(lst_words)

def count_characters(txt:str):
    character_dict = {}
    for char in txt.lower():
        if char in character_dict:
            character_dict[char] += 1
        else:
            character_dict[char] = 1
    return character_dict

def format_report(word_count, character_count_dict):
    report = ["--- Begin report of books/frankenstein.txt ---\n\n"]
    report.append(f"{word_count} words found in the document\n")

    for key in character_count_dict:
        if key == "\n":
            continue
        report.append(f"The '{key}' character was found {character_count_dict[key]} times\n")

    report.append("--- End report ---")

    return "".join(report)

if __name__ == "__main__":
    main()