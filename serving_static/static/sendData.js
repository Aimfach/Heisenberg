function sendData(){
    data = {
        power: document.getElementById("speed").value,
        horn: "on",
        light: "on"
    }
    $.ajax({
        url: '/',
        type: 'POST',
        data: data,
        success: function(msg) {
            console.log("Post send")
        }
    });

    console.log(data)
}
//$('#submit').click(function() {
//todo schön machen
//todo machen das es einen startknopf gibt
// werden dann die lichter initialisiert
//todo ajax runterladen für den pi
//todo lässige beschleunigung
//});