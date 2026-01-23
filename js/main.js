'use strict'

window.addEventListener('load', function () {
    const menuIcon = document.querySelector('#menu-icon')
    const navbar = document.querySelector('.navbar')

    if (!menuIcon || !navbar) {
        return
    }

    menuIcon.addEventListener('click', function () {
        navbar.classList.toggle('active')
    })

    navbar.querySelectorAll('a').forEach((link) => {
        link.addEventListener('click', function () {
            navbar.classList.remove('active')
        })
    })
})
