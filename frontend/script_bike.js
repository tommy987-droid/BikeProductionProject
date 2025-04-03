let urlBackEnd = "http://127.0.0.1:8000";
let form = document.getElementsByClassName("form")[0];
let result = document.getElementsByClassName("result")[0];

let idBike = document.getElementById("idBike");
let descBike = document.getElementById("desc");
let dfCoe = document.getElementById("dfCoe");

function getBike() {
  result.innerHTML = "<div class='loader'></div>";
    const urlGetBike = urlBackEnd + '/bike'
    // Gestione della richiesta GET
    fetch(urlGetBike)
        .then(response => {
            if (!response.ok) {
                throw new Error('Network response was not ok');
            }
            return response.json();
        })
        .then(data => {
            

            let html = "<table ><tr><th>ID_Type</th><th>Description</th><th>Defect_Coefficient</th></tr>";
            for (const [key, value] of Object.entries(data)) {


                html += "<tr><td>" + value[0] + "</td><td>" + value[1] + "</td><td>" + value[2] + "</td></tr>";
            }
            html += "</table>"
            result.innerHTML = html;
        })
        .catch(error => {
          result.innerHTML = "<h2>Connection Error<h2>";
        });
}
getBike()
function toggleForm() {

    form.classList.toggle("formHide");
}

function editBike() {
    let idBikeV = idBike.value;
    idBike.value =""
    let descBikeV = descBike.value;
    descBike.value =""
    let dfCoeV = dfCoe.value;
    dfCoe.value =""
    if (idBikeV === "" || descBikeV === "" || dfCoeV===""){
        window.alert("ERROR - ID, Description e Defect Coef Required");
    }else{
    let bikeEdit ={
        id: idBikeV,
        desc: descBikeV,
        defCoef :dfCoeV}
    const urlEditBike = urlBackEnd + '/edit-bike/'
    // Gestione della richiesta Post
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
        
        window.alert(data);
      getBike()
    })
    .catch(error => {
      result.innerHTML = "<h2>Connection Error<h2>";
    });
}
scroll(0, 0);
toggleForm()
}