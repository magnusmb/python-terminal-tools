import re
import sys
import argparse
from highlighter import highlight_text


def make_pattern_dict(patterns: list):
    """Makes a dictionary of patterns in the format expected of
    highlight_text().

    Each pattern is assigned one of four preset colors.

    Parameters:
    patterns (list): A list of regex patterns as strings

    Returns:
    pattern_dict (dict): Dictionary with an entry for each pattern, each
    containing the color and regex pattern.
    """
    colors = [
            '\033[0;32',
            '\033[0;33',
            '\033[0;34',
            '\033[0;35'
            ]

    pattern_dict = {}
    i = 0

    for pattern in patterns:
        pattern_dict[str(i)] = {}
        pattern_dict[str(i)]["color"]   = colors[i%4]
        pattern_dict[str(i)]["pattern"] = pattern
        i += 1

    return pattern_dict


def find_matching_lines(text, patterns):
    matching_lines = []

    for line in text:
        for pattern in patterns:
            match = re.search(pattern, line)
            if match:
                matching_lines.append(line)
                break

    return matching_lines


def parse_args(args):
    p = argparse.ArgumentParser()
    p.add_argument('--highlight', action='store_true', help='Highlight output')
    p.add_argument('patterns', nargs='+', help='Regex patterns')
    p.add_argument('file', help='Path to file you want to search for matches in')
    p.set_defaults(highlight=False)

    return p.parse_args()


def main():
    parsed_args = parse_args(sys.argv)
    input_file = parsed_args.file
    patterns = parsed_args.patterns

    with open(input_file) as f:
        all_lines = f.read().strip().split('\n')

    matching_lines = find_matching_lines(all_lines, patterns)

    if parsed_args.highlight:
        pattern_dict = make_pattern_dict(patterns)

        for line in matching_lines:
                hi_line = highlight_text(line, pattern_dict)
                print(hi_line)
    else:
        print('\n'.join(matching_lines))


if __name__ == "__main__": main()
