import re

with open('index.html', 'r', encoding='utf-8') as f:
    content = f.read()

# 1. Loader Marquee
loader_old = """    <div class="loader-initials">
      <span class="initial-y">Y</span><span class="initial-l">L</span>
    </div>
    <div class="loader-bar-container">"""
loader_new = """    <div class="loader-initials">
      <span class="initial-y">Y</span><span class="initial-l">L</span><span class="initial-dots">...</span>
    </div>
    <div class="loader-marquee" style="color: var(--text-muted); font-family: var(--font-mono); font-size: 12px; margin-bottom: 24px; max-width: 300px;">
      <marquee scrollamount="5" scrolldelay="50">Creating tools that don't just solve problems, but inspire progress.</marquee>
    </div>
    <div class="loader-bar-container">"""
content = content.replace(loader_old, loader_new)

# 2. Menu previously
menu_css_old = """/* Navigation */
.pill-nav {
  position: fixed;
  top: 24px; left: 50%;
  transform: translateX(-50%);
  background: rgba(5, 8, 20, 0.7);
  backdrop-filter: blur(20px) saturate(180%);
  border: 0.5px solid var(--border-subtle);
  border-radius: 50px;
  padding: 12px 32px;
  z-index: 1000;
  display: flex;
  gap: 24px;
  opacity: 0; /* Fade in after loader */
}
.pill-nav a {
  font-family: 'JetBrains Mono', monospace;
  font-size: 12px;
  letter-spacing: 0.04em;
  color: var(--text-secondary);
  display: flex;
  align-items: center;
  gap: 6px;
  position: relative;
  padding: 4px 0;
}
.pill-nav a .nav-num {
  color: var(--accent-cyan);
}
.pill-nav a::after {
  content: '';
  position: absolute;
  bottom: 0; left: 0;
  width: 0%;
  height: 1px;
  background: var(--accent-cyan);
  transition: width 0.3s ease;
}
.pill-nav a:hover, .pill-nav a.active {
  color: var(--text-primary);
}
.pill-nav a:hover::after, .pill-nav a.active::after {
  width: 100%;
}
.pill-nav a.active { color: var(--accent-cyan); }
.pill-nav a.active .nav-num { color: var(--text-primary); }"""

menu_css_new = """/* Navigation */
.pill-nav {
  position: fixed;
  top: 2rem;
  left: 50%;
  transform: translateX(-50%);
  border-radius: 50px;
  padding: 0.5rem;
  z-index: 1000;
  border: 1px solid rgba(255, 255, 255, 0.08);
  display: flex;
  align-items: center;
  background: rgba(255, 255, 255, 0.03);
  backdrop-filter: blur(12px);
  -webkit-backdrop-filter: blur(12px);
  opacity: 0;
}
.nav-indicator {
  position: absolute;
  height: calc(100% - 1rem);
  background: rgba(0, 212, 255, 0.2);
  border: 1px solid var(--accent-cyan);
  border-radius: 50px;
  top: 0.5rem;
  left: 0;
  width: 0;
  opacity: 0;
  transition: all 0.4s cubic-bezier(0.25, 1, 0.5, 1);
  pointer-events: none;
  box-shadow: 0 0 15px var(--border-glow);
}
.nav-links {
  display: flex;
  gap: 0.5rem;
  position: relative;
  z-index: 1;
}
.pill-nav a {
  font-family: 'JetBrains Mono', monospace;
  font-size: 0.9rem;
  padding: 0.8rem 1.5rem;
  border-radius: 50px;
  color: var(--text-secondary);
  transition: color 0.3s ease;
  display: block;
}
.pill-nav a .nav-num {
  color: var(--accent-cyan);
  margin-right: 4px;
}
.pill-nav a:hover, .pill-nav a.active {
  color: #fff;
}"""
content = content.replace(menu_css_old, menu_css_new)

menu_html_old = """  <!-- Navigation -->
  <nav class="pill-nav">
    <a href="#hero" class="hoverable active"><span class="nav-num">00.</span> Home</a>
    <a href="#about" class="hoverable"><span class="nav-num">01.</span> About</a>
    <a href="#skills" class="hoverable"><span class="nav-num">02.</span> Skills</a>
    <a href="#experience" class="hoverable"><span class="nav-num">03.</span> Exp</a>
    <a href="#work" class="hoverable"><span class="nav-num">04.</span> Work</a>
    <a href="#contact" class="hoverable"><span class="nav-num">05.</span> Contact</a>
  </nav>"""
