
#def writeNumber(value):
#    bus.write_byte(address, value)
#    # bus.write_byte_data(address, 0, value)
#    return -1
#
#def readNumber():
#    number = bus.read_byte(address)
#    # number = bus.read_byte_data(address, 1)
#    return number

def Navigate(startQR,nextQR,currOr,futureOr):

    x = startQR[0]
    y = startQR[1]
    x_f = nextQR[0]
    y_f = nextQR[1]

    delta_x = x_f - x
    # print("Delta X: {0}".format(delta_x))
    delta_y = y_f - y
    # print("Delta Y: {0}".format(delta_y))
    if currOr == futureOr:
        print("Move forward")
    elif currOr == 1 and futureOr == 3:
        print("Turn left and move forward")
    elif currOr == 1 and futureOr == 4:
        print("Turn right and move forward")
    elif currOr == 2 and futureOr == 3:
        print("Turn right and move forward")
    elif currOr == 2 and futureOr == 4:
        print("Turn left and move forward")
    elif currOr == 3 and futureOr == 1:
        print("Turn right and move forward")
    elif currOr == 3 and futureOr == 2:
        print("Turn left and move forward")
    elif currOr == 4 and futureOr == 1:
        print("Turn left and move forward")
    elif currOr == 4 and futureOr == 2:
        print("Turn right and move forward")


    # if orientation == 1: # pointed in positive x direction
    #     if abs(delta_x) < 1 and delta_y > 0 or delta_x == 0 and delta_y > 0:
    #         print("Turn left\n")
    #     #fork.forward()
    #     #writeNumber(1)
    #
    #     elif abs(delta_x) < 1 and delta_y < 0 or delta_x == 1 and delta_y < 0:
    #         #print("dX = ",delta_x)
    #         #print("dY = ",delta_y)
    #         print("Turn right\n")
    #         #writeNumber(2)
    #
    #     elif delta_x > 0 and abs(delta_y) < 1 or delta_x > 0 and delta_y == 0:
    #         print("Move forward\n")
    #         #writeNumber(3)
    #
    # elif orientation == 2: # pointed in negative x direction
    #     if delta_x < 1 and abs(delta_y) < 1 or delta_x < 1 and delta_y == 0:
    #         print("Move forward\n")
    #     #fork.forward()
    #     #writeNumber(1)
    #
    #     elif abs(delta_x) < 1 and delta_y < 0 or delta_x == 0 and delta_y < 0:
    #             print("turn left")
    #
    #     elif abs(delta_x) < 1 and delta_y > 0 or delta_x == 0 and delta_y > 0:
    #         print("turn right\n")
    #         #writeNumber(2)
    #
    # elif orientation == 3: # pointed in positive y-direction
    #     if abs(delta_x) < 1 and delta_y > 0 or delta_x == 0 and delta_y > 0:
    #         print("Move forward\n")
    #     #fork.forward()
    #     #writeNumber(1)
    #
    #     elif delta_x < 0 and abs(delta_y) < 1 or delta_x < 0 and delta_y == 0:
    #         #print("dX = ",delta_x)
    #         #print("dY = ",delta_y)
    #         print("Turn left\n")
    #         #writeNumber(2)
    #
    #     elif delta_x > 0 and abs(delta_y) < 1 or delta_x > 0 and delta_y == 0:
    #         print("Turn right\n")
    #         #writeNumber(3)
    #
    # elif orientation == 4: # pointed in negative y-direction
    #     if abs(delta_x) < 1 and delta_y < 0 or delta_x == 0 and delta_y < 0:
    #         print("Move forward\n")
    #     #fork.forward()
    #     #writeNumber(1)
    #
    #     elif delta_x > 0 and abs(delta_y) < 1 or delta_x > 0 and delta_y == 0:
    #         print("Turn left")
    #
    #     elif delta_x < 0 and abs(delta_y) < 1 or delta_x < 0 and delta_y == 0:
    #         print("Turn right")
