//NOT WORKING, THIS CODE IS ALREDY ININDEXT.HTML
//CODE IS ALSO WRONG

const url = document.getElementById("url");
const email = document.getElementById("email");
const key = document.getElementById("key");
const submitBtn = document.getElementById("submit");
const num_top_comments = document.getElementById("num_top_comments");
const sens_vadar = document.getElementById("sens_vadar");
const sens_rake = document.getElementById("sens_rake");
var reqID = 0;

const db = firebase.database();
const rootRef = db.ref('requests');

submitBtn.addEventListener('click', (e) => {
    e.preventDefault();
    rootRef.child(reqID.value).set({
        url: url.value,
        email: email.value,
        key: key.value,
        num_top_comments: num_top_comments.value,
        sens_vadar: sens_vadar.value,
        sens_rake: sens_rake.value
    })
    reqID++;

});

// function SubmitData() {
    // set(ref(db, "URLs/"+ enterURL.value),{
    //     URL: enterURL.value
    //     //Name: enterName.value,
    //     //ID: enterID.value,
    //     //Age: enterAge.value
    // })
    // .then(()=>{
    //     alert("Data added successfully");
    // })
    // .catch((error)=>{
    //     alert(error);
    // });

// }

// function FindData() {
//     const dbref = ref(db);

//     get(child(dbref, "People/" + findID.value))
//     .then((snapshot)=>{
//         if(snapshot.exists()){
//             findName.innerHTML = "Name: " + snapshot.val().Name;
//             findAge.innerHTML = "Age: " + snapshot.val().Age;
//         } else {
//             alert("No data found");
//         }
//     })
//     .catch((error)=>{
//         alert(error)
//     })
    
// }

// function UpdateData(){
//     update(ref(db, "People/"+ enterID.value),{
//         Name: enterName.value,
//         Age: enterAge.value
//     })
//     .then(()=>{
//         alert("Data updated successfully");
//     })
//     .catch((error)=>{
//         alert(error);
//     });
// }

// function RemoveData(){
//     remove(ref(db, "People/"+ enterID.value))
//     .then(()=>{
//         alert("Data deleted successfully");
//     })
//     .catch((error)=>{
//         alert(error);
//     });
// }

submitBtn.addEventListener('click', SubmitData);
