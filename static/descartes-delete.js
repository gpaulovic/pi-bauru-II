const deleteButton = document.getElementById('deleteButton');
const descartesHomeURL = '/descartes/'
deleteButton.addEventListener('click', (event) => {
    event.preventDefault();

    const descarteId = deleteButton.getAttribute('data-document')
    DeleteDescarte(descarteId);

});

function DeleteDescarte(documento) {
    fetch(`/descartes/delete/${documento}`, {
        method: 'DELETE',
    })
        .then(response => {
            if (response.ok) {
                alert('Dados excluidos com sucesso!');
                window.location.href = descartesHomeURL;
            } else {
                throw new Error();
            }
        })
        .catch(error => {
            console.error('Erro ao excluir o descartador:', error);
        });
}