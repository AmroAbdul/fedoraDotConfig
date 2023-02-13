# Copyright (c) 2010 Aldo Cortesi
# Copyright (c) 2010, 2014 dequis
# Copyright (c) 2012 Randall Ma
# Copyright (c) 2012-2014 Tycho Andersen
# Copyright (c) 2012 Craig Barnes
# Copyright (c) 2013 horsik
# Copyright (c) 2013 Tao Sauvage
#
# Permission is hereby granted, free of charge, to any person obtaining a copy
# of this software and associated documentation files (the "Software"), to deal
# in the Software without restriction, including without limitation the rights
# to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
# copies of the Software, and to permit persons to whom the Software is
# furnished to do so, subject to the following conditions:
#
# The above copyright notice and this permission notice shall be included in
# all copies or substantial portions of the Software.
#
# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
# IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
# FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
# AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
# LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
# OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
# SOFTWARE.


import os
import re
import socket
import subprocess
from typing import List  # noqa: F401
from libqtile import layout, bar, widget, hook, qtile
from libqtile.config import Click, Drag, Group, Key, Match, Screen, Rule
from libqtile.command import lazy
from libqtile.widget import Spacer
from parts.keys import keys
from parts.mouse import mouse
from qtile_extras import widget

from qtile_extras.widget.decorations import BorderDecoration, PowerLineDecoration, RectDecoration



# powerline = {
#     "decorations": [
#         PowerLineDecoration()
#     ]
# }
#mod4 or mod = super key
mod = "mod4"

home = os.path.expanduser('~')


@lazy.function
def window_to_prev_group(qtile):
    if qtile.currentWindow is not None:
        i = qtile.groups.index(qtile.currentGroup)
        qtile.currentWindow.togroup(qtile.groups[i - 1].name)

@lazy.function
def window_to_next_group(qtile):
    if qtile.currentWindow is not None:
        i = qtile.groups.index(qtile.currentGroup)
        qtile.currentWindow.togroup(qtile.groups[i + 1].name)


# def whatever():
#     bar = qtile.current_screen.all
#     if (lazy.window.toggle_maximize() and bar.size == 0):
#         window.gap=0

# @hook.subscribe.layout_change
# def layout_change(layout, group): 
#     bar = qtile.current_screen.all
#     if bar.size == 0 and lazy.window.toggle_maximize(): 
#         qtile.current_screen.top.margin = 0
#     else: 
#         qtile.current_screen.top.margin = 2




#
def window_to_previous_screen(qtile, switch_group=False, switch_screen=False):
    i = qtile.screens.index(qtile.current_screen)
    if i != 0:
        group = qtile.screens[i - 1].group.name
        qtile.current_window.togroup(group, switch_group=switch_group)
        if switch_screen == True:
            qtile.cmd_to_screen(i - 1)

def window_to_next_screen(qtile, switch_group=False, switch_screen=False):
    i = qtile.screens.index(qtile.current_screen)
    if i + 1 != len(qtile.screens):
        group = qtile.screens[i + 1].group.name
        qtile.current_window.togroup(group, switch_group=switch_group)
        if switch_screen == True:
            qtile.cmd_to_screen(i + 1)

keys.extend([
    # MOVE WINDOW TO NEXT SCREEN
    Key([mod,"shift"], "Right", lazy.function(window_to_next_screen, switch_screen=True)),
    Key([mod,"shift"], "Left", lazy.function(window_to_previous_screen, switch_screen=True)),
])
################## GROUPS ##################################
groups = []

# FOR QWERTY KEYBOARDS
group_names = ["1", "2", "3", "4", "5", "6", "7", "8", "9", "0",]

# FOR AZERTY KEYBOARDS
#group_names = ["ampersand", "eacute", "quotedbl", "apostrophe", "parenleft", "section", "egrave", "exclam", "ccedilla", "agrave",]

#group_labels = ["1 ", "2 ", "3 ", "4 ", "5 ", "6 ", "7 ", "8 ", "9 ", "0",]
#group_labels = ["", "", "", "", "", "", "", "", "", "",]
group_labels = ["α", "β", "γ", "δ", "ε", "ζ", "η", "θ", "ι", "κ",]
#group_labels = ["Web", "Edit/chat", "Image", "Gimp", "Meld", "Video", "Vb", "Files", "Mail", "Music",]

