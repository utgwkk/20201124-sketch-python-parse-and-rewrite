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
            tokens_after.append((tokenize.NUMBER, str(new_number)))
        else:
            tokens_after.append((token.type, token.string))
    
    print(tokenize.untokenize(tokens_after))

if __name__ == '__main__':
    main(sys.argv[1:])
