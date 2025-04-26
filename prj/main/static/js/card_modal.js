$('#cardModal').on('show.bs.modal', function (event) {
    var button = $(event.relatedTarget);
    var title = button.data('title');
    var description = button.data('description');
    var link = button.data('link');
    var svg = button.data('svg');
    var img = button.data('image')
    var link_text = button.data('link-text')

    var modal = $(this);
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
});