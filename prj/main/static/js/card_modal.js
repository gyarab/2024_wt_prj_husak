$('#cardModal').on('show.bs.modal', function (event) {
    const button = $(event.relatedTarget);

    const url = new URL(window.location);
    const id = button.data('id');
    console.log(button.data('id'));
    url.searchParams.set('name', id);
    history.replaceState(null, '', url);

    const title = button.data('title');
    const description = button.data('description');
    const link = button.data('link');
    const svg = button.data('svg');
    const img = button.data('image')
    const link_text = button.data('link-text')
    const type = button.data('type')
    console.log(type)

    const modal = $(this);
    modal.find('.modal-title').text(title);
    modal.find('.modal-body #modalContent').html(description);
    modal.find('#modalLink1').attr('href', link);
    modal.find('#modalLink2').attr('href', link);
    modal.find('#modalImg').attr('src', img);

    if (svg) {  
        $.ajax({
            url: svg,
            dataType: 'text',
            success: function(data) {
                const content = `
                <span>${link_text}</span>
                <span class="ms-2">${data}</span>
            `;
            modal.find('#modalLink2').html(content);
            }
        });
    }

    if(type == 'album') {
        album_modal(modal, id);
    }
});


$('#cardModal').on('hidden.bs.modal', function () { //TODO: FIX THIS
    console.log("CLOSE");
    const url = new URL(window.location);
    url.searchParams.delete('modal_id');
    history.replaceState(null, '', url.pathname + url.search);
});


function album_modal(modal, id) {
    fetch(`/api/album/${id}/`)
        .then(response => response.json())
        .then(data => {
            const songsHtml = data.songs.map(song => `
                <div class="text-start ms-2">
                    <a class="text-start ms-2 text-decoration-none link-pop" href="/skladby?name=${song.id}">
                    ${song.title}
                        <img src="/static/icons/link.svg" style="vertical-align: -2px; height: 16px;" alt="Icon">
                    </a>
                </div>
            `).join('')

            const modalContent = `
                <hr class="mt-0">
                <div class="text-start ms-2"> 
                    <strong>Songs:</strong>
                    ${songsHtml}
                </div>
            `;

            modal.find('#modalAdditional').html(modalContent);
        })
        .catch(error => {
            console.error('Error fetching album data:', error);
        });
}
