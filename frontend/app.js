async function cargarServidores() {

    const tabla = document.getElementById("servidores");
    const mensaje = document.getElementById("mensaje");

    try {

        const respuesta = await fetch("/servidores/");

        if (!respuesta.ok) {
            throw new Error(`Error HTTP: ${respuesta.status}`);
        }

        const servidores = await respuesta.json();

        tabla.replaceChildren();

        for (const servidor of servidores) {

            const fila = document.createElement("tr");

            for (const valor of [
                servidor.nombre,
                servidor.cpu,
                servidor.ram,
                servidor.estado
            ]) {

                const celda = document.createElement("td");

                celda.textContent = valor;

                fila.appendChild(celda);
            }

            fila.lastElementChild.className =
                servidor.estado === "activo"
                    ? "activo"
                    : "inactivo";

            tabla.appendChild(fila);
        }

        mensaje.textContent = "";

    } catch (error) {

        mensaje.textContent = error.message;
    }
}


document
    .getElementById("actualizar")
    .addEventListener("click", cargarServidores);


cargarServidores();