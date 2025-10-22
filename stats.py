def get_word_count(text):
    return len(text.split())

def number_chars(text):
    counts = {}
    for ch in text.lower():
        counts[ch] = counts.get(ch, 0) + 1
    return counts

def convert_to_list(counts):
    return [{"char": k, "num": v} for k, v in counts.items()]

def sort_key(item):
    return item["num"]

def sorted_report(char_counts):
    items = convert_to_list(char_counts)
    items.sort(reverse=True, key=sort_key)
    return items
