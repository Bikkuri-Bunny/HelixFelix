
## Preferences screen ##########################################################
##
## The preferences screen allows the player to configure the game to better suit
## themselves.
##
## https://www.renpy.org/doc/html/screen_special.html#preferences

screen preferences():

    tag menu

    use game_menu(_("Preferences"), scroll="viewport"):

        vbox:
            hbox:
                box_wrap True

                if renpy.variant("pc") or renpy.variant("web"):

                    vbox:
                        style_prefix "radio"
                        label _("Display")
                        textbutton _("Window") action Preference("display", "window")
                        textbutton _("Fullscreen") action Preference("display", "fullscreen")

                vbox:
                    style_prefix "radio"
                    label _("Rollback Side")
                    textbutton _("Disable") action Preference("rollback side", "disable")
                    textbutton _("Left") action Preference("rollback side", "left")
                    textbutton _("Right") action Preference("rollback side", "right")

                vbox:
                    style_prefix "check"
                    label _("Skip")
                    textbutton _("Unseen Text") action Preference("skip", "toggle")
                    textbutton _("After Choices") action Preference("after choices", "toggle")
                    textbutton _("Transitions") action InvertSelected(Preference("transitions", "toggle"))

                ## Additional vboxes of type "radio_pref" or "check_pref" can be
                ## added here, to add additional creator-defined preferences.

            null height (4 * gui.pref_spacing)

            vbox:
                style_prefix "slider"
                box_wrap True
                xalign 0.5

                vbox:

                    label _("Text Speed")

                    hbox:
                       add im.Scale("gui/slider/horizontal_idle_bar2a.png",50,73)#73
                       bar value Preference("text speed"):
                          right_bar Frame("gui/slider/horizontal_idle_bar2.png")
                          left_bar Frame("gui/slider/horizontal_hover_bar2.png")
                          ypos 18#6
                       add im.Scale("gui/slider/horizontal_idle_bar2b.png",109,88) ypos -10

                    label _("Auto-Forward Time")

                    hbox:
                       add im.Scale("gui/slider/horizontal_idle_bar2a.png",50,73)
                       bar value Preference("auto-forward time"):
                          right_bar Frame("gui/slider/horizontal_idle_bar2.png", 0, 0)
                          left_bar Frame("gui/slider/horizontal_hover_bar2.png", 0, 0)
                          ypos 18
                       add im.Scale("gui/slider/horizontal_idle_bar2b.png",109,88) ypos -10

                vbox:

                    null height 80
                    if config.has_music:
                        label _("Music Volume")

                        hbox:
                            add im.Scale("gui/slider/horizontal_idle_bar2a.png",50,73)
                            bar value Preference("music volume"):
                              right_bar Frame("gui/slider/horizontal_idle_bar2.png", 0, 0)
                              left_bar Frame("gui/slider/horizontal_hover_bar2.png", 0, 0)
                              ypos 18
                            add im.Scale("gui/slider/horizontal_idle_bar2b.png",109,88) ypos -10

                    if config.has_sound:

                        label _("Sound Volume")

                        hbox:
                            add im.Scale("gui/slider/horizontal_idle_bar2a.png",50,73)
                            bar value Preference("sound volume"):
                              right_bar Frame("gui/slider/horizontal_idle_bar2.png", 0, 0)
                              left_bar Frame("gui/slider/horizontal_hover_bar2.png", 0, 0)
                              ypos 18
                            add im.Scale("gui/slider/horizontal_idle_bar2b.png",109,88) ypos -10

                            if config.sample_sound:
                                textbutton _("Test") action Play("sound", config.sample_sound)


                    if config.has_voice:
                        label _("Voice Volume")

                        hbox:
                            add im.Scale("gui/slider/horizontal_idle_bar2a.png",50,73)
                            bar value Preference("voice volume"):
                              right_bar Frame("gui/slider/horizontal_idle_bar2.png", 0, 0)
                              left_bar Frame("gui/slider/horizontal_hover_bar2.png", 0, 0)
                              ypos 18
                            add im.Scale("gui/slider/horizontal_idle_bar2b.png",109,88) ypos -10

                            if config.sample_voice:
                                textbutton _("Test") action Play("voice", config.sample_voice)

                    if config.has_music or config.has_sound or config.has_voice:
                        null height gui.pref_spacing

                        textbutton _("Mute All"):
                            action Preference("all mute", "toggle")
                            style "mute_all_button"
                            xalign 0.5


style pref_label is gui_label
style pref_label_text is gui_label_text
style pref_vbox is vbox

style radio_label is pref_label
style radio_label_text is pref_label_text
style radio_button is gui_button
style radio_button_text is gui_button_text
style radio_vbox is pref_vbox

style check_label is pref_label
style check_label_text is pref_label_text
style check_button is gui_button
style check_button_text is gui_button_text
style check_vbox is pref_vbox

style slider_label is pref_label
style slider_label_text is pref_label_text
style slider_slider is gui_slider
style slider_button is gui_button
style slider_button_text is gui_button_text
style slider_pref_vbox is pref_vbox

style mute_all_button is check_button
style mute_all_button_text is check_button_text

style pref_label:
    top_margin gui.pref_spacing
    bottom_margin 3

style pref_label_text:
    yalign 1.0

style pref_vbox:
    xsize 338

style radio_vbox:
    spacing gui.pref_button_spacing

style radio_button:
    properties gui.button_properties("radio_button")
    foreground "gui/button/radio_[prefix_]foreground.png"

style radio_button_text:
    properties gui.button_text_properties("radio_button")

style check_vbox:
    spacing gui.pref_button_spacing

style check_button:
    properties gui.button_properties("check_button")
    foreground "gui/button/check_[prefix_]foreground.png"

style check_button_text:
    properties gui.button_text_properties("check_button")

style slider_slider:
    xsize 525

style slider_button:
    properties gui.button_properties("slider_button")
    yalign 0.5
    left_margin 15

style slider_button_text:
    properties gui.button_text_properties("slider_button")

style slider_vbox:
    xsize 675
