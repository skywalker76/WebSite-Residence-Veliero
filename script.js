/* ══════════════════════════════════════════════════════════════
   RESIDENCE VELIERO — Landing Page Scripts
   Scroll reveals, countdown, testimonials, form handling
   ══════════════════════════════════════════════════════════════ */

document.addEventListener('DOMContentLoaded', () => {
    initScrollReveal();
    initCountdown();
    initTestimonialsCarousel();
    initFormHandling();
    initParticles();
    initSmoothScroll();
    initTopBarShrink();
});

/* ─── Scroll Reveal with Intersection Observer ─── */
function initScrollReveal() {
    const observerOptions = {
        threshold: 0.15,
        rootMargin: '0px 0px -50px 0px'
    };

    const observer = new IntersectionObserver((entries) => {
        entries.forEach(entry => {
            if (entry.isIntersecting) {
                const delay = entry.target.dataset.delay || 0;
                setTimeout(() => {
                    entry.target.classList.add('visible');
                }, parseInt(delay));
                observer.unobserve(entry.target);
            }
        });
    }, observerOptions);

    // Observe all reveal elements
    document.querySelectorAll('.reveal-left, .reveal-right, .reveal-up, .usp-card, .service-card').forEach(el => {
        observer.observe(el);
    });
}

/* ─── Countdown Timer ─── */
function initCountdown() {
    const targetDate = new Date('2026-04-30T23:59:59');

    function updateCountdown() {
        const now = new Date();
        const diff = targetDate - now;

        if (diff <= 0) {
            document.getElementById('countdownDays').textContent = '00';
            document.getElementById('countdownHours').textContent = '00';
            document.getElementById('countdownMinutes').textContent = '00';
            document.getElementById('countdownSeconds').textContent = '00';
            return;
        }

        const days = Math.floor(diff / (1000 * 60 * 60 * 24));
        const hours = Math.floor((diff % (1000 * 60 * 60 * 24)) / (1000 * 60 * 60));
        const minutes = Math.floor((diff % (1000 * 60 * 60)) / (1000 * 60));
        const seconds = Math.floor((diff % (1000 * 60)) / 1000);

        const daysEl = document.getElementById('countdownDays');
        const hoursEl = document.getElementById('countdownHours');
        const minutesEl = document.getElementById('countdownMinutes');
        const secondsEl = document.getElementById('countdownSeconds');

        if (daysEl) daysEl.textContent = String(days).padStart(2, '0');
        if (hoursEl) hoursEl.textContent = String(hours).padStart(2, '0');
        if (minutesEl) minutesEl.textContent = String(minutes).padStart(2, '0');
        if (secondsEl) secondsEl.textContent = String(seconds).padStart(2, '0');
    }

    updateCountdown();
    setInterval(updateCountdown, 1000);
}

/* ─── Testimonials Carousel ─── */
function initTestimonialsCarousel() {
    const track = document.getElementById('testimonialTrack');
    const prevBtn = document.getElementById('prevBtn');
    const nextBtn = document.getElementById('nextBtn');
    const dotsContainer = document.getElementById('testimonialDots');

    if (!track || !prevBtn || !nextBtn || !dotsContainer) return;

    const cards = track.querySelectorAll('.testimonial-card');
    let currentIndex = 0;

    // Create dots
    cards.forEach((_, i) => {
        const dot = document.createElement('button');
        dot.className = `testimonials__dot ${i === 0 ? 'active' : ''}`;
        dot.setAttribute('aria-label', `Vai alla recensione ${i + 1}`);
        dot.addEventListener('click', () => scrollToCard(i));
        dotsContainer.appendChild(dot);
    });

    function scrollToCard(index) {
        if (index < 0) index = cards.length - 1;
        if (index >= cards.length) index = 0;
        currentIndex = index;

        const card = cards[index];
        const trackRect = track.getBoundingClientRect();
        const cardRect = card.getBoundingClientRect();
        const scrollLeft = card.offsetLeft - (trackRect.width / 2) + (cardRect.width / 2);

        track.scrollTo({
            left: scrollLeft,
            behavior: 'smooth'
        });

        updateDots();
    }

    function updateDots() {
        dotsContainer.querySelectorAll('.testimonials__dot').forEach((dot, i) => {
            dot.classList.toggle('active', i === currentIndex);
        });
    }

    prevBtn.addEventListener('click', () => scrollToCard(currentIndex - 1));
    nextBtn.addEventListener('click', () => scrollToCard(currentIndex + 1));

    // Auto-scroll
    let autoScroll = setInterval(() => {
        scrollToCard(currentIndex + 1);
    }, 5000);

    track.addEventListener('mouseenter', () => clearInterval(autoScroll));
    track.addEventListener('mouseleave', () => {
        autoScroll = setInterval(() => scrollToCard(currentIndex + 1), 5000);
    });

    // Detect scroll position for dots sync
    track.addEventListener('scroll', () => {
        const scrollLeft = track.scrollLeft;
        let closest = 0;
        let closestDistance = Infinity;

        cards.forEach((card, i) => {
            const distance = Math.abs(card.offsetLeft - scrollLeft - track.offsetWidth / 2 + card.offsetWidth / 2);
            if (distance < closestDistance) {
                closestDistance = distance;
                closest = i;
            }
        });

        if (closest !== currentIndex) {
            currentIndex = closest;
            updateDots();
        }
    });
}

