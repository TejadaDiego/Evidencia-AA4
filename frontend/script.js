const tabla = document.getElementById("tabla");

tabla.innerHTML = "";

fetch("http://localhost:5000/estaciones")

  .then(response => response.json())

  .then(data => {

    let contador = 1;

    data.forEach(item => {

      tabla.innerHTML += `
        <tr>
          <td>${contador++}</td>
          <td>${item.estacion_salida}</td>
          <td>${item.total_pasajeros}</td>
        </tr>
      `;

    });

  })

  .catch(error => {

    console.error(error);

    tabla.innerHTML = `
      <tr>
        <td colspan="3">
          Error cargando datos
        </td>
      </tr>
    `;

  });