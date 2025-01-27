def strip_comments(strng, markers):
    lines = strng.split('\n')
    stripped_lines = []
    for line in lines:
        min_index = len(line)
        for marker in markers:
            if marker in line:
                min_index = min(min_index, line.index(marker))
        stripped_lines.append(line[:min_index].rstrip())
    return '\n'.join(stripped_lines)
