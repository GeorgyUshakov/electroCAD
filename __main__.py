from tkinter import Tk, Canvas, Label, Toplevel, Button, PhotoImage, LAST, Entry
from numpy import matrix, cos
import os
directory = os.path.dirname(__file__)
print(directory)

root = Tk()
root.title('electroCAD α.0: electronic circuit schematic')

list = {
    'Text':{
        'Image':PhotoImage(file = directory + '/images/Text/Text.gif'),
        'Elements':{
            'Custom':{
                'Image':PhotoImage(file = directory + '/images/Text/Text.gif'),
                'Text':'Custom'
            }
        }
    },
    'Power':{
        'Image':PhotoImage(file = directory + '/images/Power/DC_up.gif'),
        'Elements':{
            'Cell_up':{
                'Image':PhotoImage(file = directory + '/images/Power/Cell_up.gif'),
                'Text':'Cell_hor (up)'
            },
            'Cell_down':{
                'Image':PhotoImage(file = directory + '/images/Power/Cell_down.gif'),
                'Text':'Cell_hor (down)'
            },
            'Cell_right':{
                'Image':PhotoImage(file = directory + '/images/Power/Cell_right.gif'),
                'Text':'Cell_hor (right)'
            },
            'Cell_left':{
                'Image':PhotoImage(file = directory + '/images/Power/Cell_left.gif'),
                'Text':'Cell_hor (left)'
            },
            'Battery_up':{
                'Image':PhotoImage(file = directory + '/images/Power/Battery_up.gif'),
                'Text':'Bat. (up)'
            },
            'Battery_down':{
                'Image':PhotoImage(file = directory + '/images/Power/Battery_down.gif'),
                'Text':'Bat. (down)'
            },
            'Battery_right':{
                'Image':PhotoImage(file = directory + '/images/Power/Battery_right.gif'),
                'Text':'Bat. (right)'
            },
            'Battery_left':{
                'Image':PhotoImage(file = directory + '/images/Power/Battery_left.gif'),
                'Text':'Bat. (left)'
            },
            'DC_up':{
                'Image':PhotoImage(file = directory + '/images/Power/DC_up.gif'),
                'Text':'DC (up)'
            },
            'DC_down':{
                'Image':PhotoImage(file = directory + '/images/Power/DC_down.gif'),
                'Text':'DC (up)'
            },
            'DC_right':{
                'Image':PhotoImage(file = directory + '/images/Power/DC_right.gif'),
                'Text':'DC (up)'
            },
            'DC_left':{
                'Image':PhotoImage(file = directory + '/images/Power/DC_left.gif'),
                'Text':'DC (up)'
            },
            'AC':{
                'Image':PhotoImage(file = directory + '/images/Power/AC.gif'),
                'Text':'AC'
            },
            'Ground_1':{
                'Image':PhotoImage(file = directory + '/images/Power/Ground_1.gif'),
                'Text':'Gnd. 1'
            },
            'Ground_2':{
                'Image':PhotoImage(file = directory + '/images/Power/Ground_2.gif'),
                'Text':'Gnd. 2'
            },
            'Fuse_horizontal':{
                'Image':PhotoImage(file = directory + '/images/Power/Fuse_horizontal.gif'),
                'Text':'Fuse (hor.)'
            },
            'Fuse_vertical':{
                'Image':PhotoImage(file = directory + '/images/Power/Fuse_vertical.gif'),
                'Text':'Fuse (ver.)'
            }
        }
    },
    'Resistors':{
        'Image':PhotoImage(file = directory + '/images/Resistors/Resistor_US_horizontal.gif'),
        'Elements':{
            'Resistor_US_horizontal':{
                'Image':PhotoImage(file = directory + '/images/Resistors/Resistor_US_horizontal.gif'),
                'Text':'Res. (US, hor.)'
            },
            'Resistor_US_vertical':{
                'Image':PhotoImage(file = directory + '/images/Resistors/Resistor_US_vertical.gif'),
                'Text':'Res. (US, ver.)'
            },
            'Resistor_EU_horizontal':{
                'Image':PhotoImage(file = directory + '/images/Resistors/Resistor_EU_horizontal.gif'),
                'Text':'Res. (EU, hor.)'
            },
            'Resistor_EU_vertical':{
                'Image':PhotoImage(file = directory + '/images/Resistors/Resistor_EU_vertical.gif'),
                'Text':'Res. (EU, ver.)'
            },
            'Rheostat_US_horizontal':{
                'Image':PhotoImage(file = directory + '/images/Resistors/Rheostat_US_horizontal.gif'),
                'Text':'Rhe. (US, hor.)'
            },
            'Rheostat_US_vertical':{
                'Image':PhotoImage(file = directory + '/images/Resistors/Rheostat_US_vertical.gif'),
                'Text':'Rhe. (US, ver.)'
            },
            'Rheostat_EU_horizontal':{
                'Image':PhotoImage(file = directory + '/images/Resistors/Rheostat_EU_horizontal.gif'),
                'Text':'Rhe. (EU, hor.)'
            },
            'Rheostat_EU_vertical':{
                'Image':PhotoImage(file = directory + '/images/Resistors/Rheostat_EU_vertical.gif'),
                'Text':'Rhe. (EU, ver.)'
            },
            'Potentiometer_US_up':{
                'Image':PhotoImage(file = directory + '/images/Resistors/Potentiometer_US_up.gif'),
                'Text':'Pot. (US, up)'
            },
            'Potentiometer_US_down':{
                'Image':PhotoImage(file = directory + '/images/Resistors/Potentiometer_US_down.gif'),
                'Text':'Pot. (US, down)'
            },
            'Potentiometer_US_right':{
                'Image':PhotoImage(file = directory + '/images/Resistors/Potentiometer_US_right.gif'),
                'Text':'Pot. (US, right)'
            },
            'Potentiometer_US_left':{
                'Image':PhotoImage(file = directory + '/images/Resistors/Potentiometer_US_left.gif'),
                'Text':'Pot. (US, left)'
            },
            'Potentiometer_EU_up':{
                'Image':PhotoImage(file = directory + '/images/Resistors/Potentiometer_EU_up.gif'),
                'Text':'Pot. (EU, up)'
            },
            'Potentiometer_EU_down':{
                'Image':PhotoImage(file = directory + '/images/Resistors/Potentiometer_EU_down.gif'),
                'Text':'Pot. (EU, down)'
            },
            'Potentiometer_EU_right':{
                'Image':PhotoImage(file = directory + '/images/Resistors/Potentiometer_EU_right.gif'),
                'Text':'Pot. (EU, right)'
            },
            'Potentiometer_EU_left':{
                'Image':PhotoImage(file = directory + '/images/Resistors/Potentiometer_EU_left.gif'),
                'Text':'Pot. (EU, left)'
            }
        }
    },
    'Capacitors':{
        'Image':PhotoImage(file = directory + '/images/Capacitors/Capacitor_vertical.gif'),
        'Elements':{
            'Capacitor_horizontal':{
                'Image':PhotoImage(file = directory + '/images/Capacitors/Capacitor_horizontal.gif'),
                'Text':'Cap. (hor.)'
            },
            'Capacitor_vertical':{
                'Image':PhotoImage(file = directory + '/images/Capacitors/Capacitor_vertical.gif'),
                'Text':'Cap. (ver.)'
            },
            'Var_cap_horizontal':{
                'Image':PhotoImage(file = directory + '/images/Capacitors/Var_cap_horizontal.gif'),
                'Text':'Var. cap. (hor.)'
            },
            'Var_cap_vertical':{
                'Image':PhotoImage(file = directory + '/images/Capacitors/Var_cap_vertical.gif'),
                'Text':'Var. cap. (ver.)'
            },
            'Pol_cap_up':{
                'Image':PhotoImage(file = directory + '/images/Capacitors/Pol_cap_up.gif'),
                'Text':'Pol. cap. (up)'
            },
            'Pol_cap_down':{
                'Image':PhotoImage(file = directory + '/images/Capacitors/Pol_cap_down.gif'),
                'Text':'Pol. cap. (down)'
            },
            'Pol_cap_right':{
                'Image':PhotoImage(file = directory + '/images/Capacitors/Pol_cap_right.gif'),
                'Text':'Pol. cap. (right)'
            },
            'Pol_cap_left':{
                'Image':PhotoImage(file = directory + '/images/Capacitors/Pol_cap_left.gif'),
                'Text':'Pol. cap. (left)'
            }
        }
    },
    'Inductors':{
        'Image':PhotoImage(file = directory + '/images/Inductors/Inductor_up.gif'),
        'Elements':{
            'Inductor_up':{
                'Image':PhotoImage(file = directory + '/images/Inductors/Inductor_up.gif'),
                'Text':'Ind. (up)'
            },
            'Inductor_down':{
                'Image':PhotoImage(file = directory + '/images/Inductors/Inductor_down.gif'),
                'Text':'Ind. (down)'
            },
            'Inductor_right':{
                'Image':PhotoImage(file = directory + '/images/Inductors/Inductor_right.gif'),
                'Text':'Ind. (right)'
            },
            'Inductor_left':{
                'Image':PhotoImage(file = directory + '/images/Inductors/Inductor_left.gif'),
                'Text':'Ind. (left)'
            }
        }
    },
    'Diodes':{
        'Image':PhotoImage(file = directory + '/images/Diodes/Diode_right.gif'),
        'Elements':{
            'Diode_up':{
                'Image':PhotoImage(file = directory + '/images/Diodes/Diode_up.gif'),
                'Text':'Diode (up)'
            },
            'Diode_down':{
                'Image':PhotoImage(file = directory + '/images/Diodes/Diode_down.gif'),
                'Text':'Diode (down)'
            },
            'Diode_right':{
                'Image':PhotoImage(file = directory + '/images/Diodes/Diode_right.gif'),
                'Text':'Diode (right)'
            },
            'Diode_left':{
                'Image':PhotoImage(file = directory + '/images/Diodes/Diode_left.gif'),
                'Text':'Diode (left)'
            },
            'Zener_up':{
                'Image':PhotoImage(file = directory + '/images/Diodes/Zener_up.gif'),
                'Text':'Zener (up)'
            },
            'Zener_down':{
                'Image':PhotoImage(file = directory + '/images/Diodes/Zener_down.gif'),
                'Text':'Zener (down)'
            },
            'Zener_right':{
                'Image':PhotoImage(file = directory + '/images/Diodes/Zener_right.gif'),
                'Text':'Zener (right)'
            },
            'Zener_left':{
                'Image':PhotoImage(file = directory + '/images/Diodes/Zener_left.gif'),
                'Text':'Zener (left)'
            },
            'Schottky_up':{
                'Image':PhotoImage(file = directory + '/images/Diodes/Schottky_up.gif'),
                'Text':'Sch. (up)'
            },
            'Schottky_down':{
                'Image':PhotoImage(file = directory + '/images/Diodes/Schottky_down.gif'),
                'Text':'Sch. (down)'
            },
            'Schottky_right':{
                'Image':PhotoImage(file = directory + '/images/Diodes/Schottky_right.gif'),
                'Text':'Sch. (right)'
            },
            'Schottky_left':{
                'Image':PhotoImage(file = directory + '/images/Diodes/Schottky_left.gif'),
                'Text':'Sch. (left)'
            },
            'LED_up':{
                'Image':PhotoImage(file = directory + '/images/Diodes/LED_up.gif'),
                'Text':'LED (up)'
            },
            'LED_down':{
                'Image':PhotoImage(file = directory + '/images/Diodes/LED_down.gif'),
                'Text':'LED (down)'
            },
            'LED_right':{
                'Image':PhotoImage(file = directory + '/images/Diodes/LED_right.gif'),
                'Text':'LED (right)'
            },
            'LED_left':{
                'Image':PhotoImage(file = directory + '/images/Diodes/LED_left.gif'),
                'Text':'LED (left)'
            }
        }
    },
    'Transistors':{
        'Image':PhotoImage(file = directory + '/images/Transistors/NPN_right.gif'),
        'Elements':{
            'NPN_up':{
                'Image':PhotoImage(file = directory + '/images/Transistors/NPN_up.gif'),
                'Text':'NPN (up)'
            },
            'NPN_down':{
                'Image':PhotoImage(file = directory + '/images/Transistors/NPN_down.gif'),
                'Text':'NPN (down)'
            },
            'NPN_right':{
                'Image':PhotoImage(file = directory + '/images/Transistors/NPN_right.gif'),
                'Text':'NPN (right)'
            },
            'NPN_left':{
                'Image':PhotoImage(file = directory + '/images/Transistors/NPN_left.gif'),
                'Text':'NPN (left)'
            },
            'PNP_up':{
                'Image':PhotoImage(file = directory + '/images/Transistors/PNP_up.gif'),
                'Text':'PNP (up)'
            },
            'PNP_down':{
                'Image':PhotoImage(file = directory + '/images/Transistors/PNP_down.gif'),
                'Text':'PNP (down)'
            },
            'PNP_right':{
                'Image':PhotoImage(file = directory + '/images/Transistors/PNP_right.gif'),
                'Text':'PNP (right)'
            },
            'PNP_left':{
                'Image':PhotoImage(file = directory + '/images/Transistors/PNP_left.gif'),
                'Text':'PNP (left)'
            },
            'NMOS_up':{
                'Image':PhotoImage(file = directory + '/images/Transistors/NMOS_up.gif'),
                'Text':'NMOS (up)'
            },
            'NMOS_down':{
                'Image':PhotoImage(file = directory + '/images/Transistors/NMOS_down.gif'),
                'Text':'NMOS (down)'
            },
            'NMOS_right':{
                'Image':PhotoImage(file = directory + '/images/Transistors/NMOS_right.gif'),
                'Text':'NMOS (right)'
            },
            'NMOS_left':{
                'Image':PhotoImage(file = directory + '/images/Transistors/NMOS_left.gif'),
                'Text':'NMOS (left)'
            },
            'PMOS_up':{
                'Image':PhotoImage(file = directory + '/images/Transistors/PMOS_up.gif'),
                'Text':'PMOS (up)'
            },
            'PMOS_down':{
                'Image':PhotoImage(file = directory + '/images/Transistors/PMOS_down.gif'),
                'Text':'PMOS (down)'
            },
            'PMOS_right':{
                'Image':PhotoImage(file = directory + '/images/Transistors/PMOS_right.gif'),
                'Text':'PMOS (right)'
            },
            'PMOS_left':{
                'Image':PhotoImage(file = directory + '/images/Transistors/PMOS_left.gif'),
                'Text':'PMOS (left)'
            }
        }
    },
    'Logic':{
        'Image':PhotoImage(file = directory + '/images/Logic/NOR_right.gif'),
        'Elements':{
            'Buffer_up':{
                'Image':PhotoImage(file = directory + '/images/Logic/Buffer_up.gif'),
                'Text':'Buf. (up)'
            },
            'Buffer_down':{
                'Image':PhotoImage(file = directory + '/images/Logic/Buffer_down.gif'),
                'Text':'Buf. (down)'
            },
            'Buffer_right':{
                'Image':PhotoImage(file = directory + '/images/Logic/Buffer_right.gif'),
                'Text':'Buf. (right)'
            },
            'Buffer_left':{
                'Image':PhotoImage(file = directory + '/images/Logic/Buffer_left.gif'),
                'Text':'Buf. (left)'
            },
            'Inverter_up':{
                'Image':PhotoImage(file = directory + '/images/Logic/Inverter_up.gif'),
                'Text':'Inv. (up)'
            },
            'Inverter_down':{
                'Image':PhotoImage(file = directory + '/images/Logic/Inverter_down.gif'),
                'Text':'Inv. (down)'
            },
            'Inverter_right':{
                'Image':PhotoImage(file = directory + '/images/Logic/Inverter_right.gif'),
                'Text':'Inv. (right)'
            },
            'Inverter_left':{
                'Image':PhotoImage(file = directory + '/images/Logic/Inverter_left.gif'),
                'Text':'Inv. (left)'
            },
            'AND_up':{
                'Image':PhotoImage(file = directory + '/images/Logic/AND_up.gif'),
                'Text':'AND (up)'
            },
            'AND_down':{
                'Image':PhotoImage(file = directory + '/images/Logic/AND_down.gif'),
                'Text':'AND (down)'
            },
            'AND_right':{
                'Image':PhotoImage(file = directory + '/images/Logic/AND_right.gif'),
                'Text':'AND (right)'
            },
            'AND_left':{
                'Image':PhotoImage(file = directory + '/images/Logic/AND_left.gif'),
                'Text':'AND (left)'
            },
            'NAND_up':{
                'Image':PhotoImage(file = directory + '/images/Logic/NAND_up.gif'),
                'Text':'NAND (up)'
            },
            'NAND_down':{
                'Image':PhotoImage(file = directory + '/images/Logic/NAND_down.gif'),
                'Text':'NAND (down)'
            },
            'NAND_right':{
                'Image':PhotoImage(file = directory + '/images/Logic/NAND_right.gif'),
                'Text':'NAND (right)'
            },
            'NAND_left':{
                'Image':PhotoImage(file = directory + '/images/Logic/NAND_left.gif'),
                'Text':'NAND (left)'
            },
            'OR_up':{
                'Image':PhotoImage(file = directory + '/images/Logic/OR_up.gif'),
                'Text':'OR (up)'
            },
            'OR_down':{
                'Image':PhotoImage(file = directory + '/images/Logic/OR_down.gif'),
                'Text':'OR (down)'
            },
            'OR_right':{
                'Image':PhotoImage(file = directory + '/images/Logic/OR_right.gif'),
                'Text':'OR (right)'
            },
            'OR_left':{
                'Image':PhotoImage(file = directory + '/images/Logic/OR_left.gif'),
                'Text':'OR (left)'
            },
            'NOR_up':{
                'Image':PhotoImage(file = directory + '/images/Logic/NOR_up.gif'),
                'Text':'NOR (up)'
            },
            'NOR_down':{
                'Image':PhotoImage(file = directory + '/images/Logic/NOR_down.gif'),
                'Text':'NOR (down)'
            },
            'NOR_right':{
                'Image':PhotoImage(file = directory + '/images/Logic/NOR_right.gif'),
                'Text':'NOR (right)'
            },
            'NOR_left':{
                'Image':PhotoImage(file = directory + '/images/Logic/NOR_left.gif'),
                'Text':'NOR (left)'
            },
            'XOR_up':{
                'Image':PhotoImage(file = directory + '/images/Logic/XOR_up.gif'),
                'Text':'XOR (up)'
            },
            'XOR_down':{
                'Image':PhotoImage(file = directory + '/images/Logic/XOR_down.gif'),
                'Text':'XOR (down)'
            },
            'XOR_right':{
                'Image':PhotoImage(file = directory + '/images/Logic/XOR_right.gif'),
                'Text':'XOR (right)'
            },
            'XOR_left':{
                'Image':PhotoImage(file = directory + '/images/Logic/XOR_left.gif'),
                'Text':'XOR (left)'
            },
            'XNOR_up':{
                'Image':PhotoImage(file = directory + '/images/Logic/XNOR_up.gif'),
                'Text':'XNOR (up)'
            },
            'XNOR_down':{
                'Image':PhotoImage(file = directory + '/images/Logic/XNOR_down.gif'),
                'Text':'XNOR (down)'
            },
            'XNOR_right':{
                'Image':PhotoImage(file = directory + '/images/Logic/XNOR_right.gif'),
                'Text':'XNOR (right)'
            },
            'XNOR_left':{
                'Image':PhotoImage(file = directory + '/images/Logic/XNOR_left.gif'),
                'Text':'XNOR (left)'
            }
        }
    },
    'Switches':{
        'Image':PhotoImage(file = directory + '/images/Switches/Switch_up.gif'),
        'Elements':{
            'Switch_up':{
                'Image':PhotoImage(file = directory + '/images/Switches/Switch_up.gif'),
                'Text':'Sw. (up)'
            },
            'Switch_down':{
                'Image':PhotoImage(file = directory + '/images/Switches/Switch_down.gif'),
                'Text':'Sw. (down)'
            },
            'Switch_right':{
                'Image':PhotoImage(file = directory + '/images/Switches/Switch_right.gif'),
                'Text':'Sw. (right)'
            },
            'Switch_left':{
                'Image':PhotoImage(file = directory + '/images/Switches/Switch_left.gif'),
                'Text':'Sw. (left)'
            },
            'Button_up':{
                'Image':PhotoImage(file = directory + '/images/Switches/Button_up.gif'),
                'Text':'But. (up)'
            },
            'Button_down':{
                'Image':PhotoImage(file = directory + '/images/Switches/Button_down.gif'),
                'Text':'But. (down)'
            },
            'Button_right':{
                'Image':PhotoImage(file = directory + '/images/Switches/Button_right.gif'),
                'Text':'But. (right)'
            },
            'Button_left':{
                'Image':PhotoImage(file = directory + '/images/Switches/Button_left.gif'),
                'Text':'But. (left)'
            }
        }
    },
    'Measurement':{
        'Image':PhotoImage(file = directory + '/images/Measurement/Voltmeter.gif'),
        'Elements':{
            'Voltmeter':{
                'Image':PhotoImage(file = directory + '/images/Measurement/Voltmeter.gif'),
                'Text':'Voltmeter'
            },
            'Ammeter':{
                'Image':PhotoImage(file = directory + '/images/Measurement/Ammeter.gif'),
                'Text':'Ammeter'
            }
        }
    },
    'Other':{
        'Image':PhotoImage(file = directory + '/images/Other/Triode.gif'),
        'Elements':{
            'Lamp_up':{
                'Image':PhotoImage(file = directory + '/images/Other/Lamp_up.gif'),
                'Text':'Lamp (up)'
            },
            'Lamp_down':{
                'Image':PhotoImage(file = directory + '/images/Other/Lamp_down.gif'),
                'Text':'Lamp (down)'
            },
            'Lamp_left':{
                'Image':PhotoImage(file = directory + '/images/Other/Lamp_left.gif'),
                'Text':'Lamp (right)'
            },
            'Lamp_right':{
                'Image':PhotoImage(file = directory + '/images/Other/Lamp_right.gif'),
                'Text':'Lamp (left)'
            },
            'Buzzer_up':{
                'Image':PhotoImage(file = directory + '/images/Other/Buzzer_up.gif'),
                'Text':'Buz. (up)'
            },
            'Buzzer_down':{
                'Image':PhotoImage(file = directory + '/images/Other/Buzzer_down.gif'),
                'Text':'Buz. (down)'
            },
            'Buzzer_right':{
                'Image':PhotoImage(file = directory + '/images/Other/Buzzer_right.gif'),
                'Text':'Buz. (right)'
            },
            'Buzzer_left':{
                'Image':PhotoImage(file = directory + '/images/Other/Buzzer_left.gif'),
                'Text':'Buz. (left)'
            },
            'Motor':{
                'Image':PhotoImage(file = directory + '/images/Other/Motor.gif'),
                'Text':'Motor'
            },
            'Antenna':{
                'Image':PhotoImage(file = directory + '/images/Other/Antenna.gif'),
                'Text':'Antenna'
            },
            'Crystal_horizontal':{
                'Image':PhotoImage(file = directory + '/images/Other/Crystal_horizontal.gif'),
                'Text':'Crys. os. (hor.)'
            },
            'Crystal_vertical':{
                'Image':PhotoImage(file = directory + '/images/Other/Crystal_vertical.gif'),
                'Text':'Crys. os. (ver.)'
            },
            'Triode':{
                'Image':PhotoImage(file = directory + '/images/Other/Triode.gif'),
                'Text':'Triode'
            }
        }
    },
    'Formatting':{
        'Image':PhotoImage(file = directory + '/images/Formatting/Junction.gif'),
        'Elements':{
            'Junction':{
                'Image':PhotoImage(file = directory + '/images/Formatting/Junction.gif'),
                'Text':'Junction'
            },
            'Crossing_horizontal':{
                'Image':PhotoImage(file = directory + '/images/Formatting/Crossing_horizontal.gif'),
                'Text':'Cros. (hor.)'
            },
            'Crossing_vertical':{
                'Image':PhotoImage(file = directory + '/images/Formatting/Crossing_vertical.gif'),
                'Text':'Cros. (ver.)'
            }
        }
    }
}

