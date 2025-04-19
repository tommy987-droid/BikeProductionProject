//Variabile che contiene l'url del backend
let urlBackEnd = "http://backend:8000";

//Variabili per l'utilizzo dei valori di input e dei form
let form = document.getElementsByClassName("form")[0];
let result = document.getElementsByClassName("result")[0];
let idBike = document.getElementById("idBike");
let descBike = document.getElementById("desc");
let dfCoe = document.getElementById("dfCoe");

//Funzione che fa una chiamata GET per visualizzare il tipo di bici disponibili
function getBike() {

  // Visualizzo il loader in attesa dei dati
  result.innerHTML = "<div class='loader'></div>";

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

      // Creazione della tabella in cui inserirò i dati delle bici disponibili
      let html = "<table ><tr><th>ID_Type</th><th>Description</th><th>Defect_Coefficient</th></tr>";
      for (const [key, value] of Object.entries(data)) {

        html += "<tr><td>" + value[0] + "</td><td>" + value[1] + "</td><td>" + value[2] + "</td></tr>";
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
// Richiamo della funzione per visualizzare il tipo di bici disponibili
getBike();

//Funzione per nascondere i form in base al click del bottone
function toggleForm() {
  form.classList.toggle("formHide");
}

//Funzione che fa una chiamata POST per modificare il tipo di bici disponibili
function editBike() {

  // Importazione valori di input e validazione
  let idBikeV = idBike.value;
  idBike.value = "";
  let descBikeV = descBike.value;
  descBike.value = "";
  let dfCoeV = dfCoe.value;
  dfCoe.value = "";
  if (idBikeV === "" || descBikeV === "" || dfCoeV === "") {
    window.alert("ERROR - ID, Description e Defect Coef Required");
  } else if (idBikeV < 1 || idBikeV > 4) {
    window.alert("ERROR - ID Bike Invalid");
  } else {

    //Creo l'oggetto da inviare nel body della richiesta
    let bikeEdit = {
      id: idBikeV,
      desc: descBikeV,
      defCoef: dfCoeV
    };

    // Url per la richiesta
    const urlEditBike = urlBackEnd + '/edit-bike/';

    // Gestione della richiesta POST
    fetch(urlEditBike, {
      method: 'POST',
      headers: {
        'Content-Type': 'application/json;charset=utf-8'
      },
      body: JSON.stringify(bikeEdit)
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
        // Richiamo della funzione per aggiornare la visualizzazione del tipo di bici disponibili
        getBike();
      })
      .catch(error => {
        //In caso di errori inserisco nell'html un messaggio di errore
        result.innerHTML = "<h2>Connection Error<h2>";
      });
  }
  // Scorrimento della pagina in alto
  scroll(0, 0);

  // Nascondo il form
  toggleForm();
}