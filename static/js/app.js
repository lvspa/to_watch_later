const formSend=document.getElementById('signup-form')

formSend.addEventListener('submit',action=>{
    action.preventDefault()
    const formData=new FormData(formSend);
    const data= Object.fromEntries(formData)

    fetch('/cads/',{
        method:'POST',
        headers:{
            'Content-Type': 'application/json'
        },
        body:JSON.stringify(data)
    }).then(res =>res.json()).then(data=>console.log("Everything OK..."))
})

