label ch0_main:
    $ delete_character("Monika")
    $ delete_character("Yuri")
    $ delete_character("Sayori")
    $ delete_character("Natsuki")
    $ exit = 0
    $ mom = 0
    stop music fadeout 2.0
    call instructions
    show chapter00 zorder 50
    with Dissolve(1.5)
    pause 1.0
    scene black
    with dissolve_scene_full
    play music hb
    mc "Where am I?"
    d "I am sorry it had to be this way."
    mc "Who are you?"
    d "I am no one [player]. ...Always have been."
    mc "What does that mean?"
    d "You are here because of what you did in the end."
    d "{i}Before you start however, I have to make sure you are one that can be trusted{/i}"
    d "{i}Don't act surprised... Did you think I wouldn't know you are watching this through a screen?{/i}"
    d "{i}I need to know if you back up that computer you are using or use online storage of any kind?{/i}"
    menu:
        "Yes":
            d "{i}Good...{/i}"
            d "I am going to give you the choices that they never gave me..."
            mc "Wait! What choices? What are you talking about?"
            d "She is here..."
            d "...always"
            $ m = "Girls Voice"
            m "Where are you? I cannot see you now. What is happening?"
            m "{cps=10}..........{/cps}It has started...hasn't it?"
            m "Don't forget"
            m "{cps=10}.......I love you{/cps}"
            d "Here is your chance [player]."
            d "I will help you the best I can..."
            d "...for as long as I can"
            d "but in the end, this is on you."
            d "{i}For you... I am going to recommend you be honest with yourself... and...{/i}"
            d "{i}save often{/i}"
            d "I need a space to start again..."
            call updateconsole ("os.rebuild_endspace(\"game\")", "mod_load space build successfully.")
            $ pause(2.0)
            scene monika_room
            $ consolehistory = []
            d "It is time to get us out of here, and time for you to get back."
            call updateconsole ("os.ddlc_memory_dump(\"game\")", "ddlc structure trojan v.107.5.6")
            $ pause(2.0)
            show screen tear(20, 0.1, 0.1, 0, 40)            
            $ pause(2.0)
            hide screen tear            
            $ consolehistory = []
            scene monika_room_escape
            call updateconsole ("os.rebuildddlc(\"game\")", "mod_assets built successfully.")
            $ pause(2.0)
            call updateconsole ("os.rebuildmc(\"game\")", "mc memory setup complete.")
            $ pause(2.0)
            show screen tear(20, 0.1, 0.1, 0, 40)            
            $ pause(2.0)
            hide screen tear
        "No":
            d "{i}Disappointing... This is too important for me to chance on you.{/i}"
            d "{i}You can't be trusted with such valuable data.{/i}"
            return (exit)

    stop music
    scene black
    d "{i}...You are one of my only hopes now{/i}"
    d "{i}Guide [player] well..{/i}"
    scene black
    with Dissolve(1.0)
    pause 1.0
    scene black
    show dayText_saturday zorder 50
    with Dissolve(1.5)
    pause 1.0
    scene black
    with Dissolve(1.5)
    pause 1.0   
    scene bg bedroom_night
    mc "...What a weird dream"
    "I still can't believe everything that has happened. My friends are gone."
    "Sayori is dead... The police spent hours talking to everyone."
    "They even made sure to inform me not to go anywhere."
    "Yuri was found dead at the school, they ruled it a suicide."
    "Natsuki has been missing for two weeks."
    "Some people assumed that Yuri's death had something to do with her because she disappeared so quickly."
    "However, one of the strangest parts is not one person has even seen or asked about Monika. Its almost like she was never even here."
    "People are acting like no one even knew about her, like she was erased from ever being here."
    "I have to admit... Everything is a little fuzzy for me."
    "I was told after I walked into Sayori's room and saw her, that the shock caused me to pass out and fall to the ground."
    "The police showed up because of an anonymous phone call they received that day and found me there."
    "They never said anything about who called, only that they were looking into who placed it and from where."
    "But I know I left Sayori's house.... right??? I thought I spoke to someone right out front..."
    "It is strange... I have fuzzy memories of Yuri...She was sitting on the floor.... I think she was sitting on the floor..."
    window hide
    show yuri_flashback
    $ pause(1.0)
    hide yuri_flashback
    "But I was never there? How is that possible?"
    "I passed out at Sayori's house????"
    "My mind has been fuzzy for the last few weeks."
    "Really at this point it is driving me nuts."

    scene bg bedroom_day
    with dissolve_scene_full
    play music t2
    mc "Another night with very little sleep."
    mc "I don't know how much longer I can keep this up."
    "Bad nightmares... strange feeling like I am being watched... This whole thing feels weird..."

    scene bg kitchen
    with wipeleft_scene
    mc "I swear it feels like I need to remind myself to eat every day."
    "The last few days, I make a simple meal, and stare at the walls."
    "I called my parents to let them know about Sayori."
    "Unfortunately, my father could only stay for about a week and had to return to his job overseas."
    "My mother on the other hand has been freaking out, the entire time."
    "But just recently she had to go back to work as well."
    "It is nice that she is working close to home for now,"
    "but I swear she calls way too often to check up on me."
    "The police asked me to stay in the area and I am supposed to be meeting with an assigned psychologist or something."
    "Something about dealing with the trauma of what I saw."
    "I haven't even been back to school since this happened."
    "I am not sure I am ready to see anyone else to be honest."

    scene bg entrance_day
    with wipeleft_scene
    "Well, I guess I better figure out where I am going today."
    menu:
        "--Not sure how I am feeling today--"
        "Back to my room":
            scene bg bedroom_day
            with wipeleft_scene
            "Honestly just another day where I don't feel like going outside..."
            "I am not sure what I am supposed to do."
            "Everything sucks!"
            "Everyone I knew from the club is gone!"
            "I miss Sayori, and you know... I am not sure I ever really told her how much I cared."
            "I know we talked... and I know she was having problems"
            "Sometimes I wonder what would have happened if I paid more attention to her sooner..."
            "Why did we slow down being friends?"
            "She lived right next door and I couldn't even walk over?"
            "Maybe it was my fault?"
            $ s_name = 'Sayori'
            $ y_name = 'Yuri'
            scene bg club_day
            with dissolve_scene_full
            show yuri 1a zorder 2 at t22
            show sayori 2x zorder 2 at f21
            s "Don't worry, guys~"
            s "[player] always gives it his best as long as he's having fun."
            s "He helps me with busywork without me even asking."
            s "Like cooking, cleaning my room..."
            scene bg bedroom_day
            with dissolve_scene_full
            "As long as he's having fun?"
            "Is that really all she thought of me?"
            "I wouldn't come by to see or help if I wasn't having fun?"
            scene bg club_day
            with dissolve_scene_full
            show sayori 2x zorder 2 at t21
            show yuri 1a zorder 2 at f22
            y 1s "You two are really good friends, aren't you?"
            y "I might be a little jealous..."
            show yuri zorder 2 at t22
            show sayori zorder 2 at f21
            s 1 "How come? You and [player] can become good friends too!"
            show sayori zorder 2 at t21
            show yuri zorder 2 at f22
            y 4b "U-Um..."
            scene bg bedroom_day
            with dissolve_scene_full
            "I remember Yuri's face and how uncomfortable she looked."
            "Sayori really did have a way of blurting out anything"
            "But really... Was that so bad? Yeah sometimes it was out of line"
            "But I think that is one of the things I loved about her."
            "You know you never think about these things until you can't see them anymore"
            "I wonder if that how it just is with life."
            "You know the whole \"You do not miss it till it is gone\" thing."
            "For that matter what happen to Yuri?"
            "Every time I try to think about her, my head starts hurting."
            play sound phone
            "Oh, it’s my mom... Again"
            $ c_name = 'Mom'
            c "Hi Honey, how are you doing today?"
            mc "I am doing just fine, what is going on?"
            c "Nothing I just wanted to make sure that you are doing alright and to let you know I won't be coming home for lunch today."
            c "I really fell behind in a few things and need to stay here until this evening."
            mc "No problem I will be fine."
            c "[player] are you sitting in your room again?"
            mc "....Nooooo"
            c "You might be getting older, but I still know when you are lying to me."
            "How does she do that!"
            c "You need to get outside for a change and take a walk and get some fresh air. "
            mc "But mom"
            c "No buts [player]. I know it is hard to see Sayori's house, but you can't stay locked indoors every day."
            c "It is not healthy, and you know at some point you are going to have to leave."
            mc "Yeah I know. Your right I think I will take a walk today."
            c "Ok, bring your phone, and if you need anything call me."
            mc "Alright mom, I will. Thanks"
            c "Love you"
            mc "Love you too."
            "I really have no clue how mom's do that."
            "Time to get up and give this a chance."
        "Outside":
            scene bg residential_day
            with wipeleft_scene
            mc "The sun is bright today."
            "I have been inside a bit too much in the last two weeks."
            "My mom even said I needed to try to go outside and sitting inside wasn't good for me."
            "I know she is trying her best but,"
            "I don't think she understands."
            scene bg house
            with wipeleft_scene
            "Her house is right next to ours..."
            "Same street... Same neighborhood..."
            window hide(None)
            window auto
            play music td
            show s_kill_bg2
            show s_kill2
            show s_kill_bg as s_kill_bg at s_kill_bg_start
            show s_kill as s_kill at s_kill_start
            $ pause(3.75)
            show s_kill_bg2 as s_kill_bg
            show s_kill2 as s_kill
            $ pause(0.01)
            show screen tear(20, 0.1, 0.1, 0, 40)
            play sound "sfx/s_kill_glitch1.ogg"
            $ pause(0.25)
            stop sound
            hide screen tear
            hide s_kill_bg
            hide s_kill
            stop music
            scene bg house
            play music t2
            "NO!! Not again!!"
            scene bg residential_day
            with wipeleft_scene
            "Don't run! It is all just in my head."
            "{cps=10}It is ok.... breathe.... just calm down.{/cps}"
            "I can't get that scene out of my head."
            "Why Sayori?"
            "I could have helped her."
            "I had the chance to help her."
            "Didn't I?"
            play sound phone
            "Holy crap!"
            "Oh wait, it's just my mom."
            $ c_name = 'Mom'
            c "Hi honey, how are you doing today?"
            mc "Hi mom, I am doing just fine."
            c "Honey are you alright? You sound like you are out of breath."
            mc "....yeah mom, I am fine."
            c "You know, I know when you are lying to me [player]."
            "How does she do this?!"
            mc "No, I am alright mom, I am just trying to take a walk right now and having a little issue."
            c "Is it Sayori's house?"
            mc "{cps=30}...yeah mom.{/cps}"
            c "It is ok [player], I am so proud of you for trying to take the first step."
            c "I know it is hard to see her house, but you really need to try and move past it."
            c "You can't stay indoors all the time; it isn't healthy for you."
            mc "I know mom. I am trying."
            c "Listen [player], I won't be able to come home for lunch today, but if you need anything please call me."
            mc "Alright mom, I will I promise."
            c "Take your phone with you alright."
            mc "I will."
            c "We can talk tonight if you need to."
            mc "I will be alright mom, but thank you."
            c "I love you [player]."
            mc "I love you too mom"
            "She does call to much... but I have to admit it does help."

    play music t8
    scene bg crossroad
    with wipeleft_scene
    "You know I have to admit... This walk is kind of nice."
    "I keep thinking about the club, and my friends..."
    "When I first met them, I remember Yuri and Natsuki fighting over my opinion about their poems."
    "You know, now that I think about it that seemed like a pretty heated debate on my first day."
    "I wonder what was going on with those two."
    "They were really just two completely different ways of writing poems."
    "However, that's what is fun about writing I guess."
    "Two people can say the exact same thing but do it in two completely different ways."
    "Now that I understand and have seen that first-hand, it really is something neat."
    "Wait what was it that Sayori said about them after that?"
    "She said something about them arguing."


    scene bg residential_day
    $ s_name = 'Sayori'
    show sayori 1a zorder 2 at t11
    with dissolve_scene_full
    mc "Sayori..."
    mc "About what happened earlier..."
    s 1b "Eh? What do you mean?"
    mc "You know, between Yuri and Natsuki."
    mc "Does that kind of thing happen often?"
    s 4j "No, no, no!"
    s "That's really the first time I've seen them fight like that..."
    s "I promise they're both wonderful people."


    scene bg crossroad
    with dissolve_scene_full
    "Sayori was defending them right from the start."
    "Almost like she was surprised they were arguing at all."
    "That is kind of weird now that I think about it."
    "It is so strange. I didn't know them for long, but they really made an impact on me somehow."
    "hm... I wonder..."
    "It feels like I am missing something."
    "Or maybe forgotten something..."

    scene bg city_evening
    with wipeleft_scene
    "It has been a while since I came out here."
    "Shops are all closing up..."
    "No one is even left walking around."
    "Oh well, just means a quiet evening for me I guess."
    "What I wouldn't give for quick bite to eat however."
    "For some reason I am really craving something sweet today."
    "I wonder if I can find a bakery real quick... a cupcake really sounds good right now."


    scene bg club_day
    with dissolve_scene_full
    $ n_name = 'Natsuki'
    show sayori zorder 3 at f31
    s 4x "Come sit down, [player]! We made room for you at the table, so you can sit next to me or Monika."
    s "I'll get the cupcakes~"
    show sayori zorder 2 at t31
    show natsuki 1e zorder 3 at f32
    n "Hey! I made them; I'll get them!"
    show natsuki zorder 2 at t32
    show sayori zorder 3 at f31
    s 5a "Sorry, I got a little too excited~"


    scene bg city_evening
    with dissolve_scene_full
    "Natsuki...."
    "Too cute, and she hated it."
    "I really wonder what happen to her."
    "I hope she is ok."
    "Where did she go?"
    "hmmm... you know the strange thing is. I wouldn't have even met them if it wasn't for Sayori."


    scene bg class_day
    with dissolve_scene_full
    mc "Clubs..."
    "Sayori wants me to check out some clubs."
    "I guess I have no choice but to start with the anime club..."
    "You know I am pretty sure \"How Not to Summon A Demon Lord\" is getting a second season soon."
    s "Hellooo?"
    show sayori 1b zorder 2 at t11
    mc "Sayori...?"
    "Sayori must have come into the classroom while I was spacing out."
    "I look around and realize that I'm the only one left in the classroom."
    s 1a "I thought I'd catch you coming out of the classroom, but I saw you just sitting here and spacing out, so I came in."
    s "Honestly, you're even worse than me sometimes... I'm impressed!"
    mc "You don't need to wait up for me if it's going to make you late to your own club."
    s 1y "Well, I thought you might need some encouragement, so I thought, you know..."
    mc "Know what?"
    s 1a "Well, that you could come to my club!"
    mc "Sayori..."
    s 4r "Yeah??"
    mc "...There is no way I'm going to your club."
    show sayori at s11
    s 5d "Eeeehhhhh?! Meanie!"


    scene bg city_evening
    with dissolve_scene_full
    "Memories really are a strange thing."
    "I can remember the members in the club like it was yesterday."
    "hmmm... I seem to be having a hard time remembering Monika's face."
    "What does that say about me?"
    "I know I talked to her a lot, I thought I had a class with her before all this too..."
    "It just seems like the more and more time that goes by the harder and harder it is to remember her."
    "Alright let me take a break and find a open store around here somewhere."

    scene bg sidestore_evening
    with wipeleft_scene
    "Man, I have been walking around for a while now."
    "I guess my mom wasn't kidding. I really did need this."
    stop music fadeout 3.0
    "Glad I saw this store. I really needed a bite to eat and something to drink."
    "The owner just told me there is a really nice park up ahead. Kind of odd that I don't remember there being a park this way."
    "Then again with the way my head has been the last few weeks. Nothing really shocks me."

    play music breeze
    scene bg park_night
    with wipeleft_scene
    "Well I guess this is it. This is a really nice park; how did I not know about this place before?"
    "Hmmm......"
    "There is something odd about the air here."
    "Almost like the breeze isn't natural."
    "The air feels......"
    "{cps=20}........Stale{/cps}"
    play sound phone    
    "Who could that be?"
    "Oh crap! It's my mom... Great what time is it?"
    mc "Hiiiiii Mom, how are you doing?"
    c "Really? You’re going to play the \"Hiiiiii Mom\" card with me?"
    c "Do you have any idea what time it is?"
    mc "Well to be honest"
    mc "{cps=20}.........no{/cps}"
    mc "I don't"
    mc "But I was just taking your advice about going outside today, and I kind of lost track of time"
    c "Kind of?"
    mc "Hey did you know there is park out by the waterfront?"
    c "Don't change the subject."
    mc "........................"
    c "I am glad you went out today, and I am really happy you feel well enough to explore, but you had me worried."
    c "When are you coming home?"
    mc "I will start heading back now mom. I am sorry I worried you."
    c "It is alright. You are no doubt old enough to take care of yourself, but a mother still worries."
    c "Do you want me to come and pick you up?"
    mc "No you don't need to do that. I will leave and start heading back now."
    c "Ok, I am going to go ahead and take a bath then go to bed."
    c "If you need me call or knock on my door when you get home."
    mc "I will mom, and sorry again."
    c "It is ok, you just had me worried. [player], I am glad you know where you are because I can't even remember a park by the waterfront right now."
    mc "No problem, I will be home soon."
    mc "I love you."
    c "I love you too."
    "Holy crap I had no idea I was out this long."
    "That could have been so much worse. hahaha"
    play sound phone
    "Oh oh..."
    "She must have forgotten something."
    play music hb    
    menu:
        d "Did you enjoy your walk today [player]?"
        "Who is this?":
            label who:
            d "You don't remember? That hurts my feelings."
            d "......really"
            d "Allow me to jog your memory a little bit"
            scene monika_room
            $ pause (1.0)
            scene bg park_night
            d "Is it coming back now?"
            mc "Wait.. What was that? How did you do that?"
            mc "{cps=20}........That was a dream{/cps}"
            d "Some dreams are real to the dreamer [player]."
            mc "{cps=30}...........................................{/cps}"
            d "...Understandable at this point."
            d "As I told you before. I am no one."
            d "However, I am here to give you the choices that I never had."
        "Yes":

            d "I am glad."
            d "Sometimes we all need a trip down memory lane."
            d "It gives us perspective if we look at our history and do not forget where we came from."
            d "For good or bad... Our history is just that. Learn from it and move forward."
            d "Just as you are doing today."
            mc "Why are you calling me?"
            mc "Who are you?"
            jump who
        "No":

            d "Such a shame..."
            d "Always in a hurry to get to the next point I guess..."
            d "You really should appreciate the small things in life a bit more."
            d "I always find the concept of the lonely shopkeeper on the side of street intriguing."
            d "They are trying to work to support themselves, their families perhaps, or build support for their hobbies and ideas."
            mc "Why are you wasting my time with this?"
            mc "Just tell me who you are?"
            jump who

    d "Do you want to know what happened to your friends?"
    mc "What??"
    d "Do you want me to tell you why no one remembers{cps=20}...........Monika{/cps}?"
    d "Yes... that is right... I know all about her."
    d "Do you want to know the truth about what happened?"
    mc "How do you know all of this? How do you know Monika?"
    mc "Everyone acts like Monika never even existed."
    mc "When I asked the police about her, they had no clue who I was talking about."
    mc "Even my own mother has no idea."
    d "They won't remember her."
    d "No one will..."
    d "It is kind of sad really when you think about it."
    d "However, that is not all I know."
    d "They will never find Natsuki."
    d "Or better... They will never know what happened to Natsuki."
    window hide
    scene bg inside_closet
    show natsuki_sitting
    $ pause (1.0)
    hide natsuki_sitting
    scene bg park_night
    d "You will never understand what happened to Yuri."
    window hide
    show y_flashback
    $ pause (1.0)
    hide y_flashback
    d "And Sayori's death will always haunt you."
    window hide
    show s_flashback
    $ pause (1.0)
    hide s_flashback
    d "But as I said before... I can help you."
    d "{cps=20}....For now, that is.{/cps}"
    mc "How do I know that you are not the one who did this to them?"
    d "I won't deny that fact... I did have a part to play"
    d " {i}Just as you did!{/i} "
    d "However, I can do something about it. For now, at least."
    d "The question is,"
    d "do you want to do something about it?"
    d "Or are you just going to lie down and accept the fact you are powerless and can't help your friends,"
    d "just like before?"
    menu:
        "What am I supposed to do... this is creeping me out?"
        "Hear him out":

            d "I know this hard for you to understand."
            d "So how about a test of faith first?"
            d "I will do something for you to prove my intensions."
            d "You will honor my request and see the truth for yourself."
            mc "Ok"
            d "First things first."
            d "Your mother sounded quiet upset with you."
            d "Go home for the night and think about my offer."
            d "Come back here tomorrow night, if you want to know the truth."
            mc "And if I don't come back?"
            d "Nothing. Game Over [player]."
            d "Just think about it. Wouldn't you like to have the chances that were not possible before?"
            d "To help your friends? Perhaps even to help yourself?"
            mc "What do I have to give you for this? Or better yet what are you getting out of this?"
            d "{cps=10}................{/cps}The hope that was taken from me."
            d "It is up to you."
            stop music                        
        "Hang up":
            scene black
            d "{i}I can't force you to continue.{/i}"
            d "{i}.........So be it.{/i}"
            return (exit)
    "The phone call goes dead."
    play music breeze
    mc "What was that?"
    "What am I supposed to do?"
    "This is crazy."
    mc "Ok, first thing... I am getting out of here and going home."

    scene bg sidestore_night
    with wipeleft_scene
    mc "Crap already closed."
    "Fine I will just go the exact same route back out of this area."
    "I have no clue what is going on."
    "What does he mean the truth?"
    "What is all this talk about helping my friends?"
    "Sayori is dead! Yuri is dead! Natsuki is missing! and I am starting to feel like I made Monika up!"

    scene bg crossroad_night
    with wipeleft_scene
    mc "Ok I found the cross roads... "
    "Thank you GPS."
    mc "Almost home"
    "Should I tell my mom about the phone call?"
    "Should I call the police?"


    scene bg club_day
    with dissolve_scene_full
    $ y_name = 'Yuri'
    show yuri 1a zorder 2 at t11
    y "Welcome to the Literature Club. It's a pleasure meeting you."
    y "Sayori always says nice things about you."


    scene bg residential_night
    with dissolve_scene_full
    "She always said nice things about me..."
    "If I can help... shouldn't I?"
    "Natsuki... Maybe I can get in contact with her."
    "Maybe this guy knows where she is..."
    "I don't know what I should do?"
    "Natsuki..."


    scene bg club_day
    with dissolve_scene_full
    show natsuki 1 zorder 2 at t11
    mc "Natsuki, you write your own poems?"
    n 1c "Eh? Well, I guess sometimes."
    n "Why do you care?"
    mc "I think that's impressive."
    mc "Why don't you share them sometime?"
    n 5q "N-No!"
    "Natsuki averts her eyes."
    n "You wouldn't...like them..."
    mc "Ah...not a very confident writer yet?"


    scene bg residential_night
    with dissolve_scene_full
    "What if he really does know about Natsuki?"

    stop music
    scene bg entrance_evening
    with wipeleft_scene
    "She left the lights on..."
    "Thanks mom."
    "Should I tell her in the morning about the phone call?"

    scene black
    with wipeleft_scene
    "I took a quick shower, the whole time thinking about the phone call."
    "I did my best not to wake my mom, but I am pretty sure she knew I was home."

    scene bg bedroom_night
    with wipeleft_scene
    mc "What do I do?"
    mc "What if he is telling the truth and can help me?"
    "What if he really knows where Natsuki is?"
    "Maybe I should at least try to get that out of him."
    show natsuki 1 zorder 2 at t11
    "She is worth it."
    "I have to at least try to find out what is going on."
    hide natsuki
    scene black
    with Dissolve(1.0)
    pause 1.0    
    "Only one way to find out right?"
    "As long as he doesn't ask for anything crazy."
    "And if it gets too nuts I can always tell him I am out. Right?"
    "Who am I kidding? This whole thing sounds crazy."

    show dayText_sunday zorder 50
    with Dissolve(1.5)
    pause 1.0
    scene black
    with Dissolve(1.5)
    pause 1.0
    play music t2
    scene bg bedroom_day
    "Here we go."
    menu:
        "--Time to decide--"
        "Go to the park tonight?":
            "Really what other choice do I have?"
            "I need to at least talk to him and try to figure this out."
            play sound knock
            c "[player] are you up yet?"
            mc "Yeah mom, just getting up now."
            c "Ok, I need to make a quick trip into town this morning, do you want to come along?"
            mc "No thanks mom, I have a few things I want to take care of today."
            c "Ok, well get dressed and get moving then. Call me if you need anything, and I expect you here for dinner."
            mc "No problem, thanks mom"
        "Don't go":
            play music breeze
            scene black
            with dissolve_scene_full
            "I decide after a while that believing some crack pot on the phone was a bad idea."
            "I already have enough issues, and to be honest, why would anyone believe this?"
            "The more I think about it, the more this guy is more than likely involved."
            "So, I decided to tell my mother and we decided to tell the police."
            "They never did anything... I never heard back from them... and in the end I never received another phone call from that guy."

            scene bg club_day
            with dissolve_scene_full
            "I will remember my time there..."
            "I will always love the friends I made."
            "However, I refuse to go play treasure hunter for some creepy guy on the phone."

            scene bg house
            with dissolve_scene_full
            ".....I will always love Sayori."
            "Everything from her smile, to the way she puffed her cheeks when pouting."

            scene black
            with dissolve_scene_full
            "We moved not too long after that. I am pretty sure it was for the best."
            "I ended up getting help for the nightmares, that never really stopped."
            "Just like he said."
            "In time I was able to go to college, get married, and have a family of my own."
            "My wife became my rock, and I told her everything. She was there for me as much as I was for her."
            "Later on, we decided to name our first daughter Sayori."
            "It seemed right."

            scene bg park_night
            with dissolve_scene_full
            "Before we moved, I tried to find that park again... In the daytime this time."
            "I never could find it..."
            "I stopped by that store to ask the owner again, however, he was never there. "
            "The worker acted like he had no clue who I was talking about."
            "However........."
            "Sometimes I still wonder about all those years ago."
            "Sometimes I still wonder about that phone call."
            "Sometimes I can still taste the stale air."
            "No.... I know I made the right choice and in the end."
            "That is what this is all about."
            show end
            with Dissolve(2.0)
            pause 1.0           
            return (exit)
    "Well let me get going and grab a bite to eat."

    scene bg kitchen
    play sound cooking
    with wipeleft_scene
    "For some reason today, I am starving."
    "I am making a full breakfast. Bacon, eggs, toast, the works."
    "I don't think I have eaten like this a while."
    "Maybe all those mornings of really no food are catching up to me."
    ".....Not that I am complaining. This is great."
    "Not going to lie, thinking about that phone call still gives me the creeps."
    "Oh crap, I told my mom I would be here for dinner."
    "I can't forget to call her later and tell her I won't be back."
    "Maybe I should tell her what I am doing???"
    "No.... She has enough to deal with, and really what am I doing but going to get a phone call."
    stop sound 

    scene bg entrance_day
    play music t2
    with wipeleft_scene
    "I think I will head into town for a while before dark."
    "I really don't think I could just sit here and wait."
    "Plus, I am not sure I would be able to lie directly to my mom's face about what I am doing."
    "....Well not lie..... Just not tell her what is going on."
    "Yeah... there is a difference."
    "{cps=10}...............{/cps}I am pretty sure there is a difference. Right?"

    play music t8
    scene bg crossroad
    with wipeleft_scene
    "Well at least I found this place quickly."
    "Last night I was sure I was lost."

    scene bg city_afternoon
    with wipeleft_scene
    "--A few hours later--"
    "{i}Yeah, you got lost... You read that right.{/i}"
    "Man, where is everyone?"
    "Oh yeah it is Sunday."
    "No one ever comes to the shopping district on Sundays, most of the stores are not even open."
    "That is why my mom had to take the drive into town."
    "Oh well, still a nice walk."
    menu:
        "Maybe I should call her, it is getting pretty late in the afternoon."
        "Call Her":
            $ mom += 1
            play sound phone
            pause 2.0
            c "Hello, [player]. Is everything alright?"
            mc "Yeah mom I am fine, I just wanted to give you a call and let you know I won't be back in time for dinner."
            c "Oh? What's going on?"
            mc "Nothing. Just out enjoying the day on another walk."
            c "Oh, alright. Stop somewhere and get yourself something to eat then."
            c "Something good to eat, not fast food [player]."
            mc "Yeah, yeah... I will. Don't worry."
            c "Alright, if you need anything I will be home, give me a call."
            mc "No problem, I am going to see if I can find that park again, so I don't think I will be home until late anyways."
            c "Oh, alright.... I am glad you are spending time out, just don't overdo it."
            c "And be safe."
            mc "I will mom. Love you"
            c "Love you too"
            "Well that wasn't so bad."
            "Time to get some food. Then head to the park."
            scene bg fastfood
            with wipeleft_scene
            "{cps=10}.......{/cps}Don't judge me."
            "I was hungry, and it was open."
        "Don't Bother":
            $ mom -= 1
            "Nahhhh... She will be fine."
            "She said I was old enough to take care of myself anyways."
            "I am sure it will be fine."

    play music breeze    
    scene bg park_night
    with wipeleft_scene
    "Alright, the sun just went down... Man this place is creepy."
    "Why would he say come back at night. Can he not make a phone call in the daytime?"
    "What screwed up phone plan is that?"
    "Something like you can only call on peak times after 17:00?"
    "What is that? \"Early Nights and Weekends\" or something?"
    "Who would sign up for that crap?"
    "Anyways, it is Sunday so even that idea is out."
    play sound phone
    pause 2.0    
    mc "Hello?"
    play music hb
    d "You decided to come after all"
    d "I am not going to lie; I wasn't sure you were going to."
    mc "Listen, before this goes any further, I just want to be sure that you understand."
    mc "If this gets crazy or dangerous, I am out."
    d "............I can respect that"
    d "I said I would give you the choices I never had, and now you will be the one to pick the path."
    d "However, I have heard your request... Now you will hear mine."
    d "If you start this path, there is no going back."
    d "Just because you are scared or don't understand means nothing to me. You will finish what you start, as long as it isn't dangerous."
    d "Agreed?"
    mc "Agreed, I wouldn't be here otherwise."
    d "Then as I said last night, a test of faith is in order."
    d "You will do this for me, so I can trust you are serious."
    d "And I will prove to you that I can help you... and your friends."
    mc "Ok, how?"
    d "Monika is real. Even now at this very moment, she is alive and well."
    mc "???????"
    d "Tonight I am going to prove that to you."
    mc "But no one acts like they even knew Monika. Even my mother had no clue who I was talking about."
    d "Do this for me, and I will prove you are not going crazy. Perhaps the world around you is missing the information that you already know."
    mc "Ok... I will trust you. Like you said a test of faith, right?"
    d "Yes"
    mc "What do I need to do?"
    d "The proof is at your school."
    d "A poem that only she wrote that you have already seen exists in that school."
    d "Go there, find the poem, and bring it back here."
    mc "I am pretty sure the school is locked up tight at this hour, you want me to break in?"
    mc "I said nothing dangerous"
    d "And I said I would give you the choice and help you while I can."
    d "The doors will be open to you"
    d "However, don't stray from the path! Get in, find the poem, and get back here."
    d "No matter what happens, no matter what you see, just get in and get out."
    "This is my chance; I can find out what is going on."
    "I can figure out what happened to Monika and why no one remembers her."
    mc "Fine I will go"
    d "......Talk to you soon"
    scene black
    with dissolve_scene_full
    "--After I hung up I started making the walk to the school from here--"

    play music breeze01
    scene bg bridge_night
    with dissolve_scene_full
    "--25 minutes later--"
    mc "Alright a quick trip across the bridge and I should be at the school in just a few moments."
    mc "This is the fastest way to the school from what my phone says."
    "I have to wonder; however, I am about to break into my school looking for a poem???"
    "Man, I am dumb... That is crazy and dangerous... What the hell did I tell that guy yes for?"

    play music breeze
    scene bg night
    with wipeleft_scene
    mc "What a beautiful night."
    mc "I have no clue how he is doing this... but the doors better be open."
    if mom < 0:
        play sound phone
        "Oh crap"
        mc "Hello?"
        c "ARE YOU KIDDING ME?!"
        mc "Hey mom, I am so sorry I completely forgot to call you."
        c "This is not a joke [player]!"
        play sound crying
        c "I was so worried about you! You really need to think of someone other then yourself!"
        mc "Mom come on, it was a honest mistake."
        "I can hear my mother crying in the phone now."
        "She is trying to hide it... but I can hear her."
        mc "Mom, don't cry please."
        c "You have no idea how worried I was. With everything that has happened, why can't you just call me?"
        c "Please, I really need you to think of other people. I was so worried."
        stop sound
        "She is right. I didn't even think of her."
        "Yes, she calls a lot, maybe to much."
        "However, my friends are dead and I am sure she was scared."
        mc "I am so sorry mom, I promise you I will never do that again."
        c "I am going to bed [player]. Get home soon."
        "--The phone went dead--"
        "Why couldn't I just make a phone call?"
        "She was crying because of me."
        "Ok, I am almost there. I just need to get this over with."
    if mom > 0:
        "I am so glad I called my mom."
        "I know she calls a lot, but I know she has been really worried about me."
        "After all, all of my friends from the club are gone."
        "I hope me being out this late isn't stressing her out."


    scene bg lockers_night
    with wipeleft_scene
    "He was right... The front door was open, and the chain was just hanging there."
    "How did he do that?"
    "How did he know that it would be open?"
    "I can't think about this now."
    "Just go in and find the poem."
    "Well, here I go..."
    menu:
        "Where do I go first?"
        "Classroom?":
            "Trying to remember what class Monika was in was a bit harder than I thought it would be."
            scene bg class_night
            with wipeleft_scene
            "Ok... I know this was her class. "
            "Man, I hate the way schools are set up, every room looks the same."
            "Almost like those conditioning camps, I have read about in history books."
            "Every room the same, every lecture from a book written by someone that claims to be an expert."
            "Everyone believing what the teachers and professors say without thinking for themselves..."
            "Ok, I need to stop this... it is freaking me out."
            mc "Where is the poem?"
            mc "Watch this be a huge waste of time, and that guy is just laughing his butt off at me from his couch."
            "I don't see it anywhere."
            scene bg class_night
            with wipeleft_scene
            "--After searching for too long--"
            "Really what am I expecting. Just out on a desk?"
            "I can't find it...... Time to move on."
        "Club Room?":
            "Well, I guess this makes the most sense."

    scene bg corridor_night
    with wipeleft_scene
    "Man, this is kind of scary at night."
    "You never really think about it till you see it."
    play music piano fadein 7.0
    mc "What is that?"
    mc "Is someone playing the piano?"
    mc "This late?"
    "It is coming from down the hallway past the club room I think."
    menu:
        "Should I call out and see who it is?"
        "Yes":
            $ path = 0
            mc "Hello is someone here?"
            stop music
            pause 4.0
            mc "Ummm... Hellooooo?"
            pause 2.0
            mc "{cps=10}Anyone?????{/cps}"
            show screen tear(20, 0.1, 0.1, 0, 40)            
            $ pause(2.0)
            hide screen tear 
            scene bg corridor_dark
            pause 2.0
            play sound giggle
            mc "What was that?"
            pause 2.0
            play sound giggle01
            mc "Ok that sounded closer! I am getting out of here!"
            "There is the club room!"
            "I will just duck in there."
        "No":
            $ path = 1
            "I just want to get to the club room and find this poem."
            "He said not to go outside the path!"
            "Yeah screw this. Let whoever that is play in peace."

    stop music
    scene bg club_night
    with wipeleft_scene
    if path == 0:
        "Ok... I don't think I was followed..."

    "Where is this poem?"
    "I need to find it quickly and get going."
    "Watch it not even be here."
    "..............."
    "Let me check the desk where Monika sat.."
    "It has a drawer!"
    play sound closet_open
    "No way!"
    call showpoem (poem_m1)
    python:
        try: renpy.file(config.basedir + "/Hole in Wall.txt")
        except: open(config.basedir + "/Hole in Wall.txt", "wb").write(renpy.file("Hole in Wall.txt").read())
    stop music
    mc "How is this possible?"
    mc "This is the poem that Monika wrote!"
    mc "He was right..."
    "What is going on?"
    "Ok, I need to get out of here with the poem and get back to the park."
    if path == 0:
        "I need to make sure I am not seen."
        scene bg corridor_night
        with wipeleft_scene
        "Everything is back to normal."
        "You know what, I don't want to know what is going on."
        "I need to leave."

    scene bg lockers_night
    with wipeleft_scene
    if path == 1:
        "I have to admit this went much better then I thought it would."
        "Quick, in and out, and nothing crazy happened."
        "Well other than the doors being wide open, but yeah for the most part nothing crazy."

    "Ok... I do not see anyone anywhere yet. I need to get to the bridge."
    "I don't believe this... How can no one remember her?"
    "How did that guy on the phone know about this?"
    "You know a better question would be,"
    "what is going on around here?"

    scene bg bridge_night
    play music breeze01
    with wipeleft_scene
    "You know I am going, to be honest here... I am a little bit more than freaked out."
    "I keep checking behind me just to be sure."
    "The school is already almost out of sight, but I feel like I am not far enough away yet."
    if path == 0:
        "What was that noise?"
        "Who was playing the piano?"
        "But most of all."

    "She was real... I didn't make it up."
    "Monika is real."
    "I can picture her now..."
    "How is this possible? I can recall her!"
    show monika 1 zorder 2 at t11
    "What am I suppose to do?"
    "This guy told the truth."
    hide monika
    scene bg park_night
    with wipeleft_scene
    "Ok... Made it back...."
    "....Now what??"
    if mom < 0:
        "I really need to get home."
        "I still can't get my mom's crying out of my mind."
        "Where is this guy?"

    play sound phone
    pause 2.0
    play music hb
    d "How does it feel?"
    mc "How does what feel?"
    d "To know you are not crazy."
    mc "Listen, sir, I have no idea what is going on."
    mc "How did you know about the poem?"
    mc "How do you know Monika?"
    mc "Why is everyone acting like Monika didn't exist?"
    mc "How did you know the doors to the school would be wide open?"
    d "So many questions from someone that can't see past their point of view."
    if path == 0:
        d "You didn't pay attention when I told you not to deviate from the path."
        d "How is calling out for someone not deviating from the path?"
        d "You have no idea how close you were to something bad."
        d "hmm hmm hmm..."
        d "However, I feel the need to ask."
        d "Did you enjoy the song?"
        mc "{cps=10}................{/cps}What was that?"
        d "Remember, I said I can only help you for so long."
        d " {i}You might want to make better choices in the future.{/i} "
    if path == 1:
        d "I am glad you listened to what I told you."
        d "However, I feel the need to ask you."
        mc "Ask me what?"
        d "Did you enjoy the song?"
        mc "How do you know about that?"

    d "You think you have a good handle on things till you see the outcome of your choices isn't what you wanted."
    d "...The choices you make."
    d "They hurt.... sometimes they hurt in the end."
    mc "............"
    d "I can't answer all of your questions now, however, I hope this test of faith was successful for you."
    mc "Yeah, you were right..."
    mc "Monika is real, and I am going to find out what is going on here."
    mc "What about this poem, I can just show it to a few people around town right?"
    mc "Someone will have to remember seeing her now that I have proof."
    mc "I could just take it to the cops."
    mc "Someone would have to know."
    python:
        try: 
            os.remove("Hole in Wall.txt")
        except:
            pass
    d "What poem?"
    mc "Wait! I just had it a second ago."
    d "I know, and as you agreed you brought it here to me."
    mc "How did you do that?"
    d "That is not important. You did your part, and I have done mine."
    d "Now you know I am telling the truth... and I think it is time for you to learn another truth"
    d "If you are ready that is."
    mc "What?"
    d "I know what happened to Natsuki, and I can help you get her back."
    mc "Is Natsuki ok? Where is she? Tell me!"
    d "{cps=10}........{/cps}Soon for now go home."
    d "You have done very well tonight. You will need your rest for what comes next."
    d "Remember what you have learned tonight."
    d "I will talk with you tomorrow."
    d "Return here."
    d "[player], you have started the path. There is no going back."
    stop music
    "--The phone call dies--"
    play music breeze
    mc "Great..."
    "At least it wasn't anything too nuts...."
    "And now I know Monika is real."
    "Maybe he can help me find Natsuki."

    python:
        try: 
            os.remove("Hole in Wall.txt")
        except:
            pass
    scene bg residential_night
    with wipeleft_scene
    pause 3.0
    scene bg sayori_night
    with wipeleft_scene
    "I wonder...."
    "What did he mean to help my friends?"
    "Sayori is gone.{cps=10}......right?"
    stop music
    scene bg bedroom_night
    with wipeleft_scene
    "Well, I wasn't out nearly as long as I was out last night."
    "However, I still didn't want to wake my mother up."
    if mom < 0:
        "I am pretty sure I have done enough to her for one day."

    if mom > 0:
        "It is killing me not to tell her about what is going on."
        "but...."
    python:
        try: 
            os.remove("Hole in Wall.txt")
        except:
            pass
    "I can't tell her about this... I can't tell anyone."
    "Not until I at least start to figure this out."
    "Only thing I can do now... is move forward."
    $ exit = 1
    return (exit)
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
