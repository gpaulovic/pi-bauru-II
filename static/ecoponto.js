function fetchAndDisplayEcopontos() {
    const ecopontosTableBody = document.getElementById('ecopontos-table-body');

    const xhr = new XMLHttpRequest();
    xhr.open('GET', '/ecopontos/get/', true);

    xhr.onload = function () {
        if (xhr.status === 200) {
            const data = JSON.parse(xhr.responseText);
            ecopontosTableBody.innerHTML = '';

            data.forEach(ecoponto => {
                const row = document.createElement('tr');
                const idCell = document.createElement('td');
                const cepCell = document.createElement('td');
                const bairroCell = document.createElement('td');
                const enderecoCell = document.createElement('td');
                const situacaoCell = document.createElement('td');
                const editCell = document.createElement('td');
                const deleteCell = document.createElement('td');

                const editLink = createLink(`editar/${ecoponto.id}`, 'glyphicon glyphicon-edit')
                const deleteLink = createLink(`delete-confirm/${ecoponto.id}`, 'glyphicon glyphicon-trash',)

                idCell.textContent = ecoponto.id;
                cepCell.textContent = ecoponto.cep;
                bairroCell.textContent = ecoponto.bairro;
                enderecoCell.textContent = ecoponto.endereco;
                situacaoCell.textContent = ecoponto.situacao;

                editCell.appendChild(editLink)
                deleteCell.appendChild(deleteLink)

                row.appendChild(idCell);
                row.appendChild(cepCell);
                row.appendChild(bairroCell);
                row.appendChild(enderecoCell);
                row.appendChild(situacaoCell);
                row.appendChild(editCell);
                row.appendChild(deleteCell);

                ecopontosTableBody.appendChild(row);
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

fetchAndDisplayEcopontos();

function saveForm(event) {
    event.preventDefault();

    const form = document.getElementById('ecopontos-save-form');
    const formData = new FormData(form);
    const cookie =  getCookie('csrftoken')

    fetch('/ecopontos/save/', {
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

const form = document.getElementById('ecopontos-save-form');
form.addEventListener('submit', saveForm);

function getCookie(name) {
    const cookieValue = document.cookie.match('(^|;)\\s*' + name + '\\s*=\\s*([^;]+)');
    return cookieValue ? cookieValue.pop() : '';
}