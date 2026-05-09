import re

with open('index.html', 'r', encoding='utf-8') as f:
    content = f.read()

head_match = re.search(r'(<head>.*?</head>)', content, re.DOTALL)
head = head_match.group(1) if head_match else ''

scripts_match = re.search(r'(<!-- External Libraries -->.*?)</body>', content, re.DOTALL)
scripts = scripts_match.group(1) if scripts_match else ''

base_template = f'''<!DOCTYPE html>
<html lang="en">
{head}
<body>
  <!-- Custom Cursor -->
  <canvas id="particle-canvas"></canvas>
  <div class="cursor-dot"></div>
  <div class="cursor-ring"></div>

  <!-- Page Loader -->
  <div class="loader">
    <div class="loader-initials">
      <span class="initial-y">Y</span><span class="initial-l">L</span><span class="initial-dots">...</span>
    </div>
    <div class="loader-bar-container">
      <div class="loader-bar"></div>
    </div>
  </div>

  <!-- Scroll Progress -->
  <div class="scroll-progress"></div>

  <!-- Ambient Glow Orbs -->
  <div class="glow-orb orb-1"></div>
  <div class="glow-orb orb-2"></div>
  <div class="glow-orb orb-3"></div>

  <!-- Neural Background -->
  <canvas id="neural-bg" style="position: fixed; top: 0; left: 0; width: 100vw; height: 100vh; z-index: -1; opacity: 0.5;"></canvas>

  <nav class="pill-nav" style="opacity: 1;">
    <div class="nav-links">
      <a href="index.html" class="hoverable"><span class="nav-num">←</span> Back to Portfolio</a>
    </div>
  </nav>

  <div class="container" style="padding-top: 120px; padding-bottom: 80px;">
    <!-- CONTENT_PLACEHOLDER -->
  </div>

{scripts}
</body>
</html>
'''

with open('base_template.html', 'w', encoding='utf-8') as f:
    f.write(base_template)
