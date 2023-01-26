"""This programs purpose is to output a descriptive explanation of the inputed model number for a 3051s transmitter
Input: Model numbers must be inputed in upper case to the Instrument Class"""

# TODO import manufac_and_devices.py Use this program to get a dictionary of lists for the available instruments.

#import libraries
from csv_to_dict import CsvToDict
from manufac_and_devices import manuf_and_devices_dict
from command_line import print_program_title, get_users_instrument_options

#Class for an instrument. This should be vague enough to descirpe any electrical instrument from any manufacturer
class Instrument:
    def __init__(self, model_number, manufacturer = "Rosemount", instrument = "3051s-Coplanar"):
        #saves inputed variables to the instrument
        self.model_number = model_number
        self.manufacturer = manufacturer
        self.instrument = instrument

        #string file name
        self.file_name = f".\data_sheets\{self.manufacturer.upper()}_{self.instrument.upper()}.csv"

    def csv_to_dict(self):
        data_sheet = CsvToDict(self.file_name)
        self.spec_options_dict = data_sheet.run()

    # TODO convert this "result" into a dictionary of dictionaries. I can output that both as text and a csv
    # returns a string detailed description of inputed model number
    def get_detailed_description(self):
        
        # initialize variables
        result = ''
        i = 0
        found_code = True

        # loops through dictionary containing spec and options dictionary
        for spec, options in self.spec_options_dict.items():
            
            # Checks if the spec's code was found
            if found_code == False:
                # if code was not found prints
                result += f"no spec\n"
            found_code = False
            
            # prints the spec's title in CAPs
            result += f"{spec.upper()}\n"

            # loops through options to see codes and their descriptions
            for code, description in options.items():

                # check if code matches the model number
                if code == self.model_number[i:i+len(code)]:
                    # prints matching code with discription
                    result += f"{code} -- {description}\n"
                    # adds length of code to placeholder i
                    i += len(code)
                    
                    found_code = True
                    # breaks out of for loop
                    break
        
        return result

if __name__ == "__main__":

    # prints logo
    print_program_title()

    # read's data_sheets folder. Return dictionary of manufacturers and devices. {Rosemount: [648, 848], JMS: [RTD]}
    manuf_devices_dict = manuf_and_devices_dict()

    # Runs command line questions w/ inputed manuf dictionary
    model_number, inputed_manufacturer, inputed_device = get_users_instrument_options(manuf_devices_dict)

    # creating instance of class Instrument
    instrument = Instrument(model_number.upper(), inputed_manufacturer, inputed_device)
    
    #convert data sheet csv to dictionary
    instrument.csv_to_dict()

    # this prints out the detailed description of the inputed model #
    result = instrument.get_detailed_description()
    print(result)