# -*- coding: utf-8 -*-

import sys
import gi

gi.require_version(namespace='Gtk', version='4.0')
gi.require_version(namespace='Adw', version='1')

from gi.repository import Adw, Gio, Gtk

#Adw.init()

class LoginWindow(Gtk.Window):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self.set_title(title='Proxmox VDI Client')
        self.set_default_size(width=300, height=180)
        self.set_size_request(width=300, height=180)
        self.set_resizable(False)
        
        self.headerbar = Gtk.HeaderBar.new()
        self.headerbar.set_show_title_buttons(False)
        self.set_titlebar(self.headerbar)

        self.button_cancel = Gtk.Button(label="Cancel")
        self.headerbar.pack_start(self.button_cancel)  
        
        self.button_login = Gtk.Button(label="Login")
        self.button_login.get_style_context().add_class ('suggested-action')
        self.headerbar.pack_end(self.button_login)   

        label_username = Gtk.Label(label='Username')
        label_password = Gtk.Label(label='Password')

        entry_username = Gtk.Entry()
        entry_username.set_placeholder_text('')
        entry_password = Gtk.PasswordEntry()
        entry_password.set_show_peek_icon(True)
        
        grid = Gtk.Grid()
        grid.set_halign(Gtk.Align.CENTER)
        grid.set_valign(Gtk.Align.CENTER)
        grid.set_row_spacing(15)
        grid.set_column_spacing(20)
        
        grid.attach(label_username,0,0,1,1)
        grid.attach(entry_username,1,0,1,1)
        grid.attach(label_password,0,1,1,1)
        grid.attach(entry_password,1,1,1,1)
        self.set_child(grid)

class MainWindow(Gtk.ApplicationWindow):

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self.set_title(title='Proxmox VDI Client')
        self.set_default_size(width=int(1366 / 2), height=int(768 / 2))
        self.set_size_request(width=int(1366 / 2), height=int(768 / 2))
        self.set_resizable(False)
        
        self.headerbar = Gtk.HeaderBar.new()
        self.set_titlebar(self.headerbar)

        self.button_left = Gtk.Button(label="Login")
        self.button_left.get_style_context().add_class ('suggested-action')
        self.button_left.connect("clicked", self.button_left_clicked) #
        self.headerbar.pack_start(self.button_left)

        vbox = Gtk.Box.new(orientation=Gtk.Orientation.VERTICAL, spacing=12)
        vbox.set_margin_top(margin=12)
        vbox.set_margin_end(margin=100)
        vbox.set_margin_bottom(margin=12)
        vbox.set_margin_start(margin=100)
        self.set_child(child=vbox)

        listbox = Gtk.ListBox.new()
        listbox.set_selection_mode(mode=Gtk.SelectionMode.NONE)
        listbox.get_style_context().add_class(class_name='boxed-list')
        vbox.append(child=listbox)
      
        for n in range(1, 4):
            adw_action_row = Adw.ActionRow.new()
            adw_action_row.set_icon_name(icon_name='computer-symbolic')
            adw_action_row.set_title(title=f'Verbindung {n}')
            adw_action_row.set_subtitle(subtitle='Verbindungsdetails')
            
            button = Gtk.Button(label="Verbinden")
            
            vbox = Gtk.Box.new(orientation=Gtk.Orientation.HORIZONTAL, spacing=12)
            vbox.set_margin_top(margin=12)
            vbox.set_margin_bottom(margin=12)
            vbox.append(child=button)
            
            adw_action_row.add_suffix(widget=vbox)
            listbox.append(child=adw_action_row)

    def button_left_clicked(self, widget):
            var = LoginWindow()
            var.set_modal(True)
            var.show()




class MyApp(Adw.Application):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.connect('activate', self.on_activate)

    def on_activate(self, app):
        self.win = MainWindow(application=app)
        self.win.present()

app = MyApp(application_id="com.example.GtkApplication")
app.run(sys.argv)

