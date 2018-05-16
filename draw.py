
#!/usr/bin/python

# ZetCode PyGTK tutorial 
# http://zetcode.com/gui/pygtk/drawing/
# This code example draws basic shapes
# with the cairo library
#

import math
import gi
gi.require_version('Gtk', '3.0')
from gi.repository import Gtk
# from gi.repository import GObject

class PyApp(Gtk.Window):

    def __init__(self):
        super(PyApp, self).__init__()

        self.set_title("Basic shapes")
        self.set_size_request(390, 240)
        self.set_position(Gtk.WindowPosition.CENTER)

        self.connect("destroy", Gtk.main_quit)

        darea = Gtk.DrawingArea()
        darea.connect("draw", self.expose) # Replace 'expose-event' with draw
        self.add(darea)

        self.show_all()

    def expose(self, widget, event):
        cr = widget.get_property('window').cairo_create()
#        cr = widget.window.cairo_create()
        cr.rectangle(20, 20, 120, 80)
        cr.set_source_rgb(.9, .9, .1)
        cr.fill()

        cr.rectangle(180, 20, 80, 80)
        cr.set_source_rgb(0.2, 0.23, 0.9)
        cr.fill()

        cr.arc(330, 60, 40, 0, 2*math.pi)
        cr.set_source_rgb(0.9, 0.23, 0.9)
        cr.fill()

        cr.arc(90, 160, 40, math.pi/4, math.pi)
        cr.set_source_rgb(0.2, 0.8, 0.6)
        cr.fill()

        cr.translate(220, 180)
        cr.scale(1, 0.7)
        cr.arc(0, 0, 50, 0, 2*math.pi)
        cr.set_source_rgb(0.9, 0.4, 0.7)
        cr.fill()


PyApp()
Gtk.main()

