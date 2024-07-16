def main():
    book_path = "books/frankenstein.txt"
    generate_report(book_path)
	

def get_book_text(path):
    with open(path) as f:
        return f.read()




def count_characters(text):
    count_chars = {}
    words = text.split()
    for char in text:
        if char.isalpha():
            char = char.lower()
            if char in count_chars:
                count_chars[char] += 1
            else:
                count_chars[char] = 1
    return len(words), count_chars

            

def sort_on(count_characters):
	return [{'name': key, 'num': value} for key, value in count_characters.items()]
    
def sort_final(sorted_dict):
    return sorted_dict["num"]

def generate_report(path):
    text = get_book_text(path)
    word_count, count_chars = count_characters(text)

    
    sorted_dict = sort_on(count_chars)
    sorted_dict.sort(reverse=True, key=sort_final)
    
    print(f"--- Begin report of {path} ---")
    print(f"{word_count} words found in the document")
    for item in sorted_dict:
        print(f"The '{item['name']}' character was found {item['num']} times")
    print("--- End report ---")
        
        
        
	

	
    
            

main()