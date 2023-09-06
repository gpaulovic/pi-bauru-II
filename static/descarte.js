function fetchAndDisplayDescartes() {
    const descartesTableBody = document.getElementById('descartes-table-body');

    const xhr = new XMLHttpRequest();
    xhr.open('GET', '/descartes/get/', true);

    xhr.onload = function () {
        if (xhr.status === 200) {
            const data = JSON.parse(xhr.responseText);
            descartesTableBody.innerHTML = '';

            data.forEach(descarte => {
                const row = document.createElement('tr');
                const idCell = document.createElement('td');
                const nomeCell = document.createElement('td');
                const tipoCell = document.createElement('td');
                const quantidadeCell = document.createElement('td');
                const descartadorCell = document.createElement('td');
                const ecopontoCell = document.createElement('td');
                const editCell = document.createElement('td');
                const deleteCell = document.createElement('td');

                const editLink = createLink(`editar/${descarte.id}`, 'glyphicon glyphicon-edit')
                const deleteLink = createLink(`delete-confirm/${descarte.id}`, 'glyphicon glyphicon-trash',)

                idCell.textContent = descarte.id;
                nomeCell.textContent = descarte.nome;
                tipoCell.textContent = descarte.tipo;
                quantidadeCell.textContent = descarte.quantidade;
                descartadorCell.textContent = descarte.descartador;
                ecopontoCell.textContent = descarte.ecoponto;

                editCell.appendChild(editLink)
                deleteCell.appendChild(deleteLink)

                row.appendChild(idCell);
                row.appendChild(nomeCell);
                row.appendChild(tipoCell);
                row.appendChild(quantidadeCell);
                row.appendChild(descartadorCell);
                row.appendChild(ecopontoCell);
                row.appendChild(editCell);
                row.appendChild(deleteCell);

                descartesTableBody.appendChild(row);
            });
        } else {
            console.error('Houve um erro ao buscar os dados da API:', xhr.status);
        }
    };

    xhr.onerror = function () {
        console.error('Houve um erro ao fazer a requisição.');
    };

    xhr.send();
}

function createLink(href, classe, id) {
    const link = document.createElement('a');

    link.href = href;

    link.id = id

    link.className = classe;

    return link;
}

fetchAndDisplayDescartes();

function saveForm(event) {
    event.preventDefault(); // Impede o envio padrão do formulário

    const form = document.getElementById('descartes-save-form');
    const formData = new FormData(form);
    const cookie =  getCookie('csrftoken')
    console.log(formData)
    console.log(cookie)

    fetch('/descartes/save/', {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json',
            'X-CSRFToken':cookie,
        },
        body: JSON.stringify(Object.fromEntries(formData)),
    })
        .then(response => {
            if (response.ok) {
                alert('Formulário salvo com sucesso!');
                window.location.href = '';
            } else {
                throw new Error();
            }
        })
        .catch(error => {
            console.error('Erro ao salvar o formulário:', error);
        });
}

const form = document.getElementById('descartes-save-form');
form.addEventListener('submit', saveForm);

function getCookie(name) {
    const cookieValue = document.cookie.match('(^|;)\\s*' + name + '\\s*=\\s*([^;]+)');
    return cookieValue ? cookieValue.pop() : '';
}