displacement = 50
x = 20
y = 15
width = x * displacement
height = y * displacement
background_colour = '#fff'
component_colour = '#000'
component_hover = '#555555fff'
component_width = 2
radius = 5
junction_radius = 3
textpoint_radius = 2
point_colour = '#eee'
point_hover = '#555555fff'
icon_width = 50
icon_height = 50
text_size = 15

rot_right = matrix([[1,0],
                    [0,1]])
rot_up = matrix([[0,1],
                 [-1,0]])
rot_left = matrix([[-1,0],
                   [0,-1]])
rot_down = matrix([[0,-1],
                   [1,0]])
rot_45 = matrix([[1/(2**0.5),-1/(2**0.5)],
                 [1/(2**0.5),1/(2**0.5)]])

canvas = Canvas(
    root,
    width = width,
    height = height,
    bg = background_colour
)

canvas.grid(
    row = 1
)

def create_whiteout(x_0, y_0, x_1, y_1):
    canvas.create_line(
        x_coord + int(x_0),
        y_coord + int(y_0),
        x_coord + int(x_1),
        y_coord + int(y_1),
        fill = background_colour,
        width = component_width
    )

def create_component(x_0, y_0, x_1, y_1):
    canvas.create_line(
        x_coord + int(x_0),
        y_coord + int(y_0),
        x_coord + int(x_1),
        y_coord + int(y_1),
        fill = component_colour,
        width = component_width
    )

def create_long(x_0, y_0, x_1, y_1, x_2, y_2):
    canvas.create_line(
        x_coord + int(x_0),
        y_coord + int(y_0),
        x_coord + int(x_1),
        y_coord + int(y_1),
        x_coord + int(x_2),
        y_coord + int(y_2),
        fill = component_colour,
        width = component_width
    )

def create_circle(x_0, y_0, x_1, y_1):
    canvas.create_oval(
        x_coord + int(x_0),
        y_coord + int(y_0),
        x_coord + int(x_1),
        y_coord + int(y_1),
        fill = background_colour,
        outline = component_colour,
        width = component_width
    )

def create_wave(x_0, y_0, x_1, y_1, angle):
    canvas.create_arc(
        x_coord + int(x_0),
        y_coord + int(y_0),
        x_coord + int(x_1*(angle/90)),
        y_coord + int(y_1*((90-angle)/90)),
        start = angle,
        extent = 180,
        style = 'arc',
        width = component_width
    )
    canvas.create_arc(
        x_coord + int(x_1),
        y_coord + int(y_1),
        x_coord + int(x_0*(angle/90)),
        y_coord + int(y_0*((90-angle)/90)),
        start = angle,
        extent = -180,
        style = 'arc',
        width = component_width
    )

def create_arc(x_0, y_0, x_1, y_1, angle):
    canvas.create_arc(
        x_coord + int(x_0),
        y_coord + int(y_0),
        x_coord + int(x_1),
        y_coord + int(y_1),
        start = angle,
        extent = 180,
        style = 'arc',
        width = component_width
    )

def create_semi(x_0, y_0, x_1, y_1, angle):
    canvas.create_arc(
        x_coord + int(x_0),
        y_coord + int(y_0),
        x_coord + int(x_1),
        y_coord + int(y_1),
        start = angle,
        extent = 180,
        fill = background_colour,
        width = component_width
    )

def create_rectangle(x_0, y_0, x_1, y_1):
    canvas.create_rectangle(
        x_coord + int(x_0),
        y_coord + int(y_0),
        x_coord + int(x_1),
        y_coord + int(y_1),
        width = component_width,
        outline = component_colour,
        fill = background_colour
    )

def create_arrow(x_0, y_0, x_1, y_1):
    canvas.create_line(
        x_coord + int(x_0),
        y_coord + int(y_0),
        x_coord + int(x_1),
        y_coord + int(y_1),
        arrow = LAST,
        width = component_width,
        fill = component_colour
    )

def create_triangle(x_0, y_0, x_1, y_1, x_2, y_2):
    canvas.create_polygon(
        x_coord + int(x_0),
        y_coord + int(y_0),
        x_coord + int(x_1),
        y_coord + int(y_1),
        x_coord + int(x_2),
        y_coord + int(y_2),
        width = component_width,
        outline = component_colour,
        fill = background_colour
    )

def create_AND(  x_0,
                y_0,
                x_1,
                y_1,
                x_2,
                y_2,
                x_3,
                y_3,
                x_4,
                y_4,
                x_5,
                y_5,
                x_6,
                y_6,
                x_7,
                y_7,
                x_8,
                y_8,
                x_9,
                y_9,
                x_10,
                y_10,
                x_11,
                y_11,
                x_12,
                y_12,
                x_13,
                y_13,
                x_14,
                y_14,
                x_15,
                y_15,
                x_16,
                y_16,
                x_17,
                y_17,
                x_18,
                y_18,
                x_19,
                y_19,
                x_20,
                y_20,
                x_21,
                y_21,
                x_22,
                y_22
            ):
    canvas.create_polygon(
        x_coord + int(x_0),
        y_coord + int(y_0),
        x_coord + int(x_1),
        y_coord + int(y_1),
        x_coord + int(x_2),
        y_coord + int(y_2),
        x_coord + int(x_3),
        y_coord + int(y_3),
        x_coord + int(x_4),
        y_coord + int(y_4),
        x_coord + int(x_5),
        y_coord + int(y_5),
        x_coord + int(x_6),
        y_coord + int(y_6),
        x_coord + int(x_7),
        y_coord + int(y_7),
        x_coord + int(x_8),
        y_coord + int(y_8),
        x_coord + int(x_9),
        y_coord + int(y_9),
        x_coord + int(x_10),
        y_coord + int(y_10),
        x_coord + int(x_11),
        y_coord + int(y_11),
        x_coord + int(x_12),
        y_coord + int(y_12),
        x_coord + int(x_13),
        y_coord + int(y_13),
        x_coord + int(x_14),
        y_coord + int(y_14),
        x_coord + int(x_15),
        y_coord + int(y_15),
        x_coord + int(x_16),
        y_coord + int(y_16),
        x_coord + int(x_17),
        y_coord + int(y_17),
        x_coord + int(x_18),
        y_coord + int(y_18),
        x_coord + int(x_19),
        y_coord + int(y_19),
        x_coord + int(x_20),
        y_coord + int(y_20),
        x_coord + int(x_21),
        y_coord + int(y_21),
        x_coord + int(x_22),
        y_coord + int(y_22),
        fill = background_colour,
        outline = component_colour,
        width = component_width
    )

def create_OR(  x_0,
                y_0,
                x_1,
                y_1,
                x_2,
                y_2,
                x_3,
                y_3,
                x_4,
                y_4,
                x_5,
                y_5,
                x_6,
                y_6,
                x_7,
                y_7,
                x_8,
                y_8,
                x_9,
                y_9,
                x_10,
                y_10,
                x_11,
                y_11,
                x_12,
                y_12,
                x_13,
                y_13,
                x_14,
                y_14,
                x_15,
                y_15,
                x_16,
                y_16,
                x_17,
                y_17,
                x_18,
                y_18,
                x_19,
                y_19,
                x_20,
                y_20,
                x_21,
                y_21,
                x_22,
                y_22,
                x_23,
                y_23,
                x_24,
                y_24,
                x_25,
                y_25,
                x_26,
                y_26,
                x_27,
                y_27,
                x_28,
                y_28,
                x_29,
                y_29,
                x_30,
                y_30,
                x_31,
                y_31,
                x_32,
                y_32,
                x_33,
                y_33,
                x_34,
                y_34,
                x_35,
                y_35,
                x_36,
                y_36,
                x_37,
                y_37,
                x_38,
                y_38,
                x_39,
                y_39,
                x_40,
                y_40,
                x_41,
                y_41,
                x_42,
                y_42,
                x_43,
                y_43,
                x_44,
                y_44,
                x_45,
                y_45,):
    canvas.create_polygon(
        x_coord + int(x_0),
        y_coord + int(y_0),
        x_coord + int(x_1),
        y_coord + int(y_1),
        x_coord + int(x_2),
        y_coord + int(y_2),
        x_coord + int(x_3),
        y_coord + int(y_3),
        x_coord + int(x_4),
        y_coord + int(y_4),
        x_coord + int(x_5),
        y_coord + int(y_5),
        x_coord + int(x_6),
        y_coord + int(y_6),
        x_coord + int(x_7),
        y_coord + int(y_7),
        x_coord + int(x_8),
        y_coord + int(y_8),
        x_coord + int(x_9),
        y_coord + int(y_9),
        x_coord + int(x_10),
        y_coord + int(y_10),
        x_coord + int(x_11),
        y_coord + int(y_11),
        x_coord + int(x_12),
        y_coord + int(y_12),
        x_coord + int(x_13),
        y_coord + int(y_13),
        x_coord + int(x_14),
        y_coord + int(y_14),
        x_coord + int(x_15),
        y_coord + int(y_15),
        x_coord + int(x_16),
        y_coord + int(y_16),
        x_coord + int(x_17),
        y_coord + int(y_17),
        x_coord + int(x_18),
        y_coord + int(y_18),
        x_coord + int(x_19),
        y_coord + int(y_19),
        x_coord + int(x_20),
        y_coord + int(y_20),
        x_coord + int(x_21),
        y_coord + int(y_21),
        x_coord + int(x_22),
        y_coord + int(y_22),
        x_coord + int(x_23),
        y_coord + int(y_23),
        x_coord + int(x_24),
        y_coord + int(y_24),
        x_coord + int(x_25),
        y_coord + int(y_25),
        x_coord + int(x_26),
        y_coord + int(y_26),
        x_coord + int(x_27),
        y_coord + int(y_27),
        x_coord + int(x_28),
        y_coord + int(y_28),
        x_coord + int(x_29),
        y_coord + int(y_29),
        x_coord + int(x_30),
        y_coord + int(y_30),
        x_coord + int(x_31),
        y_coord + int(y_31),
        x_coord + int(x_32),
        y_coord + int(y_32),
        x_coord + int(x_33),
        y_coord + int(y_33),
        x_coord + int(x_34),
        y_coord + int(y_34),
        x_coord + int(x_35),
        y_coord + int(y_35),
        x_coord + int(x_36),
        y_coord + int(y_36),
        x_coord + int(x_37),
        y_coord + int(y_37),
        x_coord + int(x_38),
        y_coord + int(y_38),
        x_coord + int(x_39),
        y_coord + int(y_39),
        x_coord + int(x_40),
        y_coord + int(y_40),
        x_coord + int(x_41),
        y_coord + int(y_41),
        x_coord + int(x_42),
        y_coord + int(y_42),
        x_coord + int(x_43),
        y_coord + int(y_43),
        x_coord + int(x_44),
        y_coord + int(y_44),
        x_coord + int(x_45),
        y_coord + int(y_45),
        fill = background_colour,
        outline = component_colour,
        width = component_width
    )

