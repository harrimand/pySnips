import gi
gi.require_version('Gtk', '3.0')

from gi.repository import Gtk

class UserInput(Gtk.Window):

    def __init__(self):
        Gtk.Window.__init__(self, title="Widgetry Wizzard")
        self.set_border_width(10)
        self.set_size_request(600, 500)
        self.set_position(Gtk.WindowPosition.CENTER)

        # Layout
        hbox = Gtk.Box(orientation=Gtk.Orientation.HORIZONTAL, spacing=10)
        self.add(hbox)

        vboxL = Gtk.Box(orientation=Gtk.Orientation.VERTICAL, spacing=20)
        hbox.pack_start(vboxL, False, False, 0)

        vboxR = Gtk.Box(orientation=Gtk.Orientation.VERTICAL, spacing=6)
        hbox.pack_start(vboxR, True, True, 0)

        # Text Entry 1
        self.text1 = Gtk.Entry()
        self.text1.set_text("Text 1")
        vboxL.pack_start(self.text1, False, False, 0)

        # Text Entry 2
        self.text2 = Gtk.Entry()
        self.text2.set_text("Text 2")
        self.text2.set_visibility(True)
        vboxL.pack_start(self.text2, False, False, 0)

        # Add Text Button
        self.button = Gtk.Button(label="Add Text")
        self.button.connect("clicked", self.add_text)
        vboxL.pack_start(self.button, False, False, 0)

        # Another Button
        self.button2 = Gtk.Button(label="Do Something")
        self.button2.connect("clicked", self.do_something)
        vboxL.pack_start(self.button2, False, False, 0)

        # Scroll Window (Packed in right side of hbox)
        self.scrolledwindow = Gtk.ScrolledWindow()
        self.scrolledwindow.set_hexpand(True)
        self.scrolledwindow.set_vexpand(True)
        vboxR.pack_start(self.scrolledwindow, True, True, 0)

        # TextView added to Scroll Window
        self.textview = Gtk.TextView()
        self.textbuffer = self.textview.get_buffer()
        self.textbuffer.set_text("This is some text inside of a Gtk.TextView. "
        + "Text entry contents will be added when you click the 'Add Text' button."
        + " Word Wrapping is enabled in this box.  Resizing the window will "
        + "resize this text window without resizing the text entries or the"
        + " button.\n\n")
        self.textview.set_wrap_mode(Gtk.WrapMode.WORD)
        self.scrolledwindow.add(self.textview)

        # Make KeyPad
        self.keypad = Gtk.Grid()
        spc = Gtk.Box(orientation=Gtk.Orientation.VERTICAL, spacing=20)
        spc.pack_start(Gtk.Label(label="       "), False, False, 0)
        self.keypad.attach(spc, 0, 0, 1, 6)
        vboxL.pack_start(self.keypad, True, True, 0)

        keys = [    " D ", " E ", " F ", " * ",
                    " A ", " B ", " C ", " / ",
                    " 7 ", " 8 ", " 9 ", " + ",
                    " 4 ", " 5 ", " 6 ", " - ",
                    " 1 ", " 2 ", " 3 ", " \\ ",
                    " . ", " 0 ", " # ", " ^2"
                    ]
        cols = 4

        self.keyPadButton = [Gtk.Button(label = k) for k in keys]
        for i, kp in enumerate(self.keyPadButton):
            kp.connect("clicked", self.key_pressed)
            self.keypad.attach(kp, i % cols + 4, i // cols, 1, 1)

        # Add Image to vboxL
        self.eventbox = Gtk.EventBox()
        self.eventbox.connect("button-press-event", self.image_clicked)
        self.image = Gtk.Image()
        self.image.set_from_file("phylo.png")
        self.image.set_tooltip_text("Wet Paint")
        self.eventbox.add(self.image)
        vboxL.pack_start(self.eventbox, False, False, 0)

    # Append entry1 and entry1 when 'Add Text' button clicked
    def add_text(self, widget):
        end_iter = self.textbuffer.get_end_iter()
        self.textbuffer.insert(end_iter, "\n" + self.text1.get_text())
        end_iter = self.textbuffer.get_end_iter()
        self.textbuffer.insert(end_iter, "\t" + self.text2.get_text())

    # Append window size when 'Do Something' button clicked
    def do_something(self, widget):
        W, H = self.get_size()
        end_iter = self.textbuffer.get_end_iter()
        self.textbuffer.insert(end_iter, "\nWindow Size: " + str(W) + " x " + str(H) + "\n")

    # Append keypad button label
    def key_pressed(self, widget):
        end_iter = self.textbuffer.get_end_iter()
        label = widget.get_label().strip()
        if label.isdigit() or label in "ABCDEF.":
            self.textbuffer.insert(end_iter, label)
        else: self.textbuffer.insert(end_iter, " " + label + " ")

    # Append Mouse Coordinates when the image is clicked.
    def image_clicked(self, widget, event):
        end_iter = self.textbuffer.get_end_iter()
        xy = " X: {0:.2f}   Y: {1:.2f}".format(event.x, event.y)
        self.textbuffer.insert(end_iter, "\n\tDon't touch the image!!\t" + xy)

window = UserInput()
window.connect("delete-event", Gtk.main_quit)
window.show_all()
Gtk.main()

