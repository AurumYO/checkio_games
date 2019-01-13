def between_markers(text: str, begin: str, end: str) -> str:
    """
    returns substring between two markers
    """
    import re
    if begin not in text:
        searched_text = text.rsplit(end)
        return searched_text[0]
    elif end not in text:
        searched_text = text.rsplit(begin)
        return searched_text[1]
    elif begin and end not in text:
        return text
    else:
        searched_text = ''.join(re.findall(r'{0}(.+?){1}'.format(begin, end), text))
        return searched_text

if __name__ == '__main__':
    print('Example:')
    print(between_markers('What is >apple<', '>', '<'))

    # These "asserts" are used for self-checking and not for testing
    assert between_markers('What is >apple<', '>', '<') == "apple", "One sym"
    assert between_markers("<head><title>My new site</title></head>",
                           "<title>", "</title>") == "My new site", "HTML"
    assert between_markers('No[/b] hi', '[b]', '[/b]') == 'No', 'No opened'
    assert between_markers('No [b]hi', '[b]', '[/b]') == 'hi', 'No close'
    assert between_markers('No hi', '[b]', '[/b]') == 'No hi', 'No markers at all'
    assert between_markers('No <hi>', '>', '<') == '', 'Wrong direction'
    print('Wow, you are doing pretty good. Time to check it!')
