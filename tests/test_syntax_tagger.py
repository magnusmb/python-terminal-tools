from syntax_tagger import *


def test_tag_takes_two_strings_and_returns_tuple():
    assert isinstance(tag("tag", "match"), tuple)


def test_tag_returns_tuple_of_tag_and_match_strings():
    tag_name = "tag"
    match_text = "match"
    assert tag(tag_name, match_text) == (tag_name, match_text)


def test_tag_text_substitutes_match_with_tagged_text():
    string = "abcd"
    tag_name = "tag"
    pattern = "c"
    expected = ["ab", ("tag", "c"), "d"]
    assert tag_string(string, pattern, tag_name) == expected


def test_tag_all_tags_all_occurences_in_string():
    full_text = ['hei\ndu kan tagge\nalt dette\n']
    pattern = "d\w+"
    tag_name = "d-word"
    expected = ['hei\n', ('d-word', 'du'), ' kan tagge\nalt ',
            ('d-word', 'dette'), '\n']
    assert tag_all_matching(full_text, pattern, tag_name) == expected
