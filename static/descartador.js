function fetchAndDisplayDescartadores() {
    const descartadoresTableBody = document.getElementById('descartadores-table-body');

    // Fazer a chamada GET para a API usando XMLHttpRequest
    const xhr = new XMLHttpRequest();
    xhr.open('GET', '/descartadores/get/', true);

    xhr.onload = function () {
        if (xhr.status === 200) {
            const data = JSON.parse(xhr.responseText);
            descartadoresTableBody.innerHTML = '';

            data.forEach(descartador => {
                const row = document.createElement('tr');
                const nomeCell = document.createElement('td');
                const documentoCell = document.createElement('td');
                const emailCell = document.createElement('td');
                const enderecoCell = document.createElement('td');
                const editCell = document.createElement('td');
                const deleteCell = document.createElement('td');

                const editLink = createLink(`editar/${descartador.documento}`, 'glyphicon glyphicon-edit')
                const deleteLink = createLink(`delete-confirm/${descartador.documento}`, 'glyphicon glyphicon-trash',)

                nomeCell.textContent = descartador.nome;
                documentoCell.textContent = descartador.documento;
                emailCell.textContent = descartador.email;
                enderecoCell.textContent = descartador.endereco;

                editCell.appendChild(editLink)
                deleteCell.appendChild(deleteLink)

                row.appendChild(nomeCell);
                row.appendChild(documentoCell);
                row.appendChild(emailCell);
                row.appendChild(enderecoCell);
                row.appendChild(editCell);
                row.appendChild(deleteCell);

                descartadoresTableBody.appendChild(row);
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
    // Cria um elemento de link <a>
    const link = document.createElement('a');

    // Define o atributo href do link com o URL especificado
    link.href = href;

    link.id = id

    link.className = classe;
    //if (classes) {
    //    link.classList.add(...classes.split(' '));
    //}

    // Retorna o elemento de link criado
    return link;
}

// Chame a função para carregar a tabela ao carregar a página
fetchAndDisplayDescartadores();


function saveForm(event) {
    event.preventDefault(); // Impede o envio padrão do formulário

    const form = document.getElementById('descartadores-save-form');
    const formData = new FormData(form);

    fetch('/descartadores/save/', {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json'
        },
        body: JSON.stringify(Object.fromEntries(formData)),
    })
        .then(response => {
            if (response.ok) {
                alert('Formulário salvo com sucesso!');
                window.location.href = '';
            } else {
                throw new Error('Erro ao excluir o descartador.');
            }
        })
        .catch(error => {
            console.error('Erro ao salvar o formulário:', error);
        });
}

const form = document.getElementById('descartadores-save-form');
form.addEventListener('submit', saveForm);