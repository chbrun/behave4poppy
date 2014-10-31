#!/usr/bin/env python
# -*- coding: utf-8 -*-

from behave import *
import json
import time
from pypot.vrep import from_vrep

# en
@given(u'Poppy initialisation')
# fr
@given(u'Poppy s\'initialise')
def step_impl(context):
    context.poppy.start_sync()

# en
@when(u'Poppy turns head to the left "{value}"')
# fr
@when(u'Poppy tourne la tête à gauche de "{value}"')
def step_impl(context, value):
    print "DEBUG"
    context.poppy.head_z.goal_position = int(value)
    print context.poppy.motors

# en
@then(u'waiting 2s')
# fr
@then(u'Attente de 2s')
def step_impl(context):
    time.sleep(2)

# en
@when(u'Poppy turns head to the right "{value}"')
# fr
@when(u'Poppy tourne la tête à droite de "{value}"')
def step_impl(context, value):
    context.poppy.head_z.goal_position = -int(value)

