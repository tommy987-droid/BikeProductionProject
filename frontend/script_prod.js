//Variabile che contiene l'url del backend
let urlBackEnd = "http://127.0.0.1:8000";

//Variabili per l'utilizzo dei valori di input e dei form
let form = document.getElementsByClassName("form");
let idBatchP = document.getElementById("idBatchP");
let idBikeP = document.getElementById("idBikeP");
let idDefectP = document.getElementById("idDefectP");
let result = document.getElementsByClassName("result")[0];
let rowsPageTag = document.getElementById("rowsPage");
let currentPageTag = document.getElementById("currentPage");
let totalPageTag = document.getElementById("totalPage");
let dataApi = "";
let outPagination = "";

// Funzione per la creazione della tabella in cui inserirò i dati delle bici prodotte
function createTable(data) {

  // Creazione della tabella in cui inserirò i dati delle bici prodotte
  let html = "<table><tr><th>ID</th><th>ID Batch</th><th>Date</th><th>ID Bike</th><th>Type Bike</th><th>Working Days</th><th>Production Time</th><th>Production Defect</th></tr>";
  for (const [key, value] of Object.entries(data)) {
    html += "<tr><td>" + value[0] + "</td><td>" + value[1] + "</td><td>" + value[2] + "</td><td>" + value[3] + "</td><td>" + value[4] + "</td><td>" + value[5] + "</td><td>" + value[6] + " Minutes</td><td>" + value[7] + "</td></tr>";
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
  let elemPag = 10;
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
    };
  }
  // Altrimenti il pulsante cliccato è Next e quindi si vogliono vedere i dati della pagina successiva
  else {
    if (outPagination.nextPage) {
      dataManag(dataApi, outPagination.nextPage);
    };
  };
};


// Funzione che fa una chiamata GET per visualizzare l'archivio delle bici prodotte
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

      // Passo i dati alla funzione per gestirne la visualizzazione
      dataManag(data);

    })
    .catch(error => {
      //In caso di errori inserisco nell'html un messaggio di errore
      result.innerHTML = "<h2>Connection Error<h2>";
    });
};

// Richiamo iniziale della funzione per visualizzare l'archivio delle bici prodotte
getProd();


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
};

//Funzione che fa una chiamata GET per filtrare la visualizzazione dell'archivio delle bici prodotte in base all'id del lotto
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

        // Passo i dati alla funzione per gestirne la visualizzazione
        dataManag(data);

        // Nascondo il form di input
        form[0].classList.toggle("formHide");
      })
      .catch(error => {
        //In caso di errori inserisco nell'html un messaggio di errore
        result.innerHTML = "<h2>Connection Error<h2>";
      });
  };
};

//Funzione che fa una chiamata GET per filtrare la visualizzazione dell'archivio delle bici prodotte in base all'id della bici
function getIdBike() {

  // Importazione valori di input e validazione
  let idBikePV = idBikeP.value;
  idBikeP.value = "";
  if (idBikePV === "") {
    window.alert("ERROR - ID Bike Required");
  } else {

    // Url per la richiesta
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

        // Passo i dati alla funzione per gestirne la visualizzazione
        dataManag(data);

        // Nascondo il form di input
        form[1].classList.toggle("formHide");
      })
      .catch(error => {
        //In caso di errori inserisco nell'html un messaggio di errore
        result.innerHTML = "<h2>Connection Error<h2>";
      });
  }
};

//Funzione che fa una chiamata GET per filtrare la visualizzazione dell'archivio delle bici prodotte in base alla difettosità
function getDefect() {

  // Importazione valori di input e validazione
  let idDefectPV = idDefectP.value;

  if (idDefectPV === "") {
    window.alert("ERROR - Defect Required");
  } else {
    // Url per la richiesta
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

