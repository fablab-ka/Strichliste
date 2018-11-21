
document.onkeyup = function (evt) {
    var bar = document.getElementById("barcode");
    if(!bar) {
        alert("No Barcode field found!");
        return;
    }
    if (evt.keyCode == 13)// Enter key pressed
    {
        document.forms[0].submit();;
    } else {
        //let key = Number(evt.key)
        //if(!isNaN(key))
        bar.value += evt.key;
    };
}