function dateFormat(date_joined) {
    const data = new Date(date_joined)
    const opcoesDeFormatacao = {
        year: 'numeric', // Ano (4 dígitos)
        month: 'numeric',  // Mês (2 dígitos)
        day: 'numeric',  // Dia do mês (1-31)
        hour: '2-digit', // Hora (00-23)
        minute: '2-digit', // Minutos (00-59)
        second: '2-digit', // Segundos (00-59)
        hour12: false, // Formato de 24 horas (true para AM/PM, false para 00-23)
    };
    return data.toLocaleString('pt-BR', opcoesDeFormatacao);
}

function fetchAndDisplayUsuarios() {
    const usuariosTableBody = document.getElementById('usuarios-table-body');

    const xhr = new XMLHttpRequest();
    xhr.open('GET', '/usuarios/get/', true);

    xhr.onload = function () {
        if (xhr.status === 200) {
            const data = JSON.parse(xhr.responseText);
            usuariosTableBody.innerHTML = '';


            data.forEach(usuario => {
                const row = document.createElement('tr');
                const idCell = document.createElement('td');
                const nomeCell = document.createElement('td');
                const emailCell = document.createElement('td');
                const documentoCell = document.createElement('td');
                const dataCriacaoCell = document.createElement('td');
                const statusCell = document.createElement('td');
                const staffCell = document.createElement('td');
                const ecopontoCell = document.createElement('td');
                const editCell = document.createElement('td');
                const deleteCell = document.createElement('td');

                const editLink = createLink(`editar/${usuario.id}`, 'glyphicon glyphicon-edit')
                const deleteLink = createLink(`delete-confirm/${usuario.id}`, 'glyphicon glyphicon-trash',)

                let status = switchStatusResult(usuario.is_active);
                let staff = switchStaffResult(usuario.is_staff);

                idCell.textContent = usuario.id;
                nomeCell.textContent = usuario.name;
                emailCell.textContent = usuario.email;
                documentoCell.textContent = usuario.document;
                dataCriacaoCell.textContent = dateFormat(usuario.date_joined);
                statusCell.textContent = status;
                staffCell.textContent = staff;
                ecopontoCell.textContent = usuario.ecoponto;

                editCell.appendChild(editLink)
                deleteCell.appendChild(deleteLink)

                row.appendChild(idCell);
                row.appendChild(nomeCell);
                row.appendChild(emailCell);
                row.appendChild(documentoCell);
                row.appendChild(dataCriacaoCell);
                row.appendChild(statusCell);
                row.appendChild(staffCell);
                row.appendChild(ecopontoCell);
                row.appendChild(editCell);
                row.appendChild(deleteCell);

                usuariosTableBody.appendChild(row);
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

function switchStaffResult(is_staff) {
    console.log(is_staff)
    if (is_staff) {
        return "SIM"
    }
    return "NÃO"
}

function switchStatusResult(is_active) {
    if (is_active) {
        return "ATIVA"
    }
    return "INATIVA"
}

function createLink(href, classe, id) {
    const link = document.createElement('a');

    link.href = href;

    link.id = id

    link.className = classe;

    return link;
}

fetchAndDisplayUsuarios();

function saveForm(event) {
    event.preventDefault();

    const form = document.getElementById('usuarios-save-form');
    const formData = new FormData(form);
    formData.get('is_staff')
    const cookie = getCookie('csrftoken')

    fetch('/usuarios/save/', {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json',
            'X-CSRFToken': cookie,
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

const form = document.getElementById('usuarios-save-form');
form.addEventListener('submit', saveForm);

function getCookie(name) {
    const cookieValue = document.cookie.match('(^|;)\\s*' + name + '\\s*=\\s*([^;]+)');
    return cookieValue ? cookieValue.pop() : '';
}