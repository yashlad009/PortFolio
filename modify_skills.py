import re

with open('index.html', 'r', encoding='utf-8') as f:
    content = f.read()

css_old = """.skill-percent {
  position: absolute;
  top: 50%; left: 50%;
  transform: translate(-50%, -50%);
  font-family: 'JetBrains Mono', monospace;
  font-size: 10px;
  color: var(--text-secondary);
}
.skill-name {
  font-family: 'JetBrains Mono', monospace;
  font-size: 13px;
  color: var(--accent-cyan);
  margin-top: 12px;
  margin-bottom: 6px;
}
.skill-desc {
  font-size: 12px;
  color: var(--text-muted);
}"""

css_new = """.skill-percent {
  position: absolute;
  top: 35%; left: 50%;
  transform: translate(-50%, -50%);
  font-family: 'JetBrains Mono', monospace;
  font-size: 10px;
  color: var(--text-primary);
}
.skill-name {
  font-family: 'JetBrains Mono', monospace;
  font-size: 13px;
  color: var(--accent-cyan);
  margin-top: 12px;
  margin-bottom: 6px;
}
.skill-desc {
  font-size: 12px;
  color: var(--text-muted);
}
.skill-card img {
  position: absolute;
  top: 65%; left: 50%;
  transform: translate(-50%, -50%);
  width: 28px; height: 28px;
  z-index: 1;
}"""

# Fix the duplicate block of .skill-card img since we added it in the previous script.
# We will just replace the exact block from the previous script.
prev_img_css = """.skill-card img {
  width: 32px; height: 32px;
  position: relative;
  z-index: 1;
}"""
content = content.replace(prev_img_css, '')
content = content.replace(css_old, css_new)

# Increase container size to 100x100 to make room, keep SVG viewbox same but scaled.
arc_container_old = """.skill-arc-container {
  position: relative;
  width: 80px; height: 80px;
  margin-bottom: 16px;
  display: flex;
  justify-content: center;
  align-items: center;
}"""
arc_container_new = """.skill-arc-container {
  position: relative;
  width: 100px; height: 100px;
  margin-bottom: 16px;
}"""
content = content.replace(arc_container_old, arc_container_new)
content = content.replace('width="80" height="80"', 'width="100%" height="100%"')

with open('index.html', 'w', encoding='utf-8') as f:
    f.write(content)
