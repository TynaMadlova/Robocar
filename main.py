def doMode():
    if uartdata == "S":
        basic.show_icon(IconNames.CONFUSED)
    elif uartdata == "T":
        basic.show_icon(IconNames.ANGRY)
    elif uartdata == "U":
        basic.show_icon(IconNames.EIGTH_NOTE)
    elif uartdata == "V":
        basic.show_leds("""
            . . . . .
            # . . . #
            # # # # #
            # . . . #
            . # # # .
        """)

def on_bluetooth_connected():
    global connected, uartdata
    basic.show_icon(IconNames.HAPPY)
    basic.pause(1000)
    connected = True
    sendDistAndSpeed()
    while connected:
        uartdata = bluetooth.uart_read_until(serial.delimiters(Delimiters.HASH))
        doMotors()
        doMode()
bluetooth.on_bluetooth_connected(on_bluetooth_connected)

def on_bluetooth_disconnected():
    global connected
    basic.show_icon(IconNames.SAD)
    connected = False
bluetooth.on_bluetooth_disconnected(on_bluetooth_disconnected)

def sendDistAndSpeed():
    pass
def doMotors():
    if uartdata == "A":
        basic.show_icon(IconNames.HOUSE)
        PCAmotor.motor_run(PCAmotor.Motors.M1, 255)
        PCAmotor.motor_run(PCAmotor.Motors.M2, 255)
    elif uartdata == "B":
        basic.show_icon(IconNames.HEART)
        PCAmotor.motor_run(PCAmotor.Motors.M1, -255)
        PCAmotor.motor_run(PCAmotor.Motors.M2, -255)
    elif uartdata == "C":
        basic.show_leds("""
            . . # . .
            . # # # #
            # # # # .
            . # # # #
            . . # . .
        """)
        PCAmotor.motor_run(PCAmotor.Motors.M1, -255)
        PCAmotor.motor_run(PCAmotor.Motors.M2, 255)
    elif uartdata == "D":
        basic.show_leds("""
            . . # . .
            # # # # .
            . # # # #
            # # # # .
            . . # . .
        """)
        PCAmotor.motor_run(PCAmotor.Motors.M1, 255)
        PCAmotor.motor_run(PCAmotor.Motors.M2, -255)
    elif uartdata == "E":
        basic.show_leds("""
            . # # # .
            # . . . #
            # # # . #
            # # . . #
            # . . . .
        """)
    elif uartdata == "F":
        basic.show_leds("""
            . # # # .
            # . . . #
            # . # # #
            # . . # #
            . . . . #
        """)
    elif uartdata == "0":
        basic.show_icon(IconNames.NO)
        PCAmotor.motor_stop_all()

uartdata = ""
connected = False
bluetooth.set_transmit_power(7)
bluetooth.start_uart_service()
basic.show_icon(IconNames.HEART)
connected = False
speed = 255

def on_forever():
    sendDistAndSpeed()
    basic.pause(200)
basic.forever(on_forever)
