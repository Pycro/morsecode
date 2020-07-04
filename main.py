def on_button_pressed_a():
    global currentChar, lookupChar
    basic.show_leds("""
        . . . . .
        . # # # .
        . # # # .
        . # # # .
        . . . . .
        """)
    currentChar = "0"
    lookupChar = "" + lookupChar + currentChar
    music.play_tone(880, music.beat(BeatFraction.HALF))
    basic.clear_screen()
input.on_button_pressed(Button.A, on_button_pressed_a)

def on_button_pressed_ab():
    global index, currentLetter, message, lookupChar, currentChar
    basic.show_icon(IconNames.YES)
    if lookupChar == "":
        radio.send_string("" + (message))
    else:
        index = mcode.index(lookupChar)
        currentLetter = letters[index]
        if currentLetter == "space":
            message = "" + message + " "
        else:
            message = "" + message + currentLetter
        lookupChar = ""
        currentChar = ""
        currentLetter = ""
        basic.show_string("" + (message))
input.on_button_pressed(Button.AB, on_button_pressed_ab)

def on_received_string(receivedString):
    global message
    basic.show_string(receivedString)
    basic.pause(5000)
    message = ""
radio.on_received_string(on_received_string)

def on_button_pressed_b():
    global currentChar, lookupChar
    basic.show_leds("""
        . . . . .
        . . . . .
        # # # # #
        # # # # #
        . . . . .
        """)
    currentChar = "1"
    lookupChar = "" + lookupChar + currentChar
    music.play_tone(659, music.beat(BeatFraction.WHOLE))
    basic.clear_screen()
input.on_button_pressed(Button.B, on_button_pressed_b)

currentLetter = ""
index = 0
mcode: List[str] = []
letters: List[str] = []
lookupChar = ""
currentChar = ""
message = ""
radio.set_group(1)
message = ""
currentChar = ""
lookupChar = ""
letters = ["a",
    "b",
    "c",
    "d",
    "e",
    "f",
    "g",
    "h",
    "i",
    "j",
    "k",
    "l",
    "m",
    "n",
    "o",
    "p",
    "q",
    "r",
    "s",
    "t",
    "u",
    "v",
    "w",
    "x",
    "y",
    "z",
    "space"]
mcode = ["01",
    "1000",
    "1010",
    "100",
    "0",
    "0010",
    "110",
    "0000",
    "00",
    "0111",
    "101",
    "0100",
    "11",
    "10",
    "111",
    "0110",
    "1101",
    "010",
    "000",
    "1",
    "001",
    "0001",
    "011",
    "1001",
    "1011",
    "1100",
    "1111"]