menu_html_new = """  <!-- Navigation -->
  <nav class="pill-nav">
    <div class="nav-indicator"></div>
    <div class="nav-links">
      <a href="#hero" class="hoverable active"><span class="nav-num">00.</span> Home</a>
      <a href="#about" class="hoverable"><span class="nav-num">01.</span> About</a>
      <a href="#skills" class="hoverable"><span class="nav-num">02.</span> Skills</a>
      <a href="#experience" class="hoverable"><span class="nav-num">03.</span> Exp</a>
      <a href="#work" class="hoverable"><span class="nav-num">04.</span> Projects</a>
      <a href="#contact" class="hoverable"><span class="nav-num">05.</span> Contact</a>
    </div>
  </nav>"""
content = content.replace(menu_html_old, menu_html_new)

# Modify Active Nav logic to move indicator
nav_logic_old = """    window.addEventListener('scroll', () => {
      let current = '';
      sections.forEach(section => {
        const sectionTop = section.offsetTop;
        const sectionHeight = section.clientHeight;
        if (pageYOffset >= (sectionTop - sectionHeight / 3)) {
          current = section.getAttribute('id');
        }
      });
      navLinks.forEach(link => {
        link.classList.remove('active');
        if (link.getAttribute('href').substring(1) === current) {
          link.classList.add('active');
        }
      });
      
      // hide scroll indicator
      if(pageYOffset > 200) {
        document.querySelector('.scroll-indicator').style.opacity = '0';
      }
    });"""

nav_logic_new = """    const navIndicator = document.querySelector('.nav-indicator');
    function updateNavIndicator(link) {
      if(!link) return;
      const rect = link.getBoundingClientRect();
      const parentRect = link.parentElement.getBoundingClientRect();
      navIndicator.style.width = `${rect.width}px`;
      navIndicator.style.left = `${rect.left - parentRect.left}px`;
      navIndicator.style.opacity = '1';
    }
    
    window.addEventListener('scroll', () => {
      let current = '';
      sections.forEach(section => {
        const sectionTop = section.offsetTop;
        const sectionHeight = section.clientHeight;
        if (pageYOffset >= (sectionTop - sectionHeight / 3)) {
          current = section.getAttribute('id');
        }
      });
      let activeLink = null;
      navLinks.forEach(link => {
        link.classList.remove('active');
        if (link.getAttribute('href').substring(1) === current) {
          link.classList.add('active');
          activeLink = link;
        }
      });
      if(activeLink) updateNavIndicator(activeLink);
      
      if(pageYOffset > 200) {
        const si = document.querySelector('.scroll-indicator');
        if(si) si.style.opacity = '0';
      }
    });

    navLinks.forEach(link => {
      link.addEventListener('mouseenter', (e) => updateNavIndicator(e.target));
      link.addEventListener('mouseleave', () => {
        const active = document.querySelector('.pill-nav a.active');
        if(active) updateNavIndicator(active);
        else navIndicator.style.opacity = '0';
      });
    });
"""
content = content.replace(nav_logic_old, nav_logic_new)


# 3. Cursor previously
cursor_css_old = """/* Custom Cursor */
.cursor-dot {
  position: fixed;
  top: 0; left: 0;
  width: 6px; height: 6px;
  background-color: var(--accent-cyan);
  border-radius: 50%;
  pointer-events: none;
  z-index: 10000;
  transform: translate(-50%, -50%);
  transition: transform 0.2s ease, width 0.2s ease, height 0.2s ease, background-color 0.2s ease;
}
.cursor-ring {
  position: fixed;
  top: 0; left: 0;
  width: 32px; height: 32px;
  border: 1.5px solid var(--accent-cyan);
  border-radius: 50%;
  pointer-events: none;
  z-index: 9999;
  transform: translate(-50%, -50%);
  transition: width 0.2s ease, height 0.2s ease, background-color 0.2s ease;
}
.cursor-dot.hover {
  transform: translate(-50%, -50%) scale(0);
}
.cursor-ring.hover {
  width: 80px; height: 80px;
  background-color: var(--accent-cyan-dim);
}"""

