import argparse
import sys
from highlighter import highlight_text

def diff(old, new):
    """Finds the differing lines of two texts. Assumes the second text is a
    changed version of the first.

    Parameters:
    old (string): the old text
    new (string): the new text

    Returns:
    (string): Merged text, differing lines prepended with + (added in new) or -
    (removed in new), unchanged lines with 0.
    """

    if len(old) == 0 and len(new) == 0:
        return ''

    old_text = [] if len(old) == 0 else old.split('\n')
    new_text = [] if len(new) == 0 else new.split('\n')
    diff_lines = []
    i = 0
    j = 0

    while i < len(old_text) and j < len(new_text):
        old_line = old_text[i]
        new_line = new_text[j]

        if old_line == new_line:
            diff_lines.append('0 ' + old_line)
            i += 1
            j += 1
        else:
            # Lines don't match, check if one is removed or added
            if new_line not in old_text:
                diff_lines.append('+ ' + new_line)
                j += 1
            elif old_line not in new_text:
                diff_lines.append('- ' + old_line)
                i += 1
            else:
                if new_text.index(old_line) > old_text.index(new_line):
                    diff_lines.append('+ ' + new_line)

                    # Remove line instead of incrementing pointer to avoid
                    # confusion with identical lines
                    new_text.remove(new_line)
                else:
                    diff_lines.append('- ' + old_line)
                    i += 1

    # Add any remaining lines
    while i < len(old_text):
        diff_lines.append('- ' + old_text[i])
        i += 1

    while j < len(new_text):
        diff_lines.append('+ ' + new_text[i])
        j += 1

    return '\n'.join(diff_lines)


def parse_args(args):
    p = argparse.ArgumentParser()
    p.add_argument('old', help='Path to old file')
    p.add_argument('new', help='Path to new file')

    return p.parse_args()


def main():
    parsed_args = parse_args(sys.argv)
    old_file = parsed_args.old
    new_file = parsed_args.new

    with open(old_file) as f:
        old_text = f.read()

    with open(new_file) as f:
        new_text = f.read()

    output = diff(old_text, new_text)
    print(output)


if __name__ == "__main__": main()