group_layouts = ["monadtall", "monadtall", "monadtall", "monadtall", "monadtall", "monadtall", "monadtall", "monadtall", "monadtall", "monadtall",]
#group_layouts = ["monadtall", "matrix", "monadtall", "bsp", "monadtall", "matrix", "monadtall", "bsp", "monadtall", "monadtall",]

for i in range(len(group_names)):
    groups.append(
        Group(
            name=group_names[i],
            layout=group_layouts[i].lower(),
            label=group_labels[i],
        ))

for i in groups:
    keys.extend([

#CHANGE WORKSPACES
        Key([mod], i.name, lazy.group[i.name].toscreen()),
        Key(["mod1" ], "Shift_L" , lazy.widget["keyboardlayout"].next_keyboard(),   desc="Next keyboard layout"),
        #Key([mod], "Tab", lazy.screen.next_group()),
        Key([mod, "shift" ], "Tab", lazy.screen.prev_group()),
        Key(["mod1"], "Tab", lazy.screen.next_group()),
        Key(["mod1", "shift"], "Tab", lazy.screen.prev_group()),

# MOVE WINDOW TO SELECTED WORKSPACE 1-10 AND STAY ON WORKSPACE
        #Key([mod, "shift"], i.name, lazy.window.togroup(i.name)),
# MOVE WINDOW TO SELECTED WORKSPACE 1-10 AND FOLLOW MOVED WINDOW TO WORKSPACE
        Key([mod, "shift"], i.name, lazy.window.togroup(i.name) , lazy.group[i.name].toscreen()),
    ])


def init_layout_theme():
    return {"margin":5,
            "border_width":2,
            "border_focus": "#91DFAE",
            "border_normal": "#070915"
            }

layout_theme = init_layout_theme()
auto_fullscreen = True
def init_max_layout_theme():
    return {"margin": 0,
            "border_width":1,
            "border_normal":"#004545"
            }
max_layout_theme = init_max_layout_theme()
@hook.subscribe.layout_change
def layout_changed(layout, group):
    if layout.name == "max":
        # For illustrative purposes, I'm assuming the bar is on the top
        qtile.current_screen.top.margin = 0
        # To get the new margin, we have to reconfigure the bar
        qtile.current_screen.top._configure(qtile, qtile.current_screen)
        # Now redraw the layout
        group.layout_all()



layouts = [
    # default layout is the first one declared
    #layout.MonadTall(margin=8, border_width=2, border_focus="#5e81ac", border_normal="#4c566a"),
    layout.Bsp(**layout_theme),   
    layout.MonadTall(**layout_theme),
    #layout.MonadWide(margin=8, border_width=2, border_focus="#5e81ac", border_normal="#4c566a"),
    layout.MonadWide(**layout_theme),
    layout.Matrix(**layout_theme),
    layout.Floating(**layout_theme),
    layout.RatioTile(**layout_theme),
    layout.Max(**max_layout_theme)
]

# COLORS FOR THE BAR
#Theme name : Garuda Default



def init_colors():
    return [["#282c34", "#282c34"],#0
            ["#1c1f24", "#1c1f24"],#1
            ["#dfdfdf", "#dfdfdf"],#2
            ["#ff6c6b", "#ff6c6b"],#3
            ["#98be65", "#98be65"],#4
            ["#da8548", "#da8548"],#5
            ["#51afef", "#51afef"],#6
            ["#c678dd", "#c678dd"],#7
            ["#46d9ff", "#46d9ff"],#8
            ["#a9a1e1", "#a9a1e1"],#9
            ["#ff00ff", "#ff00ff"], #10
            ["#070915", "#070915"],#11
            ["#91DFAE", "#91DFAE"],#12
            ["#4c566a", "#4c566a"], #13 
            ["#282c34", "#282c34"], #14
            ["#212121", "#212121"], #15
            ["#e75480", "#e75480"], #16 
            ["#2aa899", "#2aa899"], #17 
            ["#abb2bf", "#abb2bf"],# 18
            ["#81a1c1", "#81a1c1"], #19 
            ["#56b6c2", "#56b6c2"], #20 
            ["#b48ead", "#b48ead"], #21 
            ["#e06c75", "#e06c75"], #22
            ["#ff79c6", "#ff79c6"], #23
            ["#ffb86c", "#ffb86c"]] #24