cursor_css_new = """/* Custom Cursor */
#particle-canvas {
  position: fixed;
  top: 0; left: 0;
  width: 100vw; height: 100vh;
  pointer-events: none;
  z-index: 9998;
}
.cursor-dot {
  position: fixed;
  top: 0; left: 0;
  width: 8px; height: 8px;
  background-color: var(--accent-cyan);
  box-shadow: 0 0 10px var(--accent-cyan);
  border-radius: 50%;
  pointer-events: none;
  z-index: 10000;
  transform: translate(-50%, -50%);
}
.cursor-ring {
  position: fixed;
  top: 0; left: 0;
  width: 40px; height: 40px;
  border: 1px solid var(--accent-cyan);
  border-radius: 50%;
  pointer-events: none;
  z-index: 9999;
  transform: translate(-50%, -50%);
  transition: width 0.2s, height 0.2s, background-color 0.2s;
}
.cursor-ring.hover {
  width: 60px; height: 60px;
  background-color: rgba(0, 212, 255, 0.1);
}"""
content = content.replace(cursor_css_old, cursor_css_new)

cursor_html_old = """  <!-- Custom Cursor -->
  <div class="cursor-dot"></div>
  <div class="cursor-ring"></div>"""
cursor_html_new = """  <!-- Custom Cursor -->
  <canvas id="particle-canvas"></canvas>
  <div class="cursor-dot"></div>
  <div class="cursor-ring"></div>"""
content = content.replace(cursor_html_old, cursor_html_new)

cursor_js_old = """    // --- Cursor Logic ---
    const dot = document.querySelector('.cursor-dot');
    const ring = document.querySelector('.cursor-ring');
    let mouseX = window.innerWidth / 2; let mouseY = window.innerHeight / 2;
    let ringX = mouseX; let ringY = mouseY;

    window.addEventListener('mousemove', (e) => {
      mouseX = e.clientX;
      mouseY = e.clientY;
      dot.style.transform = `translate(${mouseX}px, ${mouseY}px) translate(-50%, -50%)`;
    });

    function renderCursor() {
      if(!prefersReducedMotion) {
        ringX += (mouseX - ringX) * 0.15;
        ringY += (mouseY - ringY) * 0.15;
        ring.style.transform = `translate(${ringX}px, ${ringY}px) translate(-50%, -50%)`;
        requestAnimationFrame(renderCursor);
      }
    }
    renderCursor();"""

