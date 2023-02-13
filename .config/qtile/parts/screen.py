

from libqtile.config import Screen
from libqtile import widget, bar,layout
# dfrom qtile_extras.widget.decorations import BorderDecoration, PowerLineDecoration, RectDecoration
import os
import socket
from qtile_extras.widget.decorations import BorderDecoration, PowerLineDecoration, RectDecoration




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




def init_widgets_defaults():
    return dict(font="Noto Sans",
                fontsize = 12,
                padding = 2,
                background=colors[5])

widget_defaults = init_widgets_defaults()

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

               widget.WindowName(font="Noto Sans Bold",

                        fontsize = 12,
                        format='{state}{name}',
                        foreground = colors[15],
                        background = colors[12],
                        padding=9,
                        decorations=[
                           PowerLineDecoration(
                               path="rounded_right",
                               colour = colors[9],
                               border_width = [0, 0, 2, 0],
                               padding_x = 5,
                               padding_y = None,
                           )
                       ],
                        # max_chars= 90,


                                                 ),


                widget.Sep(
                       linewidth = 0,
                       padding = 0,
                       background = colors[11],

                       


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
               widget.CurrentLayout(
                        font = "Noto Sans",
                        foreground = colors[11],
                        background = colors[7],

               

                        ),

                widget.CurrentLayoutIcon(
                       custom_icon_paths = [os.path.expanduser("~/.config/qtile/icons")],
                       foreground = colors[12],
                       background = colors[7],
                       
                       padding = 0,
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
                        text="  ",
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
                        format="%Y-%m-%d %H:%M",
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
                    text=" 󱑏 "


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
                         foreground = colors[0],
                         background = colors[4],
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
                        padding = 10,



                        ),
              ]
    return widgets_list

widgets_list = init_widgets_list()



# def init_bottom_widgets():
#     prompt = "{0}@{1}: ".format(os.environ["USER"], socket.gethostname())
#     widget_list2 = []

#     return widget_list2
# widget_list2 = init_bottom_widgets()






def init_widgets_screen1():
    widgets_screen1 = init_widgets_list()
    return widgets_screen1

def init_widgets_screen2():
    widgets_screen2 = init_widgets_list()
    return widgets_screen2

widgets_screen1 = init_widgets_screen1()
widgets_screen2 = init_widgets_screen2()


def init_screens():
    return [Screen(top=bar.Bar(widgets=init_widgets_screen1(), size=20, opacity=1)),
            Screen(top=bar.Bar(widgets=init_widgets_screen2(), size=20, opacity=1))]
screens = init_screens()