colors = init_colors()


# WIDGETS FOR THE BAR

def init_widgets_defaults():
    return dict(font="Noto Sans",
                fontsize = 12,
                padding = 2,
                background=colors[5])

widget_defaults = init_widgets_defaults()

## mouse callbacks
def open_rofi(qtile):
    qtile.cmd_spawn('dmenu_run')

extension_defaults = widget_defaults.copy()

# lazy.widget["keyboardlayout"].next_keyboard()

def init_widgets_list():
    prompt = "{0}@{1}: ".format(os.environ["USER"], socket.gethostname())
    widgets_list = [

                widget.Image(
                  filename = "~/.config/qtile/icons/python.png",
                  background = colors[22],
                  padding= 1,
                  decorations=[
                                RectDecoration(
                                            radius=12,
                                            use_widget_background=True
                        )
                    ],
                  mouse_callbacks = {
                                      'Button1': lambda: qtile.cmd_spawn('rofi -show p -modi p:rofi-power-menu -font "Saucecodepro NF 16"  -width 9'),

                }
                         
            
            ),
               widget.TextBox(
                font="SauceCode Pro NF",
                fontsize= 15,
                text=" 󰊷 ",
                background = colors[11],
                foreground = colors[12],
                padding = 0
               ),
               widget.TextBox(
                font="SauceCode Pro NF",
                fontsize= 15,
                text="  ",
                background = colors[11],
                foreground = colors[12],
                padding = 0
               ),
               widget.TextBox(
                font="SauceCode Pro NF",
                fontsize= 15,
                text="  ",
                background = colors[11],
                foreground = colors[12],
                padding = 0
               ),
               widget.TextBox(
                font="SauceCode Pro NF",
                fontsize= 15,
                text=" 󰊫 ",
                background = colors[11],
                foreground = colors[12],
                padding = 0
               ),
               widget.TextBox(
                font="SauceCode Pro NF",
                fontsize= 15,
                text="  ",
                background = colors[11],
                foreground = colors[12],
                padding = 0,
                
               ),
               widget.Sep(
                foreground=colors[11],
                background=colors[11]
               ),
               widget.GroupBox(
                       font = "JetBrains Mono",
                       fontsize = 12,
                       margin_y = 3,
                       margin_x = 0,
                       padding_y = 5,
                       padding_x = 3,
                       borderwidth = 3,
                       active = colors[16],
                       inactive = colors[7],
                       rounded = False,
                       disable_drag = True,
                       highlight_color = colors[1],
                       highlight_method = "line",
                       foreground = colors[12],
                       background = colors[11],
                       this_current_screen_border=colors[18],
                       decorations=[
                           BorderDecoration(
                               colour = colors[9],
                               border_width = [0, 0, 2, 0],
                               padding_x = 5,
                               padding_y = None,
                           ),
                           PowerLineDecoration(
                               path="rounded_right",
                               colour = colors[9],
                               border_width = [0, 0, 2, 0],
                               padding_x = 5,
                               padding_y = None,
                           )
                           
                    
                       ],

                        ),
               widget.Sep(
                        linewidth = 0,
                        padding = 10,
                        background = colors[11],
                        

                        ),
               widget.Sep(
                        linewidth = 0,
                        padding = 10,
                        background = colors[11],
                decorations=[
                           PowerLineDecoration(
                               path="rounded_right",
                               colour = colors[9],
                               border_width = [0, 0, 2, 0],
                               padding_x = 5,
                               padding_y = None,
                           )
                       ],



                        ),



                widget.Sep(
                       linewidth = 0,
                       padding = 0,
                       background = colors[11],

                       


                       ),
        
               widget.CurrentLayout(
                        font = "Noto Sans",
                        foreground = colors[11],
                        background = colors[7],

               

                        ),

                widget.CurrentLayoutIcon(
                       custom_icon_paths = [os.path.expanduser("~/.config/qtile/icons")],
                    #    foreground = colors[19],
                       background = colors[7],
                       
                       padding = 0,
                       margin_y=7,
                       font="FontAwesome",
                       scale = 0.9,
                        decorations=[
                           PowerLineDecoration(
                               path="rounded_right",
                               colour = colors[9],
                               border_width = [0, 0, 2, 0],
                               padding_x = 5,
                               padding_y = None,
                           )
                       ],

                         
                       ),
               # widget.Net(
               #          font="Noto Sans",
               #          fontsize=12,
               #          interface="enp0s31f6",
               #          foreground=colors[2],
               #          background=colors[1],
               #          padding = 0,
               #          ),
               # widget.Sep(
               #          linewidth = 1,
               #          padding = 10,
               #          foreground = colors[2],
               #          background = colors[1]
               #          ),
               # widget.NetGraph(
               #          font="Noto Sans",
               #          fontsize=12,
               #          bandwidth="down",
               #          interface="auto",
               #          fill_color = colors[8],
               #          foreground=colors[2],
               #          background=colors[1],
               #          graph_color = colors[8],
               #          border_color = colors[2],
               #          padding = 0,
               #          border_width = 1,
               #          line_width = 1,
               #          ),
               # widget.Sep(
               #          linewidth = 1,
               #          padding = 10,
               #          foreground = colors[2],
               #          background = colors[1]
               #          ),
               # # do not activate in Virtualbox - will break qtile
               # widget.ThermalSensor(
               #          foreground = colors[5],
               #          foreground_alert = colors[6],
               #          background = colors[1],
               #          metric = True,
               #          padding = 3,
               #          threshold = 80
               #          ),
               # # battery option 1  ArcoLinux Horizontal icons do not forget to import arcobattery at the top
               # widget.Sep(
               #          linewidth = 1,
               #          padding = 10,
               #          foreground = colors[2],
               #          background = colors[1]
               #          ),
               # arcobattery.BatteryIcon(
               #          padding=0,
               #          scale=0.7,
               #          y_poss=2,
               #          theme_path=home + "/.config/qtile/icons/battery_icons_horiz",
               #          update_interval = 5,
               #          background = colors[1]
               #          ),
               # # battery option 2  from Qtile
               # widget.Sep(
               #          linewidth = 1,
               #          padding = 10,
               #          foreground = colors[2],
               #          background = colors[1]
               #          ),
            #    widget.Battery(
            #             font="Noto Sans",
            #             update_interval = 10,
            #             fontsize = 12,
            #             foreground = colors[5],
            #             background = colors[1],
	        #             ),
               # widget.TextBox(
               #          font="FontAwesome",
               #          text="  ",
               #          foreground=colors[6],
               #          background=colors[1],
               #          padding = 0,
               #          fontsize=16
               #          ),
            #    widget.CPUGraph(
            #             fill_color = colors[11],
            #             graph_color = colors[12],
            #             background=colors[11],
            #             border_width = 0,
            #             line_width = 2,
            #             core = "all",
            #             type = "line",
            #            decorations=[
            #                BorderDecoration(
            #                    colour = colors[9],
            #                    border_width = [0, 0, 2, 0],
            #                    padding_x = 5,
            #                    padding_y = None,
            #                )
            #            ],
                
            #             ),
               # widget.Sep(
               #          linewidth = 1,
               #          padding = 10,
               #          foreground = colors[2],
               #          background = colors[1]
               #          ),
               # widget.TextBox(
               #          font="FontAwesome",
               #          text="  ",
               #          foreground=colors[4],
               #          background=colors[1],
               #          padding = 0,
               #          fontsize=16
               #          ),
               # widget.Memory(
               #          font="Noto Sans",
               #          format = '{MemUsed}M/{MemTotal}M',
               #          update_interval = 1,
               #          fontsize = 12,
               #          foreground = colors[5],
               #          background = colors[1],
               #         ),
               # widget.Sep(
               #          linewidth = 1,
               #          padding = 10,
               #          foreground = colors[2],
               #          background = colors[1]
               #          ),


               widget.TextBox(
                        font="FontAwesome",
                        text="",
                        foreground=colors[0],
                        background=colors[19],
                        padding = 0,
                        fontsize=16,
                        decorations=[
                           PowerLineDecoration(
                               path="rounded_right",
                               colour = colors[9],
                               border_width = [0, 0, 2, 0],
                               padding_x = 5,
                               padding_y = None,
                           )
                       ],
                        ),
               widget.Clock(
                        foreground = colors[0],
                        background = colors[19],
                        fontsize = 12,
                        padding=0,
                        format="%d-%m;%H:%M",
                        decorations=[
                           PowerLineDecoration(
                               path="rounded_right",
                               colour = colors[9],
                               border_width = [0, 0, 2, 0],
                               padding_x = 5,
                               padding_y = None,
                           )
                       ],


                        ),
                widget.TextBox(
                    background=colors[19],
                    foreground=colors[0],
                    font="FontAwesome",
                    padding=0,
                    fontsize=16,
                    text="󱑏 ",
                    decorations=[
                           PowerLineDecoration(
                               path="rounded_right",
                               colour = colors[9],
                               border_width = [0, 0, 2, 0],
                               padding_x = 5,
                               padding_y = None,
                           )
                       ],


                ),

               # widget.Sep(
               #          linewidth = 1,
               #          padding = 10,
               #          foreground = colors[2],
               #          background = colors[1]
               #          ),

                widget.KeyboardLayout(
                         font="Noto Sans Bold",
                         configured_keyboards = ['us', 'tr', 'ar'],
                         display_map = {'us':'EN','tr':'TR','ar':'AR'},
                         fontsize = 12,
                         foreground = colors[15],
                         background = colors[12],
                        decorations=[
                           PowerLineDecoration(
                               path="rounded_right",
                               colour = colors[9],
                               border_width = [0, 0, 2, 0],
                               padding_x = 5,
                               padding_y = None,
                           )
                       ],

                        ),


               widget.Systray(
                        background=colors[2],
                        icon_size=20,
                        padding = 0,



                        ),
              ]
    return widgets_list

