def index(word_list, n_gram_length=3):
    storage = {}
    # Add n_grams to storage.
    for word in word_list:
        for i in range(len(word)-n_gram_length+1):
            n_gram = word[i:i+n_gram_length]
            if n_gram in storage:
                storage[n_gram].append(word)
            else:
                storage[n_gram] = [word]

    # Get and alphabetize keys.
    keys = sorted(storage.keys())

    # Generate list of output tuples
    print('{')
    for key in keys:
        print('  {}: {},'.format(key, storage[key]))
    print('}')
