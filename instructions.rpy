
image instructions01:
    ypos 70
    Text("Welcome to Project ???", style="monika_credits_text", size=50)
image instructions02:
    ypos 110
    Text("For the best experience I would recommend to keep your saves in the same chapter", style="monika_credits_text", size=50)
image instructions03:
    ypos 170
    Text("Decisions in this life really matter, and they are likely to come back around again. Sooner or Later.", style="monika_credits_text", size=50)
image instructions04:
    ypos 300
    Text("As a side note: Text italics are spoken towards you, the player.", style="monika_credits_text", size=50)
image instructions05:
    ypos 350
    Text("Once again I can't thank you enough for this.... Really...", style="monika_credits_text", size=50)

label instructions:
    scene black
    with Dissolve(1.0)
    pause 2.0    
    show instructions01 zorder 50
    with Dissolve(1.5)
    pause 4.0
    show instructions02 zorder 50
    with Dissolve(1.5)
    pause 5.0
    show instructions03 zorder 50
    with Dissolve(1.5)
    pause 6.0
    show instructions04 zorder 50
    with Dissolve(1.5)
    pause 5.0   
    show instructions05 zorder 50
    with Dissolve(1.5)
    pause 6.0
    scene black
    with Dissolve(1.0)
    pause 2.0    
return
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
