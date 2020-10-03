


label start:

    init python:
        import os

    $ anticheat = persistent.anticheat

    $ _dismiss_pause = config.developer

    $ d_name = '???'
    $ c_name = '???'
    $ s_name = '???'
    $ m_name = 'Girl 3'
    $ n_name = 'Girl 2'
    $ y_name = 'Girl 1'

    $ quick_menu = True
    $ style.say_dialogue = style.normal
    $ allow_skipping = True
    $ config.allow_skipping = True


    if persistent.playthrough == 0:
        call ch0_main
        if exit == 0:
            return
        else:
            pass

        call demo













        call credit
    return

label endgame(pause_length=4.0):
    $ quick_menu = False
    stop music fadeout 2.0
    scene black
    show end
    with dissolve_scene_full
    pause pause_length
    $ quick_menu = True
    return
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