cursor_js_new = """    // --- Cursor Logic ---
    const dot = document.querySelector('.cursor-dot');
    const ring = document.querySelector('.cursor-ring');
    let mouseX = window.innerWidth / 2; let mouseY = window.innerHeight / 2;
    let ringX = mouseX; let ringY = mouseY;

    window.addEventListener('mousemove', (e) => {
      mouseX = e.clientX;
      mouseY = e.clientY;
      if (dot) dot.style.transform = `translate(${mouseX}px, ${mouseY}px) translate(-50%, -50%)`;
    });

    function renderCursor() {
      if(!prefersReducedMotion && ring) {
        ringX += (mouseX - ringX) * 0.15;
        ringY += (mouseY - ringY) * 0.15;
        ring.style.transform = `translate(${ringX}px, ${ringY}px) translate(-50%, -50%)`;
        requestAnimationFrame(renderCursor);
      }
    }
    renderCursor();
    
    // --- Particle Constellation Cursor Trail ---
    if (!prefersReducedMotion) {
      const pCanvas = document.getElementById('particle-canvas');
      if (pCanvas) {
        const pCtx = pCanvas.getContext('2d');
        let particles = [];
        const resizeParticleCanvas = () => {
          pCanvas.width = window.innerWidth;
          pCanvas.height = window.innerHeight;
        };
        window.addEventListener('resize', resizeParticleCanvas);
        resizeParticleCanvas();
        
        class Particle {
          constructor(x, y) {
            this.x = x; this.y = y;
            this.vx = (Math.random() - 0.5) * 2;
            this.vy = (Math.random() - 0.5) * 2;
            this.life = 1;
            this.decay = Math.random() * 0.02 + 0.02;
          }
          update() {
            this.x += this.vx; this.y += this.vy;
            this.life -= this.decay;
          }
          draw() {
            pCtx.beginPath();
            pCtx.arc(this.x, this.y, 2, 0, Math.PI * 2);
            pCtx.fillStyle = `rgba(0, 212, 255, ${this.life})`;
            pCtx.fill();
          }
        }
        
        let lastSpawnTime = 0;
        window.addEventListener('mousemove', (e) => {
          const now = Date.now();
          if (now - lastSpawnTime > 20) {
            particles.push(new Particle(e.clientX, e.clientY));
            lastSpawnTime = now;
          }
        });
        
        const renderParticles = () => {
          pCtx.clearRect(0, 0, pCanvas.width, pCanvas.height);
          for (let i = 0; i < particles.length; i++) {
            particles[i].update();
            particles[i].draw();
            for (let j = i + 1; j < particles.length; j++) {
              const dx = particles[i].x - particles[j].x;
              const dy = particles[i].y - particles[j].y;
              const dist = Math.sqrt(dx * dx + dy * dy);
              if (dist < 100) {
                pCtx.beginPath();
                pCtx.moveTo(particles[i].x, particles[i].y);
                pCtx.lineTo(particles[j].x, particles[j].y);
                const alpha = Math.min(particles[i].life, particles[j].life) * (1 - dist / 100);
                pCtx.strokeStyle = `rgba(0, 212, 255, ${alpha * 0.5})`;
                pCtx.stroke();
              }
            }
          }
          particles = particles.filter(p => p.life > 0);
          requestAnimationFrame(renderParticles);
        };
        renderParticles();
      }
    }"""
content = content.replace(cursor_js_old, cursor_js_new)

# 4. Profile Picture
profile_old = """          <img src="profile.jpg" alt="Yash Lad Portrait" onerror="this.src='https://images.unsplash.com/photo-1519085360753-af0119f7cbe7?q=80&w=800&auto=format&fit=crop'">"""
profile_new = """          <img src="profile2.jpg" alt="Yash Lad Portrait" onerror="this.src='https://images.unsplash.com/photo-1519085360753-af0119f7cbe7?q=80&w=800&auto=format&fit=crop'">"""
content = content.replace(profile_old, profile_new)

# 5. About me gap reduction
about_gap_old = """section {
  padding: 120px 0;
  min-height: 100vh;
}
.section-header {
  display: flex;
  align-items: baseline;
  gap: 16px;
  margin-bottom: 64px;
  border-bottom: 1px solid var(--border-subtle);
  padding-bottom: 24px;
}"""
about_gap_new = """section {
  padding: 80px 0;
  min-height: 100vh;
}
.section-header {
  display: flex;
  align-items: baseline;
  gap: 16px;
  margin-bottom: 32px;
  border-bottom: 1px solid var(--border-subtle);
  padding-bottom: 16px;
}"""
content = content.replace(about_gap_old, about_gap_new)

# 6. Skills alignment fix
skill_css_old = """.skill-card img {
  width: 48px; height: 48px;
  margin-bottom: 16px;
}
.skill-arc-container {
  position: relative;
  width: 60px; height: 60px;
  margin-bottom: 12px;
}
.skill-arc-svg { transform: rotate(-90deg); }"""

skill_css_new = """.skill-arc-container {
  position: relative;
  width: 80px; height: 80px;
  margin-bottom: 16px;
  display: flex;
  justify-content: center;
  align-items: center;
}
.skill-arc-svg { 
  position: absolute;
  top: 0; left: 0;
  width: 100%; height: 100%;
  transform: rotate(-90deg); 
}
.skill-card img {
  width: 32px; height: 32px;
  position: relative;
  z-index: 1;
}"""
content = content.replace(skill_css_old, skill_css_new)
content = content.replace('viewBox="0 0 60 60" width="60" height="60"', 'viewBox="0 0 60 60" width="80" height="80"')

