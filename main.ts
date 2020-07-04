input.onButtonPressed(Button.A, function () {
    basic.showLeds(`
        . . . . .
        . # # # .
        . # # # .
        . # # # .
        . . . . .
        `)
    currentChar = "0"
    lookupChar = "" + lookupChar + currentChar
    music.playTone(880, music.beat(BeatFraction.Half))
    basic.clearScreen()
})
input.onButtonPressed(Button.AB, function () {
    basic.showIcon(IconNames.Yes)
    if (lookupChar == "") {
        message = ""
    }
    index = mcode.indexOf(lookupChar)
    currentLetter = letters[index]
    if (currentLetter == "space") {
        message = "" + message + " "
    } else {
        message = "" + message + currentLetter
    }
    lookupChar = ""
    currentChar = ""
    currentLetter = ""
    basic.showString(message)
})
input.onButtonPressed(Button.B, function () {
    basic.showLeds(`
        . . . . .
        . . . . .
        # # # # #
        # # # # #
        . . . . .
        `)
    currentChar = "1"
    lookupChar = "" + lookupChar + currentChar
    music.playTone(659, music.beat(BeatFraction.Whole))
    basic.clearScreen()
})
let currentLetter = ""
let index = 0
let lookupChar = ""
let mcode: string[] = []
let letters: string[] = []
let currentChar = ""
let message = ""
message = ""
currentChar = ""
letters = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z", "space"]
mcode = ["01", "1000", "1010", "100", "0", "0010", "110", "0000", "00", "0111", "101", "0100", "11", "10", "111", "0110", "1101", "010", "000", "1", "001", "0001", "011", "1001", "1011", "1100", "1111"]
