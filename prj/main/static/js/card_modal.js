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

    switch (type) {
        case "album":
            album_modal(modal, id);
            break;
        case "artist":
            artist_modal(modal, id);
            break;
        case "band":
            band_modal(modal, id);
            break;
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
            if (!data.songs || data.songs.length === 0) {
                modal.find('#modalAdditional').html("");
                return;
            }
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

function artist_modal(modal, id) {
    fetch(`/api/artist/${id}/`)
        .then(response => response.json())
        .then(data => {
            if (!data.bands || data.bands.length === 0) {
                modal.find('#modalAdditional').html("");
                return;
            }
            const bandsHtml = data.bands.map(band => `
                <div class="text-start ms-2">
                    <a class="text-start ms-2 text-decoration-none link-pop" href="/kapely?name=${band.id}">
                    ${band.title}
                        <img src="/static/icons/link.svg" style="vertical-align: -2px; height: 16px;" alt="Icon">
                        (${band.startYear} - ${band.endYear ?? "Today"})
                    </a>
                </div>
            `).join('')

            const modalContent = `
                <hr class="mt-0">
                <div class="text-start ms-2"> 
                    <strong>Bands:</strong>
                    ${bandsHtml} 
                </div>
            `;

            modal.find('#modalAdditional').html(modalContent);
        })
        .catch(error => {
            console.error('Error fetching album data:', error);
        });
}

function band_modal(modal, id) {
    fetch(`/api/band/${id}/`)
        .then(response => response.json())
        .then(data => {
            if (!data.artists || data.artists.length === 0) {
                modal.find('#modalAdditional').html("");
                return;
            }
            const artistsHtml = data.artists.map(artist => `
                <div class="text-start ms-2">
                    <a class="text-start ms-2 text-decoration-none link-pop" href="/clenove?name=${artist.id}">
                    ${artist.name}
                        <img src="/static/icons/link.svg" style="vertical-align: -2px; height: 16px;" alt="Icon">
                    </a>
                    (${artist.startYear} - ${artist.endYear ?? "Today"})
                </div>
            `).join('')

            const modalContent = `
                <hr class="mt-0">
                <div class="text-start ms-2"> 
                    <strong>Artists:</strong>
                    ${artistsHtml}
                </div>
            `;

            modal.find('#modalAdditional').html(modalContent);
        })
        .catch(error => {
            console.error('Error fetching album data:', error);
        });
}
