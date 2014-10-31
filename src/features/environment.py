from behave import *
import json
import time

def before_all(context):
    from pypot.vrep import from_vrep
    with open('poppy_config.json') as f:
        poppy_config = json.load(f)
    scene_math = 'poppy-standing2.ttt'
    context.poppy = from_vrep(poppy_config, '127.0.0.1', 19997, scene_math)
    context.poppy.start_sync()
    for m in context.poppy.motors:
        m.compliant = False

def after_step(context,step):
    # pause necessaire pour que vrep prenne en compte le mouvement
    time.sleep(0.5)

def after_all(context):
    assert True
