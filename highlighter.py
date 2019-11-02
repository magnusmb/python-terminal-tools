#!/usr/bin/env python3
import regex as re
import sys
import argparse
from syntax_tagger import *


def highlight_text(input_text: str, rules: dict):
    """Highlights a given string according to a dictionary of highlighting
    rules.

    Parameters:
    input_text (str): The text to be highlighted.
    rules (dict): A dictionary with entries of different regex patterns with
    corresponding colors to be applied.

    Returns:
    output (str): The resulting string after highlighting rules have been
    aplied to the input text.
    """

    tagged_text = [input_text]

    for tag_name, entry in rules.items():
        tag_all_matching(tagged_text, entry["pattern"], tag_name)

    output = ''

    for elem in tagged_text:
        if isinstance(elem, str):
            output += elem
        else:
            (tag_name, text) = elem
            color = f'\033[{rules[tag_name]["color"]}m'
            reset = f'\033[0m'
            output += f'{color}{text}{reset}'

    return output


def add_patterns_to_rulebook(syntax_rules: list, rulebook: dict):
        for line in syntax_rules:
            try:
                pattern = re.search('"(.*)":', line).group(1)
                tag_name = re.search(' (\w+(-\w+)*)$', line).group(1)
            except AttributeError:
                print("\nFormat error in syntax file!")
                exit()

            rulebook[tag_name] = {"pattern": f'{pattern}'}


def add_colors_to_rulebook(theme_rules: list, rulebook: dict):
        for line in theme_rules:
            try:
                tag_name = re.search('^(\w+(-\w+)*):', line).group(1)
                color = re.search(' (\d{1,2};\d{1,2})$', line).group(1)
            except AttributeError:
                print("\nFormat error in theme file!")
                exit()

            # [tag_name, color] = line.strip().split(" : ")
            if tag_name in rulebook:
                rulebook[tag_name]["color"] = color


def parse_args(args):
    p = argparse.ArgumentParser()
    p.add_argument('syntax', help='Path to syntax pattern file')
    p.add_argument('theme', help='Path to theme file')
    p.add_argument('code', help='Path to code file desired highlighted')

    return p.parse_args()


def main():
    parsed_args = parse_args(sys.argv)
    syntax_file = parsed_args.syntax
    theme_file = parsed_args.theme
    code_file = parsed_args.code

    rules = {}

    with open(syntax_file) as f:
        syntax_lines = f.read().strip().split('\n')
        add_patterns_to_rulebook(syntax_lines, rules)

    with open(theme_file) as f:
        theme_lines = f.read().strip().split('\n')
        add_colors_to_rulebook(theme_lines, rules)

    code = ''
    with open(code_file) as f:
        code = f.read()

    highlighted = highlight_text(code, rules)

    print(highlighted)


if __name__ == "__main__": main()
