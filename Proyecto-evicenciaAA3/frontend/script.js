const tabla = document.getElementById("tabla");

// Limpiar tabla
tabla.innerHTML = "";

// Consumir API
fetch("http://localhost:5000/estaciones")
  .then(response => response.json())
  .then(data => {

    let contador = 1;

    data.forEach(item => {
      tabla.innerHTML += `
        <tr>
            <td>${contador++}</td>
            <td>${item.estacion_salida}</td>
            <td>-</td>
            <td>${item.count}</td>
        </tr>
      `;
    });

  })
  .catch(error => {
    console.error("Error:", error);
  });