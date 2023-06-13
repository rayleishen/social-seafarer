
// Import the functions you need from the SDKs you need
import { initializeApp } from "https://www.gstatic.com/firebasejs/9.22.2/firebase-app.js";
import { getAnalytics } from "https://www.gstatic.com/firebasejs/9.22.2/firebase-analytics.js";
// TODO: Add SDKs for Firebase products that you want to use
// https://firebase.google.com/docs/web/setup#available-libraries

var config = require("/config.json");


// Your web app's Firebase configuration
// For Firebase JS SDK v7.20.0 and later, measurementId is optional
const firebaseConfig = {
    apiKey: config.apiKey,
    authDomain: config.authDomain,
    databaseURL: config.databaseURL,
    projectId: config.projectId,
    storageBucket: config.storageBucket,
    messagingSenderId: config.messagingSenderId,
    appId: config.appId,
    measurementId: config.measurementId
};
  
// Initialize Firebase
const app = initializeApp(firebaseConfig);
const analytics = getAnalytics(app);

import {getDatabase, ref, get, set, child, update, remove}
from "https://www.gstatic.com/firebasejs/9.22.2/firebase-database.js"

//Copy and Paste the URL from near the top of the CDN you pasted in from firebase
// (the one where you imported "initializeApp" from),
//but change "firebase-app" to "firebase-database"


const db = getDatabase();

var enterID = document.querySelector("#enterID");
var enterName = document.querySelector("#enterName");
var enterAge = document.querySelector("#enterAge");
var findID = document.querySelector("#findID");
var findName = document.querySelector("#findName");
var findAge = document.querySelector("#findAge");


var insertBtn = document.querySelector("#insert");
var updateBtn = document.querySelector("#update");
var removeBtn = document.querySelector("#remove");
var findBtn = document.querySelector("#find");

function InsertData() {
    set(ref(db, "People/"+ enterID.value),{
        Name: enterName.value,
        ID: enterID.value,
        Age: enterAge.value
    })
    .then(()=>{
        alert("Data added successfully");
    })
    .catch((error)=>{
        alert(error);
    });
}

function FindData() {
    const dbref = ref(db);

    get(child(dbref, "People/" + findID.value))
    .then((snapshot)=>{
        if(snapshot.exists()){
            findName.innerHTML = "Name: " + snapshot.val().Name;
            findAge.innerHTML = "Age: " + snapshot.val().Age;
        } else {
            alert("No data found");
        }
    })
    .catch((error)=>{
        alert(error)
    })
    
}

function UpdateData(){
    update(ref(db, "People/"+ enterID.value),{
        Name: enterName.value,
        Age: enterAge.value
    })
    .then(()=>{
        alert("Data updated successfully");
    })
    .catch((error)=>{
        alert(error);
    });
}

function RemoveData(){
    remove(ref(db, "People/"+ enterID.value))
    .then(()=>{
        alert("Data deleted successfully");
    })
    .catch((error)=>{
        alert(error);
    });
}

insertBtn.addEventListener('click', InsertData);
updateBtn.addEventListener('click', UpdateData);
removeBtn.addEventListener('click', RemoveData);
findBtn.addEventListener('click', FindData);

