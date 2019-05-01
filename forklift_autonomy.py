# Code to run the Autonomous Forklift Scripts at a high level

import qrCode_graph as map
import Nav1 as nav
#import forklift_arduino_autonomy as forklift
#import code_reader_i2c_V3 as qrRead

# determine current QR code

## read QR code
#while True: # THIS CONDITIONAL WILL HAVE TO BE CHANGED
#    QR_array = qrRead.ReadQR()
#
#    if len(QR_array) >= 3:
#        pallet = QR_array[0]
#        rack = QR_array[1]
#        dock = QR_array[2]
#
#    if len(QR_array) >= 5:
#        x = QR_array[3]
#        y = QR_array[4]
#
#    if len(QR_array) >= 7:
#        rack1_ori = QR_array[5]
#        rack1_num = QR_array[6]
#
#    if len(QR_array) >= 9:
#        rack2_ori = QR_array[7]
#        rack2_num = QR_array[8]

# How to use script:
# 1. input x and y coordinates of starting QR code
# 2. input rack you want to go to
# 3. input starting orientation for current orientation - check calculate_orientation for numbering
# 4. input dock you want to go to
# 5. input final orientation from before you picked up the pallet


def calculate_orientation(first,second):
    fx = first[0]
    fy = first[1]
    sx = second[0]
    sy = second[1]
    dX = sx-fx
    dY = sy-fy

    if dX > 1 and dY == 0 or dX > 1 and abs(dY) < 1: # pointed in pos-x direction
        orient = 1
        print("1. pos_x")
    elif dX < 0 and dY == 0 or dX < 0 and abs(dY) < 1: # pointed in neg-x direction
        orient = 2
        print("2. neg_x")
    elif dX == 0 and dY > 0 or abs(dX) < 1 and dY > 0: # pointed in pos-y direction
        orient = 3
        print("3. pos_y")
    elif dX == 0 and dY < 0 or abs(dX) < 1 and dY < 0: # pointed in neg-y direction
        orient = 4
        print("4. neg_y")
    return orient

# start on QR 26
x = 14
y = 118.5
rack = 45
current_orientation = 4

# plug current QR and target QR into graph and get shortest path
rack_path, rack_QR = map.find_rack_path(x,y,rack)
print("\nStarting QR: {0}".format(rack_path[0]))
print("Target QR: {0}\n".format(rack_path[-1]))

# Run line follower
#forklift.LineFollower()
print("Starting line follower\n")
#orient1 = 2
# run control algorithm to get to pallet

for i in range(len(rack_path)-1):
    print(rack_path[i])
    print(rack_path[i+1])
    future_orientation = calculate_orientation(rack_path[i],rack_path[i+1])
    nav.Navigate(rack_path[i],rack_path[i+1],current_orientation,future_orientation)
    current_orientation = future_orientation
print(current_orientation)
# Run Vertical Stepper to get to mid pallet location
#vertical_stepUp(500)

# Run forklift alignment code
#forklift.ForkAlignment()

# Run Horizontal
#forklift.Horizontal_StepForward()

# Pick up pallet
#vertical_stepUp(200)

# Pull Pallet Back
#forklift.Horizontal_StepBackward()

# Pull Pallet Down
#vertical_stepDown(300)

# Run control algorithm to get to loading dock

dock = 2
print("\nPretending to pick up pallet")
print("Moving to dock {0}\n".format(dock))
rackQR = rack_path[-1]
dock_path = map.find_dock_path(rackQR,dock)
current_orientation = 4
#print("Starting QR: {0}".format(dock_path[0]))
#print("Target QR: {0}\n".format(dock_path[-1]))
#orient2 = 2
# run control algorithm to get to pallet
for i in range(len(dock_path)-1):
    print(dock_path[i])
    print(dock_path[i+1])
    future_orientation = calculate_orientation(dock_path[i],dock_path[i+1])
    nav.Navigate(dock_path[i],dock_path[i+1],current_orientation,future_orientation)
    current_orientation = future_orientation

# Drop off pallet at dock
# Run Horizontal
#forklift.Horizontal_StepForward()

# Run vertical to drop
#forklift.vertical_stepDown(200)
