input.onButtonPressed(Button.A, function () {
    hour += 1
    if (hour < 10) {
        hourstring = "" + (0 + hour)
    } else {
        hourstring = "" + hour
    }
})
input.onButtonPressed(Button.B, function () {
    minute += 1
    if (minute < 10) {
        minutestring = "" + (0 + minute)
    } else {
        minutestring = "" + minute
    }
})
let minute = 0
let hour = 0
let hourstring = ""
let minutestring = ""
hourstring = "00"
hour = 0
minutestring = "00"
minute = 0
basic.showString("" + hourstring + ":" + minutestring, 50)
basic.forever(function () {
    minute += 1
    if (input.buttonIsPressed(Button.A) || input.buttonIsPressed(Button.B)) {
    	
    } else if (minute < 10) {
        minutestring = "" + (0 + hour)
    } else if (minute == 60) {
        minutestring = "00"
        minute = 0
        hour += 1
        if (hour < 10) {
            hourstring = "" + (0 + hour)
        } else {
            hourstring = "" + hour
        }
    } else if (hourstring > "23") {
        hourstring = "00"
        hour = 0
        minutestring = "00"
        minute = 0
        basic.showString("" + hourstring + ":" + minutestring, 50)
    } else {
        minutestring = "" + minute
    }
    console.log(minutestring)
basic.showString("" + hourstring + ":" + minutestring, 50)
})
