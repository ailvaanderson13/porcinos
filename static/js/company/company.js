$(document).ready(function(){
    $('#id_cnpj').mask('00.000.000/0000-00', {reverse: true});
    $('#id_telefone').mask('(00) 00000-0000');
    $('#id_cep').mask('00000-000');
})

$('.btn-trash').on({
    'click': function () {
        let pk = $(this).val();
        Swal.fire({
            title: 'ATENÇÃO',
            text: "Tem Certeza que deseja excluir?",
            icon: 'warning',
            showCancelButton: true,
            confirmButtonColor: '#3085d6',
            cancelButtonColor: '#d33',
            confirmButtonText: 'SIM',
            cancelButtonText: 'NÃO'
        }).then((result) => {
            if (result.value) {
                $.ajax({
                    'url': '/company/delete-company/',
                    'method': 'POST',
                    'dataType': 'json',
                    'data': {
                        'pk': pk
                    },
                    success: function (data) {
                        if (data.success) {
                            Swal.fire({
                                title: 'Excluido!',
                                text: "A empresa foi excluida!",
                                icon: 'success',
                                allowOutsideClick: false,
                                allowEscapeKey: false,
                            }).then((result) => {
                                if (result.value) {
                                    location.reload();
                                }
                            })
                        } else {
                            Swal.fire(
                                'Erro!',
                                'Erro ao tentar excluir a empresa!',
                                'error'
                            )
                        }
                    }
                })
            }
        })
    }
})