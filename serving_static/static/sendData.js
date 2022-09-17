function sendData(horn, light){
    //progressbar
    let max = document.getElementById("speed").max;
    let min = document.getElementById("speed").min;
    let valueS = document.getElementById("speed").value;
    let value = (valueS-min)/(max-min)*100
    document.getElementById("speed").style.background = 'linear-gradient(to right, #FFF 0%, #82CFD0 ' + value + '%, #fff ' + value + '%, white 100%)'


    let data = {
        power: document.getElementById("speed").value,
        horn: horn,
        light: light
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