def create_XOR( x_18,
                y_18,
                x_19,
                y_19,
                x_20,
                y_20,
                x_21,
                y_21,
                x_22,
                y_22,
                x_23,
                y_23,
                x_24,
                y_24,
                x_25,
                y_25,
                x_26,
                y_26,
                x_27,
                y_27,
                x_28,
                y_28,
                x_29,
                y_29,
                x_30,
                y_30,
                x_31,
                y_31,
                x_32,
                y_32,
                x_33,
                y_33,
                x_34,
                y_34,
                x_35,
                y_35,
                x_36,
                y_36,
                x_37,
                y_37,
                x_38,
                y_38,
                x_39,
                y_39,
                x_40,
                y_40,
                x_41,
                y_41,
                x_42,
                y_42,
                x_43,
                y_43,
                x_44,
                y_44,
                x_45,
                y_45):
    canvas.create_line(
        x_coord + int(x_18),
        y_coord + int(y_18),
        x_coord + int(x_19),
        y_coord + int(y_19),
        x_coord + int(x_20),
        y_coord + int(y_20),
        x_coord + int(x_21),
        y_coord + int(y_21),
        x_coord + int(x_22),
        y_coord + int(y_22),
        x_coord + int(x_23),
        y_coord + int(y_23),
        x_coord + int(x_24),
        y_coord + int(y_24),
        x_coord + int(x_25),
        y_coord + int(y_25),
        x_coord + int(x_26),
        y_coord + int(y_26),
        x_coord + int(x_27),
        y_coord + int(y_27),
        x_coord + int(x_28),
        y_coord + int(y_28),
        x_coord + int(x_29),
        y_coord + int(y_29),
        x_coord + int(x_30),
        y_coord + int(y_30),
        x_coord + int(x_31),
        y_coord + int(y_31),
        x_coord + int(x_32),
        y_coord + int(y_32),
        x_coord + int(x_33),
        y_coord + int(y_33),
        x_coord + int(x_34),
        y_coord + int(y_34),
        x_coord + int(x_35),
        y_coord + int(y_35),
        x_coord + int(x_36),
        y_coord + int(y_36),
        x_coord + int(x_37),
        y_coord + int(y_37),
        x_coord + int(x_38),
        y_coord + int(y_38),
        x_coord + int(x_39),
        y_coord + int(y_39),
        x_coord + int(x_40),
        y_coord + int(y_40),
        x_coord + int(x_41),
        y_coord + int(y_41),
        x_coord + int(x_42),
        y_coord + int(y_42),
        x_coord + int(x_43),
        y_coord + int(y_43),
        x_coord + int(x_44),
        y_coord + int(y_44),
        x_coord + int(x_45),
        y_coord + int(y_45),
        width = component_width
    )

def create_text(x, y, writing, size):
    canvas.create_text(
        x,
        y,
        fill = component_colour,
        text = writing,
        font = ('Ariel', size),
        tags = 'text'
    )

def create_overpoint(x, y):
    overpoint =  canvas.create_oval(
        x - radius,
        y - radius,
        x + radius,
        y + radius,
        fill = point_colour,
        activefill = point_hover,
        outline = '',
        tags = 'overpoint'
    )

    canvas.tag_bind(
        overpoint,
        '<Button-2>',
        delete_window().request
    )
    canvas.tag_bind(
        overpoint,
        '<Button-1>',
        draw_wire().set_start
    )
    canvas.tag_bind(
        overpoint,
        '<B1-Motion>',
        draw_wire().set_end
    )

def create_logicpoint(x, y):
    logicpoint =  canvas.create_oval(
        x - radius,
        y - radius,
        x + radius,
        y + radius,
        fill = point_colour,
        activefill = point_hover,
        outline = '',
        tags = 'logicpoint'
    )

    canvas.tag_bind(
        logicpoint,
        '<Button-2>',
        delete_logic_window().request
    )

def create_textpoint(x, y):
    textpoint =  canvas.create_oval(
        x - textpoint_radius,
        y - textpoint_radius,
        x + textpoint_radius,
        y + textpoint_radius,
        fill = point_colour,
        activefill = point_hover,
        outline = '',
        tags = 'textpoint'
    )

    canvas.tag_bind(
        textpoint,
        '<Button-2>',
        delete_text_window().request
    )

def create_junction(x, y):
    junction =  canvas.create_oval(
        x - junction_radius,
        y - junction_radius,
        x + junction_radius,
        y + junction_radius,
        fill = component_colour,
        activefill = point_hover,
        outline = '',
        tags = 'junction'
    )

    canvas.tag_bind(
        junction,
        '<Button-2>',
        delete_window().request
    )
    canvas.tag_bind(
        junction,
        '<Button-1>',
        draw_wire().set_start
    )
    canvas.tag_bind(
        junction,
        '<B1-Motion>',
        draw_wire().set_end
    )

def create_first(indicator, x, y):
    icon = Label(
        first_order,
        text = indicator,
        image = list[indicator]['Image'],
        compound = 'top',
        width = icon_width,
        height = icon_height
    )

    locator = getattr(choose_second(), indicator)

    icon.bind(
        '<Button-1>',
        locator
    )
    icon.grid(
        row = x,
        column = y
    )

def create_second(indicator, component, x, y):
    icon = Label(
        second_order,
        text = list[indicator]['Elements'][component]['Text'],
        image = list[indicator]['Elements'][component]['Image'],
        compound = 'top',
        width = icon_width,
        height = icon_height
    )

    pre_locator = getattr(draw(), indicator)
    locator = getattr(pre_locator(), component)

    icon.bind(
        '<Button-1>',
        locator().draw
    )
    icon.grid(
        row = x,
        column = y
    )

class choose_first():
    def menu(self, event):
        global x_coord, y_coord
        point = canvas.find_closest(
                    event.x,
                    event.y
                )
        x_0, y_0, x_1, y_1 = canvas.coords(point)
        x_coord = (x_0+x_1)/2
        y_coord = (y_0+y_1)/2

        self.mainfunc()

    def mainfunc(self):
        global first_order
        first_order = Toplevel(root)
        first_order.title('Choose component type.')

        i = 0
        j = 0

        for item in list:
            create_first(
                item,
                j,
                i
            )

            i += 1
            if i == 2:
                i = 0
                j += 1

class choose_text():
    def menu(self, event):
        window.destroy()

        global x_coord, y_coord
        x_coord = x_del
        y_coord = y_del

        choose_first().mainfunc()

class choose_second():
    def Text(self, event):
        global second_order
        second_order = Toplevel(root)
        second_order.title('Create text.')

        global text_entry, offset_entry

        text_request = Label(
            second_order,
            text = 'Text'
        )
        text_entry = Entry(
            second_order,
        )
        offset_request = Label(
            second_order,
            text = 'Offset'
        )
        offset_entry = Entry(
            second_order,
        )
        up_button = Button(
            second_order,
            text = 'Up'
        )
        down_button = Button(
            second_order,
            text = 'Down'
        )
        right_button = Button(
            second_order,
            text = 'Right'
        )
        left_button = Button(
            second_order,
            text = 'Left'
        )

        note = Label(
            second_order,
            text = 'Note: text size is {}.'.format(text_size)
        )

        text_request.grid(
            row = 0,
            column = 0
        )
        text_entry.grid(
            row = 0,
            column = 1
        )
        offset_request.grid(
            row = 1,
            column = 0
        )
        offset_entry.grid(
            row = 1,
            column = 1
        )
        up_button.grid(
            row = 2,
            column = 0
        )
        down_button.grid(
            row = 2,
            column = 1
        )
        right_button.grid(
            row = 3,
            column = 1
        )
        left_button.grid(
            row = 3,
            column = 0
        )
        note.grid(
            row = 4,
            column = 0
        )

        up_button.bind(
            '<Button-1>',
            draw().Text.Custom_up().draw
        )
        down_button.bind(
            '<Button-1>',
            draw().Text.Custom_down().draw
        )
        right_button.bind(
            '<Button-1>',
            draw().Text.Custom_right().draw
        )
        left_button.bind(
            '<Button-1>',
            draw().Text.Custom_left().draw
        )

    def Power(self, event):
        global second_order
        second_order = Toplevel(root)
        second_order.title('Choose component.')

        i = 0
        j = 0

        for item in list['Power']['Elements']:
            create_second(
                'Power',
                item,
                j,
                i
            )

            i += 1
            if i == 4:
                i = 0
                j += 1

    def Resistors(self, event):
        global second_order
        second_order = Toplevel(root)
        second_order.title('Choose component.')

        i = 0
        j = 0

        for item in list['Resistors']['Elements']:
            create_second(
                'Resistors',
                item,
                j,
                i
            )

            i += 1
            if i == 4:
                i = 0
                j += 1

    def Capacitors(self, event):
        global second_order
        second_order = Toplevel(root)
        second_order.title('Choose component.')

        i = 0
        j = 0

        for item in list['Capacitors']['Elements']:
            create_second(
                'Capacitors',
                item,
                j,
                i
            )

            i += 1
            if i == 4:
                i = 0
                j += 1

    def Inductors(self, event):
        global second_order
        second_order = Toplevel(root)
        second_order.title('Choose component.')

        i = 0
        j = 0

        for item in list['Inductors']['Elements']:
            create_second(
                'Inductors',
                item,
                j,
                i
            )

            i += 1
            if i == 4:
                i = 0
                j += 1

    def Diodes(self, event):
        global second_order
        second_order = Toplevel(root)
        second_order.title('Choose component.')

        i = 0
        j = 0

        for item in list['Diodes']['Elements']:
            create_second(
                'Diodes',
                item,
                j,
                i
            )

            i += 1
            if i == 4:
                i = 0
                j += 1

    def Transistors(self, event):
        global second_order
        second_order = Toplevel(root)
        second_order.title('Choose component.')

        i = 0
        j = 0

        for item in list['Transistors']['Elements']:
            create_second(
                'Transistors',
                item,
                j,
                i
            )

            i += 1
            if i == 4:
                i = 0
                j += 1

    def Logic(self, event):
        global second_order
        second_order = Toplevel(root)
        second_order.title('Choose component.')

        i = 0
        j = 0

        for item in list['Logic']['Elements']:
            create_second(
                'Logic',
                item,
                j,
                i
            )

            i += 1
            if i == 4:
                i = 0
                j += 1

    def Switches(self, event):
        global second_order
        second_order = Toplevel(root)
        second_order.title('Choose component.')

        i = 0
        j = 0

        for item in list['Switches']['Elements']:
            create_second(
                'Switches',
                item,
                j,
                i
            )

            i += 1
            if i == 4:
                i = 0
                j += 1

    def Measurement(self, event):
        global second_order
        second_order = Toplevel(root)
        second_order.title('Choose component.')

        i = 0
        j = 0

        for item in list['Measurement']['Elements']:
            create_second(
                'Measurement',
                item,
                j,
                i
            )

            i += 1
            if i == 4:
                i = 0
                j += 1

    def Other(self, event):
        global second_order
        second_order = Toplevel(root)
        second_order.title('Choose component.')

        i = 0
        j = 0

        for item in list['Other']['Elements']:
            create_second(
                'Other',
                item,
                j,
                i
            )

            i += 1
            if i == 4:
                i = 0
                j += 1

    def Formatting(self, event):
        global second_order
        second_order = Toplevel(root)
        second_order.title('Choose component.')

        i = 0
        j = 0

        for item in list['Formatting']['Elements']:
            create_second(
                'Formatting',
                item,
                j,
                i
            )

            i += 1
            if i == 4:
                i = 0
                j += 1

class draw_wire():
    def set_start(self, event):
        point = canvas.find_closest(event.x, event.y)
        x_1, y_1, x_2, y_2 = canvas.coords(point)
        global x_start, y_start
        x_start = (x_1+x_2)/2
        y_start = (y_1+y_2)/2

    def set_end(self, event):
        point = canvas.find_closest(event.x, event.y)
        if 'point' in canvas.gettags(point):
            x_1, y_1, x_2, y_2 = canvas.coords(point)
            global x_end, y_end
            x_end = (x_1+x_2)/2
            y_end = (y_1+y_2)/2
            wire = canvas.create_line(
                x_start,
                y_start,
                x_end,
                y_end,
                width = component_width,
                fill = component_colour,
                activefill = component_hover,
                tags = 'wire'
            )
            canvas.tag_lower(wire)
            canvas.tag_bind(
                wire,
                '<Button-2>',
                delete_wire().do_it
            )
        else:
            pass

