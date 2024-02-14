"use strict";

function submit(){
    let file = document.getElementById("ppic").files[0];
    if(!file){
        console.log("No file!");
        return;
    }
    console.log(document.location);
    let R = new FileReader();
    R.addEventListener("load", () => {
        let profilepic = btoa(R.result);    //do base64 encoding
        let fname = document.getElementById("fname").value;
        let eml = document.getElementById("email").value;
        let user = document.getElementById("uname").value;
        
        let J = {
            fullName: fname,
            email: eml,
            uname: user,
            pic: profilepic
        };
        fetch( document.location.pathname,
            {   method: "POST",
                body: JSON.stringify(J)
            }
        ).then( (resp) => {
            //can also use text(), blob(), or arrayBuffer()
            resp.json().then( (J) => {
                console.log("Server said:",J);
                document.location = document.location;
            });
        }).catch( (err) => {
            console.log("Uh oh",err);
        })
    });
    R.readAsBinaryString(file);
}