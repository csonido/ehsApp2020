function callModalForm(opt){
    var url = opt['url'];
    var mode = opt['mode'] || 'POST';

    document.querySelectorAll('#main-modal').forEach(function(item){
        item.remove();
    });

    var on_form_response = function(resp){
        var modalText = '<div class="modal-content">'
        + resp.response +
        + '</div>'


        var container = document.createElement('div');
        container.id = 'main-modal'
        container.className = 'modal-container modal';
        container.innerHTML = modalText;

        document.body.appendChild(container);

        var options = {};
        var elems = document.querySelectorAll('.modal');
        var instances = M.Modal.init(elems, options);

        var mainmodal = M.Modal.getInstance(container);
        mainmodal.open();
    }

    ajax({
        mode: mode,
        url: url,
        data: null,
        callback: on_form_response
        });
}

function submitModalForm(url, mode){

}