// This function will be used later in the project.

// getTime(t): helper function that adds a "0" in front of a number t
// if t is less than 10 to make it look like an actual clock timer
function getTime(t) {
    if (t >= 10) { return t; }
    else { return "0" + t; }
}

// dynamicClock(): function that dynamically places a clock on a webpage
function dynamicClock() {
    var today = new Date();
    var hours = today.getHours() % 12;
    if ( hours == 0) { hours = 12; }
    var mins = today.getMinutes();
    var secs = today.getSeconds();
    var timeString = getTime(hours) + ":" + getTime(mins) + ":" + getTime(secs);
    document.getElementById('txt').innerHTML = timeString;
    var theTime = setTimeout(dynamicClock, 500);
}
