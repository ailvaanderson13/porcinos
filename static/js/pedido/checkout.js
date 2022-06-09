window.onload = function() {
    document.getElementById("input-code-bar").focus();
};
function get_code(){
    var code = document.querySelector('#input-code-bar');
    var qtd = parseInt(document.querySelector('#input-qtd').value);
    
    if(code){
        var content = code.value;
        if(content.length >= 5){
            $.ajax({
                'url': '/pedido/checkout/get_product/',
                'dataType': 'json',
                'method': 'POST',
                'data': {
                    'code': content,
                    'qtd': qtd,
                },
                success: function(data){
                    if(data.success){
                        if(data.item){
                            $('#body_table').append(data.item)
                        };
                        document.getElementById('input-code-bar').value = "";
                        document.getElementById('input-qtd').value = "1";
                        total_column();
                    }
                }
            });
        } else if(content.length < 5) {
            const Toast = Swal.mixin({
                toast: true,
                position: 'top-end',
                showConfirmButton: false,
                timer: 3000,
                timerProgressBar: true,
                didOpen: (toast) => {
                  toast.addEventListener('mouseenter', Swal.stopTimer)
                  toast.addEventListener('mouseleave', Swal.resumeTimer)
                }
              })
              
              Toast.fire({
                icon: 'error',
                title: 'O código deve conter 5 ou mais digitos.'
            });
        };
    }
};

var elemento = document.getElementById('input-code-bar');
elemento.addEventListener("keypress", get_code);


function total_column(){
    var qtd_line = 0;
    var qtd_total = 0;
    var valor_total = 0;
    var subtotal = 0;

    $('.qtd_line').each(function (){
        qtd_line += 1;
        $(this).empty().append(qtd_line);
    });

    $('.qtd_item').each(function (){
        qtd_total += parseInt($(this).text());
    });

    $('.val_uni').each(function (){
        valor_total += parseInt($(this).text());
    });

    $('.val_total').each(function (){
        subtotal += parseFloat($(this).text());
    });

    $('.qtd-line').empty().append(qtd_line);
    $('.qtd-total').empty().append(qtd_total);
    $('.column_subtotal').empty().append(subtotal.toFixed(2).replace('.',','));
};

$('.btn_finalizar').on('click', function(){
    let qtd_itens = $('.qtd-line').text();
    let subtotal = $('.modal-final').text();
    if(parseInt(qtd_itens) >=1){
        Swal.fire({
            position: 'center',
            title: 'Detalhes do pedido!',
            showCancelButton: true,
            confirmButtonText: 'Finalizar',
            cancelButtonText: 'Fechar',
            confirmButtonColor: '#30A5FF',
            cancelButtonColor: '#F9243F',
            html:`
                <div class="modal-body">
                    <div class="row">
                        <div class="col-sm-6 col-md-8 col-lg-12">
                            <label for="qtd">Quantidade de itens:</label>
                            <span id="qtd"><h4>${qtd_itens}</h4></span>

                            <label for="valor">Valor total: </label>
                            <h3 class="text-success soma-total">${subtotal}</h4>
                            <br>

                            <label for="pgto">Forma de pagamento</label><br>
                            <div class="row">
                                <div class="col-6">
                                    <span>Dinheiro</span>
                                    <input type="number" class="form-control">
                                    <span>Pix</span>
                                    <input type="number" class="form-control">
                                </div>
                                <div class="col-6">
                                    <span>Débito</span>
                                    <input type="number" class="form-control">
                                    <span>Crédito</span>
                                    <input type="number" class="form-control">
                                </div>
                            </div>
                            
                            <div class="pagamento">
                            <div class="col">
                                <label>Saldo</label>
                                <span class="form-control"></span>
                            </div>
                        </div>
                        </div>
                    </div><br>
                    <label for="obs">Observação</label>
                    <textarea class="form-control" id="obs" name="obs" id="obs" cols="auto" rows="auto" placeholder="Opcional"></textarea>
                </div>
            `
        }).then((result) =>{
            if(result.isConfirmed){
                
            }
        })
    }
});

$('.comeback_dash').on('click', function(){
    Swal.fire({
        title: 'Tem certeza que deseja voltar?',
        icon: 'question',
        iconHtml: '؟',
        showCancelButton: false,
        showCloseButton: false,
        showConfirmButton: false,
        html: `
            <a href="/" class="btn btn-success">Sim</a>
        `
      })
});

$('.btn_cancelar').on('click', function(){
    Swal.fire({
        title: 'Tem certeza que cancelar?',
        icon: 'warning',
        showCancelButton: false,
        showCloseButton: false,
        showConfirmButton: false,
        html: `
            <a href="/checkout" class="btn btn-success">Sim</a>
        `
      })
});

$(document).on('click', '.btn_trash', function(){
    Swal.fire({
        icon: 'warning',
        showCloseButton: true,
        confirmButtonText: 'Sim',
        cancelButtonText: 'Fechar',
        confirmButtonColor: '#30A5FF',
        cancelButtonColor: '#F9243F',
        text: 'Tem certeza que deseja excluir o item?',
    }).then((result) => {
        if (result.isConfirmed) {
            $(this).parent().parent().parent().remove();
            const Toast = Swal.mixin({
                toast: true,
                position: 'top-end',
                showConfirmButton: false,
                timer: 1500,
                timerProgressBar: true,
                didOpen: (toast) => {
                  toast.addEventListener('mouseenter', Swal.stopTimer)
                  toast.addEventListener('mouseleave', Swal.resumeTimer)
                }
              })
              
              Toast.fire({
                icon: 'success',
                title: 'Item excluido com sucesso!'
            });
            total_column();
        };
        if ($('.cart').is(':empty')){
            $('.container-cart').attr('hidden', true);
        };
    });
});