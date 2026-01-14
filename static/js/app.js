
    function cadsUser(){
        const formSend=document.getElementById('signup-form')

        formSend.addEventListener('submit',action=>{
            action.preventDefault()
            const formData=new FormData(formSend);
            const data= Object.fromEntries(formData)

            fetch('/cadastro/',{
                method:'POST',
                headers:{
                    'Content-Type': 'application/json',
                    'X-CSRFToken': getCsrfToken()
                },
                body:JSON.stringify(data)
            }).then(res =>res.json()).then(data=>{
                if(data.success){
                    window.location.href = data.redirect_url;
                }
                else{
                    console.log("Erros recebidos:", data.errors);
                }
                 if (data.errors && data.errors.password) {
                    const erroSenha = data.errors.password[0];
                    document.getElementById('password').textContent = erroSenha;
                    document.getElementById('password').style.display = 'block';
                }
                 if (data.errors && data.errors.confirm_password) {
                    const erroConfirm = data.errors.confirm_password[0];
                    document.getElementById('confirm_password').textContent = erroConfirm;
                    document.getElementById('confirm_password').style.display = 'block';
                }
                 if (data.errors && data.errors.username) {
                    const erroUser = data.errors.username[0];
                    document.getElementById('username').textContent = erroUser;
                    document.getElementById('username').style.display = 'block';
                }
                 if (data.errors && data.errors.email) {
                    const erroEmail = data.errors.email[0];
                    document.getElementById('email').textContent = erroEmail;
                    document.getElementById('email').style.display = 'block';
                }
                 //if (data.errors && data.errors.username) {
                   // const erroCnpj = data.errors.cnpj[0];
                   // document.getElementById('username-error').textContent = erroCnpj;
                    //document.getElementById('username-error').style.display = 'block';
               // }
            })
                .catch(error => {
            console.error('Erro na requisição:', error);
        });
        })
        function getCsrfToken() {
        return document.querySelector('[name=csrfmiddlewaretoken]').value;
    }
     document.addEventListener('DOMContentLoaded', cadsUser);}



