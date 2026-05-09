// Wait for DOM
document.addEventListener("DOMContentLoaded", () => {
    
    // Register GSAP plugins
    gsap.registerPlugin(ScrollTrigger);

    // Check prefers-reduced-motion
    const prefersReducedMotion = window.matchMedia("(prefers-reduced-motion: reduce)").matches;

    // --- Lenis Initialization ---
    const lenis = new Lenis({
        lerp: 0.08,
        duration: 1.2,
        smoothWheel: true,
        orientation: 'vertical',
        gestureOrientation: 'vertical',
    });

    // Update progress bar
    const progressBar = document.querySelector('.progress-bar');
    lenis.on('scroll', (e) => {
        if(progressBar) {
            progressBar.style.width = `${e.progress * 100}%`;
        }
    });

    // Sync Lenis with GSAP
    lenis.on('scroll', ScrollTrigger.update);
    gsap.ticker.add((time) => {
        lenis.raf(time * 1000);
    });
    gsap.ticker.lagSmoothing(0);


    // --- Global Mouse Tracking ---
    let mouseX = window.innerWidth / 2;
    let mouseY = window.innerHeight / 2;

    window.addEventListener('mousemove', (e) => {
        mouseX = e.clientX;
        mouseY = e.clientY;
    });


    if (!prefersReducedMotion) {
        
        // --- Custom Cursor Logic ---
        const cursorDot = document.querySelector('.cursor-dot');
        const cursorOutline = document.querySelector('.cursor-outline');
        
        if (cursorDot && cursorOutline) {
            let outlineX = mouseX;
            let outlineY = mouseY;

            const animateCursor = () => {
                // Dot follows instantly
                cursorDot.style.left = `${mouseX}px`;
                cursorDot.style.top = `${mouseY}px`;

                // Outline follows with lag
                let distX = mouseX - outlineX;
                let distY = mouseY - outlineY;
                
                outlineX += distX * 0.15;
                outlineY += distY * 0.15;
                
                cursorOutline.style.left = `${outlineX}px`;
                cursorOutline.style.top = `${outlineY}px`;
                
                requestAnimationFrame(animateCursor);
            };
            animateCursor();

            // Hover effects
            const hoverElements = document.querySelectorAll('a, .btn, .magnetic, .project-card, .skill-card, button');
            hoverElements.forEach(el => {
                el.addEventListener('mouseenter', () => {
                    cursorOutline.classList.add('cursor-hover');
                });
                el.addEventListener('mouseleave', () => {
                    cursorOutline.classList.remove('cursor-hover');
                });
            });
        }


        // --- Floating Nav Indicator Logic ---
        const navItems = document.querySelectorAll('.nav-item');
        const navIndicator = document.querySelector('.nav-indicator');
    
        if (navItems.length > 0 && navIndicator) {
            navItems.forEach(item => {
                item.addEventListener('mouseenter', (e) => {
                    const rect = e.target.getBoundingClientRect();
                    const parentRect = e.target.parentElement.getBoundingClientRect();
                    
                    navIndicator.style.width = `${rect.width}px`;
                    navIndicator.style.left = `${rect.left - parentRect.left}px`;
                    navIndicator.style.opacity = '1';
                });
            });
    
            const navContainer = document.querySelector('.nav-links');
            if (navContainer) {
                navContainer.addEventListener('mouseleave', () => {
                    navIndicator.style.opacity = '0';
                });
            }
        }

        // --- Particle Constellation Cursor Trail ---
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
                    this.x = x;
                    this.y = y;
                    this.vx = (Math.random() - 0.5) * 2;
                    this.vy = (Math.random() - 0.5) * 2;
                    this.life = 1;
                    this.decay = Math.random() * 0.02 + 0.01;
                }
                update() {
                    this.x += this.vx;
                    this.y += this.vy;
                    this.life -= this.decay;
                }
                draw() {
                    pCtx.beginPath();
                    pCtx.arc(this.x, this.y, 2, 0, Math.PI * 2);
                    pCtx.fillStyle = `rgba(6, 182, 212, ${this.life})`;
                    pCtx.fill();
                }
            }

            // Spawn particles on mouse move
            let lastSpawnTime = 0;
            window.addEventListener('mousemove', (e) => {
                const now = Date.now();
                if (now - lastSpawnTime > 20) { // throttle spawn rate
                    particles.push(new Particle(e.clientX, e.clientY));
                    lastSpawnTime = now;
                }
            });

            const renderParticles = () => {
                pCtx.clearRect(0, 0, pCanvas.width, pCanvas.height);
                
                for (let i = 0; i < particles.length; i++) {
                    particles[i].update();
                    particles[i].draw();
                    
                    // Draw constellation lines
                    for (let j = i + 1; j < particles.length; j++) {
                        const dx = particles[i].x - particles[j].x;
                        const dy = particles[i].y - particles[j].y;
                        const dist = Math.sqrt(dx * dx + dy * dy);
                        
                        if (dist < 100) {
                            pCtx.beginPath();
                            pCtx.moveTo(particles[i].x, particles[i].y);
                            pCtx.lineTo(particles[j].x, particles[j].y);
                            const alpha = Math.min(particles[i].life, particles[j].life) * (1 - dist / 100);
                            pCtx.strokeStyle = `rgba(6, 182, 212, ${alpha * 0.5})`;
                            pCtx.stroke();
                        }
                    }
                }
                
                // Remove dead particles
                particles = particles.filter(p => p.life > 0);
                requestAnimationFrame(renderParticles);
            };
            renderParticles();
        }


        // --- Aurora Background in Hero Section ---
        const aCanvas = document.getElementById('aurora-canvas');
        if (aCanvas) {
            const aCtx = aCanvas.getContext('2d');
            let time = 0;
            
            const resizeAuroraCanvas = () => {
                aCanvas.width = window.innerWidth;
                aCanvas.height = window.innerHeight;
            };
            window.addEventListener('resize', resizeAuroraCanvas);
            resizeAuroraCanvas();

            const renderAurora = () => {
                aCtx.clearRect(0, 0, aCanvas.width, aCanvas.height);
                
                // Base colors
                const color1 = 'rgba(168, 85, 247, 0.3)'; // Electric purple
                const color2 = 'rgba(6, 182, 212, 0.4)';  // Electric cyan
                const color3 = 'rgba(4, 0, 15, 0.5)';     // Deep space black accent
                
                // Mouse influence
                const targetX = mouseX;
                const targetY = mouseY;

                // Create blobs
                time += 0.005;
                
                const drawBlob = (x, y, radius, color) => {
                    const grad = aCtx.createRadialGradient(x, y, 0, x, y, radius);
                    grad.addColorStop(0, color);
                    grad.addColorStop(1, 'rgba(0,0,0,0)');
                    aCtx.fillStyle = grad;
                    aCtx.beginPath();
                    aCtx.arc(x, y, radius, 0, Math.PI * 2);
                    aCtx.fill();
                };

                // Blob 1 - tracks mouse softly
                drawBlob(
                    (aCanvas.width / 2) + Math.cos(time) * 100 + (targetX - aCanvas.width/2) * 0.1,
                    (aCanvas.height / 2) + Math.sin(time * 0.8) * 100 + (targetY - aCanvas.height/2) * 0.1,
                    aCanvas.width * 0.6,
                    color1
                );

                // Blob 2 - moving slowly
                drawBlob(
                    (aCanvas.width / 3) + Math.sin(time * 1.2) * 150,
                    (aCanvas.height / 3) + Math.cos(time * 0.7) * 150,
                    aCanvas.width * 0.5,
                    color2
                );
                
                // Blob 3 - cyan accent
                drawBlob(
                    (aCanvas.width * 0.7) + Math.cos(time * 0.9) * 200,
                    (aCanvas.height * 0.6) + Math.sin(time * 1.1) * 200,
                    aCanvas.width * 0.4,
                    color3
                );

                requestAnimationFrame(renderAurora);
            };
            renderAurora();
        }

    } // End if !prefersReducedMotion


    // --- Audio Toggle Logic ---
    const audioBtn = document.getElementById('audio-toggle');
    const audioEl = document.getElementById('ambient-audio');
    let isPlaying = false;

    if (audioBtn && audioEl) {
        audioBtn.addEventListener('click', () => {
            if (isPlaying) {
                audioEl.pause();
                audioBtn.classList.remove('playing');
                audioBtn.innerHTML = '<span class="audio-icon">🔈</span>';
            } else {
                // If there's no src, it won't play but we update UI to reflect intent
                if (audioEl.src && audioEl.src !== window.location.href) {
                    audioEl.play().catch(e => console.log("Audio play failed:", e));
                }
                audioBtn.classList.add('playing');
                audioBtn.innerHTML = '<span class="audio-icon">🔊</span>';
            }
            isPlaying = !isPlaying;
        });
    }


    // --- Interactions & Animations ---

    // Magnetic Button Effect
    const magneticElements = document.querySelectorAll('.magnetic');
    magneticElements.forEach(el => {
        el.addEventListener('mousemove', (e) => {
            const rect = el.getBoundingClientRect();
            const strength = el.dataset.strength || 20;
            const x = ((e.clientX - rect.left) / rect.width - 0.5) * strength;
            const y = ((e.clientY - rect.top) / rect.height - 0.5) * strength;
            
            gsap.to(el, {
                x: x,
                y: y,
                duration: 0.5,
                ease: "power2.out"
            });
        });
        
        el.addEventListener('mouseleave', () => {
            gsap.to(el, {
                x: 0,
                y: 0,
                duration: 0.5,
                ease: "power2.out"
            });
        });
    });

    // Enhanced Tilt Effect for Project/Skill Cards (with 3D Depth)
    const tiltCards = document.querySelectorAll('.tilt-card');
    tiltCards.forEach(card => {
        card.addEventListener('mousemove', (e) => {
            const rect = card.getBoundingClientRect();
            const x = e.clientX - rect.left;
            const y = e.clientY - rect.top;
            
            const centerX = rect.width / 2;
            const centerY = rect.height / 2;
            
            // Calculate tilt degrees
            const rotateX = ((y - centerY) / centerY) * -15; // Max 15deg
            const rotateY = ((x - centerX) / centerX) * 15;
            
            gsap.to(card, {
                rotateX: rotateX,
                rotateY: rotateY,
                transformPerspective: 1000,
                duration: 0.5,
                ease: "power2.out"
            });
        });
        
        card.addEventListener('mouseleave', () => {
            gsap.to(card, {
                rotateX: 0,
                rotateY: 0,
                duration: 0.5,
                ease: "power2.out"
            });
        });
    });

    if (!prefersReducedMotion) {
        // --- GSAP Animations using Context ---
        let ctx = gsap.context(() => {
            
            // Hero Intro Animation
            const tl = gsap.timeline();
            tl.fromTo(".hero-greeting", { opacity: 0, y: 20 }, { opacity: 1, y: 0, duration: 0.8, ease: "power3.out" })
              .fromTo(".hero-name", { opacity: 0, y: 30 }, { opacity: 1, y: 0, duration: 1, ease: "power3.out" }, "-=0.4")
              .fromTo(".hero-role", { opacity: 0, y: 20 }, { opacity: 1, y: 0, duration: 0.8, ease: "power3.out" }, "-=0.6")
              .fromTo(".hero-cta", { opacity: 0, y: 20 }, { opacity: 1, y: 0, duration: 0.8, ease: "power3.out" }, "-=0.6")
              .fromTo(".scroll-indicator", { opacity: 0 }, { opacity: 0.6, duration: 1, ease: "power2.out" }, "-=0.2");

            // Hero Parallax on Scroll
            gsap.to(".hero-content", {
                yPercent: 30,
                ease: "none",
                scrollTrigger: {
                    trigger: "#hero",
                    start: "top top",
                    end: "bottom top",
                    scrub: true
                }
            });

            // Section Entrance Animations
            const sections = gsap.utils.toArray("section:not(#hero)");
            sections.forEach(sec => {
                const header = sec.querySelector(".section-header");
                if (header) {
                    gsap.fromTo(header, 
                        { opacity: 0, y: 60 },
                        {
                            opacity: 1, 
                            y: 0,
                            duration: 1,
                            ease: "power3.out",
                            scrollTrigger: {
                                trigger: sec,
                                start: "top 80%",
                            }
                        }
                    );
                }
            });

            // About Text Reveal
            const revealTexts = gsap.utils.toArray(".reveal-text");
            revealTexts.forEach(text => {
                gsap.fromTo(text, 
                    { opacity: 0, y: 40 },
                    {
                        opacity: 1,
                        y: 0,
                        duration: 0.8,
                        ease: "power3.out",
                        scrollTrigger: {
                            trigger: text,
                            start: "top 85%",
                        }
                    }
                );
            });

            // Skills Horizontal Scroll
            const skillsContainer = document.querySelector(".skills-container");
            const skillsWrapper = document.querySelector(".skills-wrapper");
            
            if (skillsContainer && skillsWrapper) {
                // Calculate total scroll distance
                let getScrollAmount = () => -(skillsContainer.scrollWidth - window.innerWidth + window.innerWidth * 0.1);

                const tween = gsap.to(skillsContainer, {
                    x: getScrollAmount,
                    ease: "none"
                });

                ScrollTrigger.create({
                    trigger: ".skills",
                    start: "top top",
                    end: () => `+=${getScrollAmount() * -1}`,
                    pin: true,
                    animation: tween,
                    scrub: 1,
                    invalidateOnRefresh: true
                });
            }

            // Experience Timeline Stagger
            const timelineItems = gsap.utils.toArray(".timeline-item");
            timelineItems.forEach((item, i) => {
                gsap.fromTo(item,
                    { opacity: 0, x: item.classList.contains("left") ? -50 : 50 },
                    {
                        opacity: 1,
                        x: 0,
                        duration: 1,
                        ease: "power3.out",
                        scrollTrigger: {
                            trigger: item,
                            start: "top 80%",
                        }
                    }
                );
            });

            // Projects Cards Entrance
            const projectCards = gsap.utils.toArray(".project-card");
            projectCards.forEach((card, i) => {
                gsap.fromTo(card,
                    { opacity: 0, y: 60 },
                    {
                        opacity: 1,
                        y: 0,
                        duration: 0.8,
                        ease: "power3.out",
                        scrollTrigger: {
                            trigger: card,
                            start: "top 85%",
                        }
                    }
                );
            });

        }); // End context
    }
});
