const API_CONSEJOS = "http://localhost:8000";
const API_TRADUCTOR = "http://localhost:8001";

async function obtenerConsejo() {
  try {
    const response = await fetch(`${API_CONSEJOS}/consejo`);
    const data = await response.json();
    document.getElementById("consejo-aleatorio").innerText = data.consejo;
  } catch (error) {
    console.error("Error al obtener consejo:", error);
    alert("Error al obtener el consejo");
  }
}

async function agregarConsejo() {
  const texto = document.getElementById("nuevo-consejo").value.trim();
  if (!texto) {
    alert("¡El consejo no puede estar vacío!");
    return;
  }

  try {
    const response = await fetch(`${API_CONSEJOS}/consejo`, {
      method: "POST",
      headers: { "Content-Type": "application/json" },
      body: JSON.stringify({ texto }),
    });
    const data = await response.json();
    alert(`✅ ${data.mensaje}`);
    document.getElementById("nuevo-consejo").value = "";
  } catch (error) {
    console.error("Error al agregar consejo:", error);
    alert("Error al agregar el consejo");
  }
}

async function mostrarTodosConsejos() {
  try {
    const response = await fetch(`${API_CONSEJOS}/consejos`);
    const data = await response.json();
    const lista = document.getElementById("lista-consejos");
    lista.innerHTML = "";

    for (const [indice, consejo] of Object.entries(data.consejos)) {
      const item = document.createElement("div");
      item.className = "consejo-item";
      item.innerHTML = `
                <span class="consejo-texto">${consejo}</span>
                <button onclick="eliminarConsejo(${indice})" >eliminar</button>
            `;
      lista.appendChild(item);
    }
  } catch (error) {
    console.error("Error al listar consejos:", error);
  }
}

async function eliminarConsejo(indice) {
  if (!confirm("¿Seguro que quieres eliminar este consejo?")) return;

  try {
    const response = await fetch(`${API_CONSEJOS}/consejo/${indice}`, {
      method: "DELETE",
    });
    const data = await response.json();
    alert(`🗑️ ${data.mensaje}: "${data.consejo}"`);
    mostrarTodosConsejos();
  } catch (error) {
    console.error("Error al eliminar consejo:", error);
    alert("Error al eliminar el consejo");
  }
}

async function invertirTexto() {
  const texto = document.getElementById("texto-a-invertir").value.trim();
  if (!texto) {
    alert("¡Escribe algo primero!");
    return;
  }

  try {
    const response = await fetch(
      `${API_TRADUCTOR}/invertir?texto=${encodeURIComponent(texto)}`
    );
    const data = await response.json();

    const resultado = document.getElementById("resultado-invertido");
    resultado.innerHTML = `
            <p><strong>Original:</strong> ${data.original}</p>
            <p><strong>Invertido:</strong> ${data.invertido}</p>
            <p><strong>Caracteres:</strong> ${data.longitud}</p>
        `;
  } catch (error) {
    console.error("Error al invertir texto:", error);
    alert("Error al invertir el texto");
  }
}

document.addEventListener("DOMContentLoaded", () => {});