class define():
    class Text:
        def Custom(self, direction):
            text_text = text_entry.get()
            text_offset = int(offset_entry.get())

            if direction == 'up':
                create_text(
                    x_coord,
                    y_coord - int(text_offset),
                    text_text,
                    text_size
                )
                create_textpoint(
                    x_coord,
                    y_coord - int(text_offset)
                )
            elif direction == 'down':
                create_text(
                    x_coord,
                    y_coord + int(text_offset),
                    text_text,
                    text_size
                )
                create_textpoint(
                    x_coord,
                    y_coord + int(text_offset)
                )
            elif direction == 'right':
                create_text(
                    x_coord + int(text_offset),
                    y_coord,
                    text_text,
                    text_size
                )
                create_textpoint(
                    x_coord + int(text_offset),
                    y_coord
                )
            elif direction == 'left':
                create_text(
                    x_coord - int(text_offset),
                    y_coord,
                    text_text,
                    text_size
                )
                create_textpoint(
                    x_coord - int(text_offset),
                    y_coord
                )

            first_order.destroy()
            second_order.destroy()
            try:
                third_order.destroy()
            except:
                pass

    class Power:
        def Cell_hor(self, rot):
            width = displacement/4
            height = displacement
            offset = displacement/6
            size = displacement/5

            x_0, y_0 = rot * matrix([[int(-width/2)],[0]])
            x_1, y_1 = rot * matrix([[int(width/2)],[0]])
            x_2, y_2 = rot * matrix([[int(-width/2)],[int(-height/4)]])
            x_3, y_3 = rot * matrix([[int(-width/2)],[int(height/4)]])
            x_4, y_4 = rot * matrix([[int(width/2)],[int(-height/2)]])
            x_5, y_5 = rot * matrix([[int(width/2)],[int(height/2)]])
            x_6, y_6 = rot * matrix([[int(width/2 + offset + size/2)],[int(-height/2)]])
            x_7, y_7 = rot * matrix([[int(width/2 + offset + size/2)],[int(-height/2 + size)]])
            x_8, y_8 = rot * matrix([[int(width/2 + offset)],[int(-height/2 + size/2)]])
            x_9, y_9 = rot * matrix([[int(width/2 + offset + size)],[int(-height/2 + size/2)]])
            x_10, y_10 = rot * matrix([[int(-width/2 - offset)],[int(-height/2 + size/2)]])
            x_11, y_11 = rot * matrix([[int(-width/2) - offset - size],[int(-height/2 + size/2)]])

            create_whiteout(
                x_0,
                y_0,
                x_1,
                y_1
            )
            create_component(
                x_2,
                y_2,
                x_3,
                y_3
            )
            create_component(
                x_4,
                y_4,
                x_5,
                y_5
            )
            create_component(
                x_6,
                y_6,
                x_7,
                y_7
            )
            create_component(
                x_8,
                y_8,
                x_9,
                y_9
            )
            create_component(
                x_10,
                y_10,
                x_11,
                y_11
            )
            create_overpoint(
                x_coord,
                y_coord
            )

            first_order.destroy()
            second_order.destroy()

        def Cell_ver(self, rot):
            width = displacement/4
            height = displacement
            offset = displacement/6
            size = displacement/5

            x_0, y_0 = rot * matrix([[int(-width/2)],[0]])
            x_1, y_1 = rot * matrix([[int(width/2)],[0]])
            x_2, y_2 = rot * matrix([[int(-width/2)],[int(-height/4)]])
            x_3, y_3 = rot * matrix([[int(-width/2)],[int(height/4)]])
            x_4, y_4 = rot * matrix([[int(width/2)],[int(-height/2)]])
            x_5, y_5 = rot * matrix([[int(width/2)],[int(height/2)]])
            x_6, y_6 = rot * matrix([[int(width/2 + offset + size/2)],[int(-height/2)]])
            x_7, y_7 = rot * matrix([[int(width/2 + offset + size/2)],[int(-height/2 + size)]])
            x_8, y_8 = rot * matrix([[int(width/2 + offset)],[int(-height/2 + size/2)]])
            x_9, y_9 = rot * matrix([[int(width/2 + offset + size)],[int(-height/2 + size/2)]])
            x_10, y_10 = rot * matrix([[int(-width/2 - offset - size/2)],[int(-height/2)]])
            x_11, y_11 = rot * matrix([[int(-width/2) - offset - size/2],[int(-height/2 + size)]])

            create_whiteout(
                x_0,
                y_0,
                x_1,
                y_1
            )
            create_component(
                x_2,
                y_2,
                x_3,
                y_3
            )
            create_component(
                x_4,
                y_4,
                x_5,
                y_5
            )
            create_component(
                x_6,
                y_6,
                x_7,
                y_7
            )
            create_component(
                x_8,
                y_8,
                x_9,
                y_9
            )
            create_component(
                x_10,
                y_10,
                x_11,
                y_11
            )
            create_overpoint(
                x_coord,
                y_coord
            )

            first_order.destroy()
            second_order.destroy()

        def Battery_hor(self, rot):
            width = 3*displacement/4
            height = displacement
            offset = displacement/10
            size = displacement/5

            x_0, y_0 = rot * matrix([[int(-width/2)],[0]])
            x_1, y_1 = rot * matrix([[int(width/2)],[0]])
            x_2, y_2 = rot * matrix([[int(-width/2)],[int(-height/4)]])
            x_3, y_3 = rot * matrix([[int(-width/2)],[int(height/4)]])
            x_4, y_4 = rot * matrix([[int(-width/6)],[int(-height/2)]])
            x_5, y_5 = rot * matrix([[int(-width/6)],[int(height/2)]])
            x_6, y_6 = rot * matrix([[int(width/6)],[int(-height/4)]])
            x_7, y_7 = rot * matrix([[int(width/6)],[int(height/4)]])
            x_8, y_8 = rot * matrix([[int(width/2)],[int(-height/2)]])
            x_9, y_9 = rot * matrix([[int(width/2)],[int(height/2)]])
            x_10, y_10 = rot * matrix([[int(width/2 + offset + size/2)],[int(-height/2)]])
            x_11, y_11 = rot * matrix([[int(width/2 + offset + size/2)],[int(-height/2 + size)]])
            x_12, y_12 = rot * matrix([[int(width/2 + offset)],[int(-height/2 + size/2)]])
            x_13, y_13 = rot * matrix([[int(width/2 + offset + size)],[int(-height/2 + size/2)]])
            x_14, y_14 = rot * matrix([[int(-width/2 - offset)],[int(-height/2 + size/2)]])
            x_15, y_15 = rot * matrix([[int(-width/2) - offset - size],[int(-height/2 + size/2)]])

            create_whiteout(
                x_0,
                y_0,
                x_1,
                y_1
            )
            create_component(
                x_2,
                y_2,
                x_3,
                y_3
            )
            create_component(
                x_4,
                y_4,
                x_5,
                y_5
            )
            create_component(
                x_6,
                y_6,
                x_7,
                y_7
            )
            create_component(
                x_8,
                y_8,
                x_9,
                y_9
            )
            create_component(
                x_10,
                y_10,
                x_11,
                y_11
            )
            create_component(
                x_12,
                y_12,
                x_13,
                y_13
            )
            create_component(
                x_14,
                y_14,
                x_15,
                y_15
            )
            create_overpoint(
                x_coord,
                y_coord
            )

            first_order.destroy()
            second_order.destroy()

        def Battery_ver(self, rot):
            width = displacement/4
            height = displacement
            offset = displacement/6
            size = displacement/5

            x_0, y_0 = rot * matrix([[int(-width/2)],[0]])
            x_1, y_1 = rot * matrix([[int(width/2)],[0]])
            x_2, y_2 = rot * matrix([[int(-width/2)],[int(-height/4)]])
            x_3, y_3 = rot * matrix([[int(-width/2)],[int(height/4)]])
            x_4, y_4 = rot * matrix([[int(width/2)],[int(-height/2)]])
            x_5, y_5 = rot * matrix([[int(width/2)],[int(height/2)]])
            x_6, y_6 = rot * matrix([[int(width/2 + offset + size/2)],[int(-height/2)]])
            x_7, y_7 = rot * matrix([[int(width/2 + offset + size/2)],[int(-height/2 + size)]])
            x_8, y_8 = rot * matrix([[int(width/2 + offset)],[int(-height/2 + size/2)]])
            x_9, y_9 = rot * matrix([[int(width/2 + offset + size)],[int(-height/2 + size/2)]])
            x_10, y_10 = rot * matrix([[int(-width/2 - offset - size/2)],[int(-height/2)]])
            x_11, y_11 = rot * matrix([[int(-width/2) - offset - size/2],[int(-height/2 + size)]])

            create_whiteout(
                x_0,
                y_0,
                x_1,
                y_1
            )
            create_component(
                x_2,
                y_2,
                x_3,
                y_3
            )
            create_component(
                x_4,
                y_4,
                x_5,
                y_5
            )
            create_component(
                x_6,
                y_6,
                x_7,
                y_7
            )
            create_component(
                x_8,
                y_8,
                x_9,
                y_9
            )
            create_component(
                x_10,
                y_10,
                x_11,
                y_11
            )
            create_overpoint(
                x_coord,
                y_coord
            )

            first_order.destroy()
            second_order.destroy()

        def Battery_ver(self, rot):
            width = 3*displacement/4
            height = displacement
            offset = displacement/10
            size = displacement/5

            x_0, y_0 = rot * matrix([[int(-width/2)],[0]])
            x_1, y_1 = rot * matrix([[int(width/2)],[0]])
            x_2, y_2 = rot * matrix([[int(-width/2)],[int(-height/4)]])
            x_3, y_3 = rot * matrix([[int(-width/2)],[int(height/4)]])
            x_4, y_4 = rot * matrix([[int(-width/6)],[int(-height/2)]])
            x_5, y_5 = rot * matrix([[int(-width/6)],[int(height/2)]])
            x_6, y_6 = rot * matrix([[int(width/6)],[int(-height/4)]])
            x_7, y_7 = rot * matrix([[int(width/6)],[int(height/4)]])
            x_8, y_8 = rot * matrix([[int(width/2)],[int(-height/2)]])
            x_9, y_9 = rot * matrix([[int(width/2)],[int(height/2)]])
            x_10, y_10 = rot * matrix([[int(width/2 + offset + size/2)],[int(-height/2)]])
            x_11, y_11 = rot * matrix([[int(width/2 + offset + size/2)],[int(-height/2 + size)]])
            x_12, y_12 = rot * matrix([[int(width/2 + offset)],[int(-height/2 + size/2)]])
            x_13, y_13 = rot * matrix([[int(width/2 + offset + size)],[int(-height/2 + size/2)]])
            x_14, y_14 = rot * matrix([[int(-width/2 - offset)],[int(-height/2)]])
            x_15, y_15 = rot * matrix([[int(-width/2) - offset],[int(-height/2 + size)]])

            create_whiteout(
                x_0,
                y_0,
                x_1,
                y_1
            )
            create_component(
                x_2,
                y_2,
                x_3,
                y_3
            )
            create_component(
                x_4,
                y_4,
                x_5,
                y_5
            )
            create_component(
                x_6,
                y_6,
                x_7,
                y_7
            )
            create_component(
                x_8,
                y_8,
                x_9,
                y_9
            )
            create_component(
                x_10,
                y_10,
                x_11,
                y_11
            )
            create_component(
                x_12,
                y_12,
                x_13,
                y_13
            )
            create_component(
                x_14,
                y_14,
                x_15,
                y_15
            )
            create_overpoint(
                x_coord,
                y_coord
            )

            first_order.destroy()
            second_order.destroy()

        def DC_hor(self, rot):
            diameter = displacement/1.25
            offset = diameter/4
            width = diameter/4

            x_0, y_0 = rot * matrix([[int(-diameter/2)],[int(-diameter/2)]])
            x_1, y_1 = rot * matrix([[int(diameter/2)],[int(diameter/2)]])
            x_2, y_2 = rot * matrix([[int(-offset - width/2)],[int(0)]])
            x_3, y_3 = rot * matrix([[int(-offset + width/2)],[int(0)]])
            x_4, y_4 = rot * matrix([[int(offset - width/2)],[int(0)]])
            x_5, y_5 = rot * matrix([[int(offset + width/2)],[int(0)]])
            x_6, y_6 = rot * matrix([[int(offset)],[int(-width/2)]])
            x_7, y_7 = rot * matrix([[int(offset)],[int(width/2)]])

            create_circle(
                x_0,
                y_0,
                x_1,
                y_1
            )
            create_component(
                x_2,
                y_2,
                x_3,
                y_3
            )
            create_component(
                x_4,
                y_4,
                x_5,
                y_5
            )
            create_component(
                x_6,
                y_6,
                x_7,
                y_7
            )
            create_overpoint(
                x_coord,
                y_coord
            )

            first_order.destroy()
            second_order.destroy()

        def DC_ver(self, rot):
            diameter = displacement/1.25
            offset = diameter/4
            width = diameter/4

            x_0, y_0 = rot * matrix([[int(-diameter/2)],[int(-diameter/2)]])
            x_1, y_1 = rot * matrix([[int(diameter/2)],[int(diameter/2)]])
            x_2, y_2 = rot * matrix([[int(-offset)],[int(-width/2)]])
            x_3, y_3 = rot * matrix([[int(-offset)],[int(width/2)]])
            x_4, y_4 = rot * matrix([[int(offset - width/2)],[int(0)]])
            x_5, y_5 = rot * matrix([[int(offset + width/2)],[int(0)]])
            x_6, y_6 = rot * matrix([[int(offset)],[int(-width/2)]])
            x_7, y_7 = rot * matrix([[int(offset)],[int(width/2)]])

            create_circle(
                x_0,
                y_0,
                x_1,
                y_1
            )
            create_component(
                x_2,
                y_2,
                x_3,
                y_3
            )
            create_component(
                x_4,
                y_4,
                x_5,
                y_5
            )
            create_component(
                x_6,
                y_6,
                x_7,
                y_7
            )
            create_overpoint(
                x_coord,
                y_coord
            )

            first_order.destroy()
            second_order.destroy()

        def AC(self, rot):
            diameter = displacement/1.25
            width = diameter/2

            x_0, y_0 = rot * matrix([[int(-diameter/2)],[int(-diameter/2)]])
            x_1, y_1 = rot * matrix([[int(diameter/2)],[int(diameter/2)]])
            x_2, y_2 = rot * matrix([[int(-width/2)],[int(-width/2)]])
            x_3, y_3 = rot * matrix([[int(width/2)],[int(width/2)]])

            create_circle(
                x_0,
                y_0,
                x_1,
                y_1
            )
            create_wave(
                x_2,
                y_2,
                x_3,
                y_3,
                0
            )
            create_overpoint(
                x_coord,
                y_coord
            )

            first_order.destroy()
            second_order.destroy()

        def Ground_1(self, rot):
            height = int(displacement/4)
            width_1 = displacement/1.25
            width_2 = width_1 * (2/3)
            width_3 = width_1 * (1/3)

            x_0, y_0 = rot * matrix([[int(0)],[-height/2]])
            x_1, y_1 = rot * matrix([[int(0)],[height/2]])
            x_2, y_2 = rot * matrix([[int(-width_1/2)],[int(-height/2)]])
            x_3, y_3 = rot * matrix([[int(width_1/2)],[int(-height/2)]])
            x_4, y_4 = rot * matrix([[int(-width_2/2)],[int(0)]])
            x_5, y_5 = rot * matrix([[int(width_2/2)],[int(0)]])
            x_6, y_6 = rot * matrix([[int(-width_3/2)],[int(height/2)]])
            x_7, y_7 = rot * matrix([[int(width_3/2)],[int(height/2)]])

            create_whiteout(
                x_0,
                y_0,
                x_1,
                y_1
            )
            create_component(
                x_2,
                y_2,
                x_3,
                y_3
            )
            create_component(
                x_4,
                y_4,
                x_5,
                y_5
            )
            create_component(
                x_6,
                y_6,
                x_7,
                y_7
            )
            create_overpoint(
                x_coord,
                y_coord
            )

            first_order.destroy()
            second_order.destroy()

        def Ground_2(self, rot):
            width = displacement/2
            height = displacement/4
            offset = width/3

            x_0, y_0 = rot * matrix([[int(0)],[int(-height/2)]])
            x_1, y_1 = rot * matrix([[int(0)],[int(height/2)]])
            x_2, y_2 = rot * matrix([[int(-width/2)],[int(-height/2)]])
            x_3, y_3 = rot * matrix([[int(width/2)],[int(-height/2)]])
            x_4, y_4 = rot * matrix([[int(-width/2)],[int(-height/2)]])
            x_5, y_5 = rot * matrix([[int(-width/2 - offset)],[int(height/2)]])
            x_6, y_6 = rot * matrix([[int(0)],[int(-height/2)]])
            x_7, y_7 = rot * matrix([[int(-offset)],[int(height/2)]])
            x_8, y_8 = rot * matrix([[int(width/2)],[-height/2]])
            x_9, y_9 = rot * matrix([[int(width/2 - offset)],[height/2]])

            create_whiteout(
                x_0,
                y_0,
                x_1,
                y_1
            )
            create_component(
                x_2,
                y_2,
                x_3,
                y_3
            )
            create_component(
                x_4,
                y_4,
                x_5,
                y_5
            )
            create_component(
                x_6,
                y_6,
                x_7,
                y_7
            )
            create_component(
                x_8,
                y_8,
                x_9,
                y_9
            )
            create_overpoint(
                x_coord,
                y_coord
            )

            first_order.destroy()
            second_order.destroy()

        def Fuse(self, rot, angle):
            width = displacement/2

            x_0, y_0 = rot * matrix([[int(-width/2)],[0]])
            x_1, y_1 = rot * matrix([[int(width/2)],[0]])
            x_2, y_2 = rot * matrix([[int(-width/2)],[int(-width/2)]])
            x_3, y_3 = rot * matrix([[int(width/2)],[int(width/2)]])

            create_whiteout(
                x_0,
                y_0,
                x_1,
                y_1
            )
            create_wave(
                x_2,
                y_2,
                x_3,
                y_3,
                angle
            )
            create_overpoint(
                x_coord,
                y_coord
            )

            first_order.destroy()
            second_order.destroy()

    class Resistors:
        def Resistor_US(self, rot):
            height = displacement/3
            width = displacement/1.25
            point = width/12

            x_0, y_0 = rot * matrix([[int(-width/2)],[int(0)]])
            x_1, y_1 = rot * matrix([[int(width/2)],[int(0)]])
            x_2, y_2 = rot * matrix([[int(-width/2 + point*0)],[int(0)]])
            x_3, y_3 = rot * matrix([[int(-width/2 + point*1)],[int(-height/2)]])
            x_4, y_4 = rot * matrix([[int(-width/2 + point*1)],[int(-height/2)]])
            x_5, y_5 = rot * matrix([[int(-width/2 + point*3)],[int(height/2)]])
            x_6, y_6 = rot * matrix([[int(-width/2 + point*3)],[int(height/2)]])
            x_7, y_7 = rot * matrix([[int(-width/2 + point*5)],[int(-height/2)]])
            x_8, y_8 = rot * matrix([[int(-width/2 + point*5)],[int(-height/2)]])
            x_9, y_9 = rot * matrix([[int(-width/2 + point*7)],[int(height/2)]])
            x_10, y_10 = rot * matrix([[int(-width/2 + point*7)],[int(height/2)]])
            x_11, y_11 = rot * matrix([[int(-width/2 + point*9)],[int(-height/2)]])
            x_12, y_12 = rot * matrix([[int(-width/2 + point*9)],[int(-height/2)]])
            x_13, y_13 = rot * matrix([[int(-width/2 + point*11)],[int(height/2)]])
            x_14, y_14 = rot * matrix([[int(-width/2 + point*11)],[int(height/2)]])
            x_15, y_15 = rot * matrix([[int(-width/2 + point*12)],[int(0)]])

            create_whiteout(
                x_0,
                y_0,
                x_1,
                y_1
            )
            create_component(
                x_2,
                y_2,
                x_3,
                y_3
            )
            create_component(
                x_4,
                y_4,
                x_5,
                y_5
            )
            create_component(
                x_6,
                y_6,
                x_7,
                y_7
            )
            create_component(
                x_8,
                y_8,
                x_9,
                y_9
            )
            create_component(
                x_10,
                y_10,
                x_11,
                y_11
            )
            create_component(
                x_12,
                y_12,
                x_13,
                y_13
            )
            create_component(
                x_14,
                y_14,
                x_15,
                y_15
            )
            create_overpoint(
                x_coord,
                y_coord
            )

            first_order.destroy()
            second_order.destroy()

        def Resistor_EU(self, rot):
            height = displacement/4
            width = displacement/1.25

            x_0, y_0 = rot * matrix([[int(-width/2)],[int(-height/2)]])
            x_1, y_1 = rot * matrix([[int(width/2)],[int(height/2)]])

            create_rectangle(
                x_0,
                y_0,
                x_1,
                y_1
            )
            create_overpoint(
                x_coord,
                y_coord
            )

            first_order.destroy()
            second_order.destroy()

    class Capacitors:
        def Capacitor(self, rot):
            width = int(displacement/5)
            height = displacement/1.25

            x_0, y_0 = rot * matrix([[int(-width/2)],[0]])
            x_1, y_1 = rot * matrix([[int(width/2)],[0]])
            x_2, y_2 = rot * matrix([[int(-width/2)],[int(-height/2)]])
            x_3, y_3 = rot * matrix([[int(-width/2)],[int(height/2)]])
            x_4, y_4 = rot * matrix([[int(width/2)],[int(-height/2)]])
            x_5, y_5 = rot * matrix([[int(width/2)],[int(height/2)]])

            create_whiteout(
                x_0,
                y_0,
                x_1,
                y_1
            )
            create_component(
                x_2,
                y_2,
                x_3,
                y_3
            )
            create_component(
                x_4,
                y_4,
                x_5,
                y_5
            )
            create_overpoint(
                x_coord,
                y_coord
            )

            first_order.destroy()
            second_order.destroy()

        def Pol_cap(self, rot):
            height = displacement/1.25
            width = height/5
            bend = height/5
            size = height/5
            offset = height/5

            x_0, y_0 = rot * matrix([[int(-width/2)],[0]])
            x_1, y_1 = rot * matrix([[int(width/2)],[0]])
            x_2, y_2 = rot * matrix([[int(-width/2 - bend)],[int(-height/2)]])
            x_3, y_3 = rot * matrix([[int(-width/2)],[int(height/2)]])
            x_4, y_4 = rot * matrix([[int(width/2)],[int(-height/2)]])
            x_5, y_5 = rot * matrix([[int(width/2)],[int(height/2)]])
            x_6, y_6 = rot * matrix([[int(width/2 + offset + size/2)],[int(-height/2)]])
            x_7, y_7 = rot * matrix([[int(width/2) + offset + size/2],[int(-height/2 + size)]])
            x_8, y_8 = rot * matrix([[int(width/2 + offset)],[int(-height/2 + size/2)]])
            x_9, y_9 = rot * matrix([[int(width/2) + offset + size],[int(-height/2 + size/2)]])

            if rot[0,0] == 1 and rot[0,1] == 0:
                angle = -90

            elif rot[0,0] == 0 and rot[0,1] == 1:
                angle = 0

            elif rot[0,0] == -1 and rot[0,1] == 0:
                angle = 90

            elif rot[0,0] == 0 and rot[0,1] == -1:
                angle = 180

            create_whiteout(
                x_0,
                y_0,
                x_1,
                y_1
            )
            create_arc(
                x_2,
                y_2,
                x_3,
                y_3,
                angle
            )
            create_component(
                x_4,
                y_4,
                x_5,
                y_5
            )
            create_component(
                x_6,
                y_6,
                x_7,
                y_7
            )
            create_component(
                x_8,
                y_8,
                x_9,
                y_9
            )
            create_overpoint(
                x_coord,
                y_coord
            )

            first_order.destroy()
            second_order.destroy()

    class Inductors:
        def Inductor(self, rot):
            height = displacement/5
            width = displacement
            point = displacement/4

            x_0, y_0 = rot_up * rot * matrix([[int(-width/2)],[0]])
            x_1, y_1 = rot_up * rot * matrix([[int(width/2)],[0]])
            x_2, y_2 = rot_up * rot * matrix([[int(-width/2 + point*0)],[int(-height/2)]])
            x_3, y_3 = rot_up * rot * matrix([[int(-width/2 + point*1)],[int(height/2)]])
            x_4, y_4 = rot_up * rot * matrix([[int(-width/2 + point*1)],[int(-height/2)]])
            x_5, y_5 = rot_up * rot * matrix([[int(-width/2 + point*2)],[int(height/2)]])
            x_6, y_6 = rot_up * rot * matrix([[int(-width/2 + point*2)],[int(-height/2)]])
            x_7, y_7 = rot_up * rot * matrix([[int(-width/2 + point*3)],[int(height/2)]])
            x_8, y_8 = rot_up * rot * matrix([[int(-width/2 + point*3)],[int(-height/2)]])
            x_9, y_9 = rot_up * rot * matrix([[int(-width/2 + point*4)],[int(height/2)]])

            if rot[0,0] == 1 and rot[0,1] == 0:
                angle = -90

            elif rot[0,0] == 0 and rot[0,1] == 1:
                angle = 0

            elif rot[0,0] == -1 and rot[0,1] == 0:
                angle = 90

            elif rot[0,0] == 0 and rot[0,1] == -1:
                angle = 180

            create_whiteout(
                x_0,
                y_0,
                x_1,
                y_1
            )
            create_arc(
                x_2,
                y_2,
                x_3,
                y_3,
                angle
            )
            create_arc(
                x_4,
                y_4,
                x_5,
                y_5,
                angle
            )
            create_arc(
                x_6,
                y_6,
                x_7,
                y_7,
                angle
            )
            create_arc(
                x_8,
                y_8,
                x_9,
                y_9,
                angle
            )
            create_overpoint(
                x_coord,
                y_coord
            )

            first_order.destroy()
            second_order.destroy()

    class Diodes:
        def Diode(self, rot):
            width = displacement/2
            height = width/0.866

            x_0, y_0 = rot * matrix([[int(-width/2)],[-height/2]])
            x_1, y_1 = rot * matrix([[int(width/2)],[0]])
            x_2, y_2 = rot * matrix([[int(-width/2)],[int(height/2)]])
            x_3, y_3 = rot * matrix([[int(width/2)],[int(-height/2)]])
            x_4, y_4 = rot * matrix([[int(width/2)],[int(height/2)]])

            create_triangle(
                x_0,
                y_0,
                x_1,
                y_1,
                x_2,
                y_2
            )
            create_component(
                x_3,
                y_3,
                x_4,
                y_4
            )
            create_overpoint(
                x_coord,
                y_coord
            )

            first_order.destroy()
            second_order.destroy()

        def Zener(self, rot):
            width = displacement/2
            height = width/0.866
            offset = width/3

            x_0, y_0 = rot * matrix([[int(-width/2)],[-height/2]])
            x_1, y_1 = rot * matrix([[int(width/2)],[0]])
            x_2, y_2 = rot * matrix([[int(-width/2)],[int(height/2)]])
            x_3, y_3 = rot * matrix([[int(width/2)],[int(-height/2)]])
            x_4, y_4 = rot * matrix([[int(width/2)],[int(height/2)]])
            x_5, y_5 = rot * matrix([[int(width/2)],[int(-height/2)]])
            x_6, y_6 = rot * matrix([[int(width/2 + offset)],[int(-height/2 - offset)]])
            x_7, y_7 = rot * matrix([[int(width/2)],[int(height/2)]])
            x_8, y_8 = rot * matrix([[int(width/2 - offset)],[int(height/2 + offset)]])

            create_triangle(
                x_0,
                y_0,
                x_1,
                y_1,
                x_2,
                y_2
            )
            create_component(
                x_3,
                y_3,
                x_4,
                y_4
            )
            create_component(
                x_5,
                y_5,
                x_6,
                y_6
            )
            create_component(
                x_7,
                y_7,
                x_8,
                y_8
            )
            create_overpoint(
                x_coord,
                y_coord
            )

            first_order.destroy()
            second_order.destroy()

        def Schottky(self, rot):
            width = displacement/2
            height = width/0.866
            offset = width/4

            x_0, y_0 = rot * matrix([[int(-width/2)],[-height/2]])
            x_1, y_1 = rot * matrix([[int(width/2)],[0]])
            x_2, y_2 = rot * matrix([[int(-width/2)],[int(height/2)]])
            x_3, y_3 = rot * matrix([[int(width/2)],[int(-height/2)]])
            x_4, y_4 = rot * matrix([[int(width/2)],[int(height/2)]])
            x_5, y_5 = rot * matrix([[int(width/2)],[int(-height/2)]])
            x_6, y_6 = rot * matrix([[int(width/2 + offset)],[int(-height/2)]])
            x_7, y_7 = rot * matrix([[int(width/2 + offset)],[int(-height/2)]])
            x_8, y_8 = rot * matrix([[int(width/2 + offset)],[int(-height/2 + offset)]])
            x_9, y_9 = rot * matrix([[int(width/2)],[int(height/2)]])
            x_10, y_10 = rot * matrix([[int(width/2 - offset)],[int(height/2)]])
            x_11, y_11 = rot * matrix([[int(width/2 - offset)],[int(height/2)]])
            x_12, y_12 = rot * matrix([[int(width/2 - offset)],[int(height/2 - offset)]])

            create_triangle(
                x_0,
                y_0,
                x_1,
                y_1,
                x_2,
                y_2
            )
            create_component(
                x_3,
                y_3,
                x_4,
                y_4
            )
            create_component(
                x_5,
                y_5,
                x_6,
                y_6
            )
            create_component(
                x_7,
                y_7,
                x_8,
                y_8
            )
            create_component(
                x_9,
                y_9,
                x_10,
                y_10
            )
            create_component(
                x_11,
                y_11,
                x_12,
                y_12
            )
            create_overpoint(
                x_coord,
                y_coord
            )

            first_order.destroy()
            second_order.destroy()

        def LED(self, rot):
            width = displacement/2
            height = width/0.866
            offset = displacement/5
            extent = displacement/4

            x_0, y_0 = rot * matrix([[int(-width/2)],[-height/2]])
            x_1, y_1 = rot * matrix([[int(width/2)],[0]])
            x_2, y_2 = rot * matrix([[int(-width/2)],[int(height/2)]])
            x_3, y_3 = rot * matrix([[int(width/2)],[int(-height/2)]])
            x_4, y_4 = rot * matrix([[int(width/2)],[int(height/2)]])
            x_5, y_5 = rot * matrix([[int(-width/4)],[int(-height/1.8)]])
            x_6, y_6 = rot * matrix([[int(-width/4 + offset)],[int(-height/1.8 - extent)]])
            x_7, y_7 = rot * matrix([[int(width/8)],[int(-height/2.5)]])
            x_8, y_8 = rot * matrix([[int(width/8 + offset)],[int(-height/2.5 - extent)]])

            create_triangle(
                x_0,
                y_0,
                x_1,
                y_1,
                x_2,
                y_2
            )
            create_component(
                x_3,
                y_3,
                x_4,
                y_4
            )
            create_arrow(
                x_5,
                y_5,
                x_6,
                y_6
            )
            create_arrow(
                x_7,
                y_7,
                x_8,
                y_8
            )
            create_overpoint(
                x_coord,
                y_coord
            )

            first_order.destroy()
            second_order.destroy()

    class Transistors:
        def NPN(self, rot):
            diameter = displacement
            offset = diameter/5
            extent = ((diameter/2)**2 - offset**2)**(1/2)
            height = diameter/2
            base = diameter/3
            joint = height/4

            x_0, y_0 = rot * matrix([[int(-diameter/2 - offset)],[-diameter/2]])
            x_1, y_1 = rot * matrix([[int(diameter/2 - offset)],[diameter/2]])
            x_2, y_2 = rot * matrix([[int(-diameter/2 - offset)],[int(0)]])
            x_3, y_3 = rot * matrix([[int(-diameter/2 - offset + base)],[int(0)]])
            x_4, y_4 = rot * matrix([[int(-diameter/2 - offset + base)],[int(-height/2)]])
            x_5, y_5 = rot * matrix([[int(-diameter/2 - offset + base)],[int(height/2)]])
            x_6, y_6 = rot * matrix([[int(0)],[int(-extent)]])
            x_7, y_7 = rot * matrix([[int(-diameter/2 - offset + base)],[int(-height/2 + joint)]])
            x_8, y_8 = rot * matrix([[int(-diameter/2 - offset + base)],[int(height/2 - joint)]])
            x_9, y_9 = rot * matrix([[int(0)],[int(extent)]])

            create_circle(
                x_0,
                y_0,
                x_1,
                y_1
            )
            create_component(
                x_2,
                y_2,
                x_3,
                y_3
            )
            create_component(
                x_4,
                y_4,
                x_5,
                y_5
            )
            create_component(
                x_6,
                y_6,
                x_7,
                y_7
            )
            create_arrow(
                x_8,
                y_8,
                x_9,
                y_9
            )
            create_overpoint(
                x_coord,
                y_coord
            )

            first_order.destroy()
            second_order.destroy()

        def PNP(self, rot):
            diameter = displacement
            offset = diameter/5
            extent = ((diameter/2)**2 - offset**2)**(1/2)
            height = diameter/2
            base = diameter/3
            joint = height/4

            x_0, y_0 = rot * matrix([[int(-diameter/2 - offset)],[-diameter/2]])
            x_1, y_1 = rot * matrix([[int(diameter/2 - offset)],[diameter/2]])
            x_2, y_2 = rot * matrix([[int(-diameter/2 - offset)],[int(0)]])
            x_3, y_3 = rot * matrix([[int(-diameter/2 - offset + base)],[int(0)]])
            x_4, y_4 = rot * matrix([[int(-diameter/2 - offset + base)],[int(-height/2)]])
            x_5, y_5 = rot * matrix([[int(-diameter/2 - offset + base)],[int(height/2)]])
            x_6, y_6 = rot * matrix([[int(0)],[int(-extent)]])
            x_7, y_7 = rot * matrix([[int(-diameter/2 - offset + base)],[int(-height/2 + joint)]])
            x_8, y_8 = rot * matrix([[int(-diameter/2 - offset + base)],[int(height/2 - joint)]])
            x_9, y_9 = rot * matrix([[int(0)],[int(extent)]])

            create_circle(
                x_0,
                y_0,
                x_1,
                y_1
            )
            create_component(
                x_2,
                y_2,
                x_3,
                y_3
            )
            create_component(
                x_4,
                y_4,
                x_5,
                y_5
            )
            create_arrow(
                x_6,
                y_6,
                x_7,
                y_7
            )
            create_component(
                x_8,
                y_8,
                x_9,
                y_9
            )
            create_overpoint(
                x_coord,
                y_coord
            )

            first_order.destroy()
            second_order.destroy()

        def NMOS(self, rot):
            diameter = displacement
            offset = diameter/5
            extent = ((diameter/2)**2 - offset**2)**0.5
            height = diameter/2
            base = diameter/3
            lift = height/2
            retract = ((diameter/2)**2 - lift**2)**0.5
            little = height/3

            x_0, y_0 = rot * matrix([[int(-diameter/2 - offset)],[int(-diameter/2 - lift)]])
            x_1, y_1 = rot * matrix([[int(diameter/2 - offset)],[int(diameter/2 - lift)]])
            x_2, y_2 = rot * matrix([[int(-offset - retract)],[int(0)]])
            x_3, y_3 = rot * matrix([[int(-diameter/2 - offset + base)],[int(0)]])
            x_4, y_4 = rot * matrix([[int(-diameter/2 - offset + base)],[int(0)]])
            x_5, y_5 = rot * matrix([[int(-diameter/2 - offset + base)],[int(-height)]])
            x_6, y_6 = rot * matrix([[0],[0]])
            x_7, y_7 = rot * matrix([[int(-height/2)],[0]])
            x_8, y_8 = rot * matrix([[0],[int(-height/2)]])
            x_9, y_9 = rot * matrix([[int(-height/2)],[int(-height/2)]])
            x_10, y_10 = rot * matrix([[0],[int(-height)]])
            x_11, y_11 = rot * matrix([[int(-height/2)],[int(-height)]])
            x_12, y_12 = rot * matrix([[0],[int(-extent - lift)]])
            x_13, y_13 = rot * matrix([[0],[int(-height)]])
            x_14, y_14 = rot * matrix([[0],[int(-height/2)]])
            x_15, y_15 = rot * matrix([[0],[int(extent - lift)]])
            x_16, y_16 = rot * matrix([[int(-height/2)],[int(-height - little/2)]])
            x_17, y_17 = rot * matrix([[int(-height/2)],[int(-height + little/2)]])
            x_18, y_18 = rot * matrix([[int(-height/2)],[int(-height/2 - little/2)]])
            x_19, y_19 = rot * matrix([[int(-height/2)],[int(-height/2 + little/2)]])
            x_20, y_20 = rot * matrix([[int(-height/2)],[int(-little/2)]])
            x_21, y_21 = rot * matrix([[int(-height/2)],[int(little/2)]])

            create_circle(
                x_0,
                y_0,
                x_1,
                y_1
            )
            create_component(
                x_2,
                y_2,
                x_3,
                y_3
            )
            create_component(
                x_4,
                y_4,
                x_5,
                y_5
            )
            create_component(
                x_6,
                y_6,
                x_7,
                y_7
            )
            create_arrow(
                x_8,
                y_8,
                x_9,
                y_9
            )
            create_component(
                x_10,
                y_10,
                x_11,
                y_11
            )
            create_component(
                x_12,
                y_12,
                x_13,
                y_13
            )
            create_component(
                x_14,
                y_14,
                x_15,
                y_15
            )
            create_component(
                x_16,
                y_16,
                x_17,
                y_17
            )
            create_component(
                x_18,
                y_18,
                x_19,
                y_19
            )
            create_component(
                x_20,
                y_20,
                x_21,
                y_21
            )
            create_overpoint(
                x_coord,
                y_coord
            )

            first_order.destroy()
            second_order.destroy()

        def PMOS(self, rot):
            diameter = displacement
            offset = diameter/5
            extent = ((diameter/2)**2 - offset**2)**0.5
            height = diameter/2
            base = diameter/3
            lift = height/2
            retract = ((diameter/2)**2 - lift**2)**0.5
            little = height/3

            x_0, y_0 = rot * matrix([[int(-diameter/2 - offset)],[int(-diameter/2 + lift)]])
            x_1, y_1 = rot * matrix([[int(diameter/2 - offset)],[int(diameter/2 + lift)]])
            x_2, y_2 = rot * matrix([[int(-offset - retract)],[int(0)]])
            x_3, y_3 = rot * matrix([[int(-diameter/2 - offset + base)],[int(0)]])
            x_4, y_4 = rot * matrix([[int(-diameter/2 - offset + base)],[int(0)]])
            x_5, y_5 = rot * matrix([[int(-diameter/2 - offset + base)],[int(height)]])
            x_6, y_6 = rot * matrix([[0],[0]])
            x_7, y_7 = rot * matrix([[int(-height/2)],[0]])
            x_8, y_8 = rot * matrix([[0],[int(height/2)]])
            x_9, y_9 = rot * matrix([[int(-height/2)],[int(height/2)]])
            x_10, y_10 = rot * matrix([[0],[int(height)]])
            x_11, y_11 = rot * matrix([[int(-height/2)],[int(height)]])
            x_12, y_12 = rot * matrix([[0],[int(-extent + lift)]])
            x_13, y_13 = rot * matrix([[0],[int(height/2)]])
            x_14, y_14 = rot * matrix([[0],[int(height)]])
            x_15, y_15 = rot * matrix([[0],[int(extent + lift)]])
            x_16, y_16 = rot * matrix([[int(-height/2)],[int(height - little/2)]])
            x_17, y_17 = rot * matrix([[int(-height/2)],[int(height + little/2)]])
            x_18, y_18 = rot * matrix([[int(-height/2)],[int(height/2 - little/2)]])
            x_19, y_19 = rot * matrix([[int(-height/2)],[int(height/2 + little/2)]])
            x_20, y_20 = rot * matrix([[int(-height/2)],[int(-little/2)]])
            x_21, y_21 = rot * matrix([[int(-height/2)],[int(little/2)]])

            create_circle(
                x_0,
                y_0,
                x_1,
                y_1
            )
            create_component(
                x_2,
                y_2,
                x_3,
                y_3
            )
            create_component(
                x_4,
                y_4,
                x_5,
                y_5
            )
            create_component(
                x_6,
                y_6,
                x_7,
                y_7
            )
            create_arrow(
                x_9,
                y_9,
                x_8,
                y_8
            )
            create_component(
                x_10,
                y_10,
                x_11,
                y_11
            )
            create_component(
                x_12,
                y_12,
                x_13,
                y_13
            )
            create_component(
                x_14,
                y_14,
                x_15,
                y_15
            )
            create_component(
                x_16,
                y_16,
                x_17,
                y_17
            )
            create_component(
                x_18,
                y_18,
                x_19,
                y_19
            )
            create_component(
                x_20,
                y_20,
                x_21,
                y_21
            )
            create_overpoint(
                x_coord,
                y_coord
            )

            first_order.destroy()
            second_order.destroy()

    class Logic:
        def Buffer(self, rot):
            width = displacement
            height = width/0.866

            x_0, y_0 = rot * matrix([[int(-width/2)],[-height/2]])
            x_1, y_1 = rot * matrix([[int(width/2)],[0]])
            x_2, y_2 = rot * matrix([[int(-width/2)],[int(height/2)]])

            create_triangle(
                x_0,
                y_0,
                x_1,
                y_1,
                x_2,
                y_2
            )
            create_overpoint(
                x_coord,
                y_coord
            )

            first_order.destroy()
            second_order.destroy()

        def Inverter(self, rot):
            diameter = displacement*3*0.134
            offset = displacement/2

            x_0, y_0 = rot * matrix([[offset],[-diameter/2]])
            x_1, y_1 = rot * matrix([[offset + diameter],[diameter/2]])

            create_circle(
                x_0,
                y_0,
                x_1,
                y_1
            )
            create_overpoint(
                x_coord,
                y_coord
            )

            first_order.destroy()
            second_order.destroy()

        def NOT(self, rot):
            diameter = displacement*3*0.134
            offset = displacement*3*0.866

            x_0, y_0 = rot * matrix([[offset],[-diameter/2]])
            x_1, y_1 = rot * matrix([[offset + diameter],[diameter/2]])

            create_circle(
                x_0,
                y_0,
                x_1,
                y_1
            )

            first_order.destroy()
            second_order.destroy()

        def AND(self, rot):
            height = displacement*2.5
            width = displacement*3*0.866
            offset = displacement*1.5

            x_0, y_0 = rot * matrix([[0],[height/2]])
            x_1, y_1 = rot * matrix([[width - offset],[height/2]])
            x_2, y_2 = rot * matrix([[width - offset + offset*0.1],[height/2*0.995]])
            x_3, y_3 = rot * matrix([[width - offset + offset*0.2],[height/2*0.98]])
            x_4, y_4 = rot * matrix([[width - offset + offset*0.3],[height/2*0.954]])
            x_5, y_5 = rot * matrix([[width - offset + offset*0.4],[height/2*0.917]])
            x_6, y_6 = rot * matrix([[width - offset + offset*0.5],[height/2*0.866]])
            x_7, y_7 = rot * matrix([[width - offset + offset*0.6],[height/2*0.8]])
            x_8, y_8 = rot * matrix([[width - offset + offset*0.7],[height/2*0.714]])
            x_9, y_9 = rot * matrix([[width - offset + offset*0.8],[height/2*0.6]])
            x_10, y_10 = rot * matrix([[width - offset + offset*0.9],[height/2*0.436]])
            x_11, y_11 = rot * matrix([[width - offset + offset*1],[height/2*0.0]])
            x_12, y_12 = rot * matrix([[width - offset + offset*0.9],[height/2*-0.436]])
            x_13, y_13 = rot * matrix([[width - offset + offset*0.8],[height/2*-0.6]])
            x_14, y_14 = rot * matrix([[width - offset + offset*0.7],[height/2*-0.714]])
            x_15, y_15 = rot * matrix([[width - offset + offset*0.6],[height/2*-0.8]])
            x_16, y_16 = rot * matrix([[width - offset + offset*0.5],[height/2*-0.866]])
            x_17, y_17 = rot * matrix([[width - offset + offset*0.4],[height/2*-0.917]])
            x_18, y_18 = rot * matrix([[width - offset + offset*0.3],[height/2*-0.954]])
            x_19, y_19 = rot * matrix([[width - offset + offset*0.2],[height/2*-0.98]])
            x_20, y_20 = rot * matrix([[width - offset + offset*0.1],[height/2*-0.995]])
            x_21, y_21 = rot * matrix([[width - offset],[-height/2]])
            x_22, y_22 = rot * matrix([[0],[-height/2]])

            x_50, y_50 = rot * matrix([[int(width)],[int(0)]])
            x_51, y_51 = rot * matrix([[int(width/0.866)],[int(0)]])

            create_component(
                x_50,
                y_50,
                x_51,
                y_51
            )

            create_AND(
                x_0,
                y_0,
                x_1,
                y_1,
                x_2,
                y_2,
                x_3,
                y_3,
                x_4,
                y_4,
                x_5,
                y_5,
                x_6,
                y_6,
                x_7,
                y_7,
                x_8,
                y_8,
                x_9,
                y_9,
                x_10,
                y_10,
                x_11,
                y_11,
                x_12,
                y_12,
                x_13,
                y_13,
                x_14,
                y_14,
                x_15,
                y_15,
                x_16,
                y_16,
                x_17,
                y_17,
                x_18,
                y_18,
                x_19,
                y_19,
                x_20,
                y_20,
                x_21,
                y_21,
                x_22,
                y_22
            )
            create_logicpoint(
                x_coord,
                y_coord
            )

            first_order.destroy()
            second_order.destroy()

        def OR(self, rot):
            height = displacement*2.5
            width = displacement*3

            x_0, y_0 = rot * matrix([[int(width * 0.0)],[int(height * 0.5)]])
            x_1, y_1 = rot * matrix([[int(width * 0.1)],[int(height * 0.495)]])
            x_2, y_2 = rot * matrix([[int(width * 0.2)],[int(height * 0.4798)]])
            x_3, y_3 = rot * matrix([[int(width * 0.3)],[int(height * 0.4539)]])
            x_4, y_4 = rot * matrix([[int(width * 0.4)],[int(height * 0.4165)]])
            x_5, y_5 = rot * matrix([[int(width * 0.5)],[int(height * 0.366)]])
            x_6, y_6 = rot * matrix([[int(width * 0.6)],[int(height * 0.3)]])
            x_7, y_7 = rot * matrix([[int(width * 0.7)],[int(height * 0.2141)]])
            x_8, y_8 = rot * matrix([[int(width * 0.8)],[int(height * 0.1)]])
            x_9, y_9 = rot * matrix([[int(width * 0.866)],[int(height * 0.0)]])
            x_10, y_10 = rot * matrix([[int(width * 0.8)],[int(height * -0.1)]])
            x_11, y_11 = rot * matrix([[int(width * 0.7)],[int(height * -0.2141)]])
            x_12, y_12 = rot * matrix([[int(width * 0.6)],[int(height * -0.3)]])
            x_13, y_13 = rot * matrix([[int(width * 0.5)],[int(height * -0.366)]])
            x_14, y_14 = rot * matrix([[int(width * 0.4)],[int(height * -0.4165)]])
            x_15, y_15 = rot * matrix([[int(width * 0.3)],[int(height * -0.4539)]])
            x_16, y_16 = rot * matrix([[int(width * 0.2)],[int(height * -0.4798)]])
            x_17, y_17 = rot * matrix([[int(width * 0.1)],[int(height * -0.495)]])
            x_18, y_18 = rot * matrix([[int(width * 0.0)],[int(height * -0.5)]])
            x_19, y_19 = rot * matrix([[int(width * 0.01)],[int(height * -0.482)]])
            x_20, y_20 = rot * matrix([[int(width * 0.02)],[int(height * -0.464)]])
            x_21, y_21 = rot * matrix([[int(width * 0.03)],[int(height * -0.444)]])
            x_22, y_22 = rot * matrix([[int(width * 0.04)],[int(height * -0.423)]])
            x_23, y_23 = rot * matrix([[int(width * 0.05)],[int(height * -0.401)]])
            x_24, y_24 = rot * matrix([[int(width * 0.06)],[int(height * -0.377)]])
            x_25, y_25 = rot * matrix([[int(width * 0.07)],[int(height * -0.352)]])
            x_26, y_26 = rot * matrix([[int(width * 0.08)],[int(height * -0.324)]])
            x_27, y_27 = rot * matrix([[int(width * 0.09)],[int(height * -0.293)]])
            x_28, y_28 = rot * matrix([[int(width * 0.10)],[int(height * -0.258)]])
            x_29, y_29 = rot * matrix([[int(width * 0.11)],[int(height * -0.218)]])
            x_30, y_30 = rot * matrix([[int(width * 0.12)],[int(height * -0.167)]])
            x_31, y_31 = rot * matrix([[int(width * 0.13)],[int(height * -0.089)]])
            x_32, y_32 = rot * matrix([[int(width * 0.134)],[int(height * 0.0)]])
            x_33, y_33 = rot * matrix([[int(width * 0.13)],[int(height * 0.089)]])
            x_34, y_34 = rot * matrix([[int(width * 0.12)],[int(height * 0.167)]])
            x_35, y_35 = rot * matrix([[int(width * 0.11)],[int(height * 0.218)]])
            x_36, y_36 = rot * matrix([[int(width * 0.10)],[int(height * 0.258)]])
            x_37, y_37 = rot * matrix([[int(width * 0.09)],[int(height * 0.293)]])
            x_38, y_38 = rot * matrix([[int(width * 0.08)],[int(height * 0.324)]])
            x_39, y_39 = rot * matrix([[int(width * 0.07)],[int(height * 0.352)]])
            x_40, y_40 = rot * matrix([[int(width * 0.06)],[int(height * 0.377)]])
            x_41, y_41 = rot * matrix([[int(width * 0.05)],[int(height * 0.401)]])
            x_42, y_42 = rot * matrix([[int(width * 0.04)],[int(height * 0.423)]])
            x_43, y_43 = rot * matrix([[int(width * 0.03)],[int(height * 0.444)]])
            x_44, y_44 = rot * matrix([[int(width * 0.02)],[int(height * 0.464)]])
            x_45, y_45 = rot * matrix([[int(width * 0.01)],[int(height * 0.482)]])

            x_46, y_46 = rot * matrix([[int(0)],[int(-displacement)]])
            x_47, y_47 = rot * matrix([[int(displacement * 0.134)],[int(-displacement)]])
            x_48, y_48 = rot * matrix([[int(0)],[int(displacement)]])
            x_49, y_49 = rot * matrix([[int(displacement * 0.134)],[int(displacement)]])
            x_50, y_50 = rot * matrix([[int(width)],[int(0)]])
            x_51, y_51 = rot * matrix([[int(width*0.866)],[int(0)]])

            create_component(
                x_46,
                y_46,
                x_47,
                y_47
            )
            create_component(
                x_48,
                y_48,
                x_49,
                y_49
            )
            create_component(
                x_50,
                y_50,
                x_51,
                y_51
            )
            create_OR(
                x_0,
                y_0,
                x_1,
                y_1,
                x_2,
                y_2,
                x_3,
                y_3,
                x_4,
                y_4,
                x_5,
                y_5,
                x_6,
                y_6,
                x_7,
                y_7,
                x_8,
                y_8,
                x_9,
                y_9,
                x_10,
                y_10,
                x_11,
                y_11,
                x_12,
                y_12,
                x_13,
                y_13,
                x_14,
                y_14,
                x_15,
                y_15,
                x_16,
                y_16,
                x_17,
                y_17,
                x_18,
                y_18,
                x_19,
                y_19,
                x_20,
                y_20,
                x_21,
                y_21,
                x_22,
                y_22,
                x_23,
                y_23,
                x_24,
                y_24,
                x_25,
                y_25,
                x_26,
                y_26,
                x_27,
                y_27,
                x_28,
                y_28,
                x_29,
                y_29,
                x_30,
                y_30,
                x_31,
                y_31,
                x_32,
                y_32,
                x_33,
                y_33,
                x_34,
                y_34,
                x_35,
                y_35,
                x_36,
                y_36,
                x_37,
                y_37,
                x_38,
                y_38,
                x_39,
                y_39,
                x_40,
                y_40,
                x_41,
                y_41,
                x_42,
                y_42,
                x_43,
                y_43,
                x_44,
                y_44,
                x_45,
                y_45,
            )
            create_logicpoint(
                x_coord,
                y_coord
            )

            first_order.destroy()
            second_order.destroy()

        def XOR(self, rot):
            height = displacement*2.5
            width = displacement*3
            offset = displacement/3

            x_18, y_18 = rot * matrix([[int(width * 0.0) - int(offset)],[int(height * -0.5)]])
            x_19, y_19 = rot * matrix([[int(width * 0.01) - int(offset)],[int(height * -0.482)]])
            x_20, y_20 = rot * matrix([[int(width * 0.02) - int(offset)],[int(height * -0.464)]])
            x_21, y_21 = rot * matrix([[int(width * 0.03) - int(offset)],[int(height * -0.444)]])
            x_22, y_22 = rot * matrix([[int(width * 0.04) - int(offset)],[int(height * -0.423)]])
            x_23, y_23 = rot * matrix([[int(width * 0.05) - int(offset)],[int(height * -0.401)]])
            x_24, y_24 = rot * matrix([[int(width * 0.06) - int(offset)],[int(height * -0.377)]])
            x_25, y_25 = rot * matrix([[int(width * 0.07) - int(offset)],[int(height * -0.352)]])
            x_26, y_26 = rot * matrix([[int(width * 0.08) - int(offset)],[int(height * -0.324)]])
            x_27, y_27 = rot * matrix([[int(width * 0.09) - int(offset)],[int(height * -0.293)]])
            x_28, y_28 = rot * matrix([[int(width * 0.10) - int(offset)],[int(height * -0.258)]])
            x_29, y_29 = rot * matrix([[int(width * 0.11) - int(offset)],[int(height * -0.218)]])
            x_30, y_30 = rot * matrix([[int(width * 0.12) - int(offset)],[int(height * -0.167)]])
            x_31, y_31 = rot * matrix([[int(width * 0.13) - int(offset)],[int(height * -0.089)]])
            x_32, y_32 = rot * matrix([[int(width * 0.134) - int(offset)],[int(height * 0.0)]])
            x_33, y_33 = rot * matrix([[int(width * 0.13) - int(offset)],[int(height * 0.089)]])
            x_34, y_34 = rot * matrix([[int(width * 0.12) - int(offset)],[int(height * 0.167)]])
            x_35, y_35 = rot * matrix([[int(width * 0.11) - int(offset)],[int(height * 0.218)]])
            x_36, y_36 = rot * matrix([[int(width * 0.10) - int(offset)],[int(height * 0.258)]])
            x_37, y_37 = rot * matrix([[int(width * 0.09) - int(offset)],[int(height * 0.293)]])
            x_38, y_38 = rot * matrix([[int(width * 0.08) - int(offset)],[int(height * 0.324)]])
            x_39, y_39 = rot * matrix([[int(width * 0.07) - int(offset)],[int(height * 0.352)]])
            x_40, y_40 = rot * matrix([[int(width * 0.06) - int(offset)],[int(height * 0.377)]])
            x_41, y_41 = rot * matrix([[int(width * 0.05) - int(offset)],[int(height * 0.401)]])
            x_42, y_42 = rot * matrix([[int(width * 0.04) - int(offset)],[int(height * 0.423)]])
            x_43, y_43 = rot * matrix([[int(width * 0.03) - int(offset)],[int(height * 0.444)]])
            x_44, y_44 = rot * matrix([[int(width * 0.02) - int(offset)],[int(height * 0.464)]])
            x_45, y_45 = rot * matrix([[int(width * 0.01) - int(offset)],[int(height * 0.482)]])

            create_XOR(
                x_18,
                y_18,
                x_19,
                y_19,
                x_20,
                y_20,
                x_21,
                y_21,
                x_22,
                y_22,
                x_23,
                y_23,
                x_24,
                y_24,
                x_25,
                y_25,
                x_26,
                y_26,
                x_27,
                y_27,
                x_28,
                y_28,
                x_29,
                y_29,
                x_30,
                y_30,
                x_31,
                y_31,
                x_32,
                y_32,
                x_33,
                y_33,
                x_34,
                y_34,
                x_35,
                y_35,
                x_36,
                y_36,
                x_37,
                y_37,
                x_38,
                y_38,
                x_39,
                y_39,
                x_40,
                y_40,
                x_41,
                y_41,
                x_42,
                y_42,
                x_43,
                y_43,
                x_44,
                y_44,
                x_45,
                y_45,
            )
            create_logicpoint(
                x_coord,
                y_coord
            )

            first_order.destroy()
            second_order.destroy()

    class Switches:
        def Switch(self, rot):
            height = displacement
            diameter = displacement/4
            offset = displacement/3
            extent = (displacement**2 - offset**2)**0.5

            x_0, y_0 = rot * matrix([[int(0)],[int(-height/2)]])
            x_1, y_1 = rot * matrix([[int(0)],[int(height/2)]])
            x_2, y_2 = rot * matrix([[int(0)],[int(-height/2)]])
            x_3, y_3 = rot * matrix([[int(offset)],[int(-height/2 + extent)]])
            x_4, y_4 = rot * matrix([[int(-diameter/2)],[int(-height/2)]])
            x_5, y_5 = rot * matrix([[int(diameter/2)],[int(-height/2 + diameter)]])
            x_6, y_6 = rot * matrix([[int(-diameter/2)],[int(height/2 - diameter)]])
            x_7, y_7 = rot * matrix([[int(diameter/2)],[int(height/2)]])

            create_whiteout(
                x_0,
                y_0,
                x_1,
                y_1
            )
            create_component(
                x_2,
                y_2,
                x_3,
                y_3
            )
            create_circle(
                x_4,
                y_4,
                x_5,
                y_5
            )
            create_circle(
                x_6,
                y_6,
                x_7,
                y_7
            )
            create_overpoint(
                x_coord,
                y_coord
            )

            first_order.destroy()
            second_order.destroy()

        def Button(self, rot):
            height = displacement
            diameter = displacement/5
            offset = displacement/4
            extent = displacement/3

            x_0, y_0 = rot * matrix([[int(0)],[int(-height/2)]])
            x_1, y_1 = rot * matrix([[int(0)],[int(height/2)]])
            x_2, y_2 = rot * matrix([[int(offset)],[int(-height/2)]])
            x_3, y_3 = rot * matrix([[int(offset)],[int(height/2)]])
            x_4, y_4 = rot * matrix([[int(offset)],[int(0)]])
            x_5, y_5 = rot * matrix([[int(offset + extent)],[int(0)]])

            x_6, y_6 = rot * matrix([[int(-diameter/2)],[int(-height/2)]])
            x_7, y_7 = rot * matrix([[int(diameter/2)],[int(-height/2 + diameter)]])
            x_8, y_8 = rot * matrix([[int(-diameter/2)],[int(height/2 - diameter)]])
            x_9, y_9 = rot * matrix([[int(diameter/2)],[int(height/2)]])

            create_whiteout(
                x_0,
                y_0,
                x_1,
                y_1
            )
            create_component(
                x_2,
                y_2,
                x_3,
                y_3
            )
            create_component(
                x_4,
                y_4,
                x_5,
                y_5
            )
            create_circle(
                x_6,
                y_6,
                x_7,
                y_7
            )
            create_circle(
                x_8,
                y_8,
                x_9,
                y_9
            )
            create_overpoint(
                x_coord,
                y_coord
            )

            first_order.destroy()
            second_order.destroy()

    class Measurement:
        def Voltmeter(self, rot):
            diameter = displacement/1.25

            x_0, y_0 = rot * matrix([[int(-diameter/2)],[int(-diameter/2)]])
            x_1, y_1 = rot * matrix([[int(diameter/2)],[int(diameter/2)]])

            create_circle(
                x_0,
                y_0,
                x_1,
                y_1
            )
            create_text(
                x_coord,
                y_coord,
                'V',
                20
            )
            create_overpoint(
                x_coord,
                y_coord
            )

            first_order.destroy()
            second_order.destroy()

        def Ammeter(self, rot):
            diameter = displacement/1.25

            x_0, y_0 = rot * matrix([[int(-diameter/2)],[int(-diameter/2)]])
            x_1, y_1 = rot * matrix([[int(diameter/2)],[int(diameter/2)]])

            create_circle(
                x_0,
                y_0,
                x_1,
                y_1
            )
            create_text(
                x_coord,
                y_coord,
                'A',
                20
            )
            create_overpoint(
                x_coord,
                y_coord
            )

            first_order.destroy()
            second_order.destroy()

    class Other:
        def Motor(self, rot):
            diameter = displacement/1.25

            x_0, y_0 = rot * matrix([[int(-diameter/2)],[int(-diameter/2)]])
            x_1, y_1 = rot * matrix([[int(diameter/2)],[int(diameter/2)]])

            create_circle(
                x_0,
                y_0,
                x_1,
                y_1
            )
            create_text(
                x_coord,
                y_coord,
                'M',
                20
            )
            create_overpoint(
                x_coord,
                y_coord
            )

            first_order.destroy()
            second_order.destroy()

        def Lamp(self, rot):
            diameter = displacement/1.25
            width = displacement/3
            height = width

            x_0, y_0 = rot * matrix([[int(-diameter/2)],[int(-diameter/2)]])
            x_1, y_1 = rot * matrix([[int(diameter/2)],[int(diameter/2)]])
            x_2, y_2 = rot_up * rot * matrix([[int(-width/2)],[int(-height/2)]])
            x_3, y_3 = rot_up * rot * matrix([[int(width/2)],[int(height/2)]])
            x_4, y_4 = rot_up * rot * matrix([[int(-diameter/2)],[int(0)]])
            x_5, y_5 = rot_up * rot * matrix([[int(-width/2)],[int(0)]])
            x_6, y_6 = rot_up * rot * matrix([[int(diameter/2)],[int(0)]])
            x_7, y_7 = rot_up * rot * matrix([[int(width/2)],[int(0)]])

            if rot[0,0] == 1 and rot[0,1] == 0:
                angle = 90

            elif rot[0,0] == 0 and rot[0,1] == 1:
                angle = 0

            elif rot[0,0] == -1 and rot[0,1] == 0:
                angle = -90

            elif rot[0,0] == 0 and rot[0,1] == -1:
                angle = 180

            create_circle(
                x_0,
                y_0,
                x_1,
                y_1
            )
            create_arc(
                x_2,
                y_2,
                x_3,
                y_3,
                angle
            )
            create_component(
                x_4,
                y_4,
                x_5,
                y_5
            )
            create_component(
                x_6,
                y_6,
                x_7,
                y_7
            )
            create_overpoint(
                x_coord,
                y_coord
            )

            first_order.destroy()
            second_order.destroy()

        def Buzzer(self, rot):
            diameter = displacement/1.5
            height = diameter/2
            offset = displacement/4

            x_0, y_0 = rot * matrix([[int(offset)],[int(-diameter/2)]])
            x_1, y_1 = rot * matrix([[int(offset + diameter)],[int(diameter/2)]])

            x_2, y_2 = rot * matrix([[int(0)],[int(-height/2)]])
            x_3, y_3 = rot * matrix([[int(offset + diameter/3)],[int(-height/2)]])
            x_4, y_4 = rot * matrix([[int(0)],[int(height/2)]])
            x_5, y_5 = rot * matrix([[int(offset + diameter/3)],[int(height/2)]])

            x_6, y_6 = rot * matrix([[int(0)],[int(height/2)]])
            x_7, y_7 = rot * matrix([[int(0)],[int(-height/2)]])

            if rot[0,0] == 1 and rot[0,1] == 0:
                angle = 90

            elif rot[0,0] == 0 and rot[0,1] == 1:
                angle = 180

            elif rot[0,0] == -1 and rot[0,1] == 0:
                angle = -90

            elif rot[0,0] == 0 and rot[0,1] == -1:
                angle = 0

            create_whiteout(
                x_6,
                y_6,
                x_7,
                y_7
            )
            create_component(
                x_2,
                y_2,
                x_3,
                y_3
            )
            create_component(
                x_4,
                y_4,
                x_5,
                y_5
            )
            create_semi(
                x_0,
                y_0,
                x_1,
                y_1,
                angle
            )
            create_overpoint(
                x_coord,
                y_coord
            )

            first_order.destroy()
            second_order.destroy()

        def Antenna(self, rot):
            width = displacement/2
            height = width * 0.866

            x_0, y_0 = rot * matrix([[int(0)],[int(0)]])
            x_1, y_1 = rot * matrix([[int(0)],[int(-height)]])
            x_2, y_2 = rot * matrix([[int(0)],[int(0)]])
            x_3, y_3 = rot * matrix([[int(-width/2)],[int(-height)]])
            x_4, y_4 = rot * matrix([[int(0)],[int(0)]])
            x_5, y_5 = rot * matrix([[int(width/2)],[int(-height)]])

            create_component(
                x_0,
                y_0,
                x_1,
                y_1
            )
            create_component(
                x_2,
                y_2,
                x_3,
                y_3
            )
            create_component(
                x_4,
                y_4,
                x_5,
                y_5
            )
            create_overpoint(
                x_coord,
                y_coord
            )

            first_order.destroy()
            second_order.destroy()

        def Crystal_oscillator(self, rot):
            width = displacement/5
            height = displacement/1.25
            offset = width/2

            x_0, y_0 = rot * matrix([[int(-width/2 - offset)],[0]])
            x_1, y_1 = rot * matrix([[int(width/2 + offset)],[0]])
            x_2, y_2 = rot * matrix([[int(-width/2 - offset)],[int(-height/2)]])
            x_3, y_3 = rot * matrix([[int(-width/2 - offset)],[int(height/2)]])
            x_4, y_4 = rot * matrix([[int(width/2 + offset)],[int(-height/2)]])
            x_5, y_5 = rot * matrix([[int(width/2 + offset)],[int(height/2)]])
            x_6, y_6 = rot * matrix([[int(-width/2)],[int(-height/2)]])
            x_7, y_7 = rot * matrix([[int(width/2)],[int(height/2)]])

            create_whiteout(
                x_0,
                y_0,
                x_1,
                y_1
            )
            create_component(
                x_2,
                y_2,
                x_3,
                y_3
            )
            create_component(
                x_4,
                y_4,
                x_5,
                y_5
            )
            create_rectangle(
                x_6,
                y_6,
                x_7,
                y_7
            )
            create_overpoint(
                x_coord,
                y_coord
            )

            first_order.destroy()
            second_order.destroy()

        def Triode(self, rot):
            diameter = displacement
            height = diameter/6
            width = diameter/1.5
            grid = width/4
            gap = (width - 3*grid)/2
            heater = diameter/4
            extent = diameter/5
            tooth = diameter/10

            x_0, y_0 = rot * matrix([[int(-diameter/2)],[-diameter/2]])
            x_1, y_1 = rot * matrix([[int(diameter/2)],[diameter/2]])

            x_2, y_2 = rot * matrix([[int(-width/2)],[int(-height)]])
            x_3, y_3 = rot * matrix([[int(width/2)],[int(-height)]])
            x_4, y_4 = rot * matrix([[int(-width/2)],[int(0)]])
            x_5, y_5 = rot * matrix([[int(-width/2 + grid)],[int(0)]])
            x_6, y_6 = rot * matrix([[int(-grid/2)],[int(0)]])
            x_7, y_7 = rot * matrix([[int(grid/2)],[int(0)]])
            x_8, y_8 = rot * matrix([[int(width/2 - grid)],[int(0)]])
            x_9, y_9 = rot * matrix([[int(width/2)],[int(0)]])
            x_10, y_10 = rot * matrix([[int(-width/2)],[int(height)]])
            x_11, y_11 = rot * matrix([[int(width/2)],[int(height)]])
            x_12, y_12 = rot * matrix([[int(width/2)],[int(height + tooth)]])

            x_13, y_13 = rot * matrix([[int(-width/2 - gap)],[int(0)]])
            x_14, y_14 = rot * matrix([[int(-diameter/2)],[int(0)]])

            x_15, y_15 = rot * matrix([[int(0)],[int(-height)]])
            x_16, y_16 = rot * matrix([[int(0)],[int(-diameter/2)]])

            x_17, y_17 = rot * matrix([[int(-width/2)],[int(height)]])
            x_18, y_18 = rot * matrix([[int(-width/2)],[int(displacement)]])
            x_19, y_19 = rot * matrix([[int(-displacement)],[int(displacement)]])

            x_20, y_20 = rot * matrix([[int(-0.707*heater)],[int(diameter/2 - heater + 0.707*heater + extent)]])
            x_21, y_21 = rot * matrix([[int(-0.707*heater)],[int(diameter/2 - heater + 0.707*heater)]])
            x_22, y_22 = rot * matrix([[int(0)],[int(diameter/2 - heater)]])
            x_23, y_23 = rot * matrix([[int(0.707*heater)],[int(diameter/2 - heater + 0.707*heater)]])
            x_24, y_24 = rot * matrix([[int(0.707*heater)],[int(diameter/2 - heater + 0.707*heater + extent)]])

            create_circle(
                x_0,
                y_0,
                x_1,
                y_1
            )
            create_component(
                x_2,
                y_2,
                x_3,
                y_3
            )
            create_component(
                x_4,
                y_4,
                x_5,
                y_5
            )
            create_component(
                x_6,
                y_6,
                x_7,
                y_7
            )
            create_component(
                x_8,
                y_8,
                x_9,
                y_9
            )
            create_component(
                x_10,
                y_10,
                x_11,
                y_11
            )
            create_component(
                x_11,
                y_11,
                x_12,
                y_12
            )
            create_component(
                x_13,
                y_13,
                x_14,
                y_14
            )
            create_component(
                x_15,
                y_15,
                x_16,
                y_16
            )
            create_long(
                x_17,
                y_17,
                x_18,
                y_18,
                x_19,
                y_19
            )
            create_component(
                x_20,
                y_20,
                x_21,
                y_21
            )
            create_component(
                x_21,
                y_21,
                x_22,
                y_22
            )
            create_component(
                x_22,
                y_22,
                x_23,
                y_23
            )
            create_component(
                x_23,
                y_23,
                x_24,
                y_24
            )
            create_overpoint(
                x_coord,
                y_coord
            )

            first_order.destroy()
            second_order.destroy()

    class Formatting:
        def Junction(self):
            create_junction(
                x_coord,
                y_coord
            )

            first_order.destroy()
            second_order.destroy()

        def Crossing(self, rot):
            width = displacement/3
            height = width

            x_0, y_0 = rot_up * rot * matrix([[int(-width/2)],[int(-height/2)]])
            x_1, y_1 = rot_up * rot * matrix([[int(width/2)],[int(height/2)]])
            x_2, y_2 = rot_up * rot * matrix([[int(-width/2)],[int(0)]])
            x_3, y_3 = rot_up * rot * matrix([[int(-component_width/2)],[int(0)]])
            x_4, y_4 = rot_up * rot * matrix([[int(width/2)],[int(0)]])
            x_5, y_5 = rot_up * rot * matrix([[int(component_width/2)],[int(0)]])

            if rot[0,0] == 1 and rot[0,1] == 0:
                angle = 90

            elif rot[0,0] == 0 and rot[0,1] == 1:
                angle = 0

            elif rot[0,0] == -1 and rot[0,1] == 0:
                angle = -90

            elif rot[0,0] == 0 and rot[0,1] == -1:
                angle = 180

            create_whiteout(
                x_2,
                y_2,
                x_3,
                y_3
            )
            create_whiteout(
                x_4,
                y_4,
                x_5,
                y_5
            )
            create_arc(
                x_0,
                y_0,
                x_1,
                y_1,
                angle
            )
            create_overpoint(
                x_coord,
                y_coord
            )

            first_order.destroy()
            second_order.destroy()

    class Misc:
        def Var_arrow(self, rot):
            width = displacement/1.25
            height = displacement/2.5
            offset = displacement/10

            x_0, y_0 = rot * matrix([[int(-width/2)],[int(height/2)]])
            x_1, y_1 = rot * matrix([[int(width/2 + offset)],[int(-height/2 - offset)]])

            create_arrow(
                x_0,
                y_0,
                x_1,
                y_1
            )
            create_overpoint(
                x_coord,
                y_coord
            )

            first_order.destroy()
            second_order.destroy()

        def Pot_arrow(self, rot):
            offset = displacement/3

            x_0, y_0 = rot * matrix([[int(displacement/2)],[int(0)]])
            x_1, y_1 = rot * matrix([[int(offset/2)],[int(0)]])

            create_arrow(
                x_0,
                y_0,
                x_1,
                y_1
            )
            create_overpoint(
                x_coord,
                y_coord
            )

            first_order.destroy()
            second_order.destroy()

