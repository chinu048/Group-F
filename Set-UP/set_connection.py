import visa
# sys.path.append(os.path.dirname(os.getcwd()) + "/Generating-Functions" )
# import
rm = visa.ResourceManager()

def setup():
    if "GPIB0::20::INSTR" in rm.list_resources():
        keithley = rm.open_resource("GPIB0::20::INSTR")
        return True
    else:
        return False


def reset():
    keithley = rm.open_resource("GPIB0::20::INSTR")
    keithley.write("*rst; status:preset; *cls")

def output():
    keithley = rm.open_resource("GPIB0::20::INSTR")
    keithley.write(":OUTP ON")

def general_setup():
    rm = visa.ResourceManager()
    keithley = rm.open_resource("GPIB0::20::INSTR")
    return keithley
