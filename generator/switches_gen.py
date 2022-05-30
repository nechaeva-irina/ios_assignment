from model.testdata_model import Values
import os
import jsonpickle

testdata = [
    Values(switches_value=0, steppers_value=10, sliders_value=1, picker_red=80, picker_blue=100, picker_green=200)]

file = os.path.join(os.path.dirname(os.path.abspath(__file__)), "../data/switches.json")

with open(file, "w") as f:
    jsonpickle.set_encoder_options("json", indent=2)
    f.write(jsonpickle.encode(testdata))
