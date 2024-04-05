import re
def load_file(file_path):
    with open(file_path, 'r', encoding="utf-8") as f:
        text = f.read()
    return text


def parse_text(text: str) -> (int, int):
    sentence_end_symbols = "[.!?]"
    distributors_symbols = "[,.:; !?]"

    text = (text.replace("\n", " ")
            .replace(", ", ",")
            .replace(". ", ".")
            .replace("...", ".")
            .replace(": ", ":")
            .replace("; ", ";")
            .replace("! ", "!")
            .replace("? ", "?"))

    count_words = len(re.split(distributors_symbols, text))
    count_sentences = len(re.split(sentence_end_symbols, text))

    return count_words - 1, count_sentences - 1


if __name__ == '__main__':
    text = load_file("test.txt")
    print(parse_text(text))