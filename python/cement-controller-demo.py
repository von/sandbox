#!/usr/bin/env python
"""Demo of cement framework

builtoncement.org/

pip install cement
"""

from __future__ import print_function  # So we can get at print()

from cement.core import controller, foundation, handler


class MyAppBaseController(controller.CementBaseController):
    class Meta:
        label = 'base'
        description = "cemment controller demo"

        config_defaults = dict(
            foo='bar',
            some_other_option='my default value',
        )

        arguments = [
            (['-p', '--peal'],
             dict(action='store_true',
                  help='peal!')),
        ]

    @controller.expose(hide=True)
    def default(self):
        print('Inside base.default function.')
        if self.pargs.peal:
            print("Recieved option 'peal'")

    @controller.expose(help="the 'apple' command")
    def apple(self):
        print("Inside base.apple function.")


# Define a second controller that is embedded
class MySecondController(controller.CementBaseController):
    class Meta:
        label = 'citrus'
        stacked_on = "base"
        stacked_type = "embedded"
        arguments = [
            (['-s', '--slice'],
             dict(action='store_true',
                  help='the slice option')),
        ]

    @controller.expose(help="the 'orange' command")
    def orange(self):
        print('Inside citrus.orange function.')
        if self.pargs.peal:
            print("Recieved option 'peal'")


# Define a third controller that is nested
# XXX This doesn't seem to act as expected, seems to act
# just as an embedded controller
class MyThirdController(controller.CementBaseController):
    class Meta:
        label = 'yellow'
        stacked_on = "base"
        stacked_type = "nested"
        arguments = [
            (['-d', '--dice'],
             dict(action='store_true',
                  help='the dice option')),
        ]

    @controller.expose(help="the 'banana' command")
    def banana(self):
        print('Inside yellow.banana function.')
        if self.pargs.dice:
            print("Recieved option 'dice'")


# Define a fourth controller that is not stacked
# This allows a controller to have separate options
# By defining a default(), this can appear to be at
# the same level as base commands.
class MyFourthController(controller.CementBaseController):
    class Meta:
        label = 'grape'
        description = "the 'grape' command (controller really)"
        stacked_on = None
        arguments = [
            (['-j', '--juice'],
             dict(action='store_true',
                  help='the juice option')),
        ]

    @controller.expose(hide=True)
    def default(self):
        print('Inside grape.default function.')
        if self.pargs.juice:
            print("Recieved option 'juice'")

    @controller.expose(help="the 'grape' command")
    def concord(self):
        print('Inside grape.concord function.')
        if self.pargs.juice:
            print("Recieved option 'juice'")


class MyApp(foundation.CementApp):
    class Meta:
        label = 'helloworld'
        base_controller = MyAppBaseController

# create the app
app = MyApp()

# Register any handlers that aren't passed directly to CementApp
handler.register(MySecondController)
handler.register(MyThirdController)
handler.register(MyFourthController)

try:
    # setup the application
    app.setup()

    # run the application
    app.run()
finally:
    # close the app
    app.close()
