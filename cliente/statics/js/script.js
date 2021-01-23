function addBootstrapClass(){

    const fields = [
        document.getElementById("id_username"),
        document.getElementById("id_password"),
        document.getElementById("id_nome"),
        document.getElementById("id_endereco"),
        document.getElementById("id_telefone"),
        document.getElementById("id_data_nascimento"),
    ]

    for(let i = 0; i < fields.length; i++){
        if(fields[i] !== null) {
            console.log(fields[i].classList)
            if (fields[i].classList) fields[i].classList.add('form-control')
            else fields[i].className += 'form-control'
        }
    }
}
addBootstrapClass()