class draw():
    class Text:
        class Custom_up:
            def draw(self, event):
                define().Text.Custom(self,'up')

        class Custom_down:
            def draw(self, event):
                define().Text.Custom(self,'down')

        class Custom_right:
            def draw(self, event):
                define().Text.Custom(self,'right')

        class Custom_left:
            def draw(self, event):
                define().Text.Custom(self,'left')

    class Power:
        class Cell_up:
            def draw(self, event):
                define().Power.Cell_ver(self,rot_up)

        class Cell_down:
            def draw(self, event):
                define().Power.Cell_ver(self,rot_down)

        class Cell_right:
            def draw(self, event):
                define().Power.Cell_hor(self,rot_right)

        class Cell_left:
            def draw(self, event):
                define().Power.Cell_hor(self,rot_left)

        class Battery_up:
            def draw(self, event):
                define().Power.Battery_ver(self,rot_up)

        class Battery_down:
            def draw(self, event):
                define().Power.Battery_ver(self,rot_down)

        class Battery_right:
            def draw(self, event):
                define().Power.Battery_hor(self,rot_right)

        class Battery_left:
            def draw(self, event):
                define().Power.Battery_hor(self,rot_left)

        class DC_up:
            def draw(self, event):
                define().Power.DC_ver(self,rot_up)

        class DC_down:
            def draw(self, event):
                define().Power.DC_ver(self,rot_down)

        class DC_right:
            def draw(self, event):
                define().Power.DC_hor(self,rot_right)

        class DC_left:
            def draw(self, event):
                define().Power.DC_hor(self,rot_left)

        class AC:
            def draw(self, event):
                define().Power.AC(self, rot_right)

        class Ground_1:
            def draw(self, event):
                define().Power.Ground_1(self, rot_right)

        class Ground_2:
            def draw(self, event):
                define().Power.Ground_2(self, rot_right)

        class Fuse_horizontal:
            def draw(self, event):
                define().Power.Fuse(self, rot_right, 0)

        class Fuse_vertical:
            def draw(self, event):
                define().Power.Fuse(self, rot_up, 90)

    class Resistors:
        class Resistor_US_horizontal:
            def draw(self, event):
                define().Resistors.Resistor_US(self, rot_right)

        class Resistor_US_vertical:
            def draw(self, event):
                define().Resistors.Resistor_US(self, rot_up)

        class Rheostat_US_horizontal:
            def draw(self, event):
                define().Resistors.Resistor_US(self, rot_right)
                define().Misc.Var_arrow(self, rot_right)

        class Rheostat_US_vertical:
            def draw(self, event):
                define().Resistors.Resistor_US(self, rot_up)
                define().Misc.Var_arrow(self, rot_up)

        class Potentiometer_US_up:
            def draw(self, event):
                define().Resistors.Resistor_US(self, rot_right)
                define().Misc.Pot_arrow(self, rot_up)

        class Potentiometer_US_down:
            def draw(self, event):
                define().Resistors.Resistor_US(self, rot_right)
                define().Misc.Pot_arrow(self, rot_down)

        class Potentiometer_US_right:
            def draw(self, event):
                define().Resistors.Resistor_US(self, rot_up)
                define().Misc.Pot_arrow(self, rot_right)

        class Potentiometer_US_left:
            def draw(self, event):
                define().Resistors.Resistor_US(self, rot_up)
                define().Misc.Pot_arrow(self, rot_left)

        class Resistor_EU_horizontal:
            def draw(self, event):
                define().Resistors.Resistor_EU(self, rot_right)

        class Resistor_EU_vertical:
            def draw(self, event):
                define().Resistors.Resistor_EU(self, rot_up)

        class Rheostat_EU_horizontal:
            def draw(self, event):
                define().Resistors.Resistor_EU(self, rot_right)
                define().Misc.Var_arrow(self, rot_right)

        class Rheostat_EU_vertical:
            def draw(self, event):
                define().Resistors.Resistor_EU(self, rot_up)
                define().Misc.Var_arrow(self, rot_up)

        class Potentiometer_EU_up:
            def draw(self, event):
                define().Resistors.Resistor_EU(self, rot_right)
                define().Misc.Pot_arrow(self, rot_up)

        class Potentiometer_EU_down:
            def draw(self, event):
                define().Resistors.Resistor_EU(self, rot_right)
                define().Misc.Pot_arrow(self, rot_down)

        class Potentiometer_EU_right:
            def draw(self, event):
                define().Resistors.Resistor_EU(self, rot_up)
                define().Misc.Pot_arrow(self, rot_right)

        class Potentiometer_EU_left:
            def draw(self, event):
                define().Resistors.Resistor_EU(self, rot_up)
                define().Misc.Pot_arrow(self, rot_left)

    class Capacitors:
        class Capacitor_horizontal:
            def draw(self, event):
                define().Capacitors.Capacitor(self, rot_right)

        class Capacitor_vertical:
            def draw(self, event):
                define().Capacitors.Capacitor(self, rot_up)

        class Pol_cap_up:
            def draw(self, event):
                define().Capacitors.Pol_cap(self, rot_up)

        class Pol_cap_down:
            def draw(self, event):
                define().Capacitors.Pol_cap(self, rot_down)

        class Pol_cap_right:
            def draw(self, event):
                define().Capacitors.Pol_cap(self, rot_right)

        class Pol_cap_left:
            def draw(self, event):
                define().Capacitors.Pol_cap(self, rot_left)

        class Var_cap_horizontal:
            def draw(self, event):
                define().Capacitors.Capacitor(self, rot_right)
                define().Misc.Var_arrow(self, rot_right)

        class Var_cap_vertical:
            def draw(self, event):
                define().Capacitors.Capacitor(self, rot_up)
                define().Misc.Var_arrow(self, rot_up)

    class Inductors:
        class Inductor_up:
            def draw(self, event):
                define().Inductors.Inductor(self, rot_up)

        class Inductor_down:
            def draw(self, event):
                define().Inductors.Inductor(self, rot_down)

        class Inductor_right:
            def draw(self, event):
                define().Inductors.Inductor(self, rot_right)

        class Inductor_left:
            def draw(self, event):
                define().Inductors.Inductor(self, rot_left)

    class Diodes:
        class Diode_up:
            def draw(self, event):
                define().Diodes.Diode(self, rot_up)

        class Diode_down:
            def draw(self, event):
                define().Diodes.Diode(self, rot_down)

        class Diode_right:
            def draw(self, event):
                define().Diodes.Diode(self, rot_right)

        class Diode_left:
            def draw(self, event):
                define().Diodes.Diode(self, rot_left)

        class Zener_up:
            def draw(self, event):
                define().Diodes.Zener(self, rot_up)

        class Zener_down:
            def draw(self, event):
                define().Diodes.Zener(self, rot_down)

        class Zener_right:
            def draw(self, event):
                define().Diodes.Zener(self, rot_right)

        class Zener_left:
            def draw(self, event):
                define().Diodes.Zener(self, rot_left)

        class Schottky_up:
            def draw(self, event):
                define().Diodes.Schottky(self, rot_up)

        class Schottky_down:
            def draw(self, event):
                define().Diodes.Schottky(self, rot_down)

        class Schottky_right:
            def draw(self, event):
                define().Diodes.Schottky(self, rot_right)

        class Schottky_left:
            def draw(self, event):
                define().Diodes.Schottky(self, rot_left)

        class LED_up:
            def draw(self, event):
                define().Diodes.LED(self, rot_up)

        class LED_down:
            def draw(self, event):
                define().Diodes.LED(self, rot_down)

        class LED_right:
            def draw(self, event):
                define().Diodes.LED(self, rot_right)

        class LED_left:
            def draw(self, event):
                define().Diodes.LED(self, rot_left)

    class Transistors:
        class NPN_up:
            def draw(self, event):
                define().Transistors.NPN(self, rot_up)

        class NPN_down:
            def draw(self, event):
                define().Transistors.NPN(self, rot_down)

        class NPN_right:
            def draw(self, event):
                define().Transistors.NPN(self, rot_right)

        class NPN_left:
            def draw(self, event):
                define().Transistors.NPN(self, rot_left)

        class PNP_up:
            def draw(self, event):
                define().Transistors.PNP(self, rot_up)

        class PNP_down:
            def draw(self, event):
                define().Transistors.PNP(self, rot_down)

        class PNP_right:
            def draw(self, event):
                define().Transistors.PNP(self, rot_right)

        class PNP_left:
            def draw(self, event):
                define().Transistors.PNP(self, rot_left)

        class NMOS_up:
            def draw(self, event):
                define().Transistors.NMOS(self, rot_up)

        class NMOS_down:
            def draw(self, event):
                define().Transistors.NMOS(self, rot_down)

        class NMOS_right:
            def draw(self, event):
                define().Transistors.NMOS(self, rot_right)

        class NMOS_left:
            def draw(self, event):
                define().Transistors.NMOS(self, rot_left)

        class PMOS_up:
            def draw(self, event):
                define().Transistors.PMOS(self, rot_up)

        class PMOS_down:
            def draw(self, event):
                define().Transistors.PMOS(self, rot_down)

        class PMOS_right:
            def draw(self, event):
                define().Transistors.PMOS(self, rot_right)

        class PMOS_left:
            def draw(self, event):
                define().Transistors.PMOS(self, rot_left)

    class Logic:
        class Buffer_up:
            def draw(self, event):
                define().Logic.Buffer(self, rot_up)

        class Buffer_down:
            def draw(self, event):
                define().Logic.Buffer(self, rot_down)

        class Buffer_right:
            def draw(self, event):
                define().Logic.Buffer(self, rot_right)

        class Buffer_left:
            def draw(self, event):
                define().Logic.Buffer(self, rot_left)

        class Inverter_up:
            def draw(self, event):
                define().Logic.Buffer(self, rot_up)
                define().Logic.Inverter(self, rot_up)

        class Inverter_down:
            def draw(self, event):
                define().Logic.Buffer(self, rot_down)
                define().Logic.Inverter(self, rot_down)

        class Inverter_right:
            def draw(self, event):
                define().Logic.Buffer(self, rot_right)
                define().Logic.Inverter(self, rot_right)

        class Inverter_left:
            def draw(self, event):
                define().Logic.Buffer(self, rot_left)
                define().Logic.Inverter(self, rot_left)

        class AND_up:
            def draw(self, event):
                define().Logic.AND(self, rot_up)

        class AND_down:
            def draw(self, event):
                define().Logic.AND(self, rot_down)

        class AND_right:
            def draw(self, event):
                define().Logic.AND(self, rot_right)

        class AND_left:
            def draw(self, event):
                define().Logic.AND(self, rot_left)

        class NAND_up:
            def draw(self, event):
                define().Logic.AND(self, rot_up)
                define().Logic.NOT(self, rot_up)

        class NAND_down:
            def draw(self, event):
                define().Logic.AND(self, rot_down)
                define().Logic.NOT(self, rot_down)

        class NAND_right:
            def draw(self, event):
                define().Logic.AND(self, rot_right)
                define().Logic.NOT(self, rot_right)

        class NAND_left:
            def draw(self, event):
                define().Logic.AND(self, rot_left)
                define().Logic.NOT(self, rot_left)

        class OR_up:
            def draw(self, event):
                define().Logic.OR(self, rot_up)

        class OR_down:
            def draw(self, event):
                define().Logic.OR(self, rot_down)

        class OR_right:
            def draw(self, event):
                define().Logic.OR(self, rot_right)

        class OR_left:
            def draw(self, event):
                define().Logic.OR(self, rot_left)

        class NOR_up:
            def draw(self, event):
                define().Logic.OR(self, rot_up)
                define().Logic.NOT(self, rot_up)

        class NOR_down:
            def draw(self, event):
                define().Logic.OR(self, rot_down)
                define().Logic.NOT(self, rot_down)

        class NOR_right:
            def draw(self, event):
                define().Logic.OR(self, rot_right)
                define().Logic.NOT(self, rot_right)

        class NOR_left:
            def draw(self, event):
                define().Logic.OR(self, rot_left)
                define().Logic.NOT(self, rot_left)

        class XOR_up:
            def draw(self, event):
                define().Logic.OR(self, rot_up)
                define().Logic.XOR(self, rot_up)

        class XOR_down:
            def draw(self, event):
                define().Logic.OR(self, rot_down)
                define().Logic.XOR(self, rot_down)

        class XOR_right:
            def draw(self, event):
                define().Logic.OR(self, rot_right)
                define().Logic.XOR(self, rot_right)

        class XOR_left:
            def draw(self, event):
                define().Logic.OR(self, rot_left)
                define().Logic.XOR(self, rot_left)

        class XNOR_up:
            def draw(self, event):
                define().Logic.OR(self, rot_up)
                define().Logic.NOT(self, rot_up)
                define().Logic.XOR(self, rot_up)

        class XNOR_down:
            def draw(self, event):
                define().Logic.OR(self, rot_down)
                define().Logic.NOT(self, rot_down)
                define().Logic.XOR(self, rot_down)

        class XNOR_right:
            def draw(self, event):
                define().Logic.OR(self, rot_right)
                define().Logic.NOT(self, rot_right)
                define().Logic.XOR(self, rot_right)

        class XNOR_left:
            def draw(self, event):
                define().Logic.OR(self, rot_left)
                define().Logic.NOT(self, rot_left)
                define().Logic.XOR(self, rot_left)

    class Switches:
        class Switch_up:
            def draw(self, event):
                define().Switches.Switch(self, rot_up)

        class Switch_down:
            def draw(self, event):
                define().Switches.Switch(self, rot_down)

        class Switch_right:
            def draw(self, event):
                define().Switches.Switch(self, rot_right)

        class Switch_left:
            def draw(self, event):
                define().Switches.Switch(self, rot_left)

        class Button_up:
            def draw(self, event):
                define().Switches.Button(self, rot_up)

        class Button_down:
            def draw(self, event):
                define().Switches.Button(self, rot_down)

        class Button_right:
            def draw(self, event):
                define().Switches.Button(self, rot_right)

        class Button_left:
            def draw(self, event):
                define().Switches.Button(self, rot_left)

    class Measurement:
        class Voltmeter:
            def draw(self, event):
                define().Measurement.Voltmeter(self, rot_up)

        class Ammeter:
            def draw(self, event):
                define().Measurement.Ammeter(self, rot_down)

    class Other:
        class Lamp_up:
            def draw(self, event):
                define().Other.Lamp(self, rot_up)

        class Lamp_down:
            def draw(self, event):
                define().Other.Lamp(self, rot_down)

        class Lamp_right:
            def draw(self, event):
                define().Other.Lamp(self, rot_right)

        class Lamp_left:
            def draw(self, event):
                define().Other.Lamp(self, rot_left)

        class Buzzer_up:
            def draw(self, event):
                define().Other.Buzzer(self, rot_up)

        class Buzzer_down:
            def draw(self, event):
                define().Other.Buzzer(self, rot_down)

        class Buzzer_right:
            def draw(self, event):
                define().Other.Buzzer(self, rot_right)

        class Buzzer_left:
            def draw(self, event):
                define().Other.Buzzer(self, rot_left)

        class Motor:
            def draw(self, event):
                define().Other.Motor(self, rot_right)

        class Antenna:
            def draw(self, event):
                define().Other.Antenna(self, rot_right)

        class Crystal_horizontal:
            def draw(self, event):
                define().Other.Crystal_oscillator(self, rot_right)

        class Crystal_vertical:
            def draw(self, event):
                define().Other.Crystal_oscillator(self, rot_up)

        class Triode:
            def draw(self, event):
                define().Other.Triode(self, rot_right)

    class Formatting:
        class Junction:
            def draw(self, event):
                define().Formatting.Junction(self)

        class Crossing_horizontal:
            def draw(self, event):
                define().Formatting.Crossing(self, rot_up)

        class Crossing_vertical:
            def draw(self, event):
                define().Formatting.Crossing(self, rot_right)

