image demo01:
    ypos 70
    Text("This is the end of the demo.", style="monika_credits_text", size=50)
image demo02:
    ypos 140
    Text("I hope you enjoyed the story and will look forward to the next chapters.", style="monika_credits_text", size=50)
image demo03:
    ypos 200
    Text("Believe me there is a long way to go still.", style="monika_credits_text", size=50)
image demo04:
    ypos 270
    Text("Thank you", style="monika_credits_text", size=50)

label demo:
    scene black
    pause 2.0
    show demo01 zorder 50
    with Dissolve(1.5)
    pause 4.0
    show demo02 zorder 50
    with Dissolve(1.5)
    pause 4.0
    show demo03 zorder 50
    with Dissolve(1.5)
    pause 4.0
    show demo04 zorder 50
    with Dissolve(1.5)
    pause 2.0
    scene black
    with Dissolve(1.5)
    pause 2.0
return
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
# Test
