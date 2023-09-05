const deleteButton = document.getElementById('deleteButton');
const descartadoresHomeURL = '/descartadores/'
deleteButton.addEventListener('click', (event) => {
    event.preventDefault();

    const descartadorDocumento = deleteButton.getAttribute('data-document')

    console.log(descartadorDocumento)
    if (descartadorDocumento) {
        DeleteDescartador(descartadorDocumento);
    } else {
        alert('Informe o ID do produto a ser excluído.');
    }
});

function DeleteDescartador(documento) {
    fetch(`/descartadores/delete/${documento}`, {
        method: 'DELETE',
    })
        .then(response => {
            if (response.ok) {
                alert('Dados excluidos com sucesso!');
                window.location.href = descartadoresHomeURL;
            } else {
                throw new Error('Erro ao excluir o descartador.');
            }
        })
        .catch(error => {
            console.error('Erro ao excluir o descartador:', error);
        });
}