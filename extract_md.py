import re

def extract_fragments_from_md(filepath):
    with open(filepath, 'r', encoding='utf-8') as file:
        md_text = file.read()

    fragments = []
    question_types = []

    # Regex patterns
    lo_sample_pattern = re.compile(r'<lo-sample/>(.*?)\* questionType', re.DOTALL)
    question_type_pattern = re.compile(r'questionType:(.*?)</small>', re.DOTALL)

    # Find all matches of <lo-sample/> and questionType
    lo_sample_matches = lo_sample_pattern.findall(md_text)
    question_type_matches = question_type_pattern.findall(md_text)

    # Extract fragments and question types
    for lo_sample, question_type in zip(lo_sample_matches, question_type_matches):
        fragment = re.sub(r'<small>.*?</small>', '', lo_sample.strip(), flags=re.DOTALL)
        fragment = re.sub(r'<small>', '', fragment)
        fragment = re.sub(r'</small>', '', fragment)
        question_type = question_type.strip()
        fragments.append(fragment)
        question_types.append(question_type)

    return fragments, question_types

# Example Markdown file
filepath = "content.md"
fragments, question_types = extract_fragments_from_md(filepath)

with open("content_new.md", "w", encoding="utf-8") as output_file:
    for fragment in fragments:
        output_file.write(fragment.strip() + "\n\n")
