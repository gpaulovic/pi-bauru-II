const deleteButton = document.getElementById('deleteButton');
const usuariosHomeURL = '/usuarios/'
deleteButton.addEventListener('click', (event) => {
    event.preventDefault();

    const usuarioId = deleteButton.getAttribute('data-id')
    fetch(`/usuarios/delete/${usuarioId}`, {
        method: 'DELETE',
    })
        .then(response => {
            if (response.ok) {
                alert('Dados excluidos com sucesso!');
                window.location.href = usuariosHomeURL;
            } else {
                throw new Error();
            }
        })
        .catch(error => {
            console.error('Erro ao excluir o ecoponto:', error);
        });
});