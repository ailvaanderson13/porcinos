$(document).ready(function(){
    $('.large').html('<i class="fas fa-spinner fa-spin"></i>')
    dashboard();
})

async function dashboard(){
    for (dash of $('.dash')){
        let id_card = dash.getAttribute('id_card');
        if (id_card){
            let response = await get_data(id_card);
            if (response.info > 0){
                $(`.card-${id_card}`).empty().html(response.info);
            } else{
                $(`.card-${id_card}`).empty().html(0);

            }
        }
    }
}

async function get_data(id_card){
    let url = `/onload/card/?id_card=${id_card}`
    return new Promise(resolve => {
        fetch(url).then((response)=>response.json()).then((response)=>{
            resolve(response);
        })
    })
}