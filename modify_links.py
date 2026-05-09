with open('index.html', 'r', encoding='utf-8') as f:
    content = f.read()

content = content.replace('href="https://github.com/yashlad"', 'href="https://github.com/yashlad009"')
content = content.replace('href="#" target="_blank" class="hoverable" aria-label="LinkedIn"', 'href="https://www.linkedin.com/in/yash-lad-4bb46632a" target="_blank" class="hoverable" aria-label="LinkedIn"')

with open('index.html', 'w', encoding='utf-8') as f:
    f.write(content)