widgets_list = init_widgets_list()



def init_bottom_widgets():
    prompt = "{0}@{1}: ".format(os.environ["USER"], socket.gethostname())
    widget_list2 = [


               widget.WindowName(font="Noto Sans Bold",

                        fontsize = 12,
                        format='{state}{name}',
                        foreground = colors[12],
                        background = colors[11],
                        padding=9,
                        decorations=[
                           PowerLineDecoration(
                               path="rounded_right",
                               colour = colors[9],
                               border_width = [0, 0, 2, 0],
                               padding_x = 5,
                               padding_y = None,
                           )
                       ],)

        
    ]
    return widget_list2

widget_list2 = init_bottom_widgets()



def init_widgets_screen1():
    widgets_screen1 = init_widgets_list()
    return widgets_screen1

def init_widgets_screen2():
    widgets_screen2 = init_bottom_widgets()
    return widgets_screen2

widgets_screen1 = init_widgets_screen1()
widgets_screen2 = init_widgets_screen2()


# def init_screens():
#     return [Screen(top=bar.Bar(widgets=init_widgets_screen1(), size=20, opacity=1)),
#            Screen(bottom=bar.Bar(widgets=init_widgets_screen2(),size=20,opacity=1))]
screens = [
    Screen(
        top=bar.Bar(widgets=init_widgets_screen1(), size=20, opacity=1)
        )
        ]

