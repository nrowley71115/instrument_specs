"""The purpose of this program is to determine the options for manufacturers and devices through the csv files' names in the 'data_sheets' folder.
The data sheets are named in this convention: MANUFACTURER_DEVICE.csv
Input: none
Output: a dictionary of lists. The key will be the manufacturers and values are a list of all the manufacturers' devices """

import os

PATH = './data_sheets/'

def manuf_and_devices_dict():
    # a list of strings containing all of the file names within data_sheets folder
    files = os.listdir(PATH)

    # Create variable
    manuf_devices_dict = {}
    manufacturer_repeat = False

    # Loops through list of file names
    for file in files:
        
        # splits string file names into before and after '_' 
        split_string = file.split('_')
        manufacturer, device = split_string

        # gets rid of '.csv' at the end of the string
        index = device.index('.')
        device = device[:index]

        # loops through the dictionary of lists
        for key, value in manuf_devices_dict.items():
            
            # has the manufacturer already been entered?
            if key == manufacturer:
                manufacturer_repeat = True
                break
            
            # the manufacturer is not yet in the dictionary
            else:
                manufacturer_repeat = False

        if manufacturer_repeat == True:
            device_list = manuf_devices_dict[manufacturer]
            device_list.append(device)
            manuf_devices_dict[manufacturer] = device_list
            pass
        else:
            manuf_devices_dict[manufacturer] = [device]

    return(manuf_devices_dict)