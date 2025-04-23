def count_words(sentence):
    # return len(sentence.strip().split())
    count = 0
    is_word = False

    for char in sentence:
        if char not in [' ', '\n', '\t']:
            if not is_word:
                count += 1
                is_word = True
        else:
            is_word = False

    return count



if __name__ == '__main__':
    sentence = "This is a sample sentence for counting words."
    word_count = count_words(sentence)
    print(word_count)  # 8 should be printed