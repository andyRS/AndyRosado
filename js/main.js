window.addEventListener('load', function () {


    /***************************toogle  icon menu bar******************************************/
    let menuIocn = document.querySelector('#menu-icon');
    let navbar = document.querySelector('.navbar');


    menuIocn.onclick = () => {
        menuIocn.classList.toggle('bx-x')
        navbar.classList.toggle('active')
    }

    /*************Scroll sections active link***********************/
    let sections = document.querySelectorAll('section');
    let navLinks = document.querySelectorAll('header nav a');

    window.onscroll = () => {
        sections.forEach(sec => {
            let top = window.scrollY;
            let offset = sec.offsetTop - 150;
            let height = sec.offsetHeight;
            let id = sec.getAttribute('id');

            if (top >= offset && top < offset + height) {
                navLinks.forEach(links => {
                    links.classList.remove('active');
                    document.querySelector('header nav a[href*=' + id + ']').classList.add('active');
                });
            }
        });
    };

    /***************************Sticky navbar******************************************/

    let header = document.querySelector('header');


    header.classList.toogle('sticky', window.scrollY > 100);

    /***************************remove toglle menu icon and navbar when click navbar link (Scroll) / Quitar menu cuando de un click******************************************/
    menuIocn.classList.remove('bx-x')
    navbar.classList.remove('active')


    /***************************Tipado jS/ Typed JS******************************************/
   

});