class delete_wire():
    def do_it(self, event):
        wires = canvas.find_overlapping(
            event.x - 5,
            event.y - 5,
            event.x + 5,
            event.y + 5
        )
        for wire in wires:
            if 'wire' in canvas.gettags(wire):
                canvas.delete(wire)
            else:
                pass

class delete_window():
    def request(self, event):
        global x_del, y_del
        point = canvas.find_closest(
                    event.x,
                    event.y
                )
        x_0, y_0, x_1, y_1 = canvas.coords(point)
        x_del = (x_0+x_1)/2
        y_del = (y_0+y_1)/2
        global window
        window = Toplevel(root)
        window.title('Remove component?')
        text = Label(
            window,
            text = 'Do you wish to remove this component from your schematic?'
        )
        yes = Button(
            window,
            text = 'Yes'
        )
        no = Button(
            window,
            text = 'No'
        )
        add = Button(
            window,
            text = 'Add text or component'
        )
        text.grid(
            row = 0
        )
        yes.grid(
            row = 1,
            column = 0
        )
        no.grid(
            row = 1,
            column = 1
        )
        add.grid(
            row = 1,
            column = 2
        )
        yes.bind(
            '<Button-1>',
            delete_component().delete
        )
        no.bind(
            '<Button-1>',
            delete_component().forget
        )
        add.bind(
            '<Button-1>',
            choose_text().menu
        )

