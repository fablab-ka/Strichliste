
document.onkeyup = function (evt) {
    var bar = document.getElementById("barcode");
    var regex = new RegExp("^[a-zA-Z0-9]+$");

    if(!bar) {
        alert("No Barcode field found!");
        return;
    }
    if (evt.keyCode == 13)// Enter key pressed
    {
        document.forms[0].submit();;
    } else if(evt.keyCode >= 49 && evt.keyCode <= 90){
        //let key = Number(evt.key)
        //if(!isNaN(key))
        bar.value += evt.key.toLowerCase();
    };
}