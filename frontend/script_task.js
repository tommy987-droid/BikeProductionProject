//Variabile che contiene l'url del backend
let urlBackEnd = "http://127.0.0.1:8000";

//Variabili per l'utilizzo dei valori di input e dei form
let form = document.getElementsByClassName("form");
let result = document.getElementsByClassName("result")[0];
let idTask = document.getElementById("idTaskT");
let idBike = document.getElementById("idBikeT");
let idBike2 = document.getElementById("idBike2T");
let idTask2 = document.getElementById("idTask2T");
let minTime = document.getElementById("minTimeT");
let maxTime = document.getElementById("maxTimeT");

//Funzione che fa una chiamata GET per visualizzare le tempistiche dei task
function getTask() {
  // Visualizzo il loader in attesa dei dati
  result.innerHTML = "<div class='loader'></div>";
  // Url per la richiesta
  const urlGetTask = urlBackEnd + '/task';

  // Gestione della richiesta GET
  fetch(urlGetTask)
    .then(response => {
      if (!response.ok) {
        throw new Error('Network response was not ok');
      }
      return response.json();
    })
    .then(data => {

      // Creazione della tabella in cui inserirò i dati dei task
      let html = "<table ><tr><th>ID_Bike</th><th>Description Bike</th><th>ID Task</th><th>Task Description</th><th>Min Time</th><th>Max Time</th></tr>";

      for (const [key, value] of Object.entries(data)) {
        html += "<tr><td>" + value[0] + "</td><td>" + value[1] + "</td><td>" + value[2] + "</td><td>" + value[3] + "</td><td>" + value[4] + " Minutes</td><td>" + value[5] + " Minutes</td></tr>";
      }
      html += "</table>";

      // Inserimento della tabella nell'html
      result.innerHTML = html;
    })
    .catch(error => {

      //In caso di errori inserisco nell'html un messaggio di errore
      result.innerHTML = "<h2>Connection Error<h2>";
    });
};

// Richiamo della funzione per visualizzare le tempistiche dei task
getTask();

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

//Funzione che fa una chiamata POST per modificare le tempistiche dei task
function editTask() {

  // Importazione valori di input e validazione
  let idTaskV = idTask.value;
  idTask.value = "";
  let idBikeV = idBike.value;
  idBike.value = "";
  let minTimeV = minTime.value;
  minTime.value = "";
  let maxTimeV = maxTime.value;
  maxTime.value = "";
  if (idTaskV === "" || idBikeV === "" || minTimeV === "" || maxTimeV === "") {
    window.alert("ERROR - ID Task, ID Bike, Min e Max Required");
  } else {

    //Creo l'oggetto da inviare nel body della richiesta
    let taskEdit = {
      idTask: idTaskV,
      idBike: idBikeV,
      min: minTimeV,
      max: maxTimeV
    };

    // Url per la richiesta
    const urlEditTask = urlBackEnd + '/edit-task/';

    // Gestione della richiesta POST
    fetch(urlEditTask, {
      method: 'POST',
      headers: {
        'Content-Type': 'application/json;charset=utf-8'
      },
      body: JSON.stringify(taskEdit)
    })
      .then(response => {
        if (!response.ok) {
          throw new Error('Network response was not ok');
        }
        return response.json();
      })
      .then(data => {
        // Alert con il numero di righe aggiornate
        window.alert(data);

        // Richiamo della funzione per aggiornare la visualizzazione delle tempistiche dei task
        getTask()
      })
      .catch(error => {

        //In caso di errori inserisco nell'html un messaggio di errore
        result.innerHTML = "<h2>Connection Error<h2>";
      });
  }
}

//Funzione che fa una chiamata GET per filtrare la visualizzazione le tempistiche dei task in base all'id del task
function getIdTask() {

  // Importazione valori di input e validazione
  let idTask2V = idTask2.value;
  idTask2.value = "";
  if (idTask2V === "") {
    window.alert("ERROR - ID Task Required");
  } else {

    // Url per la richiesta
    const urlGet = urlBackEnd + '/task/view?idTask=' + idTask2V;

    // Gestione della richiesta GET
    fetch(urlGet)
      .then(response => {
        if (!response.ok) {
          throw new Error('Network response was not ok');
        }
        return response.json();
      })
      .then(data => {

        // Creazione della tabella in cui inserirò i dati dei task filtrati
        let html = "<table ><tr><th>ID_Bike</th><th>Description Bike</th><th>ID Task</th><th>Task Description</th><th>Min Time</th><th>Max Time</th></tr>";
        for (const [key, value] of Object.entries(data)) {
          html += "<tr><td>" + value[0] + "</td><td>" + value[1] + "</td><td>" + value[2] + "</td><td>" + value[3] + "</td><td>" + value[4] + "</td><td>" + value[5] + "</td></tr>";
        }
        html += "</table>";
        // Inserimento della tabella nell'html
        result.innerHTML = html;
        // Nascondo il form di input
        form[1].classList.toggle("formHide");
      })
      .catch(error => {
        //In caso di errori inserisco nell'html un messaggio di errore
        result.innerHTML = "<h2>Connection Error<h2>";
      });
  }
};

//Funzione che fa una chiamata GET per filtrare la visualizzazione le tempistiche dei task in base all'id della bici
function getIdBike() {

  // Importazione valori di input e validazione
  let idBike2V = idBike2.value;
  idBike2.value = "";
  if (idBike2V === "") {
    window.alert("ERROR - ID Bike Required");
  } else {

    // Url per la richiesta
    const urlGet = urlBackEnd + '/task/view?idBike=' + idBike2V;

    // Gestione della richiesta GET
    fetch(urlGet)
      .then(response => {
        if (!response.ok) {
          throw new Error('Network response was not ok');
        }
        return response.json();
      })
      .then(data => {

        // Creazione della tabella in cui inserirò i dati dei task filtrati
        let html = "<table ><tr><th>ID_Bike</th><th>Description Bike</th><th>ID Task</th><th>Task Description</th><th>Min Time</th><th>Max Time</th></tr>";
        for (const [key, value] of Object.entries(data)) {

          html += "<tr><td>" + value[0] + "</td><td>" + value[1] + "</td><td>" + value[2] + "</td><td>" + value[3] + "</td><td>" + value[4] + "</td><td>" + value[5] + "</td></tr>";
        }
        html += "</table>";
        // Inserimento della tabella nell'html
        result.innerHTML = html;
        // Nascondo il form di input
        form[2].classList.toggle("formHide");
      })
      .catch(error => {
        //In caso di errori inserisco nell'html un messaggio di errore
        result.innerHTML = "<h2>Connection Error<h2>";
      });
  }
};