skills_row2_start = content.find('      <div class="skills-grid">')
skills_row2_end = content.find('  </section>', skills_row2_start)
if skills_row2_start != -1 and skills_row2_end != -1:
    row2_content = content[skills_row2_start:skills_row2_end]
    content = content.replace(row2_content, '')

content = content.replace('.skills-grid.top-row { grid-template-columns: repeat(4, 1fr); }', '.skills-grid.top-row { grid-template-columns: repeat(auto-fit, minmax(200px, 1fr)); }')

# 7. Rename "Selected Work" to "Projects" and use photos "Task Tracker.png" and "Study Stack.png"
content = content.replace('<h2 class="section-title">SELECTED WORK</h2>', '<h2 class="section-title">PROJECTS</h2>')
content = content.replace('<span class="nav-num">04.</span> Work</a>', '<span class="nav-num">04.</span> Projects</a>')
content = content.replace('href="#work"', 'href="#projects"')
content = content.replace('id="work"', 'id="projects"')

project1_visual_old = """          <div class="project-visual p1">
            <svg class="visual-bg-pattern" width="100%" height="100%" xmlns="http://www.w3.org/2000/svg">
              <defs>
                <pattern id="circuit" width="60" height="60" patternUnits="userSpaceOnUse">
                  <path d="M10 10L30 30M30 30L50 10M30 30V50" stroke="rgba(0,212,255,0.2)" stroke-width="2" fill="none"/>
                  <circle cx="10" cy="10" r="3" fill="rgba(0,212,255,0.4)"/>
                  <circle cx="50" cy="10" r="3" fill="rgba(0,212,255,0.4)"/>
                  <circle cx="30" cy="50" r="3" fill="rgba(0,212,255,0.4)"/>
                </pattern>
              </defs>
              <rect width="100%" height="100%" fill="url(#circuit)"/>
            </svg>
            <div class="visual-watermark">TASK TRACKER</div>
          </div>"""
project1_visual_new = """          <div class="project-visual p1" style="background: none;">
            <img src="Task Tracker.png" alt="Task Tracker" style="width: 100%; height: 100%; object-fit: cover;">
          </div>"""
content = content.replace(project1_visual_old, project1_visual_new)

project2_visual_old = """          <div class="project-visual p2">
            <svg class="visual-bg-pattern" width="100%" height="100%" xmlns="http://www.w3.org/2000/svg">
              <defs>
                <pattern id="chart" width="80" height="80" patternUnits="userSpaceOnUse">
                  <path d="M0 60 Q 20 20, 40 40 T 80 10" stroke="rgba(123,92,250,0.2)" stroke-width="2" fill="none"/>
                  <rect x="15" y="40" width="10" height="40" fill="rgba(123,92,250,0.1)"/>
                  <rect x="55" y="20" width="10" height="60" fill="rgba(123,92,250,0.1)"/>
                </pattern>
              </defs>
              <rect width="100%" height="100%" fill="url(#chart)"/>
            </svg>
            <div class="visual-watermark">APMS PRO</div>
          </div>"""
project2_visual_new = """          <div class="project-visual p2" style="background: none;">
            <img src="Study Stack.png" alt="Study Stack" style="width: 100%; height: 100%; object-fit: cover;">
          </div>"""
content = content.replace(project2_visual_old, project2_visual_new)

# 8. Remove shipped consistency
github_section_old = """      <!-- GitHub Activity -->
      <div class="github-section gs-reveal">
        <span class="github-label">Shipped Consistently</span>
        <img src="https://ghchart.rshah.org/00d4ff/yashlad" alt="GitHub contributions" class="github-img">
        <p class="github-caption">Real commits. Real projects. Real consistency.</p>
      </div>"""
content = content.replace(github_section_old, '')

# 9. Make footer attractive
footer_old = """    <div class="footer">
      <span>© 2025 Yash Lad</span>
      <span>Designed & Built by Yash Lad</span>
      <span>Made with ♥ in Pimpri, Maharashtra</span>
    </div>"""
footer_new = """    <div class="footer" style="flex-direction: column; gap: 16px; padding: 48px; background: var(--bg-card); border-top: 1px solid var(--border-glow);">
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
content = content.replace(footer_old, footer_new)

with open('index.html', 'w', encoding='utf-8') as f:
    f.write(content)
