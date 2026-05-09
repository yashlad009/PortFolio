
    // Prefers Reduced Motion Check
    const prefersReducedMotion = window.matchMedia('(prefers-reduced-motion: reduce)').matches;

    // --- Cursor Logic ---
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
    }

    const hoverables = document.querySelectorAll('a, button, .hoverable, input, textarea');
    hoverables.forEach(el => {
      el.addEventListener('mouseenter', () => {
        dot.classList.add('hover');
        ring.classList.add('hover');
      });
      el.addEventListener('mouseleave', () => {
        dot.classList.remove('hover');
        ring.classList.remove('hover');
      });
    });



    // --- Page Loader & Initial Animations ---
    window.addEventListener('load', () => {
      const tl = gsap.timeline();
      
      if(!prefersReducedMotion) {
        tl.to('.initial-y', { x: 0, opacity: 1, duration: 0.8, ease: "power3.out" })
          .to('.initial-l', { x: 0, opacity: 1, duration: 0.8, ease: "power3.out" }, "<")
          .to('.loader-bar', { width: "100%", duration: 2, ease: "power2.inOut" })
          .to('.loader', { y: "-100%", duration: 0.8, ease: "power4.inOut" })
          .to('.pill-nav', { opacity: 1, y: 0, duration: 0.5 }, "-=0.2")
          .fromTo('.hero-intro', { opacity: 0 }, { opacity: 1, duration: 0.5 }, "-=0.2")
          .to('.hero-name span', { y: 0, opacity: 1, duration: 0.8, stagger: 0.06, ease: "power3.out" }, "-=0.3")
          .fromTo('.hero-tagline', { opacity: 0, y: 20 }, { opacity: 1, y: 0, duration: 0.8 }, "-=0.4")
          .fromTo('.hero-ctas', { opacity: 0, y: 20 }, { opacity: 1, y: 0, duration: 0.8 }, "-=0.6")
          .fromTo('.hero-content .avail-badge', { opacity: 0 }, { opacity: 1, duration: 0.8 }, "-=0.4")
          .fromTo('.scroll-indicator', { opacity: 0 }, { opacity: 1, duration: 0.8 }, "-=0.2");
      } else {
        document.querySelector('.loader').style.display = 'none';
        gsap.set('.pill-nav, .hero-intro, .hero-tagline, .hero-ctas, .avail-badge, .scroll-indicator', { opacity: 1 });
        gsap.set('.hero-name span', { y: 0, opacity: 1 });
      }

      // --- Typewriter Effect ---
      const roles = ["AI/ML Engineering Student", "Creative Developer", "Intelligent Systems Builder", "Problem Solver"];
      const roleEl = document.querySelector('.hero-role');
      let roleIdx = 0; let charIdx = 0; let isDeleting = false;

      function typeWriter() {
        const currentRole = roles[roleIdx];
        if (isDeleting) {
          roleEl.innerText = currentRole.substring(0, charIdx - 1) + "|";
          charIdx--;
        } else {
          roleEl.innerText = currentRole.substring(0, charIdx + 1) + "|";
          charIdx++;
        }

        let typeSpeed = isDeleting ? 30 : 60;

        if (!isDeleting && charIdx === currentRole.length) {
          typeSpeed = 2000;
          isDeleting = true;
        } else if (isDeleting && charIdx === 0) {
          isDeleting = false;
          roleIdx = (roleIdx + 1) % roles.length;
          typeSpeed = 500;
        }

        setTimeout(typeWriter, typeSpeed);
      }
      setTimeout(typeWriter, 1200 + 2800); // start after initial load
    });

    // --- Scroll Progress Bar ---
    const scrollProgress = document.querySelector('.scroll-progress');
    window.addEventListener('scroll', () => {
      const totalScroll = document.documentElement.scrollTop;
      const windowHeight = document.documentElement.scrollHeight - document.documentElement.clientHeight;
      const scroll = `${totalScroll / windowHeight * 100}%`;
      scrollProgress.style.width = scroll;
    });

    // --- Active Nav Highlight ---
    const sections = document.querySelectorAll('section');
    const navLinks = document.querySelectorAll('.pill-nav a');
    
    const navIndicator = document.querySelector('.nav-indicator');
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


    // --- Three.js Neural Network Background ---
    if (!prefersReducedMotion) {
      const canvas = document.getElementById('neural-bg');
      const scene = new THREE.Scene();
      const camera = new THREE.PerspectiveCamera(75, window.innerWidth / window.innerHeight, 0.1, 1000);
      const renderer = new THREE.WebGLRenderer({ canvas: canvas, alpha: true, antialias: true });
      
      renderer.setSize(window.innerWidth, window.innerHeight);
      renderer.setPixelRatio(window.devicePixelRatio);
      camera.position.z = 150;

      const nodes = [];
      const nodeCount = 120;
      const maxDistance = 30;

      // Create nodes
      const geometry = new THREE.CircleGeometry(0.3, 8);
      const material = new THREE.MeshBasicMaterial({ color: 0x00d4ff, transparent: true, opacity: 0.6 });
      
      for (let i = 0; i < nodeCount; i++) {
        const mesh = new THREE.Mesh(geometry, material);
        mesh.position.x = (Math.random() - 0.5) * 400;
        mesh.position.y = (Math.random() - 0.5) * 200;
        mesh.position.z = (Math.random() - 0.5) * 50;
        mesh.userData = {
          vx: (Math.random() - 0.5) * 0.2,
          vy: (Math.random() - 0.5) * 0.2
        };
        scene.add(mesh);
        nodes.push(mesh);
      }

      // Create lines
      const lineMaterial = new THREE.LineBasicMaterial({ color: 0x00d4ff, transparent: true, opacity: 0.15 });
      const lineGeometry = new THREE.BufferGeometry();
      const lineMesh = new THREE.LineSegments(lineGeometry, lineMaterial);
      scene.add(lineMesh);

      // Mouse interaction
      const mouse = new THREE.Vector2(9999, 9999);
      const raycaster = new THREE.Raycaster();
      const plane = new THREE.Plane(new THREE.Vector3(0, 0, 1), 0);

      window.addEventListener('mousemove', (event) => {
        mouse.x = (event.clientX / window.innerWidth) * 2 - 1;
        mouse.y = -(event.clientY / window.innerHeight) * 2 + 1;
      });

      function animateThree() {
        requestAnimationFrame(animateThree);

        raycaster.setFromCamera(mouse, camera);
        const intersectPoint = new THREE.Vector3();
        raycaster.ray.intersectPlane(plane, intersectPoint);

        const positions = [];
        const colors = [];

        for (let i = 0; i < nodes.length; i++) {
          const node = nodes[i];
          node.position.x += node.userData.vx;
          node.position.y += node.userData.vy;

          if (node.position.x > 200 || node.position.x < -200) node.userData.vx *= -1;
          if (node.position.y > 100 || node.position.y < -100) node.userData.vy *= -1;

          // Repel from mouse
          if(intersectPoint) {
            const distToMouse = node.position.distanceTo(intersectPoint);
            if (distToMouse < 40) {
              const dir = node.position.clone().sub(intersectPoint).normalize();
              node.position.add(dir.multiplyScalar(0.5));
            }
          }

          for (let j = i + 1; j < nodes.length; j++) {
            const node2 = nodes[j];
            const dist = node.position.distanceTo(node2.position);
            
            if (dist < maxDistance) {
              positions.push(node.position.x, node.position.y, node.position.z);
              positions.push(node2.position.x, node2.position.y, node2.position.z);
            }
          }
        }

        lineGeometry.setAttribute('position', new THREE.Float32BufferAttribute(positions, 3));
        renderer.render(scene, camera);
      }
      animateThree();

      window.addEventListener('resize', () => {
        camera.aspect = window.innerWidth / window.innerHeight;
        camera.updateProjectionMatrix();
        renderer.setSize(window.innerWidth, window.innerHeight);
      });
    }

    
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

    // --- GSAP Scroll Animations ---
    gsap.registerPlugin(ScrollTrigger);

    if (!prefersReducedMotion) {
      // General Reveal
      gsap.utils.toArray('.gs-reveal').forEach(el => {
        gsap.fromTo(el, 
          { opacity: 0, y: 50 }, 
          {
            scrollTrigger: { trigger: el, start: "top 80%" },
            opacity: 1, y: 0, duration: 0.8, ease: "power2.out"
          }
        );
      });

      // Section Headers
      gsap.utils.toArray('.section-header').forEach(header => {
        const num = header.querySelector('.section-num');
        const title = header.querySelector('.section-title');
        
        const tl = gsap.timeline({ scrollTrigger: { trigger: header, start: "top 80%" }});
        tl.fromTo(num, { x: -40, opacity: 0 }, { x: 0, opacity: 1, duration: 0.6 })
          .fromTo(title, { opacity: 0, y: 20 }, { opacity: 1, y: 0, duration: 0.6 }, "-=0.4");
      });

      // Stats Counters
      const stats = document.querySelectorAll('.stat-num');
      ScrollTrigger.create({
        trigger: '.stats-grid',
        start: "top 80%",
        onEnter: () => {
          stats.forEach(stat => {
            const target = +stat.getAttribute('data-target');
            gsap.to(stat, {
              innerHTML: target,
              duration: 2,
              snap: { innerHTML: 1 },
              onUpdate: function() {
                if(target > 50) stat.innerHTML = Math.round(this.targets()[0].innerHTML) + "%";
                else if(target === 3 || target === 5) stat.innerHTML = Math.round(this.targets()[0].innerHTML) + "+";
              }
            });
          });
        },
        once: true
      });

      // Skills Arc and Stagger
      gsap.fromTo('.gs-skill', 
        { opacity: 0, y: 40 },
        {
          scrollTrigger: { trigger: '.skills-grid', start: "top 75%" },
          opacity: 1, y: 0, duration: 0.6, stagger: 0.12, ease: "power2.out",
          onStart: () => {
            setTimeout(() => {
              document.querySelectorAll('.skill-arc-progress').forEach(arc => {
                const percent = arc.getAttribute('data-percent');
                const offset = 176 - (176 * percent) / 100;
                arc.style.strokeDashoffset = offset;
              });
            }, 300);
          }
        }
      );

      // Timeline Cards
      gsap.utils.toArray('.gs-tl-left').forEach(el => {
        gsap.fromTo(el, { opacity: 0, x: -80 }, { scrollTrigger: { trigger: el, start: "top 85%" }, opacity: 1, x: 0, duration: 0.8 });
      });
      gsap.utils.toArray('.gs-tl-right').forEach(el => {
        gsap.fromTo(el, { opacity: 0, x: 80 }, { scrollTrigger: { trigger: el, start: "top 85%" }, opacity: 1, x: 0, duration: 0.8 });
      });

      // Project Cards
      gsap.utils.toArray('.gs-project').forEach(el => {
        gsap.fromTo(el, 
          { opacity: 0, scale: 0.97 }, 
          { scrollTrigger: { trigger: el, start: "top 85%" }, opacity: 1, scale: 1, duration: 0.8 }
        );
      });
    }

  