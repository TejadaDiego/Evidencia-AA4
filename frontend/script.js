const tabla = document.getElementById("tabla");

// consumir API
fetch("http://localhost:5000/estaciones")

    .then(response => response.json())

    .then(data => {

        tabla.innerHTML = "";

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

        console.error("Error:", error);

        tabla.innerHTML = `
            <tr>
                <td colspan="3">
                    Error cargando datos
                </td>
            </tr>
        `;
    });