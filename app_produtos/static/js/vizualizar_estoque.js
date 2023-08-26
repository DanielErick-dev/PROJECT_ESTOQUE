function mostrarMensagemRemover(mensagem)  {
    console.log('testando validação de remoçao')
    var mensagemElement = document.createElement('div');
    mensagemElement.className = 'mensagem-removido';
    mensagemElement.textContent = mensagem;
    document.body.appendChild(mensagemElement);


    setTimeout(function() {
        document.body.removeChild(mensagemElement);
   }, 9000);
}

function mostrarMensagemAdicionar(mensagem)  {
    if (validacao_ok) {
        consele.log('testando validação')
        var mensagemElement = document.createElement('div');
        mensagemElement.className = 'mensagem-adicionado';
        mensagemElement.textContent = mensagem;
        document.body.appendChild(mensagemElement);


        setTimeout(function() {
            document.body.removeChild(mensagemElement);
       }, 9000);
    } else {
        console.log('validação não foi executada corretamente')
    }
}