# (async function () {
# // Reset uArm to its home position.
# await UArm.reset();
# await UArm.set_position({"x": 200, "y": 100, "z": 50});
# }());



#logger_init(logging.DEBUG)
#logger_init(logging.INFO)


import time
import numpy
from uf.wrapper.swift_api import SwiftAPI
from uf.utils.log import *

logger_init(logging.VERBOSE)
swift = SwiftAPI()
time.sleep(2)

positions = numpy.linspace(-200,200,5)
swift.set_gripper(True)

time.sleep(5)

swift.set_gripper(False)
