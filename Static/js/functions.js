function getCookie(name) {
    var cookieValue = null;
    if (document.cookie && document.cookie !== '') {
        var cookies = document.cookie.split(';');
        for (var i = 0; i < cookies.length; i++) {
            var cookie = jQuery.trim(cookies[i]);
            if (cookie.substring(0, name.length + 1) === (name + '=')) {
                cookieValue = decodeURIComponent(cookie.substring(name.length + 1));
                break;
            }
        }
    }
    return cookieValue;
}

addQuestion = () =>{
    let contenido = document.getElementById("contenido").value;
    let descripcion = document.getElementById("descripcion").value;
    let categoria = document.getElementById("categoria").value;
    // console.log(categoria)
    if(categoria == 0 || contenido == "" || descripcion == "")
        alert("Llena todos los campos")
    else{
        let formData = new FormData();

        formData.append("csrfmiddlewaretoken", getCookie("csrftoken"));
        formData.append("contenido", contenido);
        formData.append("descripcion", descripcion);
        formData.append("categoria", categoria);

        $.ajax({
            type: "POST",
            url: "http://127.0.0.1:8000/preguntas/addquestionurl",
            data: formData,
            processData : false,
            contentType: false,
            success: data => {
                    alert("Tu pregunta se ha publicado exitosamente");
                    redirectHome();
            },
            error: data => {
                    alert("Ha habido un problema publicando tu pregunta :C, intenta denuevo");
            }
        })
    }
}

addAnswwer = () =>{
    let idQuestion = document.getElementById("question").dataset.idquestion;
    let contenido = document.getElementById("contenidoAns").value;

    if(contenido == null)
        alert('No puedes dejar el campo de tu respuesta vacio');
    else{
        let formData = new FormData();

        formData.append("csrfmiddlewaretoken", getCookie("csrftoken"));
        formData.append("contenido", contenido);
        formData.append("idQuestion", idQuestion);
        $.ajax({
            type: 'POST',
            url: 'http://127.0.0.1:8000/preguntas/addanswersurl',
            data: formData,
            processData : false,
            contentType: false,
            success: data => {
                alert("Tu respuesta se ha publicado exitosamente");
                redirectQuestion();
            },
            error: data => {
                alert("Ha habido un problema publicando tu respuesta :C, intenta denuevo");
            }
        })
    }
}

editQuestion = () =>{
    let contenido = document.getElementById("contenido").value;
    let descripcion = document.getElementById("descripcion").value;
    let categoria = document.getElementById("categoriasAnswers").value;
    let idQuestion = document.getElementById("question").dataset.idquestion;

    if(categoria == 0 || contenido == "" || descripcion == "")
        alert("No dejes ningún campo sin llenar antes de guardar cambios")
    else{
        let formData = new FormData();

        formData.append("csrfmiddlewaretoken", getCookie("csrftoken"));
        formData.append("contenido", contenido);
        formData.append("descripcion", descripcion);
        formData.append("categoria", categoria);
        formData.append("idQuestion", idQuestion);

        $.ajax({
            type: "POST",
            url: "http://127.0.0.1:8000/preguntas/editquestionsurl",
            data: formData,
            processData : false,
            contentType: false,
            success: data => {
                    alert("Tu pregunta se ha editado exitosamente");
                    redirectQuestion();
            },
            error: data => {
                    alert("Ha habido un problema editando tu pregunta :C, intenta denuevo");
            }
        })
    }
}

deleteQuestion = () =>{
    let idQuestion = document.getElementById("question").dataset.idquestion;
    let formData = new FormData();
    formData.append("csrfmiddlewaretoken", getCookie("csrftoken"));
    formData.append('idQuestion', idQuestion)

    $.ajax({
        type: 'POST',
        url: 'http://127.0.0.1:8000/preguntas/deletequestion',
        data: formData,
        processData : false,
        contentType: false,
        success: data => {
            alert("Tu pregunta se ha eliminado exitosamente");
            window.location.replace('http://127.0.0.1:8000/preguntas/home');
        },
        error: data => {
            alert("Ha habido un problema eliminando tu pregunta :C, intenta denuevo, al mismo tiempo, piensa si de verdad quieres eliminar esta pregunta");
        }
    })
}

editAnswer = (element) =>{
    let idAnswer = element.dataset.idanswer;
    let divPadre = element.parentNode;
    let divContenido = divPadre.children;
    let contenido = divContenido[0].value;
    if(contenido == "")
        alert("No puedes dejar la respuesta vacia");
    else{
        let formData = new FormData();

        formData.append("csrfmiddlewaretoken", getCookie("csrftoken"));
        formData.append("contenido", contenido);
        formData.append("idAnswer", idAnswer);
        $.ajax({
            type: 'POST',
            url: 'http://127.0.0.1:8000/preguntas/editanswer',
            data: formData,
            processData : false,
            contentType: false,
            success: data => {
                alert("Tu respuesta se ha actualizado exitosamente");
                redirectQuestion();
            },
            error: data => {
                alert("Ha habido un problema actualizando tu respuesta :C, intenta denuevo");
            }
        })
    }
}

