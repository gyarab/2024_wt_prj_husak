document.addEventListener('DOMContentLoaded', function () {
    const searchInput = document.getElementById('cardSearch');
    const cards = document.querySelectorAll('.card-element');

    searchInput.addEventListener('input', function () {
        const query = this.value.toLowerCase();

        cards.forEach(card => {
            const title = card.querySelectorAll('.card-img-wrapper')[0].getAttribute('data-title')?.toLowerCase() || '';
            const matches = title.includes(query)

            card.style.display = matches ? 'block' : 'none';
        });
    });
});