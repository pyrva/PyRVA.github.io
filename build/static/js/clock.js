function showTime(){
    document.getElementById("clock").innerText = (new Date()).toLocaleTimeString('en-US');
    setTimeout(showTime, 1000);
}

showTime();
