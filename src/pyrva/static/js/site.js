// Mobile Menu Toggle
document.querySelector('#mobile-menu-button').addEventListener('click', function () {
    document.querySelectorAll('#mobile-menu-button svg').forEach(function (svg) {
        svg.classList.toggle('hidden');
    });
    document.querySelector('#mobile-menu').classList.toggle('hidden');
});

// Hero CTA Auto Expand FAQ Item
document.querySelector('#speak').addEventListener('click', function () {
    document.querySelector('#present').open = true;
});
