//Variabile che contiene l'url del backend
let urlBackEnd = "http://127.0.0.1:8000";

//Variabili per l'utilizzo dei valori di input e dei form
let nStations = document.getElementById("nStations");
let hoursDay = document.getElementById("hoursDay");
let bike1 = document.getElementById("bike1");
let bike2 = document.getElementById("bike2");
let bike3 = document.getElementById("bike3");
let bike4 = document.getElementById("bike4");
let result = document.getElementsByClassName("result")[0];
let labelTypeB = document.getElementsByClassName("typeB");

//Funzione che fa una chiamata GET per popolare i label delle bici disponibili
function getBike() {
  // Url per la richiesta
  const urlGetBike = urlBackEnd + '/bike';

  // Gestione della richiesta GET
  fetch(urlGetBike)
    .then(response => {
      if (!response.ok) {
        throw new Error('Network response was not ok');
      }
      return response.json();
    })
    .then(data => {
      // Popolo i label con le informazioni
      for (const [key, value] of Object.entries(data)) {
        labelTypeB[value[0] - 1].innerText = value[1];
      }
    })
    .catch(error => {
      //In caso di errori inserisco nell'html un messaggio di errore
      result.innerHTML = "<h2>Connection Error<h2>";
    });
};
//Funzione per popolare label delle bici disponibili
getBike()

//Funzione per generare valori randomici per la creazione delle bici
function randomData() {
  nStations.value = Math.floor(Math.random() * 20) + 1;
  hoursDay.value = Math.floor(Math.random() * 20) + 4;
  bike1.value = Math.floor(Math.random() * 51);
  bike2.value = Math.floor(Math.random() * 51);
  bike3.value = Math.floor(Math.random() * 51);
  bike4.value = Math.floor(Math.random() * 51);

}

//Funzione che fa una chiamata GET per avviare la produzione delle bici
function startP() {

  // Importazione valori di input e validazione
  let nStationsV = nStations.value;
  nStations.value = "";
  if (nStationsV === "") {
    nStationsV = 1;
  }
  let hoursDayV = hoursDay.value;
  hoursDay.value = "";
  if (hoursDayV === "") {
    hoursDayV = 8;
  }
  let value1 = bike1.value;
  bike1.value = "";
  if (value1 === "") {
    value1 = 0;
  }
  let value2 = bike2.value;
  bike2.value = "";
  if (value2 === "") {
    value2 = 0;
  }
  let value3 = bike3.value;
  bike3.value = "";
  if (value3 === "") {
    value3 = 0;
  }

  let value4 = bike4.value;
  bike4.value = "";
  if (value4 === "") {
    value4 = 0;
  }

  // Url per la richiesta
  const urlGet = urlBackEnd + '/?nStations=' + nStationsV + '&hoursDay=' + hoursDayV + '&bike1=' + value1 + '&bike2=' + value2 + '&bike3=' + value3 + '&bike4=' + value4;

  // Gestione della richiesta GET
  fetch(urlGet)
    .then(response => {
      if (!response.ok) {
        throw new Error('Network response was not ok');
      }
      return response.json();
    })
    .then(data => {

      // Creazione della tabella in cui inserirò gli output di produzione
      let html = "<table><tr><th colspan='6'>Total Time Work</th></tr>";

      // Tempo di lavorazione totale
      html += "<tr><td colspan='6'>" + data["timeWork"] + " Minutes</th></tr>";
      html += "<tr><th>ID_Batch</th><th>Data</th><th>Working_Days</th><th>Bike</th><th>Time Product</th><th>Defect</th></tr>";

      //Singole bici prodotte
      let dataP = data["bikeMake"];
      for (const [key, value] of Object.entries(dataP)) {
        html += "<tr><td>" + value[0] + "</td><td>" + value[1] + "</td><td>" + value[2] + "</td><td>" + value[4] + "</td><td>" + value[5] + " Minutes</td><td>" + value[6] + "</td></tr>";
      }
      html += "</table>";
      // Inserimento della tabella nell'html
      result.innerHTML = html;
    })
    .catch(error => {
      //In caso di errori inserisco nell'html un messaggio di errore
      result.innerHTML = "<h2>Connection Error<h2>";
    });
  // Scorrimento della pagina in alto
  scroll(0, 0);
};

