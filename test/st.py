# work same as kivy.App used to run the App
from kivy.base import runTouchApp

# to use .kv file as a string we have to import it
from kivy.lang import Builder

# A Widget is the base building block of GUI interfaces in Kivy
from kivy.uix.widget import Widget

# The Clock object allows you to schedule a
# function call in the future
from kivy.clock import Clock

# Animation and AnimationTransition are
# used to animate Widget properties
from kivy.animation import Animation

# The Properties classes are used when
# you create an EventDispatcher.
from kivy.properties import ListProperty

# Core class for creating the default Kivy window.
from kivy.core.window import Window

# As name suggest used when random thiungs required
from random import random

# load the kv file as string
Builder.load_string(''' 
<Root>: 

# Setting the position (initial) of boxes  
	AnimRect: 
		pos: 500, 50 

# creation and animation of red box 
<AnimRect>: 
	canvas: 
		Color: 
			rgba: 0, 1, 0, 1 
		Rectangle: 
			pos: self.pos 
			size: self.size 
''')


# Create the root class
class Root(Widget):
    pass



# Create the Animation class
# And add animaton
# green colour box is animated through this class
class AnimRect(Widget):

    def anim_to_random_pos(self):
        Animation.cancel_all(self)
        random_x = random() * (Window.width - self.width)
        random_y = random() * (Window.height - self.height)

        anim = Animation(size=(100, 300),
                         duration=1,
                         t='linear')
        anim.start(self)

    def on_touch_down(self, touch):
        if self.collide_point(*touch.pos):
            self.anim_to_random_pos()

        # run the App


runTouchApp(Root())
