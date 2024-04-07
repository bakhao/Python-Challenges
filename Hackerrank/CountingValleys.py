

def countingValleys(steps, path):
     altitude = 0
     numberValleys = 0
     for direction in path:
         print(f"altitude {altitude}")
         if direction == "U":
             altitude += 1
             if altitude == 0:
                 numberValleys += 1
         else:
             altitude -= 1
     return numberValleys