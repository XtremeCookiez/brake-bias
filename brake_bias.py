from math import pi

LEG_FORCE = 100 * 4.45
MC_AREA = pi * ((22/2)**2)
LP = LEG_FORCE / MC_AREA # Line pressure

HPS = 0.45
HP_PLUS = 0.55

def torque(piston_diameters:list, pad_height:float, rotor_diameter:float, pad_friction: float = HPS):
    piston_areas = [pi*(d/2)**2 for d in piston_diameters]
    return LP * sum(piston_areas) * ((rotor_diameter / 2) - (pad_height / 2)) * pad_friction

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
    "330i Front, 135i Rear": {
        "front": {
            "piston_diameters": [57],
            "pad_height": 63.6,
            "rotor_diameter": 325
        }, 
            "rear": {
            "piston_diameters": [42, 42],
            "pad_height": 76,
            "rotor_diameter": 328
        }
    },
    "Front 330i, Rear 325i": {
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
    # "Front 330i, Rear 325i HP+": {
    #     "front": {
    #         "piston_diameters": [57],
    #         "pad_height": 63.6,
    #         "rotor_diameter": 325
    #     }, 
    #     "rear": {
    #         "piston_diameters": [40],
    #         "pad_height": 59.2,
    #         "rotor_diameter": 294, "pad_friction": HP_PLUS,
    #     }
    # },
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
    # "Front 135i, Rear M3": {
    #     "front": {
    #         "piston_diameters": [28,32,36,28,32,36],
    #         "pad_height": 74,
    #         "rotor_diameter": 325
    #     }, 
    #     "rear": {
    #         "piston_diameters": [42],
    #         "pad_height": 59.2,
    #         "rotor_diameter": 328
    #     }
    # },
    # "Front 135i, Rear M3 HP+": {
    #     "front": {
    #         "piston_diameters": [28,32,36,28,32,36],
    #         "pad_height": 74,
    #         "rotor_diameter": 325
    #     }, 
    #     "rear": {
    #         "piston_diameters": [42],
    #         "pad_height": 59.2,
    #         "rotor_diameter": 328,
    #         "pad_friction": HP_PLUS,
    #     }
    # },
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
    },
    # "Front 996, Rear M3": {
    #     "front": {
    #         "piston_diameters": [36, 36, 40, 40],
    #         "pad_height": 90,
    #         "rotor_diameter": 325
    #     }, 
    #     "rear": {
    #         "piston_diameters": [42],
    #         "pad_height": 59.2,
    #         "rotor_diameter": 328
    #     }
    # },
    # "Front 996, Rear M3 HP+": {
    #     "front": {
    #         "piston_diameters": [36, 36, 40, 40],
    #         "pad_height": 90,
    #         "rotor_diameter": 325
    #     }, 
    #     "rear": {
    #         "piston_diameters": [42],
    #         "pad_height": 59.2,
    #         "rotor_diameter": 328,
    #         "pad_friction": HP_PLUS,
    #     }
    # },
    # "Front 996 CSL, Rear M3": {
    #     "front": {
    #         "piston_diameters": [36, 36, 40, 40],
    #         "pad_height": 90,
    #         "rotor_diameter": 345
    #     }, 
    #     "rear": {
    #         "piston_diameters": [42],
    #         "pad_height": 59.2,
    #         "rotor_diameter": 328
    #     }
    # },
    "996": {
        "front": {
            "piston_diameters": [36, 36, 40, 40],
            "pad_height": 90,
            "rotor_diameter": 325
        }, 
        "rear": {
            "piston_diameters": [28,28, 30, 30],
            "pad_height": 73,
            "rotor_diameter": 328
        }
    },
        "996 CSL": {
        "front": {
            "piston_diameters": [36, 36, 40, 40],
            "pad_height": 90,
            "rotor_diameter": 345
        }, 
        "rear": {
            "piston_diameters": [28,28, 30, 30],
            "pad_height": 73,
            "rotor_diameter": 328
        }
    },
    "996 CSL Front, 135i Rear": {
        "front": {
            "piston_diameters": [36, 36, 40, 40],
            "pad_height": 90,
            "rotor_diameter": 345
        }, 
        "rear": {
            "piston_diameters": [42, 42],
            "pad_height": 76,
            "rotor_diameter": 328
        }
    },
    "996 Front, Z32 Rear": {
        "front": {
            "piston_diameters": [36, 36, 40, 40],
            "pad_height": 90,
            "rotor_diameter": 325
        }, 
        "rear": {
            "piston_diameters": [38.1, 38.1],
            "pad_height": 35.85,
            "rotor_diameter": 328
        }
    },
    "996 Front, 135i Rear": {
        "front": {
            "piston_diameters": [36, 36, 40, 40],
            "pad_height": 90,
            "rotor_diameter": 325
        }, 
        "rear": {
            "piston_diameters": [42, 42],
            "pad_height": 76,
            "rotor_diameter": 328
        }
    },
    "Z32": {
        "front": {
            "piston_diameters": [40.45, 40.45, 40.45, 40.45],
            "pad_height": 50.5,
            "rotor_diameter": 325
        }, 
        "rear": {
            "piston_diameters": [38.1, 38.1],
            "pad_height": 35.85,
            "rotor_diameter": 328
        }
    },
    "135i Front, Z32 Rear": {
        "front": {
            "piston_diameters": [28,32,36,28,32,36],
            "pad_height": 74,
            "rotor_diameter": 325
        },
        "rear": {
            "piston_diameters": [38.1, 38.1],
            "pad_height": 35.85,
            "rotor_diameter": 328
        }
    },
    "Z32 Front, 135i Rear": {
        "front": {
            "piston_diameters": [40.45, 40.45, 40.45, 40.45],
            "pad_height": 50.5,
            "rotor_diameter": 325
        }, 
        "rear": {
            "piston_diameters": [42, 42],
            "pad_height": 76,
            "rotor_diameter": 328
        }
    },
    "Front M3, Rear Z32": {
        "front": {
            "piston_diameters": [60],
            "pad_height": 63.6,
            "rotor_diameter": 325
        }, 
        "rear": {
            "piston_diameters": [42, 42],
            "pad_height": 76,
            "rotor_diameter": 328
        }
    },
        "Front M3 CSL, Rear Z32": {
        "front": {
            "piston_diameters": [60],
            "pad_height": 63.6,
            "rotor_diameter": 345
        }, 
        "rear": {
            "piston_diameters": [42, 42],
            "pad_height": 76,
            "rotor_diameter": 328
        }
    },
}

for name, values in combos.items():
    front = torque(**values["front"])
    rear = torque(**values["rear"])

    bias = front / (front + rear) * 100

    print(f"{name}: {bias:.1f}% ({front:.0f}|{rear:.0f})")