window.addEventListener('load', () => {

  /*************************** Dynamic Year ***************************/
  const yearEl = document.getElementById('footer-year');
  if (yearEl) yearEl.textContent = new Date().getFullYear();

  /*************************** Toggle menu ***************************/
  const menuButton = document.querySelector('#menu-icon');
  const menuIcon = menuButton ? menuButton.querySelector('i') : null;
  const navbar = document.querySelector('.navbar');

  const setMenuState = (isOpen) => {
    if (!menuButton || !menuIcon || !navbar) return;
    menuButton.setAttribute('aria-expanded', String(isOpen));
    menuButton.setAttribute('aria-label', isOpen ? 'Cerrar menú' : 'Abrir menú');
    menuIcon.classList.toggle('bx-menu', !isOpen);
    menuIcon.classList.toggle('bx-x', isOpen);
  };

  if (menuButton && navbar) {
    menuButton.addEventListener('click', () => {
      const isOpen = navbar.classList.toggle('active');
      setMenuState(isOpen);
    });
  }

  /*************************** Scroll sections active link ***************************/
  const sections = document.querySelectorAll('section');
  const navLinks = document.querySelectorAll('header nav a');

  window.addEventListener('scroll', () => {
    const top = window.scrollY;

    sections.forEach((sec) => {
      const offset = sec.offsetTop - 150;
      const height = sec.offsetHeight;
      const id = sec.getAttribute('id');
      if (!id) return;

      if (top >= offset && top < offset + height) {
        navLinks.forEach((link) => {
          link.classList.remove('active');
          link.removeAttribute('aria-current');
        });
        const active = document.querySelector(`header nav a[href*="${id}"]`);
        if (active) {
          active.classList.add('active');
          active.setAttribute('aria-current', 'page');
        }
      }
    });

    const header = document.querySelector('header');
    if (header) header.classList.toggle('sticky', top > 100);

    if (navbar) navbar.classList.remove('active');
    setMenuState(false);
  });

  /*************************** Portfolio Filters ***************************/
  const filterBtns = document.querySelectorAll('.filter-btn');
  const portfolioBoxes = document.querySelectorAll('.portfolio-box');

  filterBtns.forEach(btn => {
    btn.addEventListener('click', () => {
      // Update active state
      filterBtns.forEach(b => {
        b.classList.remove('active');
        b.setAttribute('aria-selected', 'false');
      });
      btn.classList.add('active');
      btn.setAttribute('aria-selected', 'true');

      const filter = btn.dataset.filter;

      portfolioBoxes.forEach(box => {
        if (filter === 'all') {
          box.classList.remove('hidden');
          box.style.display = '';
        } else {
          const categories = box.dataset.category || '';
          if (categories.includes(filter)) {
            box.classList.remove('hidden');
            box.style.display = '';
          } else {
            box.classList.add('hidden');
            box.style.display = 'none';
          }
        }
      });
    });
  });

  /*************************** ScrollReveal ***************************/
  if (window.ScrollReveal) {
    ScrollReveal({ distance: '60px', duration: 1500, delay: 200 });
    ScrollReveal().reveal('.home-content, .heading', { origin: 'top' });
    ScrollReveal().reveal('.home-img, .services-container, .portfolio-box, .contact form, .testimonial-box', { origin: 'bottom' });
    ScrollReveal().reveal('.home-content h1, .about-img', { origin: 'left' });
    ScrollReveal().reveal('.home-desc, .about-content', { origin: 'right' });
    ScrollReveal().reveal('.about-stats, .tech-stack', { origin: 'bottom', delay: 400 });
  }

  /*************************** TypedJS ***************************/
  if (window.Typed && document.querySelector('.multiple-text')) {
    new Typed('.multiple-text', {
      strings: [
        'Consultor SEO',
        'Auditor Técnico Web',
        'Desarrollador Full-Stack',
        'Especialista en Google Ads'
      ],
      typeSpeed: 80,
      backSpeed: 60,
      backDelay: 1500,
      loop: true
    });
  }

  /*************************** Testimonials Carousel ***************************/
  const track = document.querySelector('.carousel-track');
  const slides = document.querySelectorAll('.testimonial-slide');
  const prevBtn = document.querySelector('.carousel-prev');
  const nextBtn = document.querySelector('.carousel-next');
  const dotsContainer = document.querySelector('.carousel-dots');

  if (track && slides.length > 0 && dotsContainer) {
    let currentSlide = 0;
    let autoplayTimer = null;

    // Create dots
    slides.forEach((_, i) => {
      const dot = document.createElement('button');
      dot.classList.add('carousel-dot');
      if (i === 0) dot.classList.add('active');
      dot.setAttribute('aria-label', `Ir al testimonio ${i + 1}`);
      dot.addEventListener('click', () => goToSlide(i));
      dotsContainer.appendChild(dot);
    });

    const dots = dotsContainer.querySelectorAll('.carousel-dot');

    function goToSlide(index) {
      currentSlide = index;
      track.style.transform = `translateX(-${currentSlide * 100}%)`;
      dots.forEach((d, i) => d.classList.toggle('active', i === currentSlide));
    }

    function nextSlide() {
      goToSlide((currentSlide + 1) % slides.length);
    }

    function prevSlide() {
      goToSlide((currentSlide - 1 + slides.length) % slides.length);
    }

    if (nextBtn) nextBtn.addEventListener('click', () => { nextSlide(); resetAutoplay(); });
    if (prevBtn) prevBtn.addEventListener('click', () => { prevSlide(); resetAutoplay(); });

    // Swipe support
    let touchStartX = 0;
    track.addEventListener('touchstart', (e) => { touchStartX = e.changedTouches[0].screenX; }, { passive: true });
    track.addEventListener('touchend', (e) => {
      const diff = touchStartX - e.changedTouches[0].screenX;
      if (Math.abs(diff) > 50) {
        if (diff > 0) nextSlide(); else prevSlide();
        resetAutoplay();
      }
    }, { passive: true });

    // Autoplay
    function startAutoplay() { autoplayTimer = setInterval(nextSlide, 5000); }
    function resetAutoplay() { clearInterval(autoplayTimer); startAutoplay(); }
    startAutoplay();

    // Pause on hover
    const wrapper = document.querySelector('.carousel-wrapper');
    if (wrapper) {
      wrapper.addEventListener('mouseenter', () => clearInterval(autoplayTimer));
      wrapper.addEventListener('mouseleave', startAutoplay);
    }
  }

  /*************************** Contact Form (PRO) ***************************/
  const form = document.querySelector('#contact-form');
  if (!form) return;

  const status = document.querySelector('#form-status');
  const submitBtn = form.querySelector('input[type="submit"], button[type="submit"]');

  const qs = (sel) => form.querySelector(sel);

  const ensureErrorEl = (input) => {
    if (!input || !input.id) return null;
    const expectedId = `${input.id}-error`;
    let el = document.getElementById(expectedId);
    if (!el) {
      el = document.createElement('span');
      el.className = 'error-message';
      el.id = expectedId;
      input.insertAdjacentElement('afterend', el);
    }
    const describedby = (input.getAttribute('aria-describedby') || '').trim();
    if (!describedby.includes(expectedId)) {
      input.setAttribute('aria-describedby', describedby ? `${describedby} ${expectedId}` : expectedId);
    }
    return el;
  };

  const setStatus = (message, type = 'info') => {
    if (!status) return;
    status.textContent = message || '';
    status.classList.remove('is-success', 'is-error', 'is-info');
    status.classList.add(type === 'success' ? 'is-success' : type === 'error' ? 'is-error' : 'is-info');
  };

  const setError = (input, message) => {
    if (!input) return;
    const errorEl = ensureErrorEl(input);
    if (errorEl) errorEl.textContent = message || '';
    input.classList.add('input-error');
  };

  const clearError = (input) => {
    if (!input) return;
    const errorEl = ensureErrorEl(input);
    if (errorEl) errorEl.textContent = '';
    input.classList.remove('input-error');
  };

  const normalizePhone = (value) => value.replace(/[^\d+]/g, '').trim();

  const fullNameEl = qs('#full-name');
  const emailEl = qs('#email');
  const phoneEl = qs('#phone');
  const subjectEl = qs('#subject');
  const msgEl = qs('#message');
  const honeypotEl = qs('input[name="company"]');

  const fields = [
    {
      input: fullNameEl,
      validate: (v) => (v.trim().length >= 3 ? true : 'Ingresa un nombre válido (mínimo 3 caracteres).')
    },
    {
      input: emailEl,
      validate: (v) =>
        (/^[^\s@]+@[^\s@]+\.[^\s@]+$/.test(v.trim()) ? true : 'Ingresa un correo válido.')
    },
    {
      input: phoneEl,
      validate: (v) => {
        if (v.trim() === '') return true;
        const cleaned = normalizePhone(v);
        const digits = cleaned.replace(/\D/g, '');
        return digits.length >= 7 ? true : 'Ingresa un teléfono válido (mínimo 7 dígitos).';
      }
    },
    {
      input: subjectEl,
      validate: (v) => (v.trim() === '' || v.trim().length >= 3 ? true : 'Agrega un asunto claro.')
    },
    {
      input: msgEl,
      validate: (v) => (v.trim().length >= 10 ? true : 'Cuéntame un poco más (mínimo 10 caracteres).')
    }
  ];

  fields.forEach(({ input, validate }) => {
    if (!input) return;
    ensureErrorEl(input);
    input.addEventListener('input', () => {
      const result = validate(input.value);
      if (result === true) clearError(input);
    });
  });

  if (msgEl) {
    msgEl.addEventListener('keydown', (e) => {
      if (e.key === 'Enter' && (e.ctrlKey || e.metaKey)) {
        form.requestSubmit?.();
      }
    });
  }

  form.addEventListener('submit', async (e) => {
    e.preventDefault();

    if (honeypotEl && honeypotEl.value.trim() !== '') {
      setStatus('No se pudo enviar el mensaje', 'error');
      return;
    }

    let valid = true;
    let firstInvalid = null;

    fields.forEach(({ input, validate }) => {
      if (!input) return;
      const result = validate(input.value);
      if (result !== true) {
        setError(input, result);
        valid = false;
        if (!firstInvalid) firstInvalid = input;
      } else {
        clearError(input);
      }
    });

    if (!valid) {
      setStatus('Revisa los campos marcados para continuar.', 'error');
      firstInvalid?.focus();
      return;
    }

    if (submitBtn) {
      submitBtn.disabled = true;
      submitBtn.dataset.originalText = submitBtn.value || submitBtn.textContent || '';
      if (submitBtn.value !== undefined) submitBtn.value = 'Enviando...';
      else submitBtn.textContent = 'Enviando...';
    }
    setStatus('Enviando mensaje...', 'info');

    const data = new URLSearchParams();
    data.append('full-name', fullNameEl?.value?.trim() || '');
    data.append('email', emailEl?.value?.trim() || '');
    data.append('phone', normalizePhone(phoneEl?.value || ''));
    data.append('topic', subjectEl?.value?.trim() || '');
    data.append('msg', msgEl?.value?.trim() || '');
    data.append('company', honeypotEl?.value || '');

    try {
      const response = await fetch('/contact.php', {
        method: 'POST',
        headers: { 'Content-Type': 'application/x-www-form-urlencoded' },
        body: data.toString()
      });

      let payload = null;
      const contentType = response.headers.get('content-type') || '';

      if (contentType.includes('application/json')) {
        payload = await response.json().catch(() => null);
      } else {
        const text = await response.text().catch(() => '');
        payload = { message: text };
      }

      if (response.ok && (payload?.ok === true || payload?.message?.toUpperCase?.() === 'OK')) {
        setStatus(payload?.ui_message || 'Mensaje enviado correctamente', 'success');
        form.reset();
        fields.forEach(({ input }) => input && clearError(input));
        setTimeout(() => setStatus('', 'info'), 6000);
      } else {
        setStatus(payload?.ui_message || 'No se pudo enviar el mensaje', 'error');
      }
    } catch (err) {
      setStatus('Error de conexión. Intenta de nuevo.', 'error');
    } finally {
      if (submitBtn) {
        submitBtn.disabled = false;
        const original = submitBtn.dataset.originalText || 'Enviar Mensaje';
        if (submitBtn.value !== undefined) submitBtn.value = original;
        else submitBtn.textContent = original;
      }
    }
  });
});

