const usuariosHomeURL = '/usuarios/'
document.addEventListener('DOMContentLoaded', function () {
    const updateForm = document.getElementById('usuario-update-form');

    updateForm.addEventListener('submit', function (event) {
        event.preventDefault();

        const formData = new FormData(updateForm);
        const usuarioId = updateForm.getAttribute('data-id')

        let hasDataToSubmit = false;
        for (const value of formData.values()) {
            if (value) {
                hasDataToSubmit = true;
                break;
            }
        }

        if (!hasDataToSubmit) {
            alert('Preencha pelo menos um campo para atualizar.');
            return;
        }

        if (!formData.get('id')){
            formData.set('id',usuarioId)
        }

        console.log(formData)
        fetch(`/usuarios/update/${usuarioId}`, {
            method: 'PATCH',
            headers: {
                'Content-Type': 'application/json',
                'X-CSRFToken': getCookie('csrftoken'),
            },
            body: JSON.stringify(Object.fromEntries(formData)),
        })
            .then(response => {
                if (response.ok) {
                    alert('Dados atualizados com sucesso!');
                    window.location.href = usuariosHomeURL;
                } else {
                    throw new Error('Erro ao atualizar dados.');
                }
            })
            .catch(error => {
                console.error(error);
            });
    });
});

function getCookie(name) {
    const cookieValue = document.cookie.match('(^|;)\\s*' + name + '\\s*=\\s*([^;]+)');
    return cookieValue ? cookieValue.pop() : '';
}