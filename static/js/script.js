document.addEventListener("DOMContentLoaded", () => {
    // 1. Mobile Menu Toggle
    const mobileMenuBtn = document.getElementById('mobile-menu-btn');
    const navLinks = document.getElementById('nav-links');

    if (mobileMenuBtn) {
        mobileMenuBtn.addEventListener('click', () => {
            navLinks.classList.toggle('show');
        });
    }

    // 2. Active Nav
    const currentPath = window.location.pathname;
    const navItems = document.querySelectorAll('.nav-item');

    navItems.forEach(link => {
        if (link.getAttribute('href') === currentPath) {
            link.classList.add('active');
        } else if (currentPath === '/' && link.getAttribute('href') === '/') {
            link.classList.add('active');
        }
    });

    // 3. Abstract Toggle
    const toggleButtons = document.querySelectorAll('.toggle-abstract-btn');

    toggleButtons.forEach(button => {
        button.addEventListener('click', function () {
            const cardBody = this.closest('.pub-card-body');
            const abstractContent = cardBody.querySelector('.pub-abstract-content');

            // Toggle visibility
            if (abstractContent.classList.contains('hidden')) {
                abstractContent.classList.remove('hidden');
                this.innerHTML = 'Hide Abstract <i class="fas fa-chevron-up"></i>';
            } else {
                abstractContent.classList.add('hidden');
                this.innerHTML = 'Show Abstract <i class="fas fa-chevron-down"></i>';
            }
        });
    });
});