document.addEventListener('DOMContentLoaded', function () {
    const searchInput = document.getElementById('cardSearch');
    const cards = document.querySelectorAll('.card-element');
    console.log(cards)

    searchInput.addEventListener('input', function () {
        const query = this.value.toLowerCase();
        console.log(query)

        cards.forEach(card => {
            const title = card.querySelectorAll('.card-img-wrapper')[0].getAttribute('data-title')?.toLowerCase() || '';
            console.log(title)
            const matches = title.includes(query)

            card.style.display = matches ? 'block' : 'none';
        });
    });
});