# screens = [
#     Screen(
#         bottom=bar.Bar([
#             widget.GroupBox(),
#             window_name,
#             ], 30),
#         ),
#     Screen(
#         bottom=bar.Bar([
#             widget.GroupBox(),
#             window_name,
#             ], 30),
#         )
#     ]

dgroups_key_binder = None
dgroups_app_rules = []

# ASSIGN APPLICATIONS TO A SPECIFIC GROUPNAME
# BEGIN

#########################################################
################ assgin apps to groups ##################
#########################################################
# @hook.subscribe.client_new
# def assign_app_group(client):
#     d = {}
#     #####################################################################################
#     ### Use xprop fo find  the value of WM_CLASS(STRING) -> First field is sufficient ###
#     #####################################################################################
#     d[group_names[0]] = ["Navigator", "Firefox", "Vivaldi-stable", "Vivaldi-snapshot", "Chromium", "Google-chrome", "Brave", "Brave-browser",
#               "navigator", "firefox", "vivaldi-stable", "vivaldi-snapshot", "chromium", "google-chrome", "brave", "brave-browser", ]
#     d[group_names[1]] = [ "Atom", "Subl", "Geany", "Brackets", "Code-oss", "Code", "TelegramDesktop", "Discord",
#                "atom", "subl", "geany", "brackets", "code-oss", "code", "telegramDesktop", "discord", ]
#     d[group_names[2]] = ["Inkscape", "Nomacs", "Ristretto", "Nitrogen", "Feh",
#               "inkscape", "nomacs", "ristretto", "nitrogen", "feh", ]
#     d[group_names[3]] = ["Gimp", "gimp" ]
#     d[group_names[4]] = ["Meld", "meld", "org.gnome.meld" "org.gnome.Meld" ]
#     d[group_names[5]] = ["Vlc","vlc", "Mpv", "mpv" ]
#     d[group_names[6]] = ["VirtualBox Manager", "VirtualBox Machine", "Vmplayer",
#               "virtualbox manager", "virtualbox machine", "vmplayer", ]
#     d[group_names[7]] = ["Thunar", "Nemo", "Caja", "Nautilus", "org.gnome.Nautilus", "Pcmanfm", "Pcmanfm-qt",
#               "thunar", "nemo", "caja", "nautilus", "org.gnome.nautilus", "pcmanfm", "pcmanfm-qt", ]
#     d[group_names[8]] = ["Evolution", "Geary", "Mail", "Thunderbird",
#               "evolution", "geary", "mail", "thunderbird" ]
#     d[group_names[9]] = ["Spotify", "Pragha", "Clementine", "Deadbeef", "Audacious",
#               "spotify", "pragha", "clementine", "deadbeef", "audacious" ]
#     ######################################################################################
#
# wm_class = client.window.get_wm_class()[0]
#
#     for i in range(len(d)):
#         if wm_class in list(d.values())[i]:
#             group = list(d.keys())[i]
#             client.togroup(group)
#             client.group.cmd_toscreen(toggle=False)

