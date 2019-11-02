import regex as re

def tag(tag_name, match):
    return (tag_name, match)


def tag_string(string, pattern, tag_name):
    match = re.search(pattern, string)

    if match is not None:
        (start, end) = match.span()
        tagged = tag(tag_name, match.group(0))
        return [string[:start], tagged, string[end:]]

    return [string]


def tag_all_matching(full_text, pattern, tag_name):
    i = 0

    while i < len(full_text):
        if isinstance(full_text[i], str):
            full_text[i:i+1] = tag_string(full_text[i], pattern, tag_name)
        i += 1

    return full_text
