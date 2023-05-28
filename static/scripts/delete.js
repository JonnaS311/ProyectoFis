var divs = document.getElementsByClassName("elemento");
function eliminar(dato) {
  // Obtener el valor del token CSRF desde las cookies
  var csrftoken = document.querySelector('[name=csrfmiddlewaretoken]').value;

  var data = {
    id: dato,
    'csrfmiddlewaretoken': csrftoken
  }; // Obtener el ID del div clickeado

  fetch('/carrito/', {
    method: 'POST',
    headers: {
      'Content-Type': 'application/json',
      'X-CSRFToken': csrftoken
    },
    body: JSON.stringify(data)
  })
    .then(function (response) {
      if (response.ok) {
        // La solicitud fue exitosa
        return response.text();
      } else {
        // Ocurrió un error en la solicitud
        throw new Error('Error en la solicitud');
      }
    })
    .then(function (responseText) {
      console.log(responseText);
    })
    .catch(function (error) {
      console.error(error);
    });
}