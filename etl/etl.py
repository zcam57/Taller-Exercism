def transform(legacy_data):

    result = {
        letter.lower(): score
        for score, letters in legacy_data.items()
        for letter in letters
        }
    return result