import visa
rm = visa.ResourceManager()

def setup():
    if "GPIB0::20::INSTR" in rm.list_resources():
        keithley = rm.open_resource("GPIB0::20::INSTR")
        return "Successful Setup"
    else:
        return "GPIB Port has not been detected"

def reset():
    keithley = rm.open_resource("GPIB0::20::INSTR")
    keithley.write("*rst; status:preset; *cls")

def output():
    keithley = rm.open_resource("GPIB0::20::INSTR")
    keithley.write(":OUTP ON")
