def deck_txt_to_list(path):

    list_of_cards = []
    reserved_words = ["MONSTER CARDS", "SPELL CARDS", "TRAP CARDS", "EXTRA DECK CARDS", "SIDE DECK CARDS"]
    deck_txt = open(path, 'r')
    line_list = []

    for line in deck_txt:
        stripped_line = line.strip()
        aux = stripped_line.strip("|- ")
        if not aux == '':
            line_list.append(aux)

    for line in line_list:
        if (reserved_words[0] in line) or\
                (reserved_words[1] in line) or \
                (reserved_words[2] in line) or \
                (reserved_words[3] in line) or \
                (reserved_words[4] in line):

            line_list.remove(line)

    for e in line_list:
        row = e.split("x ")
        list_of_cards.append(row[1])

    return list_of_cards
