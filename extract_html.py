from bs4 import BeautifulSoup
import re

def normalize_string(topic, text):
    text = re.sub(r'\W+', ' ', text)
    text = re.sub(r'[0-9]', ' ', text)
    tokens = re.split(r' +', text)
    tokens = list(filter(None, tokens))
    return (topic, tokens)

def read_file(filename):
    with open(filename, 'r') as file:
        for line in file:
            # Process each line here
            (topic, tokens) = normalize_string(line)
            topics.append(topic)
            fragments.append(tokens)
    return (fragments, topics)

def extract_fragments_from_html(html_filename):
    with open(html_filename, 'r', encoding='utf-8') as file:
        html_content = file.read()
        # print(len(html_content))

    soup = BeautifulSoup(html_content, 'html.parser')
    fragments = []

    # post_items = soup.find_all('div', class_='cmty-view-post-item')
    # for item in post_items:
    #     print(".", end='')
    #     label = item.find('div', class_='cmty-view-post-item-label').text.strip()
    #     text = item.find('div', class_='cmty-view-post-item-text').text.strip()
    #     fragments.append((label, text))

    label_elements = soup.find_all('div', class_='cmty-view-post-item-label')
    text_elements = soup.find_all('div', class_='cmty-view-post-item-text')

    for label_elem, text_elem in zip(label_elements, text_elements):
        label = label_elem.text.strip()
        text = text_elem.text.strip()
        fragments.append((label, text))

    return fragments

def read_all_htmls():
    global section
    fragments = []
    topics = []
    for year in range(1998, 2022):
        section = 0
        filename = 'html/page_{}.html'.format(year)
        result_list = extract_fragments_from_html(filename)
        print(len(result_list))
        for item in result_list:
            # print(get_topic(item[0]), end=', ')
            (topic, tokens) = normalize_string(get_topic(item[0], year), item[1]) # item[0] topic, item[1] body text
            topics.append(topic)
            fragments.append(tokens)
    return (fragments, topics)

section = 0

def get_topic(label, year):
    global section
    topic_sequences = {1998:['Geometry', 'NumberTheory', 'Algebra', 'Combinatorics'],
                       1999:['Geometry', 'NumberTheory', 'Algebra', 'Combinatorics'],
                       2000:['Algebra', 'Geometry', 'NumberTheory', 'Combinatorics'],
                       2001:['Geometry', 'NumberTheory', 'Algebra', 'Combinatorics'],
                       2002:['Geometry', 'NumberTheory', 'Algebra', 'Combinatorics'],
                       2003:['Geometry', 'NumberTheory', 'Algebra', 'Combinatorics'],
                       2004:['Geometry', 'NumberTheory', 'Algebra', 'Combinatorics'],
                       2005:['Algebra', 'Combinatorics', 'Geometry', 'NumberTheory'],
                       2006:['Algebra', 'Combinatorics', 'Geometry', 'NumberTheory'],
                       2007:['Algebra', 'Combinatorics', 'Geometry', 'NumberTheory'],
                       2008:['Algebra', 'Combinatorics', 'Geometry', 'NumberTheory'],
                       2009:['Algebra', 'Combinatorics', 'Geometry', 'NumberTheory'],
                       2010:['Algebra', 'Combinatorics', 'Geometry', 'NumberTheory'],
                       2011:['Algebra', 'Combinatorics', 'Geometry', 'NumberTheory'],
                       }
    if label[0] == "A":
        return "Algebra"
    elif label[0] == "C":
        return "Combinatorics"
    elif label[0] == "G":
        return "Geometry"
    elif label[0] == "N":
        return "NumberTheory"
    elif label[0] == "1":
        section += 1
    return topic_sequences[year][section-1]