/* ─── Form Handling ─── */
function initFormHandling() {
    const form = document.getElementById('quoteForm');
    if (!form) return;

    form.addEventListener('submit', (e) => {
        e.preventDefault();

        // Validate
        const required = form.querySelectorAll('[required]');
        let valid = true;

        required.forEach(input => {
            if (!input.value.trim() && input.type !== 'checkbox') {
                input.style.borderColor = '#F98AA5';
                valid = false;
            } else if (input.type === 'checkbox' && !input.checked) {
                valid = false;
            } else {
                input.style.borderColor = '#e8ecf0';
            }
        });

        if (!valid) {
            // Shake animation
            form.style.animation = 'shake 0.5s ease-out';
            setTimeout(() => form.style.animation = '', 500);
            return;
        }

        // Collect data
        const formData = new FormData(form);
        const data = Object.fromEntries(formData.entries());
        console.log('Form submitted:', data);

        // Show success state
        const formCol = form.parentElement;
        formCol.innerHTML = `
            <div class="form form--success">
                <div class="form__success-icon">
                    <svg width="40" height="40" viewBox="0 0 24 24" fill="none" stroke="white" stroke-width="2.5">
                        <polyline points="20 6 9 17 4 12"/>
                    </svg>
                </div>
                <h3 class="form__success-title">Richiesta Inviata!</h3>
                <p class="form__success-text">Grazie! Ti risponderemo entro 24 ore con il preventivo personalizzato per la tua famiglia.</p>
            </div>
        `;
    });

    // Live validation feedback
    form.querySelectorAll('.form__input').forEach(input => {
        input.addEventListener('focus', () => {
            input.style.borderColor = '#2684BA';
        });
        input.addEventListener('blur', () => {
            if (!input.value.trim() && input.hasAttribute('required')) {
                input.style.borderColor = '#F98AA5';
            } else {
                input.style.borderColor = '#e8ecf0';
            }
        });
    });
}

/* ─── Floating Particles (subtle ocean bubbles) ─── */
function initParticles() {
    const container = document.getElementById('particles');
    if (!container) return;

    const particleCount = 20;

    for (let i = 0; i < particleCount; i++) {
        const particle = document.createElement('div');
        const size = Math.random() * 6 + 2;
        const left = Math.random() * 100;
        const delay = Math.random() * 20;
        const duration = Math.random() * 15 + 15;

        particle.style.cssText = `
            position: absolute;
            width: ${size}px;
            height: ${size}px;
            background: rgba(255, 255, 255, ${Math.random() * 0.12 + 0.03});
            border-radius: 50%;
            left: ${left}%;
            bottom: -20px;
            animation: floatUp ${duration}s linear ${delay}s infinite;
            pointer-events: none;
        `;
        container.appendChild(particle);
    }

    // Add keyframe
    if (!document.getElementById('particleStyles')) {
        const style = document.createElement('style');
        style.id = 'particleStyles';
        style.textContent = `
            @keyframes floatUp {
                0% { transform: translateY(0) translateX(0); opacity: 0; }
                10% { opacity: 1; }
                90% { opacity: 1; }
                100% { transform: translateY(-100vh) translateX(${Math.random() > 0.5 ? '' : '-'}${Math.random() * 100}px); opacity: 0; }
            }
            @keyframes shake {
                0%, 100% { transform: translateX(0); }
                20%, 60% { transform: translateX(-6px); }
                40%, 80% { transform: translateX(6px); }
            }
        `;
        document.head.appendChild(style);
    }
}

/* ─── Smooth Scroll for anchor links ─── */
function initSmoothScroll() {
    document.querySelectorAll('a[href^="#"]').forEach(anchor => {
        anchor.addEventListener('click', (e) => {
            const target = document.querySelector(anchor.getAttribute('href'));
            if (target) {
                e.preventDefault();
                const offset = 60; // top bar height
                const top = target.getBoundingClientRect().top + window.pageYOffset - offset;
                window.scrollTo({ top, behavior: 'smooth' });
            }
        });
    });
}

/* ─── Top Bar shrink on scroll ─── */
function initTopBarShrink() {
    const topBar = document.querySelector('.top-bar');
    if (!topBar) return;

    let lastScroll = 0;

    window.addEventListener('scroll', () => {
        const scrollY = window.scrollY;

        if (scrollY > 200) {
            topBar.style.height = '38px';
            topBar.style.fontSize = '0.72rem';
        } else {
            topBar.style.height = '';
            topBar.style.fontSize = '';
        }

        lastScroll = scrollY;
    }, { passive: true });
}
