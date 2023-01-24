"""The purpose of this program is to communicate with the command line.
Input: A dictionary of lists. The key is the manufacturer and the list is all the available devices from said manufacturer
Interum: Allows user to select from these choices in the command line & input model number
Output: Returns a list of 3 elements. model_number, manufacturer, and device"""

import pyfiglet
from manufac_and_devices import manuf_and_devices_dict

def get_users_instrument_options(manuf_devices_dict):
    
    # manuf_devices_dict is a dictionary of key manufacturers and lists of their devices. All strings are in CAPS
    available_manuf = []
    available_devices = []

    for key, values in manuf_devices_dict.items():
        available_manuf.append(key)

    string = f'-AVAILABLE MANUFACTURERS-\n{available_manuf}\n\n'
    print(string)
    
    loop = True

    while loop:
        inputed_manufacturer = input("What is the manufacturer of your instrument? ")
        inputed_manufacturer = inputed_manufacturer.upper()
        inputed_manufacturer = inputed_manufacturer.strip()

        for manufacturer in available_manuf:
            
            if inputed_manufacturer == manufacturer:
                loop = False
    
    for key, values in manuf_devices_dict.items():
        if key == inputed_manufacturer:
            available_devices = values

    string = f'\n\n-AVAILABLE MANUFACTURERS-\n{available_devices}\n\n'
    print(string)

    loop = True

    while loop:
        inputed_device = input("What is the device of your instrument? ")
        inputed_device = inputed_device.upper()
        inputed_device = inputed_device.strip()

        for device in available_devices:
            
            if inputed_device == device:
                loop = False

    model_number = input("What is the model number? ")

    return model_number, inputed_manufacturer, inputed_device


def print_program_title():
    result = pyfiglet.figlet_format("EASTMAN", font = "big") 
    print(result)
    result = pyfiglet.figlet_format("INSTRUMENT MODEL NUMBER", font = 'small') 
    print(result)


if __name__ == "__main__":
    manuf_and_devices = manuf_and_devices_dict()

    print_program_title()

    get_users_instrument_options(manuf_and_devices)