class delete_logic_window():
    def request(self, event):
        global x_del, y_del
        point = canvas.find_closest(
                    event.x,
                    event.y
                )
        x_0, y_0, x_1, y_1 = canvas.coords(point)
        x_del = (x_0+x_1)/2
        y_del = (y_0+y_1)/2
        global window
        window = Toplevel(root)
        window.title('Remove logic gate?')
        text = Label(
            window,
            text = 'Do you wish to remove this logic gate from your schematic?'
        )
        yes = Button(
            window,
            text = 'Yes'
        )
        no = Button(
            window,
            text = 'No'
        )
        text.grid(
            row = 0
        )
        yes.grid(
            row = 1,
            column = 0
        )
        no.grid(
            row = 1,
            column = 1
        )
        yes.bind(
            '<Button-1>',
            delete_logic().delete
        )
        no.bind(
            '<Button-1>',
            delete_logic().forget
        )

class delete_text_window():
    def request(self, event):
        global x_del, y_del
        x_del = event.x
        y_del = event.y
        global window
        window = Toplevel(root)
        window.title('Remove text?')
        text = Label(
            window,
            text = 'Do you wish to remove this text from your schematic?'
        )
        yes = Button(
            window,
            text = 'Yes'
        )
        no = Button(
            window,
            text = 'No'
        )
        text.grid(
            row = 0
        )
        yes.grid(
            row = 1,
            column = 0
        )
        no.grid(
            row = 1,
            column = 1
        )
        yes.bind(
            '<Button-1>',
            delete_text().delete
        )
        no.bind(
            '<Button-1>',
            delete_text().forget
        )

