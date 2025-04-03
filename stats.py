from typing import List, Dict

def get_num_words(text: str):
    words = text.split()
    return len(words)

def get_char_count(text: str):
    text = text.lower()
    result = {}
    for char in text:
        if char in result.keys():
            result[char] += 1
        else:
            result[char] = 1
    return result

def sort_count_descending(chars: Dict):
    if not chars:
        return {}

    sorted = []
    for k, v in chars.items():
        if k.isalpha():
            sorted.append({
                'character': k,
                'count': v
            })
    def return_count(l: List):
        return l['count']
    sorted.sort(reverse=True, key=return_count)
    return sorted
