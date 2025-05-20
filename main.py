
def on_button_pressed_a():
    global hour, hourstring
    hour += 1
    if hour < 10:
        hourstring = "" + str((0 + hour))
    else:
        hourstring = "" + str(hour)
input.on_button_pressed(Button.A, on_button_pressed_a)

def on_button_pressed_b():
    global minute, minutestring
    minute += 1
    if minute < 10:
        minutestring = "" + str((0 + minute))
    else:
        minutestring = "" + str(minute)
input.on_button_pressed(Button.B, on_button_pressed_b)

minute = 0
hour = 0
hourstring = ""
minutestring = ""
hourstring = "00"
hour = 0
minutestring = "00"
minute = 0
basic.show_string("" + hourstring + ":" + minutestring, 50)

def on_forever():
    global minute, minutestring, hour, hourstring
    minute += 1
    if input.button_is_pressed(Button.A) or input.button_is_pressed(Button.B):
        pass
    elif minute < 10:
        minutestring = "" + str((0 + hour))
    elif minute == 60:
        minutestring = "00"
        minute = 0
        hour += 1
        if hour < 10:
            hourstring = "" + str((0 + hour))
        else:
            hourstring = "" + str(hour)
    elif hourstring > "23":
        hourstring = "00"
        hour = 0
        minutestring = "00"
        minute = 0
        basic.show_string("" + hourstring + ":" + minutestring, 50)
    else:
        minutestring = "" + str(minute)
    basic.show_string("" + hourstring + ":" + minutestring, 50)
basic.forever(on_forever)