// Lightbox for zoomable gallery images
window.addEventListener('load', () => {
  const zoomables = document.querySelectorAll('.gallery-zoomable');
  if (!zoomables.length) return;

  const overlay = document.createElement('div');
  overlay.className = 'lightbox-overlay';
  overlay.setAttribute('role', 'dialog');
  overlay.setAttribute('aria-modal', 'true');
  overlay.innerHTML = '<button type="button" class="lightbox-close" aria-label="Cerrar imagen ampliada"><i class="bx bx-x" aria-hidden="true"></i></button><img src="" alt="" />';
  document.body.appendChild(overlay);

  const overlayImg = overlay.querySelector('img');
  const closeBtn = overlay.querySelector('.lightbox-close');
  let lastFocused = null;

  function openLightbox(img) {
    overlayImg.src = img.currentSrc || img.src;
    overlayImg.alt = img.alt || '';
    overlay.classList.add('active');
    lastFocused = document.activeElement;
    closeBtn.focus();
    document.body.style.overflow = 'hidden';
  }

  function closeLightbox() {
    overlay.classList.remove('active');
    overlayImg.src = '';
    document.body.style.overflow = '';
    if (lastFocused) lastFocused.focus();
  }

  zoomables.forEach((img) => {
    img.setAttribute('tabindex', '0');
    img.setAttribute('role', 'button');
    img.setAttribute('aria-label', 'Ver imagen ampliada: ' + (img.alt || ''));
    img.addEventListener('click', () => openLightbox(img));
    img.addEventListener('keydown', (e) => {
      if (e.key === 'Enter' || e.key === ' ') {
        e.preventDefault();
        openLightbox(img);
      }
    });
  });

  closeBtn.addEventListener('click', closeLightbox);
  overlay.addEventListener('click', (e) => {
    if (e.target === overlay) closeLightbox();
  });
  document.addEventListener('keydown', (e) => {
    if (e.key === 'Escape' && overlay.classList.contains('active')) closeLightbox();
  });
});
