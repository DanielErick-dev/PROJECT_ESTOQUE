function mostrarMensagemRemover(mensagem)  {
            var mensagemElement = document.createElement('div');
            mensagemElement.className = 'mensagem-removido';
            mensagemElement.textContent = mensagem;
            document.body.appendChild(mensagemElement);


            setTimeout(function() {
                document.body.removeChild(mensagemElement);
           }, 3000);
        }
function mostrarMensagemAdicionar(mensagem)  {
            var mensagemElement = document.createElement('div');
            mensagemElement.className = 'mensagem-adicionado';
            mensagemElement.textContent = mensagem;
            document.body.appendChild(mensagemElement);


            setTimeout(function() {
                document.body.removeChild(mensagemElement);
           }, 3000);
        }