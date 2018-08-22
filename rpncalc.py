
import gi
gi.require_version('Gtk', '3.0')

from gi.repository import Gtk, Pango
from rpn import rpn

class UserInput(Gtk.Window, rpn):

    def __init__(self):
        Gtk.Window.__init__(self, title="RPN Calculator")
        self.set_border_width(10)
        self.set_size_request(600, 500)
        self.set_position(Gtk.WindowPosition.CENTER)

        # Layout
        vbox = Gtk.Box(orientation=Gtk.Orientation.VERTICAL, spacing=10)
        self.add(vbox)

        # Scroll Window (Packed in right side of hbox)
        self.scrolledwindow = Gtk.ScrolledWindow()
        self.scrolledwindow.set_hexpand(True)
        self.scrolledwindow.set_vexpand(True)
        vbox.pack_start(self.scrolledwindow, True, True, 0)

        # TextView added to Scroll Window
        self.textview = Gtk.TextView()
        font = Pango.FontDescription('monospace 14')
        self.textview.modify_font(font)
        self.textbuffer = self.textview.get_buffer()
        self.textbuffer.set_text("RPN Calculator by Darrell Harriman\
        \n\n\tEnter h for help\n\n")
        self.textview.set_wrap_mode(Gtk.WrapMode.WORD)
        self.scrolledwindow.add(self.textview)

        # Text Entry 1
        self.text1 = Gtk.Entry()
        self.text1.set_text("")
        self.text1.connect("activate", self.submit_entry1)
        vbox.pack_start(self.text1, False, False, 0)

        self.R = rpn("")
        self.text1.grab_focus()

# Update stack and textview when 'Enter' pressed 
    def submit_entry1(self, widget):
        rpnStr = self.text1.get_text()
        if rpnStr == '?':
            self.textbuffer.set_text(self.R.help())
            self.text1.set_text("")
        elif rpnStr.startswith("exit"):
            Gtk.main_quit()
        else:
            self.R.update(rpnStr)
            rStr = self.R.getStack()
            # end_iter = self.textbuffer.get_end_iter()
            self.textbuffer.set_text(rStr)
            # self.textbuffer.insert(end_iter, "\n" + rpnStr)
            self.text1.set_text("")
#            adj = self.scrolledwindow.get_vadjustment()
#            adj.set_value(adj.upper - adj.page_size)

            # it = self.textbuffer.get_iter_at_line(self.textbuffer.get_line_count())
            # self.textview.scroll_to(it)


window = UserInput()
window.connect("delete-event", Gtk.main_quit)
window.show_all()
Gtk.main()


