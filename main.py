import sys
import tokenize

def main(argv):
    for filename in argv:
        process(filename)

def process(filename):
    tokenized = tokenize.generate_tokens(tokenize.open(filename).readline)
    tokens_after = []

    for token in tokenized:
        if token.type == tokenize.NUMBER:
            new_number = int(token.string) * 2
            tokens_after.append((tokenize.NUMBER, str(new_number), token.start, token.end, token.line))
        else:
            tokens_after.append(token)

    with open(filename, 'wt') as f_out:
        f_out.write(tokenize.untokenize(tokens_after))

if __name__ == '__main__':
    main(sys.argv[1:])
