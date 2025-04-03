let urlBackEnd = "http://127.0.0.1:8000";
let form = document.getElementsByClassName("form");
let result = document.getElementsByClassName("result")[0];

let idTask = document.getElementById("idTaskT");
let idBike = document.getElementById("idBikeT");
let idBike2 = document.getElementById("idBike2T");
let idTask2 = document.getElementById("idTask2T");
let minTime = document.getElementById("minTimeT");
let maxTime = document.getElementById("maxTimeT");

function getTask() {
  result.innerHTML = "<div class='loader'></div>";
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

            let html = "<table ><tr><th>ID_Bike</th><th>Description Bike</th><th>ID Task</th><th>Task Description</th><th>Min Time</th><th>Max Time</th></tr>";
            for (const [key, value] of Object.entries(data)) {


                html += "<tr><td>" + value[0] + "</td><td>" + value[1] + "</td><td>" + value[2] + "</td><td>" + value[3] + "</td><td>" + value[4] + " Minutes</td><td>" + value[5] + " Minutes</td></tr>";
            }
            html += "</table>";
            result.innerHTML = html;
        })
        .catch(error => {
          result.innerHTML = "<h2>Connection Error<h2>";
        });
}
getTask()
function toggleForm(id) {
    if (id == 0){
      form[1].classList.add("formHide");
      form[2].classList.add("formHide");
    } else if(id == 1){
      form[0].classList.add("formHide");
      form[2].classList.add("formHide");
    } 
    else{
      form[0].classList.add("formHide");
      form[1].classList.add("formHide");
    }
    form[id].classList.toggle("formHide");
}

function editTask() {
    let idTaskV = idTask.value;
    idTask.value =""
    let idBikeV = idBike.value;
    idBike.value =""
    let minTimeV = minTime.value;
    minTime.value =""
    let maxTimeV = maxTime.value;
    maxTime.value =""
    if (idTaskV === "" || idBikeV === "" || minTimeV === "" || maxTimeV===""){
        window.alert("ERROR - ID Task, ID Bike, Min e Max Required");
    }else{
    let taskEdit ={
      idTask: idTaskV,
      idBike: idBikeV,
      min: minTimeV,
      max :maxTimeV
      }
    const urlEditTask = urlBackEnd + '/edit-task/'
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
        
        window.alert(data);
        getTask()
    })
    .catch(error => {
      result.innerHTML = "<h2>Connection Error<h2>";
    });
}
}

function getIdTask(){
  let idTask2V = idTask2.value;
    idTask2.value =""
    if (idTask2V === ""){
      window.alert("ERROR - ID Task Required");
  }else{
  const urlGet = urlBackEnd+'/task/view?idTask='+idTask2V ;

  // Gestione della richiesta GET
  fetch(urlGet)
  .then(response => {
    if (!response.ok) {
        throw new Error('Network response was not ok');
    }
    return response.json();
})
.then(data => {
   

    let html = "<table ><tr><th>ID_Bike</th><th>Description Bike</th><th>ID Task</th><th>Task Description</th><th>Min Time</th><th>Max Time</th></tr>";
    for (const [key, value] of Object.entries(data)) {


        html += "<tr><td>" + value[0] + "</td><td>" + value[1] + "</td><td>" + value[2] + "</td><td>" + value[3] + "</td><td>" + value[4] + "</td><td>" + value[5] + "</td></tr>";
    }
    html += "</table>"
    result.innerHTML = html;
    form[1].classList.toggle("formHide");
})
.catch(error => {
  result.innerHTML = "<h2>Connection Error<h2>";
});
  }
};
function getIdBike(){
  let idBike2V = idBike2.value;
  idBike2.value =""
    if (idBike2V === ""){
      window.alert("ERROR - ID Bike Required");
  }else{
  const urlGet = urlBackEnd+'/task/view?idBike='+idBike2V ;

  // Gestione della richiesta GET
  fetch(urlGet)
  .then(response => {
    if (!response.ok) {
        throw new Error('Network response was not ok');
    }
    return response.json();
})
.then(data => {
    

    let html = "<table ><tr><th>ID_Bike</th><th>Description Bike</th><th>ID Task</th><th>Task Description</th><th>Min Time</th><th>Max Time</th></tr>";
    for (const [key, value] of Object.entries(data)) {


        html += "<tr><td>" + value[0] + "</td><td>" + value[1] + "</td><td>" + value[2] + "</td><td>" + value[3] + "</td><td>" + value[4] + "</td><td>" + value[5] + "</td></tr>";
    }
    html += "</table>"
    result.innerHTML = html;
    form[2].classList.toggle("formHide");
})
.catch(error => {
  result.innerHTML = "<h2>Connection Error<h2>";
});
  }
};