# END
# ASSIGN APPLICATIONS TO A SPECIFIC GROUPNAME



main = None

@hook.subscribe.startup_once
def start_once():
    home = os.path.expanduser('~')
    subprocess.call([home + '/.config/qtile/scripts/autostart.sh'])
    # subprocess.call([home + '/.config/qtile/scripts/NotfiyOnKeyboardChange.sh'])


@hook.subscribe.startup
def start_always():
    # Set the cursor to something sane in X
    subprocess.Popen(['xsetroot', '-cursor_name', 'left_ptr'])

@hook.subscribe.client_new
def set_floating(window):
    if (window.window.get_wm_transient_for()
            or window.window.get_wm_type() in floating_types):
        window.floating = True



floating_types = ["notification", "toolbar", "splash", "dialog"]


follow_mouse_focus = True
bring_front_click = False
cursor_warp = False
floating_layout = layout.Floating(float_rules=[
    # Run the utility of `xprop` to see the wm class and name of an X client.
    *layout.Floating.default_float_rules,
    Match(wm_class='confirmreset'),  # gitk
    Match(wm_class='makebranch'),  # gitk
    Match(wm_class='maketag'),  # gitk
    Match(wm_class='ssh-askpass'),  # ssh-askpass
    Match(title='branchdialog'),  # gitk
    Match(title='pinentry'),  # GPG key password entry
    Match(wm_class='Arcolinux-welcome-app.py'),
    Match(wm_class='Arcolinux-calamares-tool.py'),
    Match(wm_class='confirm'),
    Match(wm_class='dialog'),
    Match(wm_class='download'),
    Match(wm_class='error'),
    Match(wm_class='file_progress'),
    Match(wm_class='notification'),
    Match(wm_class='splash'),
    Match(wm_class='toolbar'),
    Match(wm_class='Arandr'),
    Match(wm_class='feh'),
    Match(wm_class='Galculator'),
    Match(wm_class='archlinux-logout'),
    Match(wm_class='xfce4-terminal'),

],  fullscreen_border_width = 0, border_width = 0)
auto_fullscreen = True

focus_on_window_activation = "focus" # or smart

wmname = "LG3D"
