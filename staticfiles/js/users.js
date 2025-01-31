function showModalView(route, pk) {
    $.ajax({
        url: '/users/' + route + '/',
        dataType: 'json',
        type: 'GET',
        data: {'pk': pk},
        success: function (r) {
            if (r.success) {
                $('#modal-user').empty().html(r.form);
                $('#modal-user').modal('show');
                initializeModalStyles();
            } else {
                toastr.info(r.message)
            }
        },
        fail: function (r) {
            toastr.error(r);
        }
    });
};
function initializeModalStyles() {
    // Inicializa estilos para inputs con Bootstrap 5
    $('#modal-user .input-group input').each(function () {
        if ($(this).val().trim() !== '') {
            $(this).parent('.input-group').addClass('is-filled');
        }
    });

    // Inicializa tooltips, popovers, etc. de Bootstrap
    $('[data-bs-toggle="tooltip"]').tooltip();
    $('[data-bs-toggle="popover"]').popover();

    // Reaplica los estilos para select2 si se utiliza
    $('.select2').select2({
        dropdownParent: $('#modal-user .modal-body')
    });

    // Cualquier otro componente dinámico que necesite reiniciarse
    console.log("Estilos inicializados correctamente en el modal.");
}