function showModalView(route, pk) {
    $.ajax({
        url: '/users/' + route + '/',
        dataType: 'json',
        type: 'GET',
        data: {'pk': pk},
        success: function (r) {
            if (r.success) {
                // $('#exampleModal .modal-body').empty().html(r.form);
                var modalElement = document.getElementById('exampleModal');
                var modalBodyElement = modalElement.querySelector('.modal-body');

                // Limpia el contenido anterior
                modalBodyElement.innerHTML = '';

                // Inserta el nuevo contenido
                modalBodyElement.innerHTML = r.form;

                // Usa el método de Bootstrap para mostrar el modal
                var modal = new bootstrap.Modal(modalElement, {
                    keyboard: false
                });
                modal.show();
            } else {
                toastr.info(r.message)
            }
        },
        fail: function (r) {
            toastr.error(r);
        }
    });
};
