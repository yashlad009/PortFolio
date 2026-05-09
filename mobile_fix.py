with open('index.html', 'r', encoding='utf-8') as f:
    content = f.read()

# 1. Fix "04. Work" in mobile menu
content = content.replace('<a href="#projects" class="mobile-link hoverable">04. Work</a>', '<a href="#projects" class="mobile-link hoverable">04. Projects</a>')

# 2. Fix footer responsiveness
old_footer = """<div class="footer" style="flex-direction: column; gap: 16px; padding: 48px; background: var(--bg-card); border-top: 1px solid var(--border-glow);">
      <div style="display: flex; gap: 24px; font-size: 14px;">
        <a href="https://github.com/yashlad009" target="_blank" class="hoverable" style="color: var(--accent-cyan);">GitHub ↗</a>
        <a href="https://www.linkedin.com/in/yash-lad-4bb46632a" target="_blank" class="hoverable" style="color: var(--accent-cyan);">LinkedIn ↗</a>
      </div>
      <div style="display: flex; justify-content: space-between; width: 100%; max-width: 800px; margin-top: 16px; opacity: 0.6;">
        <span>© 2025 Yash Lad</span>
        <span>Designed & Built by Yash Lad</span>
        <span>Made with ♥ in Pimpri, Maharashtra</span>
      </div>
    </div>"""

new_footer = """<div class="footer new-footer">
      <div class="footer-links">
        <a href="https://github.com/yashlad009" target="_blank" class="hoverable">GitHub ↗</a>
        <a href="https://www.linkedin.com/in/yash-lad-4bb46632a" target="_blank" class="hoverable">LinkedIn ↗</a>
      </div>
      <div class="footer-info">
        <span>© 2025 Yash Lad</span>
        <span>Designed & Built by Yash Lad</span>
        <span>Made with ♥ in Pimpri, Maharashtra</span>
      </div>
    </div>"""
content = content.replace(old_footer, new_footer)

# Add CSS for footer and mobile menu toggle
new_css = """/* New Footer & Mobile fixes */
.new-footer {
  flex-direction: column;
  gap: 16px;
  padding: 48px;
  background: var(--bg-card);
  border-top: 1px solid var(--border-glow);
  width: 100vw;
  font-family: 'JetBrains Mono', monospace;
  font-size: 11px;
  color: var(--text-muted);
}
.new-footer .footer-links {
  display: flex;
  gap: 24px;
  font-size: 14px;
}
.new-footer .footer-links a {
  color: var(--accent-cyan);
}
.new-footer .footer-info {
  display: flex;
  justify-content: space-between;
  width: 100%;
  max-width: 800px;
  margin-top: 16px;
  opacity: 0.6;
}

.menu-btn.open span:nth-child(1) { transform: translateY(7px) rotate(45deg); }
.menu-btn.open span:nth-child(2) { opacity: 0; }
.menu-btn.open span:nth-child(3) { transform: translateY(-7px) rotate(-45deg); }

@media (max-width: 768px) {
  .new-footer .footer-info {
    flex-direction: column;
    align-items: center;
    gap: 8px;
  }
}
"""
content = content.replace("/* Accessibility */", new_css + "\n/* Accessibility */")

# Add JS for mobile menu
new_js = """
    // --- Mobile Menu Toggle ---
    const menuBtn = document.querySelector('.menu-btn');
    const mobileMenu = document.querySelector('.mobile-menu');
    const mobileLinks = document.querySelectorAll('.mobile-link');

    if(menuBtn && mobileMenu) {
      menuBtn.addEventListener('click', () => {
        mobileMenu.classList.toggle('active');
        menuBtn.classList.toggle('open');
      });

      mobileLinks.forEach(link => {
        link.addEventListener('click', () => {
          mobileMenu.classList.remove('active');
          menuBtn.classList.remove('open');
        });
      });
    }

    // --- GSAP Scroll Animations ---"""
content = content.replace("// --- GSAP Scroll Animations ---", new_js)

# Fix horizontal scrolling issue by ensuring overflow is hidden properly.
# `body { overflow-x: hidden; }` already exists. 

with open('index.html', 'w', encoding='utf-8') as f:
    f.write(content)
