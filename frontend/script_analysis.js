let urlBackEnd = "http://127.0.0.1:8000";
let form = document.getElementsByClassName("form");
let idBatchG = document.getElementById("idBatchG");
let idBikeG = document.getElementById("idBikeG");
let result = document.getElementsByClassName("result")[0];



function toggleForm(id) {
  if (id == 0) {
    form[1].classList.add("formHide");
  }
  else {
    form[0].classList.add("formHide");
  }
  form[id].classList.toggle("formHide");
}


function getChart(parameter) {
  let createChart = {
    "total": "false",
    "idBatch": "false",
    "idBike": 0
  }

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
  // Gestione della richiesta Post
  result.innerHTML = "<div class='loader'></div>";



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
      form[0].classList.add("formHide");
      form[1].classList.add("formHide");

      result.innerHTML = '<img src="' + urlBackEnd + "/" + data["path"] + '" alt="chart">';


    })
    .catch(error => {
      result.innerHTML = "<h2>Connection Error<h2>";
    });

};






