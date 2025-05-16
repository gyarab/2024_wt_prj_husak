document.addEventListener('DOMContentLoaded', function () {
    const params = new URLSearchParams(window.location.search);
    const name = params.get('name');

    if (name) {
        const modalTriggers = document.querySelectorAll('[data-bs-toggle="modal"]');
        const targetCard = Array.from(modalTriggers).find(el => el.getAttribute('data-title') === name);

        if (targetCard) {
            targetCard.click();
        }
    }
});