deleteAnswer = (element) =>{
    let idAnswer = element.dataset.idanswer;
    let formData = new FormData();
    formData.append("csrfmiddlewaretoken", getCookie("csrftoken"));
    formData.append("idAnswer", idAnswer);
    $.ajax({
        type: 'POST',
        url: 'http://127.0.0.1:8000/preguntas/deleteanswer',
        data : formData,
        processData : false,
        contentType: false,
        success: data => {
            alert("Tu respuesta se ha eliminado exitosamente");
            redirectQuestion();
        },
        error: data => {
            alert("Ha habido un problema eliminando tu respuesta :C, intenta denuevo, o puedes reconsiderar si enverdad quieres borrarla :D");
        }
    })

}

updateInfo = () =>{
    let username = document.getElementById("username").value;
    let nombres = document.getElementById("nombres").value;
    let apellidos = document.getElementById("apellidos").value;
    let correo = document.getElementById("email").value;
    let foto = document.getElementById("foto");

    let emailRegex = /^(([^<>()[\]\.,;:\s@\"]+(\.[^<>()[\]\.,;:\s@\"]+)*)|(\".+\"))@(([^<>()[\]\.,;:\s@\"]+\.)+[^<>()[\]\.,;:\s@\"]{2,})$/i;

    let formData = new FormData();

    if(username == "" || nombres=="" || apellidos=="" || correo=="")
        alert("No puede quedar ningun campo vacio")
    else if(username.length<4)
        alert("El nombre de usuario debe tener almenos 4 caracteres");
    else if(!emailRegex.test(correo)){
        alert("Correo no valido")
    }
    else{
        formData.append("csrfmiddlewaretoken", getCookie("csrftoken"));
        formData.append('username', username);
        formData.append('nombres', nombres);
        formData.append('apellidos', apellidos);
        formData.append('correo', correo);
        formData.append('foto', foto.files[0]);

        $.ajax({
            type: 'POST',
            url: 'http://127.0.0.1:8000/preguntas/editprofile',
            data : formData,
            processData : false,
            contentType: false,
            success: data => {
                alert("Tu información se actualizó correctamente");
                window.location.reload();
            },
            error: data => {
                alert("Ha habido un problema actualizando tu perfil :C, intenta denuevo");
            }
        })
    }
}

// questionsByCategory = () =>{
//     let categoria = document.getElementById("categorias").value;
//     if (categoria==0)
//         alert("Escoja una categoria porfavor");
//     else{
//         formData = new FormData();
//         formData.append("csrfmiddlewaretoken", getCookie("csrftoken"));
//         formData.append("categoria", categoria);
//         $.ajax({
//             type: 'POST',
//             url: 'http://127.0.0.1:8000/preguntas/bycategory',
//             data : formData,
//             processData : false,
//             contentType: false,
//             }
//         )
//     }
// }
// ###########################################################################

redirectHome = () =>{
    window.location.replace("home");
}

redirectQuestion = () =>{
    let url = "http://127.0.0.1:8000/preguntas/answers/" + document.getElementById("question").dataset.idquestion;
    window.location.replace(url);
}

disabledAttrCategorias = () =>{
    document.getElementById("categorias").setAttribute("disabled", "true");
    let button = document.getElementById("categoriasButton")
    button.setAttribute("disabled", "true");
    button.style.pointerEvents = "none";
}

changeInputs = () => {
    let inputs = document.getElementsByClassName("input-profile");
    let cambios = false;
    for(let i=0; i<inputs.length-1; i++){
        inputs[i].disabled=(inputs[i].disabled)?false:true;
    }
    let button = document.getElementById("update")
    document.getElementById("cancel").style.display = "initial";
    if(inputs[0].disabled){
        //Lo se, no es la mejor forma
        window.location.reload();
    }
    else{
        document.getElementById("foto").removeAttribute("style");
        button.textContent = "Guardar cambios";
        button.removeAttribute("onclick");
        button.setAttribute("onclick", "updateInfo()");
    }
}

validateFileType = () =>{
    let filename = document.getElementById("foto").value;
    let dotIndex = filename.lastIndexOf(".")+1;
    let extFile = filename.substring(dotIndex, filename.length).toLowerCase();
    if(extFile!="jpg" && extFile!= 'jpeg' && extFile!="png")
        alert("Solo se permiten archivos jpg/jpeg/png");
}