# Assignment 5

All programs require the `argparse` package. External regex package `regex` is
needed to run `highlighter.py`.

```bash
pip3 install argparse regex
```

I have made tests for `diff.py` and `syntax_tagger.py`.

```bash
python3 -m pytest
```
(Make sure to run the test in the folder containing `diff.py` and
`syntax_tagger.py`)


## Syntax highlighter
`highlighter.py` is a program that will print highlighted text to the terminal,
according to syntax and theme rules you supply.

To run the program:
```bash
python3 highlighter.py [ syntax rules path ] [ theme path ] [ file to highlight ]
```

### Syntax and theme files format
The syntax file is expected to be in this format: `"[ regex pattern ]": [
tagname ]`. One line per tag.

Example:
```
"\b(if|elif|else)\b": conditionals
```

The theme file is expected to be in this format: `[ tagname ]: [ ANSI-color ]`,
where ANSI code is one or two digits, followed by a semicolon followed by
another one or two digits. Also one line per tag.

Example:
```
conditionals: 0;34
```

I have supplied demo-files for Python and Elm (code examples are in the
`demo_files` folder).


## Grep
`grep.py` finds lines in a file that match a given regex pattern. Gives a
colorful output with `--highlight`. Patterns must be delimited with double or
single quotes, `'`/`"`. If your regex includes quotes they must be escaped with
backslash, like this:`\"`.

```bash
python3 grep.py [ --highlight ] [ pattern [ pattern ... ] ] [ file path ]
```


## Diff
`diff.py` finds the changed lines from two files and marks the differing lines.

```bash
python3 diff.py [ old file path ] [ new file path ]
```
