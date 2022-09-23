function sendData(horn, light, charge){
    //progressbar
    let max = document.getElementById("speed").max;
    let min = document.getElementById("speed").min;
    let valueS = document.getElementById("speed").value;
    let value = (valueS-min)/(max-min)*100
    document.getElementById("speed").style.background = 'linear-gradient(to right, var(--backgroundObject) 0%, rgba(130, 207, 208, 1) ' + value + '%, var(--backgroundObject) ' + value + '%, var(--backgroundObject) 100%)'


    let data = {
        power: document.getElementById("speed").value,
        horn: horn,
        light: light,
        charge: charge
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