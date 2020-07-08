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
    if(categoria == 0 || contenido == null || descripcion == null)
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
// ###########################################################################

redirectHome = () =>{
    window.location.replace("home");
}