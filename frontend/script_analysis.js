//Variabile che contiene l'url del backend
let urlBackEnd = "http://127.0.0.1:8000";

//Variabili per l'utilizzo dei valori di imput
let form = document.getElementsByClassName("form");
let idBatchG = document.getElementById("idBatchG");
let idBikeG = document.getElementById("idBikeG");
let result = document.getElementsByClassName("result")[0];

//Funzione per nascondere i form in base al click del bottone
function toggleForm(id) {
  if (id == 0) {
    form[1].classList.add("formHide");
  }
  else {
    form[0].classList.add("formHide");
  }
  form[id].classList.toggle("formHide");
}

//Funzione che fa una chiamata POST per visualizzare i grafici
function getChart(parameter) {
  
  //Creo l'oggetto con valori preimpostati
  let createChart = {
    "total": "false",
    "idBatch": "false",
    "idBike": 0
  }
  
  //In base al tipo di grafico che voglio creare popolo i parametri 
  if (parameter === 0) {
    createChart["total"] = "true";
  } else if (parameter === 1) {
    let idBatchGV = idBatchG.value;
    idBatchG.value = "";
    if (idBatchGV === "") {
      window.alert("ERROR - ID Batch Required");
      return false;
    }
    else {
      createChart["idBatch"] = idBatchGV;
    }
  } else if (parameter === 2) {
    let idBikeGV = idBikeG.value;
    idBikeG.value = "";
    if (idBikeGV === "") {
      window.alert("ERROR - ID Bike Required");
      return false;
    }
    else {
      createChart["idBike"] = idBikeGV;
    }
  }

  const urlCreateChart = urlBackEnd + '/create-chart/'

  // Lancio il loader in attesa dei dati
  result.innerHTML = "<div class='loader'></div>";

  // Gestione della richiesta Post
  fetch(urlCreateChart, {
    method: 'POST',
    headers: {
      'Content-Type': 'application/json;charset=utf-8'
    },
    body: JSON.stringify(createChart)
  })
    .then(response => {
      if (!response.ok) {
        throw new Error('Network response was not ok');
      }
      return response.json();
    })
    .then(data => {
      //Nascondo i form qualora fossero aperti
      form[0].classList.add("formHide");
      form[1].classList.add("formHide");

      //Se non ho errori nella richiesta, inserisco nell'html la path del grafico creato
      result.innerHTML = '<img src="' + urlBackEnd + "/" + data["path"] + '" alt="chart">';

    })
    .catch(error => {
      //In caso di errori inserisco nell'html un messaggio di errore
      result.innerHTML = "<h2>Connection Error<h2>";
    });

};






