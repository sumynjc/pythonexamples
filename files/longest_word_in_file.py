from string import punctuation

def longest_word_in_file(file_name:str) -> str:
    max =''
    f = open(file_name, 'r', encoding='utf-8')
    text =  f.read().split()
    for t in text:
        current = t.strip(punctuation)
        if len(current) > len(max):
            max = current

    return max
