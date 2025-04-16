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
let rowsPageTag = document.getElementById("rowsPage");
let currentPageTag = document.getElementById("currentPage");
let totalPageTag = document.getElementById("totalPage");
let dataApi = "";
let outPagination = "";

// Funzione per la creazione della tabella in cui inserirò i dati delle bici prodotte
function createTable(data) {

  // Creazione della tabella in cui inserirò i dati dei task
  let html = "<table ><tr><th>ID_Bike</th><th>Description Bike</th><th>ID Task</th><th>Task Description</th><th>Min Time</th><th>Max Time</th></tr>";

  for (const [key, value] of Object.entries(data)) {
    html += "<tr><td>" + value[0] + "</td><td>" + value[1] + "</td><td>" + value[2] + "</td><td>" + value[3] + "</td><td>" + value[4] + " Minutes</td><td>" + value[5] + " Minutes</td></tr>";
  };
  html += "</table>";

  // Inserimento della tabella nell'html
  result.innerHTML = html;
};

// Funzione che esegue la paginazione
function pagination(elements, currentPag) {
  // Se non specificato considero di essere alla pagina numero 1
  let pag = currentPag || 1;
  // Numero di elementi per pagina
  let elemPag = 14;
  // Calcolo l'offset di spostamento della "finestra" di elementi che voglio restituire
  let offset = (pag - 1) * elemPag;
  // Estraggo la porzione di oggetti che mi interessa
  let elemPagin = elements.slice(offset).slice(0, elemPag);
  // Calcolo il numero totale di pagine
  let totalPag = Math.ceil(elements.length / elemPag);

  // Restituisco un oggetto contenente la porzione paginata e tutte le informazioni necessarie alla navigazione
  return {
    currentPage: pag,
    previousPage: pag - 1 ? pag - 1 : null,
    nextPage: totalPag > pag ? pag + 1 : null,
    totalPag: totalPag,
    elemPagin: elemPagin
  };
};

// Funzione di gestione della visualizzazione dei dati
function dataManag(data, pag) {
  // Salvo i dati nella variabile globale per poterli riutilizzare in seguito
  dataApi = data;

  // Chiamo la funzione di paginazione per suddividerli
  outPagination = pagination(data, pag);

  // Salvo nella variabile data solo gli elementi della prima pagina
  data = outPagination.elemPagin;

  // Con questi elementi vado a creare la tabella visualizzata
  createTable(data);

  // Popolo gli elementi di navigazione per visualizzare il totale delle pagine, la paginacorrente e le righe per pagina 
  totalPageTag.innerText = outPagination.totalPag;
  currentPageTag.innerText = outPagination.currentPage;
  rowsPageTag.innerText = data.length;
};

// Funzione che effettua effettivamente la navigazione tra le pagine
function navPage(choice) {
  // Se viene passato il valore 0 il pulsante cliccato è Previous e quindi si vogliono vedere i dati della pagina precedente
  if (choice === 0) {
    if (outPagination.previousPage) {
      dataManag(dataApi, outPagination.previousPage);
    }
  }
  // Altrimenti il pulsante cliccato è Next e quindi si vogliono vedere i dati della pagina successiva
  else {
    if (outPagination.nextPage) {
      dataManag(dataApi, outPagination.nextPage);
    }
  };
};

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

      // Passo i dati alla funzione per gestirne la visualizzazione
      dataManag(data);

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
  };
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
        getTask();
        // Nascondo il form di input
        form[0].classList.toggle("formHide");

      })
      .catch(error => {

        //In caso di errori inserisco nell'html un messaggio di errore
        result.innerHTML = "<h2>Connection Error<h2>";
      });
  };
};

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

        // Passo i dati alla funzione per gestirne la visualizzazione
        dataManag(data);

        // Nascondo il form di input
        form[1].classList.toggle("formHide");
      })
      .catch(error => {
        //In caso di errori inserisco nell'html un messaggio di errore
        result.innerHTML = "<h2>Connection Error<h2>";
      });
  };
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

        // Passo i dati alla funzione per gestirne la visualizzazione
        dataManag(data);
        // Nascondo il form di input
        form[2].classList.toggle("formHide");
      })
      .catch(error => {
        //In caso di errori inserisco nell'html un messaggio di errore
        result.innerHTML = "<h2>Connection Error<h2>";
      });
  };
};
