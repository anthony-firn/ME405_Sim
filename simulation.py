import numpy as np
import math

timestep = .1 # (sec)

def main():
    print("starting sim")
    mw = .222     # Mass of wheel (kg)
    mb = 1.179    # Mass of body (kg)
    rw = .005     # Radius of wheel (m)
    rb = .349     # Distance from center of wheel to c.g. of body (m)
    Iwyy = 1      # Centroidal moment of inertia of wheel
    Ibyy = 1      # Centroidal moment of inertia of body
    g = 9.8       # Acceleration due to gravity (m/(s^2))
    pos = 0       # Horizontal displacement of balance bot
    pitch = 2     # Angular displacement of body in pitch axis (radians)
    posDot = 0    # Horizontal velocity of balance bot
    pitchDot = 0  # Angular velocity of body in pitch axis
    
    while True :

        c = math.cos(pitch)
        s = math.sin(pitch)
        
        mx = mb + (2*mw) + (2*(Iwyy / (rw*rw)))
        Ipitch = (mb*rb*rb) + Ibyy

        # assuming Tm is T
        Tm = 0

        A = np.matrix([[1, 0, 0, 0], [0, 1, 0, 0], [0, 0, mx, mb*rb*c], [0, 0, mb*rb*c, Ipitch]])
        b = np.matrix([[posDot], [pitchDot], [(2*Tm)/rw + mb*rb*s*(pitchDot**2)], [2*Tm + mb*rb*s*g]])
        print("A: \n" + str(A))
        print("b: \n" + str(b))
        
        res = np.matmul(A.I, b)

        print("res: \n" + str(res))

        posDot = res.item(0, 0)
        pitchDot = res.item(1, 0)
        posDotDot = res.item(2, 0)
        pitchDotDot = res.item(3, 0)

        print("velocity is: " + str(posDot) + "\nrotational velocity is: " + str(pitchDot))
        print("\nacceleration is: " + str(posDotDot) + "\nrotational acceleration is: " + str(pitchDotDot))

        pos = .5*posDotDot*(timestep**2) + posDot*timestep + pos
        pitch = .5*pitchDotDot*(timestep**2) + pitchDot*timestep + pitch

        print("position is: " + str(pos) + "pitch is: " + str(pitch))
if __name__ == "__main__" :
    main()
