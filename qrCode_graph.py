import networkx as nx

def find_rack_path(startX,startY,rack): # find the path from the start to the appropriate rack

    G = nx.Graph()
    # all connected QR codes
    G.add_edges_from([(3,4),(4,5),(5,6),(6,7),(7,9),(8,10),(9,15),
                      (10,11),(10,16),(11,12),(11,18),(12,13),(13,14),(13,19),
                      (14,15),(15,17),(16,21),(17,20),(19,25),(21,23),
                      (23,27),(24,30),(25,32),(26,28),(27,29),(28,34),(29,30),
                      (29,35),(30,31),(31,32),(32,33),(33,34),(34,41),
                      (36,37),(37,38),(38,39),(39,41)])

    # dictionary listing all QR codes and their corresponding x-y coordinates
    positions = {2:(9.5,8), 3:(21,18.5), 4:(46,18.5), 5:(50.5,18.5),
                 6:(66,18.5), 7:(76,18), 8:(14,22), 9:(76.5,29),
                 10:(13.5,41.5), 11:(31.5,42), 12:(50.5,41.5),
                 13:(53.5,41.5), 14:(66,41.5), 15:(76.5,41.5),
                 16:(14,47.5), 17:(76.5,49.5), 18:(31.5,60.5),
                 19:(54,60.5), 20:(76.5,62), 21:(14,67.5),
                 22:(88,71.5), 23:(14,78), 24:(31.5,80.5), 25:(54,80.5),
                 26:(80,81), 27:(14.5,98), 28:(80,99), 29:(14.5,104.5),
                 30:(31.5,104.5), 31:(41,104.5), 32:(54,104.5),
                 33:(61,104.5), 34:(80,104.5), 35:(14,118.5),
                 36:(21,127.5), 37:(41,127), 38:(61,127.5),
                 39:(80,127.5), 40:(9.5,133.5), 41:(80,119)}

    # dictionary listing the racks and the QR codes in front of them
    racks = {7:(4,6),36:(5,6),80:(12,14),13:(9,17),91:(19,25),42:(18,24),
             45:(16,21),72:(23,27),57:(31,33),46:(37,38),64:(37,38),
             23:(28,39)}

    for numR,rackQRs in racks.items():
        if rack == numR:
            target_rack_qrs = rackQRs # rack match found
            #print(target_rack_qrs)

    target1 = target_rack_qrs[0] # rack QR code 1
    target2 = target_rack_qrs[1] # rack QR code 2

    for qr,coords in positions.items(): # look for the corresponding QR code
        if target1 == qr:
            target1_coords = coords
            #print(target1_coords)

    for qr,coords in positions.items(): # look for the corresponding QR code
        if target2 == qr:
            target2_coords = coords
            #print(target2_coords)

    target1_x = target1_coords[0]
    target1_y = target1_coords[1]
    target1_start_coords = (target1_x,target1_y)
    start_coords = (startX,startY)

    target2_x = target2_coords[0]
    target2_y = target2_coords[1]
    target2_start_coords = (target2_x,target2_y)

    for numS,coordS in positions.items(): # look fo
        if coordS == start_coords:
            startQR = numS
            #print("Starting QR: {0}".format(startQR))

    shortest_path_1 = nx.shortest_path(G,startQR,target1) # calculate shortest path 1
    #print("Shortest path 1: ", shortest_path_1)
    #print(startQR)

    shortest_path_2 = nx.shortest_path(G,startQR,target2) # calculate shortest path 2
    #print("Shortest path 2: ", shortest_path_2)

    path_ = []

    if len(shortest_path_1) < len(shortest_path_2): # use the first shortest path if it's shorter than the second
        for i in shortest_path_1:
            #print(i)
            coords = positions[i]
            path_.append(coords)
        print("\nChose path 1")
        print(path_)
    elif len(shortest_path_1) > len(shortest_path_2): # use the second shortest path if it's shorter than the first
        for i in shortest_path_2:
            #print(i)
            coords = positions[i]
            path_.append(coords)
        print("\nChose path 2")
        print(path_)
    else: # if both paths are the same then use the first one
        for i in shortest_path_1:
            #print(i)
            coords = positions[i]
            path_.append(coords)
        print("\nPaths were same length")
        print(path_)

    return path_, target_rack_qrs

#dock a = 2
#dock b = 22
#dock c = 40
def find_dock_path(startQR,target_dock): # find path from rack to the appropriate dock
#    print(startQR)
#    print(target_dock)
    # match the dock with the corresponding QR code number
    if target_dock == 1:
        dock = 8
    elif target_dock == 2:
        dock = 20
    elif target_dock == 3:
        dock = 35
    G = nx.Graph()
    # all connected QR codes
    G.add_edges_from([(3,4),(4,5),(5,6),(6,7),(7,9),(8,10),(9,15),
                      (10,11),(10,16),(11,12),(11,18),(12,13),(13,14),(13,19),
                      (14,15),(15,17),(16,21),(17,20),(21,23),
                      (23,27),(24,30),(25,32),(26,28),(27,29),(28,34),(29,30),
                      (29,35),(30,31),(31,32),(32,33),(33,34),(34,41),
                      (36,37),(37,38),(38,39),(39,41)])
    # dictionary listing all QR codes and their corresponding x-y coordinates
    positions = {2:(9.5,8), 3:(21.5,18.5), 4:(46,18.5), 5:(50.5,18.5),
                 6:(66,18.5), 7:(76,18), 8:(14,22), 9:(76.5,29),
                 10:(13.5,41.5), 11:(31.5,42), 12:(50.5,41.5),
                 13:(53.5,41.5), 14:(66,41.5), 15:(76.5,41.5),
                 16:(14,47.5), 17:(76.5,49.5), 18:(31.5,60.5),
                 19:(54,60.5), 20:(76.5,62), 21:(14,67.5),
                 22:(88,71.5), 23:(14,78), 24:(31.5,80.5), 25:(54,80.5),
                 26:(80,81), 27:(14.5,98), 28:(80,99), 29:(14.5,104.5),
                 30:(31.5,104.5), 31:(41,104.5), 32:(54,104.5),
                 33:(61,104.5), 34:(80,104.5), 35:(14,118.5),
                 36:(21,127.5), 37:(41,127), 38:(61,127.5),
                 39:(80,127.5), 40:(9.5,133.5), 41:(80,119)}

    for numS,coordS in positions.items(): # look fo
        if coordS == startQR:
            startQR = numS

    dock_path = nx.shortest_path(G,startQR,dock) # find shortest path to dock
    # print(shortest_path)
    path = []
    for i in dock_path:
            #print(i)
            coords = positions[i]
            path.append(coords)
    return path

#pallet_path = find_rack_path(21,18.5,23)
#print(pallet_path)

#dock_path = find_dock_path(38,2)
#print(dock_path)
