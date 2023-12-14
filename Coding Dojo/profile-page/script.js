console.log("page loaded...");

var requestSpan = document.querySelector("#requests");
var connectionSpan = document.querySelector("#connections");

var username = document.querySelector("#username");


function accept(id){
    var element = document.querySelector(id);
    element.remove();
    requestSpan.innerText--;
    connectionSpan.innText++;
}

function ignore(id){
    var element = document.querySelector(id);
    element.remove();
    requestSpan.innerText--;

}

function edit(){
    username.innerText = "nigga"
}