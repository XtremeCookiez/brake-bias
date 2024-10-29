from math import pi

LEG_FORCE = 100 * 4.45
MC_AREA = pi * ((22/2)**2)
LP = LEG_FORCE / MC_AREA # Line pressure

def torque(piston_diameters:list, pad_height:float, rotor_diameter:float):
    piston_areas = [pi*(d/2)**2 for d in piston_diameters]
    return LP * sum(piston_areas) * ((rotor_diameter / 2) - (pad_height / 2))


combos = {
    "Stock 330i": {
        "front": {
            "piston_diameters": [57],
            "pad_height": 63.6,
            "rotor_diameter": 325
        }, 
        "rear": {
            "piston_diameters": [42],
            "pad_height": 59.2,
            "rotor_diameter": 320
        }
    },
    "My 325i": {
        "front": {
            "piston_diameters": [57],
            "pad_height": 63.6,
            "rotor_diameter": 325
        }, 
        "rear": {
            "piston_diameters": [40],
            "pad_height": 59.2,
            "rotor_diameter": 294
        }
    },
    "Front 330i, Rear M3": {
        "front": {
            "piston_diameters": [57],
            "pad_height": 63.6,
            "rotor_diameter": 325
        }, 
        "rear": {
            "piston_diameters": [42],
            "pad_height": 59.2,
            "rotor_diameter": 328
        }
    },
    "Front 135i, Rear M3": {
        "front": {
            "piston_diameters": [28,32,36,28,32,36],
            "pad_height": 74,
            "rotor_diameter": 325
        }, 
        "rear": {
            "piston_diameters": [42],
            "pad_height": 59.2,
            "rotor_diameter": 328
        }
    },
        "135i": {
        "front": {
            "piston_diameters": [28,32,36,28,32,36],
            "pad_height": 74,
            "rotor_diameter": 325
        }, 
        "rear": {
            "piston_diameters": [42, 42],
            "pad_height": 76,
            "rotor_diameter": 328
        }
    }
}

for name, values in combos.items():
    front = torque(**values["front"])
    rear = torque(**values["rear"])

    bias = front / (front + rear) * 100

    print(f"{name}: {bias:.1f}% ({front:.0f}|{rear:.0f})")