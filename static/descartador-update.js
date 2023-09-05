const descartadoresHomeURL = '/descartadores/'
document.addEventListener('DOMContentLoaded', function () {
    const updateForm = document.getElementById('descartador-update-form');

    updateForm.addEventListener('submit', function (event) {
        event.preventDefault();

        const formData = new FormData(updateForm);
        const descartadorDocumento = updateForm.getAttribute('data-document')

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

        if (!formData.get('documento')){
            formData.set('documento',descartadorDocumento)
        }

        console.log(formData)
        fetch(`/descartadores/update/${descartadorDocumento}`, {
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
                    window.location.href = descartadoresHomeURL;
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