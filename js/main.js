window.addEventListener('load', () => {
    /***************************toogle  icon menu bar******************************************/
    const menuButton = document.querySelector('#menu-icon');
    const menuIcon = menuButton ? menuButton.querySelector('i') : null;
    const navbar = document.querySelector('.navbar');

    const setMenuState = (isOpen) => {
        if (!menuButton || !menuIcon || !navbar) {
            return;
        }
        menuButton.setAttribute('aria-expanded', isOpen);
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


    /*************Scroll sections active link***********************/
    const sections = document.querySelectorAll('section');
    const navLinks = document.querySelectorAll('header nav a');

    window.addEventListener('scroll', () => {
        sections.forEach(sec => {
            const top = window.scrollY;
            const offset = sec.offsetTop - 150;
            const height = sec.offsetHeight;
            const id = sec.getAttribute('id');
            const activeLink = id ? document.querySelector(`header nav a[href*="${id}"]`) : null;

            if (top >= offset && top < offset + height && activeLink) {
                navLinks.forEach(links => {
                    links.classList.remove('active');
                });
                activeLink.classList.add('active');
            }
        });


        /***************************Sticky navbar******************************************/
        const header = document.querySelector('header');

        if (header) {
            header.classList.toggle('sticky', window.scrollY > 100);
        }

        /***************remove toglle menu icon and navbar when click navbar link (Scroll) / Quitar menu cuando de un click**************/
        if (navbar) {
            navbar.classList.remove('active');
        }
        setMenuState(false);
    });


    /***************************Scroll reveal******************************************/
    if (window.ScrollReveal) {
        ScrollReveal({
            /* reset: true,*/
            distance: '80px',
            duration: 2000,
            delay: 200
        });

        ScrollReveal().reveal('.home-content, .heading', {
            origin: 'top'
        });
        ScrollReveal().reveal('.home-img, .services-container, .portfolio-box, .contact form', {
            origin: 'bottom'
        });

        ScrollReveal().reveal('.home-content h1, .about-img ', {
            origin: 'left'
        });

        ScrollReveal().reveal('.home-content p, .about-content ', {
            origin: 'right'
        });
    }


    /*TypedJS*/
    if (window.Typed && document.querySelector('.multiple-text')) {
        new Typed('.multiple-text', {
            strings: ['Frontend Developer', 'SEO', 'Blogger'],
            typeSpeed: 100,
            backSpeed: 100,
            backDelay: 1000,
            loop: true
        });
    }

    /***************************Contact form validation******************************************/
    const form = document.querySelector('#contact-form');
    if (form) {
        const status = document.querySelector('#form-status');
        const fields = [
            {
                input: document.querySelector('#full-name'),
                validate: (value) => value.trim().length >= 3 || 'Ingresa un nombre válido.'
            },
            {
                input: document.querySelector('#email'),
                validate: (value) =>
                    /^[^\s@]+@[^\s@]+\.[^\s@]+$/.test(value.trim()) ||
                    'Ingresa un correo válido.'
            },
            {
                input: document.querySelector('#phone'),
                validate: (value) => {
                    const digits = value.replace(/\D/g, '');
                    return digits.length >= 7 || 'Ingresa un teléfono válido.';
                }
            },
            {
                input: document.querySelector('#subject'),
                validate: (value) => value.trim().length >= 3 || 'Agrega un asunto claro.'
            },
            {
                input: document.querySelector('#textarea'),
                validate: (value) =>
                    value.trim().length >= 10 || 'Cuéntanos un poco más en tu mensaje.'
            }
        ];

        const setError = (input, message) => {
            if (!input) {
                return;
            }
            const error = document.querySelector(`#${input.id}-error`);
            if (error) {
                error.textContent = message;
            }
            input.classList.add('input-error');
        };

        const clearError = (input) => {
            if (!input) {
                return;
            }
            const error = document.querySelector(`#${input.id}-error`);
            if (error) {
                error.textContent = '';
            }
            input.classList.remove('input-error');
        };

        fields.forEach(({ input, validate }) => {
            if (!input) {
                return;
            }
            input.addEventListener('input', () => {
                const result = validate(input.value);
                if (result === true) {
                    clearError(input);
                }
            });
        });

        form.addEventListener('submit', (event) => {
            event.preventDefault();
            let isValid = true;

            if (status) {
                status.textContent = '';
            }

            fields.forEach(({ input, validate }) => {
                if (!input) {
                    return;
                }
                const result = validate(input.value);
                if (result !== true) {
                    setError(input, result);
                    isValid = false;
                } else {
                    clearError(input);
                }
            });

            if (isValid) {
                form.reset();
                if (status) {
                    status.textContent = '¡Gracias! Tu mensaje fue enviado correctamente.';
                }
            } else if (status) {
                status.textContent = 'Revisa los campos marcados para continuar.';
            }
        });
    }
});
