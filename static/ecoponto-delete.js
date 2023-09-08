const deleteButton = document.getElementById('deleteButton');
const ecopontosHomeURL = '/ecopontos/'
deleteButton.addEventListener('click', (event) => {
    event.preventDefault();

    const ecopontoId = deleteButton.getAttribute('data-document')
    DeleteEcoponto(ecopontoId);

});

function DeleteEcoponto(id) {
    fetch(`/ecopontos/delete/${id}`, {
        method: 'DELETE',
    })
        .then(response => {
            if (response.ok) {
                alert('Dados excluidos com sucesso!');
                window.location.href = ecopontosHomeURL;
            } else {
                throw new Error();
            }
        })
        .catch(error => {
            console.error('Erro ao excluir o ecoponto:', error);
        });
}