import re

first = True
with open('author-quote.txt') as txt:
    with open('author-quote.json', 'w') as json:
        json.write("[")
        for line in txt:
            # print(line)
            if not first:
                json.write(",")
            else:
                first = False
            author, quote = line.split('\t')
            quote = quote.replace('\n', '')
            quote = quote.replace('"', '\'')
            json.write("{")
            json.write(f'"author": "{author}",')
            json.write(f'"text": "{quote}"')
            json.write("}")
    #     for c in classes:
    #         the_file.write(f'DROP TABLE "{c}" CASCADE CONSTRAINTS;\n')
    #     the_file.writelines(lines)
        json.write("]")
