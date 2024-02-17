import re
text = None
with open("input.md", "r") as file:
    text = file.read()

patterns = [
    #listelem
    (r'^\d+\.\s(.+)$', r'<li>\1</li>'),
    #h1,h2,h3
    (r'^# (.+)$', r'<h1>\1</h1>'),
    (r'^## (.+)$', r'<h2>\1</h2>'),
    (r'^### (.+)$', r'<h3>\1</h3>'),
    #bold
    (r'\*\*(.+?)\*\*', r'<b>\1</b>'),
    #italic
    (r'\*(.+?)\*', r'<i>\1</i>'),
    #image
    (r'!\[([^\]]+)\]\(([^\)]+)\)', r'<img src="\2" alt="\1"/>'),
    #link
    (r'\[([^\]]+)\]\(([^\)]+)\)', r'<a href="\2">\1</a>'),
]

def apply_patterns(text, patterns):
    for pattern, replacement in patterns:
        text = re.sub(pattern, replacement, text, flags=re.MULTILINE)
    return text

# add <ol> and </ol> tags
lines = apply_patterns(text, patterns).split('\n')
inside_ol = False

for i, line in enumerate(lines):
    line = line.strip()
    
    if line.startswith('<li>'):
        if not inside_ol:
            lines[i] = '<ol>\n' + line
            inside_ol = True
    
    elif inside_ol and not line.startswith('<li>'):
        lines[i-1] += '\n</ol>'
        inside_ol = False

if inside_ol:
    lines[-1] += '\n</ol>'

print('\n'.join(lines))