class delete_component():
    def delete(self, event):
        find = canvas.find_overlapping(
                    x_del - displacement/1.8,
                    y_del - displacement/1.8,
                    x_del + displacement/1.8,
                    y_del + displacement/1.8
                )

        for thing in find:
            if 'point' not in canvas.gettags(thing):
                if 'wire' not in canvas.gettags(thing):
                    if 'textpoint' not in canvas.gettags(thing):
                        if 'text' not in canvas.gettags(thing):
                            canvas.delete(thing)

        window.destroy()

    def forget(self, event):
        window.destroy()

class delete_logic():
    def delete(self, event):
        find = canvas.find_overlapping(
                    x_del,
                    y_del - displacement,
                    x_del + displacement*3,
                    y_del + displacement
                )

        for thing in find:
            if 'point' not in canvas.gettags(thing):
                if 'wire' not in canvas.gettags(thing):
                    if 'textpoint' not in canvas.gettags(thing):
                        canvas.delete(thing)

        window.destroy()

    def forget(self, event):
        window.destroy()

class delete_text():
    def delete(self, event):
        find = canvas.find_overlapping(
                    x_del - int(text_size/2),
                    y_del - int(text_size/2),
                    x_del + int(text_size/2),
                    y_del + int(text_size/2)
                )

        for thing in find:
            if 'textpoint' in canvas.gettags(thing):
                canvas.delete(thing)
            elif 'text' in canvas.gettags(thing):
                canvas.delete(thing)

        window.destroy()

    def forget(self, event):
        window.destroy()

class hide_canvas():
    def hide(self, event):
        canvas.itemconfig(
            'point',
            fill = '',
        )
        canvas.itemconfig(
            'overpoint',
            fill = '',
        )
        canvas.itemconfig(
            'textpoint',
            fill = '',
        )
        hide_button.config(
            text = 'Show grid'
        )
        hide_button.bind(
            '<Button-1>',
            self.show
        )

    def show(self, event):
        canvas.itemconfig(
            'point',
            fill = point_colour,
            activefill = point_hover
        )
        canvas.itemconfig(
            'overpoint',
            fill = point_colour,
            activefill = point_hover
        )
        hide_button.config(
            text = 'Hide grid'
        )
        hide_button.bind(
            '<Button-1>',
            self.hide
        )

class clear_canvas():
    def request(self, event):
        global clear_window
        clear_window = Toplevel(root)
        clear_window.title('Clear grid?')
        text = Label(
            clear_window,
            text = 'Do you wish to clear the grid by removing your schematic?'
        )
        yes = Button(
            clear_window,
            text = 'Yes'
        )
        no = Button(
            clear_window,
            text = 'No'
        )
        text.grid(
            row = 0
        )
        yes.grid(
            row = 1,
            column = 0
        )
        no.grid(
            row = 1,
            column = 1
        )
        yes.bind(
            '<Button-1>',
            self.clear
        )
        no.bind(
            '<Button-1>',
            self.forget
        )

    def clear(self, event):
        everything = canvas.find_all()

        for thing in everything:
            if 'point' not in canvas.gettags(thing):
                canvas.delete(thing)

        clear_window.destroy()

    def forget(self, event):
        clear_window.destroy()

hide_button = Button(
    root,
    text = 'Hide grid'
)
hide_button.bind(
    '<Button-1>',
    hide_canvas().hide
)
hide_button.grid(
    row = 0
)

clear_button = Button(
    root,
    text = 'Clear'
)
clear_button.bind(
    '<Button-1>',
    clear_canvas().request
)
clear_button.grid(
    row = 2
)

def create_point(x, y):
    point =  canvas.create_oval(
        x - radius,
        y - radius,
        x + radius,
        y + radius,
        fill = point_colour,
        activefill = point_hover,
        outline = '',
        tags = 'point'
    )

    canvas.tag_bind(
        point,
        '<Button-1>',
        draw_wire().set_start
    )

    canvas.tag_bind(
        point,
        '<B1-Motion>',
        draw_wire().set_end
    )

    canvas.tag_bind(
        point,
        '<Button-2>',
        choose_first().menu
    )

for i in range(0, width, displacement):
    for j in range(0, height, displacement):
        create_point(i, j)

root.mainloop()