import re

def normalize_string(line):
    topic, text = line.split('\t')
#    text = text.strip()
    text = re.sub(r'\W+', ' ', text)
    text = re.sub(r'[0-9]', ' ', text)
    tokens = re.split(r' +', text)
    tokens = list(filter(None, tokens))
    return (topic, tokens)

def read_file(filename):
    fragments = []
    topics = []
    with open(filename, 'r') as file:
        for line in file:
            # Process each line here
            (topic, tokens) = normalize_string(line)
            topics.append(topic)
            fragments.append(tokens)
    return (fragments, topics)

def main():
    (fragments, topics) = read_file('test_input.txt')
    print(fragments)
    print("******************")
    print(topics)

if __name__ == '__main__':
    main()