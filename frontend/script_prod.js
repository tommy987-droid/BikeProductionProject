//Variabile che contiene l'url del backend
let urlBackEnd = "http://127.0.0.1:8000";

//Variabili per l'utilizzo dei valori di input e dei form
let form = document.getElementsByClassName("form");
let idBatchP = document.getElementById("idBatchP");
let idBikeP = document.getElementById("idBikeP");
let idDefectP = document.getElementById("idDefectP");
let result = document.getElementsByClassName("result")[0];

//Funzione che fa una chiamata GET per visualizzare l'archivio delle bici prodotte
function getProd() {
  // Visualizzo il loader in attesa dei dati
  result.innerHTML = "<div class='loader'></div>";

  // Url per la richiesta
  const urlGetTask = urlBackEnd + '/prod';

  // Gestione della richiesta GET
  fetch(urlGetTask)
    .then(response => {
      if (!response.ok) {
        throw new Error('Network response was not ok');
      }
      return response.json();
    })
    .then(data => {

      // Creazione della tabella in cui inserirò i dati delle bici prodotte
      let html = "<table><tr><th>ID</th><th>ID Batch</th><th>Date</th><th>ID Bike</th><th>Type Bike</th><th>Working Days</th><th>Production Time</th><th>Production Defect</th></tr>";
      for (const [key, value] of Object.entries(data)) {
        html += "<tr><td>" + value[0] + "</td><td>" + value[1] + "</td><td>" + value[2] + "</td><td>" + value[3] + "</td><td>" + value[4] + "</td><td>" + value[5] + "</td><td>" + value[6] + " Minutes</td><td>" + value[7] + "</td></tr>";
      }
      html += "</table>";

      // Inserimento della tabella nell'html
      result.innerHTML = html;
    })
    .catch(error => {
      //In caso di errori inserisco nell'html un messaggio di errore
      result.innerHTML = "<h2>Connection Error<h2>";
    });
}

// Richiamo della funzione per visualizzare l'archivio delle bici prodotte
getProd()

//Funzione per nascondere i form in base al click del bottone
function toggleForm(id) {
  if (id == 0) {
    form[1].classList.add("formHide");
    form[2].classList.add("formHide");
  } else if (id == 1) {
    form[0].classList.add("formHide");
    form[2].classList.add("formHide");
  }
  else {
    form[0].classList.add("formHide");
    form[1].classList.add("formHide");
  }
  form[id].classList.toggle("formHide");
}

//Funzione che fa una chiamata GET per filtrare la visualizzare dell'archivio delle bici prodotte in base all'id del lotto
function getIdBatch() {

  // Importazione valori di input e validazione
  let idBatchPV = idBatchP.value;
  idBatchP.value = "";
  if (idBatchPV === "") {
    window.alert("ERROR - ID Batch Required");

  } else {
    // Url per la richiesta
    const urlGet = urlBackEnd + '/prod/view?idBatch=' + idBatchPV;

    // Gestione della richiesta GET
    fetch(urlGet)
      .then(response => {
        if (!response.ok) {
          throw new Error('Network response was not ok');
        }
        return response.json();
      })
      .then(data => {

        let html = "<table><tr><th>ID</th><th>ID Batch</th><th>Date</th><th>ID Bike</th><th>Type Bike</th><th>Working Days</th><th>Production Time</th><th>Production Defect</th></tr>";
        for (const [key, value] of Object.entries(data)) {
          html += "<tr><td>" + value[0] + "</td><td>" + value[1] + "</td><td>" + value[2] + "</td><td>" + value[3] + "</td><td>" + value[4] + "</td><td>" + value[5] + "</td><td>" + value[6] + " Minutes</td><td>" + value[7] + "</td></tr>";
        }
        html += "</table>";
        result.innerHTML = html;
        form[0].classList.toggle("formHide");
      })
      .catch(error => {
        result.innerHTML = "<h2>Connection Error<h2>";
      });
  }
};

function getIdBike() {
  let idBikePV = idBikeP.value;
  idBikeP.value = ""
  if (idBikePV === "") {
    window.alert("ERROR - ID Bike Required");
  } else {
    const urlGet = urlBackEnd + '/prod/view?idBike=' + idBikePV;

    // Gestione della richiesta GET
    fetch(urlGet)
      .then(response => {
        if (!response.ok) {
          throw new Error('Network response was not ok');
        }
        return response.json();
      })
      .then(data => {

        let html = "<table><tr><th>ID</th><th>ID Batch</th><th>Date</th><th>ID Bike</th><th>Type Bike</th><th>Working Days</th><th>Production Time</th><th>Production Defect</th></tr>";
        for (const [key, value] of Object.entries(data)) {
          html += "<tr><td>" + value[0] + "</td><td>" + value[1] + "</td><td>" + value[2] + "</td><td>" + value[3] + "</td><td>" + value[4] + "</td><td>" + value[5] + "</td><td>" + value[6] + " Minutes</td><td>" + value[7] + "</td></tr>";
        }
        html += "</table>";
        result.innerHTML = html;
        form[1].classList.toggle("formHide");
      })
      .catch(error => {
        result.innerHTML = "<h2>Connection Error<h2>";
      });
  }
};

function getDefect() {
  let idDefectPV = idDefectP.value;

  if (idDefectPV === "") {
    window.alert("ERROR - Defect Required");
  } else {
    const urlGet = urlBackEnd + '/prod/view?defect=' + idDefectPV;

    // Gestione della richiesta GET
    fetch(urlGet)
      .then(response => {
        if (!response.ok) {
          throw new Error('Network response was not ok');
        }
        return response.json();
      })
      .then(data => {

        let html = "<table><tr><th>ID</th><th>ID Batch</th><th>Date</th><th>ID Bike</th><th>Type Bike</th><th>Working Days</th><th>Production Time</th><th>Production Defect</th></tr>";
        for (const [key, value] of Object.entries(data)) {
          html += "<tr><td>" + value[0] + "</td><td>" + value[1] + "</td><td>" + value[2] + "</td><td>" + value[3] + "</td><td>" + value[4] + "</td><td>" + value[5] + "</td><td>" + value[6] + " Minutes</td><td>" + value[7] + "</td></tr>";
        }
        html += "</table>";
        result.innerHTML = html;
        form[2].classList.toggle("formHide");
      })
      .catch(error => {
        result.innerHTML = "<h2>Connection Error<h2>";
      });
  }
};

