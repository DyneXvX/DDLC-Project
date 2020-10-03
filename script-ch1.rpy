label ch1_main:
    $ delete_character("Monika")
    $ delete_character("Yuri")
    $ delete_character("Sayori")
    $ delete_character("Natsuki") 
    $ exit = 0    
    stop music   
    $ f_name = 'Faye'
    $ r_name = 'Ryan'
    $ faye = 0
    scene black
    with Dissolve(1.0)
    pause 1.0
    scene black
    show chapter01 zorder 50
    with Dissolve(1.5)
    pause 1.0
    scene black
    with Dissolve(1.5)
    pause 1.0    
    show dayText_monday zorder 50
    with Dissolve(1.5)
    pause 1.0
    scene black    
    python:        
        try: 
            os.remove("Hole in Wall.txt")
        except:
            pass

    scene bg bedroom_day
    with dissolve_scene_full
    play music t2
    "I have no idea what to do."
    "Last night made zero since."
    "How was I able to find a poem from someone that no one remembers?"
    "Then almost like a shot to the brain, I can remember what she looked like completely now."
    "It is almost like a fog has been lifted."
    "----------------------------------------"
    "Then when I get back to the park the poem vanishes right out of my pocket,"
    "but a guy on the phone knows all about this."
    "Including knowing about what happened at the school..."
    mc "If this was a test of faith, I think he might have overdone it just a bit..."
    play sound knock
    c "Hey you up yet?"
    mc "Yeah mom, I am getting dressed what’s going on?"
    if mom < 0:
        c "After you and your excuse not to call you better be glad, I didn't drop a bucket of water on you this morning."
        menu:
            "Should I apologize?"
            "Yes":
                $ mom += 1
                ## mom = 0
                mc "Hey mom, I am  sorry for not calling last night"
                c "Thank you [player]. I just hope you understand why I was so upset."
                mc "I do I promise that won't happen again."
            "No":
                ## mom == -1
                pass
    else:
        c "Hey I just wanted to say thanks for calling me last night."
        mc "No problem mom it was my fault for being out so late."
    
    c "Ok I need to get going to work [player], Faye is downstairs don't keep her waiting I am sure she is on her way to school."
    mc "Alright, tell her I will be done in just a minute please."
    "Faye is one of my friends from school."
    "I have known her for at least a year now maybe two to be honest"
    "Her and Sayori were what you call \"School Friends\"."
    "However, they never really seemed to hit it off for some reason."
    "I have always enjoyed her company she is really down to earth and has always been  nice to me."

    scene bg kitchen
    with wipeleft_scene
    $ restore_character("faye")
    show faye s1a at t11 zorder 2
    f "Hey [player], how are you doing this morning?"
    mc "Hey Faye, good morning I am doing well."
    mc "Looks like you are on your way to school."
    f s1d "Yeah, I just wanted to drop by and see how you were doing."
    f s1e "I was kind of hoping you were going to come back to school soon."
    mc "...I have been thinking about it lately."
    mc "However I am not  sure yet."
    f "Well, I am just glad you are at least considering it."
    f s1f "I do understand the situation, but you can't stop your life completely."
    mc "................."
    f s1e "I don't think Sayori would want you to be locked up indoors"
    mc "Yeah I know."
    f s1a "Ok will you at least promise me you will consider it?"
    menu:
        "Promise her?"
        "Yes":
            $ faye += 1            
            mc "Yes Faye, I promise I will."
            f s1c "Thank you [player]."
        "No":
            mc "I said I have been thinking about."
            "That should be good enough for her."
            f s1e "...Alright."
            f s1a "I guess that is better than nothing."
    f s1a "I need to get ready to go, I don't want to be late for school."
    mc "Here let me walk you out."
    hide faye
    
    scene bg entrance_day
    with wipeleft_scene
    show faye s1a at t11 zorder 2
    f "Hey [player]."
    mc "Yeah what's the matter, Faye?"
    f s1h "I am really glad I came by today. You are starting to look like you are doing better."
    if faye > 0:
        show faye s1a at f11 zorder 2
        f s1c "Plus I have kind of missed you lately."

    show faye s1a at t11 zorder 2
    mc "Thanks, Faye. I am trying."
    f "I know."
    f s1d "Would it be ok if I come by again soon?"
    mc "Of course Faye. You are always welcome to come by."
    f s1h "Ok, thanks [player], I will."
    f s2a "I need to go. Bye."
    mc "Bye Faye."
    hide faye
    "It  has been a while since I have seen her."
    "We used to talk quite a bit."
    "However, after Sayori I kind of started blowing her off."
    "Ok, I need to make some food."

    scene bg kitchen
    with wipeleft_scene    
    play sound cooking
    "You know, I wonder if I should talk to Faye about what happened."
    "She has always been kind to me."
    "I don't think she would judge me."
    "Heck, she might even offer some advice."
    "{cps=10}............................{/cps}"
    "Ok, who am I kidding? She would tell me I need to see a doctor."
    "And to be perfectly honest, I wouldn't blame her."
    stop sound
      
    scene bg kitchen
    with wipeleft_scene
    "Faye does have a good point, I am feeling better."
    "Maybe I should talk to my mom about this."
    stop music
    scene bg park_night
    $ pause(2.0)  
    "What am I thinking about!"
    play music t2
    scene bg kitchen    
    "I need to figure out what happened last night first."
    "I started the \"path\". I said I would continue it."
    
    scene bg bedroom_day
    with wipeleft_scene
    "Ok, he said to come back tonight, and he would tell me more."
    "If he knows what happened to Natsuki I need to hear him out."

    scene black
    with wipeleft_scene
    "{i}After spending the afternoon watching TV{/i}"
    "{i}and playing some games online.{/i}"
    "{i}You know what maybe I do need to go back to school.{/i}"

    scene bg hallway
    with wipeleft_scene
    "You know I might drop by the school this afternoon and see if I can walk Faye home."
    "It was nice of her to stop by."
    "Plus I really could use someone to talk to."
    menu:
        "Should I go to school and walk her home?"
        "Yes":
            $ path = 1
            "Let me get ready real quick."
            "I don't want her getting in any trouble if I just show up on school grounds, out of uniform."
            jump walk_faye
        "No":
            "I am not sure I should go there yet."
            "Maybe I should at least talk to my mom about going to school before I just show up on school grounds."
            "...Yeah that is for the best."
            "I will just have to call Faye later."
            "Might as well go ahead and watch some TV till this evening."
            "I need to remember to call my mom and let her know I am taking off before she gets home this evening as well."
            jump evening_walk

label walk_faye:
    
    scene bg bathroom
    with wipeleft_scene
    show mc 1a at t11 zorder 2:
        zoom 0.7
    mc "Feels like it has been a while since I put this on."
    "It has only been 3 weeks, but it feels a lot longer."
    "You know, I hate to admit this, however, I have always hated this mirror."
    "What is it about mirrors?"
    "It always feels like the other you in the mirror is about to jump out."
    ".......Creepy"
    play music hb
    mc 1e "I am getting that headache again"
    "I need to figure out what is going on with these headaches."
    mc 1v "Trauma or whatever... they want to call it."
    mc "I am getting tired of these."
    hide mc
    window hide(None)
    window auto
    play music td
    show s_kill_bg2
    pause 4.0
    stop music

    scene bg bathroom
    show mc 1v at t11 zorder 2:
        zoom 0.7
    mc "Damn it!"
    play music t2
    mc 1e "Get this under control!"
    mc "I am sure I will be hearing from this psychologist soon,"
    mc "and what am I going to say?"
    mc "Hey, I get really bad headaches and keep seeing my dead friend."
    "...They are going to lock me up."    
    hide mc
    
    scene bg entrance_day
    with wipeleft_scene
    "Alright let me head to the school before I miss her."
    "I hope she doesn't get upset by me just showing up."

    play music t8
    scene bg school_front
    with wipeleft_scene
    "Ok... Where is she?"
    play sound school_bell
    "Great I got here just in time."
    pause 2.0
    "There she is."
    play sound school
    mc "Hey, Faye!"
    show faye s1c at f11 zorder 2
    f "[player]! Hey, what are you doing up here?"
    show faye s1a at t11 zorder 2
    f "I didn't see you in any classes."    
    mc "No, I didn't go to class today."
    mc "However, after your visit this morning I thought it would be nice if I could come by and,"
    mc "walk you home after school."
    f s1h "Yeah, I would love that."
    f s1c "Thank you."
    hide faye
    stop sound

    
    scene bg residential_day
    with wipeleft_scene
    show faye s1a at t11 zorder 2
    $ faye += 1
    f "I am so glad you decided to come up to the school for me."
    mc "Hey it is no big deal."
    mc "When you came to visit me this morning it just got me thinking."
    f s1e "Thinking about what?"
    mc "Well I haven't seen you in a few weeks."
    mc "Plus I have kind of missed talking to you."
    f s1h "Thank you."
    f s1d "I don't remember you being this sweet before."
    mc "Ahhh don't read to much into it. It has been a few weeks."
    show faye s1u at f11 zorder 2
    f "Fine."
    mc "What are you mad now?"
    show faye s1a at t11 zorder 2
    f "No. I am not mad. Whatever you say I am just glad you came."
    hide faye
    
    scene bg faye_house
    with wipeleft_scene
    show faye s1a at t11 zorder 2
    f "Hey [player], do you mind if ask you a question?"
    mc "Sure Faye, what's on your mind."
    f s1e "I know you have gone through a lot, and I wasn't going to bring it up."
    f "However, I do want you to know that I am here for you."
    f "I know sometimes you forget to ask. However, if you ever need anything or just want to talk."
    f "I am here for you."
    mc "{cps=10}...........Faye{/cps}"
    f s1a "...yes?"
    mc "Do you remember {cps=10}.......Monika at all?{/cps}"
    f "Monika??? That name does sound familiar. Strange I feel like I knew her, but I can't seem to remember her face."
    f "Do you know what I mean. haha."
    f s1j "That is so funny, I am sorry, I don't remember her off the top of my head. Was she in one of our classes last year?"
    mc "{cps=10}...................How did you know Monika was a she?{/cps}"
    f s1e "The name [player]. I am pretty sure Monika is not a guy's name. Are you ok?"
    "Maybe I should ask her about the phone call and the park...."
    menu:
        "Tell her about the phone call?"
        "Yes":
            "ouch...... My head........again..........."
            hide faye
            window hide
            play music hb
            pause 3.0
            play sound static
            show layer screens:
                truecenter
                parallel:
                    zoom 1.5
                    easeout 0.35 zoom 1.0
                parallel:
                    xpos 0
                    easein_elastic 0.35 xpos 640
            show noise onlayer front:
                alpha 0.3
                1.35
                linear 1.0 alpha 0.0
            show glitch_color2 onlayer front           
            scene black
            $ pause(4.0)
            stop sound
            hide noise onlayer front
            hide glitch_color onlayer front
            d "{i} What do you think you're doing? {/i}"
            $ pause(2.0)
            window hide
            play sound static
            show layer screens:
                truecenter
                parallel:
                    zoom 1.5
                    easeout 0.35 zoom 1.0
                parallel:
                    xpos 0
                    easein_elastic 0.35 xpos 640
            show noise onlayer front:
                alpha 0.3
                1.35
                linear 1.0 alpha 0.0
            show glitch_color2 onlayer front           
            scene black
            $ pause(4.0)
            stop sound
            hide noise onlayer front
            hide glitch_color onlayer front    


            play music t8
            scene bg faye_house
            with dissolve_scene_full                  
            show faye s1a at t11 zorder 2
            f s1e "Are you ok [player]?"
            mc "Yeah I just have had a reoccurring headache lately. It comes and goes."
            f s1a "Oh really? Well, it might be allergies I suppose."
            mc "Yeah, you are more than likely right."
        "No":
            pass
    f "Hey [player]. Just because you have me thinking now."
    f "Do you know a girl who used to wear a big white bow in her hair?"    
    mc "!!!!"
    f "I can't seem to remember that girl's name and next time I see her I wanted to ask her where she got it from."
    f s1c "What do you think? Me with a blue hair bow... Don't lie you know I would look great with one."
    mc "{cps=10}..... yeah, you would look great with a bow, Faye.{/cps}"
    show faye s1j at f11 zorder 2
    f "Are you saying I don't look great now?"
    mc "No! I think you look great."
    show faye s1c at t11 zorder 2
    f "Haha! You are so much fun to play with."
    mc "Crap, I should have seen that coming."
    f s1a "Yes, you should have. Anyways I need to go inside, thank you so much for walking me home [player]."
    mc "No problem, Faye I have missed talking with you."
    f "I have missed you too."
    f "Don't forget what I said. If you ever need someone to talk to you can always call me."
    mc "I won't forget Faye."
    mc "Thank you"
    f s2a "Bye [player]. I hope to see you soon."
    hide faye
    "I hope so too."
    "I guess I better get home and relax before I go out tonight."
    "At least I got to see her today."
    jump evening_walk

label evening_walk:
    play music t2
    scene bg entrance_evening
    with wipeleft_scene
    "Alright time to get moving."
    menu:
        "Call mom first before heading out?"
        "Yes":
            $ mom += 1
            play sound phone
            pause 4.0
            c "Hey [player], what is going on?"
            mc "Hey Mom, I just wanted to give you a quick call and let you know I am heading out."
            c "Oh? Are you going to see Faye?"
            if path == 1:
                mc "No I walked up to school at the end and decided to walk her home today."
                c "You did?"
                mc "Well don't sound too surprised mom."
                c "No, It is just I am so glad that you did that."
                mc "Yeah I really thought it was nice of her to stop by this morning."
                mc "Plus I have to admit I kind of miss talking with her."
                c "I am so happy to hear that."
                c "Well you be careful and don't stay out too late."
                mc "I won't mom, I promise."
                mc "Talk to you later."
                c "Alright [player] bye."
            else:
                mc "No, not now. I have been thinking about dropping by, however."
                c "Well that is at least you are thinking about her."
                c "I have to admit I was really happy to see her come by the house this morning."
                mc "Yeah, so was I mom. She has always been a good friend."
                c "Well don't leave her hanging too long now [player]."
                mc "What do you mean?"
                c "Don't try that with me. She is a nice girl and you should make sure she knows it by now."
                mc ".................."
                c "Ok, I won't say anything else about her."
                mc "Thanks mom"
        "No":
            $ mom -= 1
            if mom < 0:
                "It will be fine this is not like last time. I am just taking off before she gets home."
                "She didn't even ask me to call if I went out, so I am sure it will be fine."
            if path == 1:
                "Regardless of what happens tonight, I am glad I was able to spend time with Faye again."
                "I didn't realize how much I missed her till I went to school today."
    
    play music breeze
    scene bg sidestore_evening
    with wipeleft_scene
    "I might as well stop real quick and see if the owner is in this evening."
    mc "Hello is anyone out here tonight?"   
    show ryan at l31 zorder 2
    r "Good Evening Sir, how can I.... oh hey [player]! How have you been?"
    mc "Hey Ryan I didn't know you were working here."
    show ryan at t11 zorder 2
    r "Yeah, just part-time in the evenings. What's going one with you?"
    mc "Nothing really. Just out for an evening walk."
    r "Well, I am sure that is good for you. I hope you are starting to feel better."
    mc "Oh yeah, I am getting a bit better every day."
    mc "Speaking of which is the owner in?"    
    r "The owner?"
    mc "Yeah, I spoke to him inside the other night. Older guy, I am guessing in his 40s."
    r "No, sorry [player] I have no clue who you are talking about. It is only me and a woman named Sarah and her sister that work here."
    mc "hmm... Really?"
    r "Yeah I am thinking a customer was playing around with you."
    "That is a really weird thing to do."
    mc "Yeah I guess. Oh well, not a big deal."
    mc "I am going to get going then Ryan, it was nice seeing you again."
    r "Yeah it was [player], you take care of yourself."
    hide ryan

    play music breeze
    scene bg park_night
    with wipeleft_scene
    "hmm... that was weird."
    "Why would some random guy tell me he is the store owner for no reason?"
    "Wasn't he the guy that told me about this park too?"
    "Whatever, some people are just weird."
    play sound phone
    pause 4.0
    mc "Hello"
    play music hb
    d "Good evening [player]. How was the day today?"
    mc "It was just fine thanks for asking."
    
    if path == 1:
        d "I have to say I am glad you were able to reconnect with Faye."
        d "We all should hold on to our relationships with others as tight as we can."
        d "Believe me, before you know it they are gone. Like sand slipping through your fingers on the beach."
        mc "Ok, you are creeping me out with how much you know about me."

    else:
        d "I will say it is kind of a shame you didn't spend time with Faye today."
        mc "What? How did you know about that?"
        d "Everything we do in this world would be meaningless if it only affected you and you alone."
        d "People have fought wars, famine, struggles, and everything in between just to hold on to that feeling of being close to someone."
        d "Trust me... If you can spend time with another, then do it. Don't let that moment pass you by. It is so important."
        mc "Ok I need to know something."
    
    mc "Are you spying on me or something?"
    d "No, I wouldn't say that."
    mc "Really then what would you say?"
    d "I would say I am just keeping tabs on my investment from time to time."
    mc "So, I am an investment to you then?"
    d "Yes, very much so."
    d "Don't take this the wrong way, but helping you is also helping me."
    d "You might not understand this yet, but it is in my best interest to help you, and to make sure you succeed."
    mc "You know I am not going to lie to you, for some reason that makes me feel better about this whole deal."
    d "..........It should."
    mc "Alright it is time to get to the point of all of this."
    mc "You said you knew about Natsuki, is that true or not?"
    d "It is very true. However, before we get started remember, you started this path, you must finish it regardless if you understand it or not."
    mc "I remember and I am sure you remember me saying nothing dangerous."
    d "I do."
    d "If that is settled let us get started."

    scene bg park_night
    with wipeleft_scene
    d "What I am about to tell you will be confusing at first. However, in time you will come to understand I promise."
    mc "Ok."
    d "Natsuki is fine. However, to her, everything stopped."
    mc "What do you mean everything stopped?"
    d "She is aware of this, however, at the same time she unable to do anything about it."
    d "As far as you know she disappeared soon after Sayori killed herself as well as Yuri."
    mc "Yeah, the word has been she might have had something to do with Yuri's death at the school over the weekend before the fair."
    d "That is correct, but she had nothing to do with it."
    d "The question is. Do you want her back that Friday before the weekend or not?"
    mc "What?"
    d "Do you want her back?"

    menu:
        "Save Natsuki?"
        "Yes":
            d "Then while I still can I will need you to do something like you did last night."
            d "However, my ability to keep helping you is getting more difficult as time passes."
            mc "Wait what does that mean?"
            d "It means at some point you will have to act on your own and make your own choices free of outside influence."
            mc "I have no idea what you are talking about just help me get Natsuki back alive and well."
            d "Go home tonight. When you wake up tomorrow morning you will have 12 hours to find her. It is the only time I can offer this."
            d "You will have to search for something left behind. Like what you did with Monika in the school."
            mc "What like find another poem?"
            d "To be honest, I don't know."
            d "It must be proof of her. Something that ties her to you and something that ties her to this world at this time."
            d "Find it and bring it back here within the 12 hours."
            d "If you can do that we can save her."
            d "However, if you can't find it or don't make it back here in time."
            mc "Then what?"
            d "Game Over [player]"
        "No":
            d "I can not force you to take this path."
            d "All I can do offer you the choices that were not offered before."
            mc "I have no clue what you are talking about and to be honest, you explaining it sounds more confusing"
            d "As I said, I can not force you. All I can do is offer."
            d "Are you sure you won't go after her?"
            menu:
                "Yes, I won't go after her.":
                    $ exit = 0
                    return(exit)
                "No, I changed my mind. After last night lets do this.":
                    pass
    mc "I am going after her."
    mc "I do not know who you are but somehow last night you helped me recover a little piece of Monika."
    mc "Even to the point I was able to recall her perfectly now."
    if path == 1:
        mc "Somehow by doing that even Faye remembered something about her."
        mc "She might not have known who she was talking about with the bow, but she knew something."
        mc "That is more than anyone else I have talked with."
    else:
        "I wish I would have talked to Faye about all of this"
        "I have to admit I could use a little support right now."
        "Oh well, all I can do is move forward."
    d "Then let it begin [player]."
    d "Remember the rules for this."
    d "1. You only have tomorrow."
    d "2. You must find something that links her to you and this world at this time."
    d "3. You must return it to this park by the time limit."
    d "4. If you fail. I won't be able to help with what happens next."
    d "As you have requested it will be nothing dangerous. However, don't be stupid and put yourself in danger either."
    mc "Fine. So I would have better luck finding a certain needle in a stack 10 feet high of needles right?"
    window hide
    stop music    
    pause 3.0
    play sound static
    show layer screens:
        truecenter
        parallel:
            zoom 1.5
            easeout 0.35 zoom 1.0
        parallel:
            xpos 0
            easein_elastic 0.35 xpos 640
    show noise onlayer front:
        alpha 0.3
        1.35
        linear 1.0 alpha 0.0
    show glitch_color2 onlayer front           
    scene black
    $ pause(4.0)
    stop sound
    hide noise onlayer front
    hide glitch_color onlayer front
    menu:
        "This is so stupid":
            d "{i}hmmmm..... perhaps I shouldn't count you out just yet.{/i}"
            d "{i}His time is 12 hours once the sun rises... Your time is 30 minutes. Remember that.{/i}"
        "Why am I dealing with crap in a game?":
            d "{i}So, it is starting to work. Good.{/i}"
            d "{i}There is no point in telling you what is going on yet.{/i}" 
            d "{i}Remember 12 hours for him, 30 minutes for you.{/i}"
    d "{i}Because of how important this is, I am going to explain how this will work.{/i}"
    d "{i}When [player] wakes up tomorrow the timer starts.{/i}"
    d "{i}Saving afterward will be pointless. You need to be able to guide him to finish the path in 30 minutes of your time.{/i}"
    d "{i}If not, then your window will close.{/i}"
    d "{i}The only way to restart is to re-start the day before the timer begins.{/i}"
    d "{i}I can't say this enough... Once you begin the path, you must finish the path.{/i}"
    $ pause(2.0)
    window hide
    play sound static
    show layer screens:
        truecenter
        parallel:
            zoom 1.5
            easeout 0.35 zoom 1.0
        parallel:
            xpos 0
            easein_elastic 0.35 xpos 640
    show noise onlayer front:
        alpha 0.3
        1.35
        linear 1.0 alpha 0.0
    show glitch_color2 onlayer front           
    scene black
    $ pause(4.0)
    stop sound
    hide noise onlayer front
    hide glitch_color onlayer front
    
    scene bg park_night
    play music hb
    mc "God my head is killing me..." 
    d "Hopefully those won't be going on much longer."
    d "I guess we will save that for another day [player]."
    d "Go home. Get some rest. Remember what I said."
    d "You only have tomorrow."
    stop music    

    play music breeze
    scene bg residential_night
    with wipeleft_scene
    "Well, that didn't take as long as I thought it would."
    "Maybe I should say I long as the last time took."
    "I am no closer to figuring out who is calling me."
    "I am no closer to understanding what happened to my friends."
    "and I am no closer to helping anyone."
    "What am I suppose to do?"
    "He told the truth last time, but this just seems to be getting crazier and crazier."

    stop music
    scene bg entrance_evening
    with wipeleft_scene
    "What am I suppose to do?"

    scene bg bedroom_night
    with wipeleft_scene
    "This is it. If he is telling the truth I can see Natsuki again."
    "Then I will know he has been telling the truth, and I need to stop second-guessing his help."
    "However, if this starts to feel like I am going the wrong way. Then I am out, and this will be the end for our \"investment\"."
    jump natsuki
    
label natsuki:
    scene black
    with Dissolve(1.5)
    pause 1.0    
    show dayText_tuesday zorder 50
    with Dissolve(1.5)
    pause 1.0
    scene black
    play music t2
    scene bg bedroom_day
    with wipeleft_scene
    "I am surprised, my mom didn't wake me up this morning"
    "I only have today to figure this out."
    "I need to find something that connects Natsuki to me and \"this world\"."
    "I don't even understand that means."

    python:
        start = datetime.datetime.now()
        goal = datetime.datetime.now() + datetime.timedelta(minutes = 30)
        # Begin Timer

    scene bg kitchen
    with wipeleft_scene   
    play sound cooking
    "I don't have a lot of time to figure this out today."
    "He said I needed to find this item today and return with it to the park."
    "This is pretty much like what happened in the school."
    "I wonder if I should look for something like Monika's poem."
    "I mean it would have to be something from Natsuki."
    if path == 1:
        "Ok, what about asking Faye?"
        "She is in school right now, but she might have a better idea."
        "What would I ask her?"
        "Hey, do you happen to know if Natsuki has any items or belongings at school?"
        "Yeah, I can see that look on her face."
        "She would freak out and start asking a million questions."
    else:
        "I never met up with Faye yesterday."
        "I could use her help with this today."
        "Maybe she could check Natsuki's locker or something for me."
        "Holy crap, did that I really just think about that?"
        "I don't even want to think about me asking her that. What would the question be like?"
        "Please, Faye can you break into Natsuki's locker and find something for me."
        "She would kill me."
        
    stop sound
    play sound knock
    "Who is that this early?"
    stop sound

    scene bg entrance_day
    with wipeleft_scene
    show faye c1ba at t11 zorder 2
    f "Hey good morning [player]."
    mc "Faye, Hey good morning I was just thinking about you."
    show faye c1bw2 at f11 zorder 2
    f "Oh were you?"
    mc "Yeah, I was I was just finishing cooking my breakfast in the kitchen and you popped in my head."
    show faye c1bw2 at t11 zorder 2
    f "Do I want to know what you were thinking about?"
    menu:
        "I was just thinking about..."
        "How nice it was too see you yesterday":
            $ faye += 1
            f c1bw2 "Ok, you don't need to falter me [player]!"
            f "I was just coming by and checking up on a friend."
            f "Something smells really good [player]."
            
        "I have a question for you.":
            f c1bf "Oh, that's it?"
            mc "Yeah????"
            "I don't think I will ever understand her."
            mc "What are you upset about now?"
            f "I am not upset."
            f "Something smells good [player]."
    
    show faye c1ba at t11 zorder 2
    f "I didn't mean to interrupt your breakfast, do you mind if I come to the kitchen with you so you can finish up?"
    mc "No, of course not, come on in."
    hide faye

    scene bg kitchen
    with wipeleft_scene
    show faye c1ba at f11 zorder 2
    f "Look who made enough food for two people!"
    mc "Wait this is my breakfast."
    f c1bc "Oh come on. You know you want to share it with me."
    mc "Fine... Help yourself."
    show faye c1bk at t11 zorder 2
    f "Thank you, don't mind if I do."
    hide faye
    scene black
    with wipeleft_scene
    "And just like that... she ate most of the food..."
    "How! Where does she put it!"
    "{cps=10}...........{/cps}Thanks Faye"
    scene bg kitchen
    with wipeleft_scene
    show faye c1ba at t11 zorder 2
    mc "Wait a minute, something just dawned on me."
    f c1bb "What's up?"
    mc "Aren't you suppose to be in school now?"
    show faye c1bf at f11 zorder 2
    f "Really? You just thought of that?"
    f "Me not being in our school uniform wasn't a clue?"
    show faye c1bf at t11 zorder 2
    mc "Oh, yeah... I guess that makes sense now that I see it."
    mc "I am not sure I have ever seen you in \"Normal\" clothes before."
    f "I am not sure if I should yell at you for just noticing, or maybe laugh at you for being so dumb."
    show faye c1ba at t11 zorder 2
    mc "Ok, well what is the deal? Why are you not in school?"
    f "It's a holiday [player]."
    f c1be "You really didn't know that?"
    mc "Don't look at me like that. I really didn't know."
    f "Ok, I think I am going to talk to your mother. You need to go back to school and get your life back on the right path."
    hide faye
    stop music
    scene bg park_night
    with dissolve_scene_full
    mc "Alright it is time to get to the point of all of this."
    mc "You said you knew about Natsuki, is that true or not?"
    d "It is very true. However, before we get started remember, you started this path, you must finish it regardless if you understand it or not."

    
    scene bg kitchen
    with dissolve_scene_full
    play music t2
    show faye c1ba at t11 zorder 2
    "Crap, what I am doing goofing around? I only have today."
    f "So [player], what are you doing today?"
    mc "Well, I have a few things I need to get to work on."
    f "Really? Like what?"
    mc "Well to be honest with you, I am kind of trying to work on myself a little bit."
    f c1be "Working on yourself?"
    mc "Yeah, you know I agree with you about school."
    mc "Actually I agree with you about a lot of things. I need to get back on the right path."
    show faye c1bh at f11 zorder 2
    f "Well that is great. I am glad to hear it."
    f "So, you really are starting to feel better then?"
    show faye c1bh at t11 zorder 2
    mc "Yes, I am. let us just say I want to get some closure and start moving forward."
    f "Well if there is anything I can help you with just ask."
    mc "You know what? There is something you can help me with Faye."
    menu:
        "Ask Faye for help with the item with Natsuki?"
        "Yes":
            mc "Hey, let me ask something."
            show faye c1be at t11 zorder 2
            mc "I know you have heard all about the literature club, and I know you have heard all the rumors."
            mc "I am sorry I haven't talked with you about it."
            mc "I was just kind of wondering if you know if anyone had heard anything from Natsuki since it happened?"
            mc "I was told she kind of just disappeared right after."
            f "No, unfortunately not."
            f "There were rumors for a while that she might have had something to do with it."
            mc "Why would people say such things?"
            f c1ba "I think people are just looking for someone to blame."
            f  "I didn't know her that well, I think I saw her a few times in the halls."
            f c1bd "However, if I found out that my friends had killed themselves that weekend I would have a hard time coming back."
            f "After all, that is kind of what happened to you wasn't it?"
            mc "Yeah, that is a very good point."
            f c1be "I mean I hate to say this. However, I am sure people are saying rumors about you as well."
            f "They just aren't saying it around me because everyone knows we are friends."
            mc "You know I am sorry about that. I am sure people are saying stuff about you being friends with me now."
            "I never even took the time to think about Faye's point of view in all of this."
            "I am sure people are spreading all kinds of rumors about her now."
            "Hanging out with some guy right in the middle of a club that kills themselves."
            f c1bd "Hey, don't worry about it. You are my friend and I don't care what people think about you."
            f "You are a good person and you got stuck in the middle of all of this."
            f "Plus you lost someone you have been friends with for years."
            f "People can say whatever they want. I don't care."
            
            menu:
                "Maybe I should talk to Faye about the club?"
                
                "Yes":                   
                    $ faye += 2
                    mc "I am sorry, I haven't even really taken the time to talk to you about the club."
                    f "It is ok. I am sure it is really hard on you still."
                    mc "It is... But I do want you to know at least some of it."
                    f c1bc "Ok"
                    mc "Ok, how to start?"
                    mc "I didn't really know the club members for very long."
                    show faye c1ba at t11 zorder 2
                    mc "Sayori had been bugging me to join a club"
                    mc "I thought about joining the Anime club or looking into others."
                    mc "But well you remember how Sayori was."
                    f c3ba "Yeah, she didn't really let you get anything past her."
                    mc "Yeah, that is right. She always had a way of pushing me to do things."
                    mc "However, Faye..."
                    f c1be "...."
                    mc "I had no idea what was happening to her."
                    mc "I swear I had no idea about her depression."
                    mc "I had no idea how bad it was."
                    mc "I wish I would have known in advance. Maybe I could have done something to help her."
                    show faye c1be at f11 zorder 2
                    f "Please don't blame yourself. Sayori didn't tell anyone."
                    f "We might not have gotten along like best friends, but what we shared was our friendship with you, and even I didn't know what she was going through."
                    show faye c1be at t11 zorder 2
                    mc "I know. At first, I did blame myself."
                    mc "However I know now that I can't anymore. I will never be able to move forward or understand if I keep blaming myself."
                    f c1ba "That is for the best [player]."
                    mc "I don't know what happened to the other club members."
                    mc "After Sayori's house my memory gets fuzzy and I seem to have a lot of headaches now."
                    f c1be "That is probably because of the shock and stress of what you saw."
                    mc "Yeah, I know I am supposed to be meeting with a psychologist over it sometime soon."
                    f c1bc "Well, I think it is great that you can talk about it now."
                    mc "The only things that  I don't understand are what happened to Yuri, and I also have no clue where Natsuki went."
                    f c1ba "Wasn't there another member in the club?"
                    "...................?"                   
                    mc "Yeah, there was, but I can't remember her."
                    "I decided it was best to play that off for now."
                    "She knows there was another person, but not who the other person is?"
                "No":
                    pass
        "No":
            pass  
    mc "You haven't heard anything about what happened to Natsuki have you?"
    mc "I really wish I could talk to her about all of this."
    f "No I am sorry I haven't."
    if path == 1:
        f c1ba "You know something strange happened yesterday that I should tell you about"
        mc "Really?"
        f "Yeah, after you walked me home I got a phone call from some guy."
        mc "From some guy?"
        f "Yeah, at first he creeped me out, but he said he was trying to help you and then he asked how the walk was and if you were doing ok."
        f "You know, to be honest, he knew quite a bit about you."
        mc "That didn't strike you as odd?"
        show faye c1bs at t11 zorder 2
        f "Well now that you say it like that..."
        f "Yeah, I guess it is kind of odd."
        show faye c1ba at t11 zorder 2
        f "Anyways, while we were chatting I went to grab an apple from the fridge and he said the weirdest thing."
        f "He said that I needed to remember to take care of myself and to try to eat healthily."
        f "He started talking about someone he used to know and how she lived in kind of a bad relationship."
        f "I guess something about her dad, and how she never got enough to eat."
        f c1bd "He said he always thought that 4'11'' was too short for the girl."
        f "However, he was really glad that I was taking care of myself."
        mc "Well that is kind of a weird thing to say."
        f c1bb "You know, I don't remember telling him I was getting an apple now that I think about it."
        f "Then he told me to remind you to eat a full breakfast so you could start your day right, and then he thanked me and hung up."
        "........and she still ate most of the food."
        mc "Yeah, that goes on my list of weird conversations to have with someone you don't know."
        mc "He never told his name?"
        f "No... He didn't."
        ".... 4'11''?"
    f "Well I can understand you want to talk to Natsuki."
    f "Just keep in mind no one really knows what happened."
    f "I mean to be honest, for all we know she could be at home like you have been."
    f "I doubt the students at our school know anything anyway."
    mc "Yeah that is a good point, but you think some of her friends would have said something by now."
    f "I don't know, and I know I am not helping you however I am not friends with really anyone she knows."
    show faye c3ba at f11 zorder 2
    f "Now I am sure if she was at fault and the police knew about it, then this whole city would know."
    f "One way or another those events were what everyone was talking about, and I am sure no one will forget them."
    show faye c3ba at t11 zorder 2
    f "I know you are trying to find closure just be careful."
    mc "I know. Thank you for being honest with me, Faye."    
    f "Hey, it is not a problem. "
    f c1ba "I am going to go ahead and take off, I have a few errands I want to do today."
    mc "Oh, ...ok"
    show faye c1bc at f11 zorder 2    
    menu:
        f "Oh does me needing to leave bother you?"
        "Yes":
            $ faye += 1
            show faye c1ba at t11 zorder 2
            f "Oh, you're so sweet."
            f c1bh "If it makes you feel any better I don't want to leave."
            f c1bc "but, I need to get the errands done."
            f "I would invite you to come along, but I am meeting a couple of girlfriends at the mall for shopping."
            mc "No, it is ok Faye, I have a busy day myself today."
            f "Alright, but perhaps another time ok?"           
            mc "Oh course Faye, anytime."            
            f c1bh "ok it is a date then."
        "No":
            $ faye -= 2
            show faye c1t1 at t11 zorder 2
            f "Well you don't have to be rude."
            f "You could have just asked me to leave."
            mc "No, I didn't mean it like that it is just if you have to go then you have to go. Sorry Faye"
            f "Yeah, I get it."        
    hide faye

    scene bg entrance_day
    with wipeleft_scene
    show faye c1ba at t11 zorder 2
    f "Well thank you [player] for letting me stop by and hang out with you again for a bit."
    mc "Don't worry about it Faye, like I said you are always welcome to come by when you want."
    if faye >= 5:
        f "You know [player], I like spending time with you."
        f "If it is alright with you I would like us to start spending more time together." 
        f "You don't need to say anything now, I know you still have a lot going on."
        f "But please think about it, ok?"
    f c2ba "Ok, I am going to head out. Have a good day."
    mc "You too, Faye. I will talk to you soon."
    if faye >= 5:
        f "I will be looking forward to it."
    hide faye
    "Alright let me head up to my room and grab my stuff. Time to figure out where I need to go, and really what I need to get."

    scene bg bedroom_day
    with wipeleft_scene
    
    menu:
        "Should I call my mom first and let her know I am heading out?"
        "Yes":
            $ mom += 1
            play sound phone
            pause 4.0            
            play sound phone
            pause 4.0
            c "Hello, I am sorry I can't get to the phone please leave your name and number and I will call you back as soon as I can."
            "Voice Mail, she must be busy."
            mc "Hey, mom it's me. I just wanted you to know I am heading out for the day and will talk to you later."
            "--Hangs Up--"
            "Well, at least she knows I am taking off."
        "No":
            "No, I am not worried about it. Plus it is a holiday if she needs me she can just call me."
            
    "Ok... Now I need to find something that links Natsuki... and I have no clue where to go or what I am looking for."
    "Faye said, however, that even if she was around she could be at her house and no one would know."
    "Maybe I should go to her house? I don't even know where that is."
    "Maybe I should go to the school again? It is a holiday and I doubt anyone would be there."
    "Natsuki liked manga, maybe I should hit up the local book store?"
    "I don't even know what I am looking for, but I have to at least try."


label StartingSearch:
    $ downtown = 0
    scene bg entrance_day
    with wipeleft_scene
    menu:
        "Where to head out to first?"
        "Outside":
            pass
        "Back to my room":
            scene bg bedroom_day
            with wipeleft_scene
            mc "What did I come up here for again?"
            "......."
            "I can't remember. Oh well"
            jump StartingSearch
        "Kitchen":
            scene kitchen
            with wipeleft_scene
            mc "I just ate. Why am I wasting time going through the kitchen?"
            "....."
            jump StartingSearch
 
    python:
        checktime = datetime.datetime.now()        
        timespent = checktime - start 
        minutes = timespent.total_seconds() / 60    
    if checktime < goal:        
        scene bg residential_day
        play music t8
        with wipeleft_scene
        "Ok, I still have time."
        if minutes < 20:
            menu:
                "Where to start"
                "Sayori's House":
                    scene bg sayori_house
                    with wipeleft_scene
                    "....Still empty"
                    "Sometimes it feels like she is just going to run out and ask me to walk her to school."
                    "I should have said that she would be late"
                    "Then chase me down the street."
                    "While she was yelling at me that whole time."
                    "........"
                    "I would be lying if I said I didn't miss it, however."
                    "--Looks around outside--"
                    "Well, I don't see anything, and I am not breaking in."
                    python:
                        checktime = datetime.datetime.now()        
                        timespent = checktime - start 
                        minutes = timespent.total_seconds() / 60
                    if checktime < goal: 
                        if minutes < 20:
                            menu:
                                "Where to next?"
                                "Downtown":
                                    scene bg city_day
                                    with wipeleft_scene
                                    ##Downtown Daytime Script
                                    "Once again no one is around."
                                    "I only seem to come this way when it is on a Sunday or a holiday."
                                    "It just makes downtown look empty when no one is around."
                                    "--Looks around for anything that might help--"
                                    "...Nothing, this is getting me nowhere really fast."
                                    "Who am I kidding! This is taking forever."
                                    "I would almost rather have been given the needle stack and started searching that!"
                                    python:
                                        checktime = datetime.datetime.now()        
                                        timespent = checktime - start 
                                        minutes = timespent.total_seconds() / 60
                                    if checktime < goal:
                                        if minutes < 15:
                                            "Ok while I am downtown let me check out the bookstore."
                                            "You know it is more of a library, but yeah.. whatever"
                                            scene bg library
                                            with wipeleft_scene
                                            $ library = 1
                                            "Well, once again no one is here."
                                            "Not sure what I was expecting... It is a bookstore."
                                            "--Looks around the manga section and tables--"
                                            "Wait a minute.... what is this?"
                                            call showpoem(poem_ryan)
                                            python:
                                                try: renpy.file(config.basedir + "/Hey Ryan.txt")
                                                except: open(config.basedir + "/Hey Ryan.txt", "wb").write(renpy.file("Hey Ryan.txt").read())
                                            stop music
                                            "Holy Crap! It is a note to Ryan from Natsuki?"
                                            "It is just lying out here on the table?"
                                            "I didn't even know the two of them were friends."
                                            "And I thought she didn't talk to anyone about her manga collection."
                                            "Wait is this it?"
                                            play music breeze
                                            scene bg park_night                                    
                                            with dissolve_scene_full
                                            d "Remember the rules for this."
                                            d "1. You only have tomorrow."
                                            d "2. You must find something that links her to you and this world at this time."
                                            play music t8
                                            scene bg library
                                            with dissolve_scene_full
                                            "Yeah, that is right. This isn't for me, this is for Ryan..."
                                            "I need to find Ryan and quickly."
                                            "He works at that corner store. I guess I will head there next."
                                            jump crossroad_evening             
                                        else: 
                                            "Well it is too late now to hit up the library, I guess I will head to the crossroads."
                                            jump crossroad_evening
                                    else:
                                        jump fail
                                "School":
                                    scene bg school_front
                                    with wipeleft_scene
                                    ##School Daytime Script
                                    "Well, I am not 100 percent sure what I was expecting."
                                    "No one is around anywhere."
                                    "It is a holiday after all I suppose."
                                    "hmm... I had better at least look around"
                                    scene black
                                    with dissolve_scene_full
                                    "--After searching the grounds and checking the entrances--"
                                    scene bg courtyard_day
                                    with dissolve_scene_full
                                    "Nothing..."
                                    "All of the doors are locked or chained."
                                    "This is nothing like the other night."
                                    "I guess the smart thing to do at this time is to circle around then head back to the house."
                                    "I should start heading to the crossroads."
                                    jump crossroad_evening
                        else:
                            menu:
                                "Where to next?"
                                "Downtown":
                                    label Downtown_evening:
                                    ##Downtown Evening Script
                                    scene bg city_evening
                                    with wipeleft_scene
                                    if downtown == 1:
                                        "Wait a minute?!"
                                        "How did I get here?"
                                        "I was heading to the park and somehow got turned around?!"
                                        "I didn't even make it to the park?"                                        
                                    "Ok, this day is going quick."
                                    "I am supposed to find an item that links Natsuki to me, this world, and this time."
                                    "I wonder if that guy on the phone is like a fan of \"The Da Vinci Code\" or something?"
                                    "I mean really what is wrong with just speaking English?"
                                    "Hey [player], head to X, and pick up Y."
                                    "You know he did it the first time."
                                    "I wonder why he can't do the same thing again?"
                                    scene black
                                    with dissolve_scene_full
                                    "--After searching around for a while and not finding anyone, or anything--"
                                    scene bg city_evening
                                    with dissolve_scene_full
                                    "....Great. Nothing"
                                    "Well, it is too late to head to the school."
                                    if downtown == 1:
                                        "I guess I will head back to the crossroads and visit Ryan."
                                        "The bookstore is closed by now...."
                                        jump crossroad_evening
                                    "I guess I will head to the crossroads and make my way to the park."
                                    "Hopefully it is on the way."
                                    jump crossroad_evening
                                "Crossroads":                                
                                    label crossroad_evening:                                       
                                        python:
                                            checktime = datetime.datetime.now()        
                                            timespent = checktime - start 
                                            minutes = timespent.total_seconds() / 60
                                        if checktime < goal:
                                            play music breeze
                                            scene bg crossroad_evening
                                            with wipeleft_scene                                            
                                            if library == 1:
                                                "I need to get to the store and see if Ryan is working, maybe he can help me out."
                                            if downtown == 1:
                                                "I can't believe I am here again... I made one big loop and found nothing."
                                            "While I am in the area there is no harm in grabbing a drink."                                            
                                            scene bg sidestore_evening
                                            with wipeleft_scene
                                            show ryan at t31 zorder 2
                                            r "Hey, good evening [player]. What brings you by this evening."
                                            show ryan at t11 zorder 2
                                            if library == 1:
                                                mc "Hey Ryan, I found something that was supposed to go to you."
                                                r "Really? And you brought it all the way here? Thanks, man."
                                                "--You hand Ryan the note--"
                                                    python:        
                                                        try: 
                                                            os.remove("Hole in Wall.txt")
                                                        except:
                                                            pass
                                                r "Oh..."
                                                mc "You alright Ryan?"
                                                r "Yeah, I guess you read it right?"
                                                mc "Yeah, I did. Its alright man, she was my friend too remember."
                                                r "No it's not that."
                                                mc "What's up?"
                                                r "I really liked her. I mean her dad is an ass, but she always had a smile on her face."
                                                mc "Yeah she is really cute."
                                                r "I know, and man did she hate hearing that!"
                                                mc "Hahaha"
                                                r "I haven't been able to go to her house since the whole thing happened."
                                                r "She just disappeared, and then people started spreading rumors."
                                                r "Don't get me wrong, I don't think she did anything at all."
                                                r "But I can't seem to bring myself to see if she is there or not."
                                                mc "Hey Ryan, I don't think she had anything to do with this either. To be honest, I think she is just as confused as I am."
                                                r "Yeah, after seeing you the other day, I started thinking the same thing."
                                                r "I need to go by there and see if she is even there and if she is ok."
                                                mc "I will tell you what man. I need to talk to her too. Do you mind if I go over there and see?"
                                                r "No of course not. I am sure you two do need to talk to anyways."
                                                r "Hey, if you do go, and she is there. Tell her I am sorry for not coming over myself."
                                                mc "I promise I will tell you if she is ok."
                                                r "Thanks. Here is her address, just a word of advice. Her dad really is an ass."
                                                    python:        
                                                        try: 
                                                            os.remove("Hole in Wall.txt")
                                                        except:
                                                            pass
                                                mc "Thanks man"
                                                scene black
                                                with dissolve_scene_full
                                                "--I took off and headed for the Natsuki's house.--"                                                
                                                jump natsuki_house
                                            mc "Just taking a walk in the evening air."
                                            mc "I guess you are working hard again."
                                            r "Yeah you gotta do what you can to make a few extra dollars, you know?"
                                            mc "Yes sir I can understand"
                                            r "So, how have you been?"
                                            mc "Not bad, really just taking every day one step at a time."
                                            r "Well that is really good to hear."
                                            if faye >= 5:
                                                r "You know I have to tell you [player] I think Faye has a bit of crush on you."
                                                mc "What? Why do you say that?"
                                                r "She talks about you all of the time."
                                                mc "......"
                                                r "Don't keep her waiting man."
                                                mc "Yeah, I am starting to notice that too."
                                                r "She is a good person [player], and those are very hard to come by."
                                                mc "Thanks Ryan"
                                            r "Hey [player], while you're here do you mind if I ask you a question?"
                                            mc "No, what's up?"
                                            r "What happened with the club? Really?"
                                            mc "You know Ryan, I hate to tell you this, but I don't really know."
                                            mc "After I saw Sayori I passed out."
                                            mc "It was the police the got me out."
                                            mc "I heard about Yuri from the police after I got out of the hospital."
                                            mc "I have no clue what happened to Natsuki."
                                            r "Yeah, I was going to go by her house, but I haven't found the courage yet."
                                            mc "Wait. What? I didn't know you are friends with Natsuki."
                                            r "It is kind of a long story, but yeah she is my friend."
                                            r "I don't think Natsuki had anything to do with this," 
                                            r "however, after everything that happened and with the way her dad is people just started spreading rumors."
                                            r "I don't know, I guess I was kind of afraid to stop by after everything."
                                            r "Not a really good friend am I?"
                                            mc "This has been tough on everyone Ryan."
                                            r "Yeah I know...."
                                            mc "Hey could you do me a favor and tell me where she lives?"
                                            mc "I would love to talk to her."
                                            r "Really?"
                                            mc "Yeah, after what happened I would like to see for myself if she is home and how she is."
                                            r "Yeah, I don't mind, but [player], I am not kidding. Her dad is an ass. If they have been there the whole time be careful."
                                            mc "I will man, thank you."
                                            r "While you are heading that way.. Do me a favor. If she is there, tell her I am sorry for not coming by myself and I hope she understands."
                                            mc "I will... and I will tell you what happens."
                                            r "Thanks [player]."
                                            scene black
                                            with dissolve_scene_full
                                            "--After saying goodby and thanks I left for Natsuki's house--"
                                            jump natsuki_house
                                        else:
                                            jump fail
                    else:
                        jump fail                    
                "Crossroads":
                    scene bg crossroad
                    with wipeleft_scene
                    ##Crossroad Daytime Script
                    "I have always loved this part of town."
                    "Just seems like such an inviting space."
                    menu:
                        "Which way?"
                        "Downtown":
                            jump Downtown_evening
                        "Sidestore":
                            scene bg sidestore_afternoon
                            with wipeleft_scene
                            "--I decided to stop by the store and see if Ryan was in today. However, they said he wouldn't be here till this evening--"
                            "I still remember that weird guy that was here the first time I found the park."
                            "I wonder what happened to the guy."
                            "Why would someone lie about being a worker here or the owner, then give me directions to a park?"
                            "I tell you the world is full of crazy people with nothing better to do with their time."
                            scene black
                            with dissolve_scene_full
                            "--After searching around for a bit, I decided it was kind of pointless in this area and was just wasting my time here--"
                            scene bg sidestore_afternoon
                            with dissolve_scene_full
                            "Ok... Well, I guess I can start heading in the direction of the park. That is the only thing this way."
                            $ downtown = 1
                            "Afterwards I guess I will have to just have to cross the bridge then head back past the school into downtown."
                            jump Downtown_evening



        else:
            menu:
                "I need to get moving"
                "Sayori's House":
                    scene bg sayori_evening
                    with wipeleft_scene
                    "Evening Sayori's house script"
                    jump crossroad_evening
                "Crossroads":
                    jump crossroad_evening

    else:
        scene bg residential_night
        with wipeleft_scene
        play music breeze
        "Crap! I spent to much time goofing off!"
        "What was I doing all day!?" 
        "He said I only had today and it is already night."
        jump fail



    label natsuki_house:
        python:
            checktime = datetime.datetime.now()        
            timespent = checktime - start 
            minutes = timespent.total_seconds() / 60
        if checktime < goal:
            play music breeze
            scene bg natsuki_evening
            with dissolve_scene_full
            "Alright this is the address"
            "It doesn't look like anyone is here."
            pause 3.0
            "Ok... It doesn't look like anyone has been here for awhile either."
            "Great. It is already dark, I have found nothing, and I am running out of time."
            $ pause(2.0)
            show screen tear(20, 0.1, 0.1, 0, 40)            
            $ pause(2.0)
            hide screen tear
            play sound audio.closet_close
            "What was that?"
            "Did the door just open?"
            "Ok... You know what, I think I am getting use to this."
            "I will just go in, look around and be quick about it."
            stop music
            scene bg natsuki_room_night
            with wipeleft_scene
            "This has to be her room."
            "Not what I pictured, but yeah I can see it."
            "Clean, quiet, cute..."
            "Alright... Let me look around"
            "{cps=10}............................{/cps}"
            "hmmm... nothing..."
            "Wait a minute"
            "This drawer on the desk is locked. With a pre-selected number combo?"            
            jump lock
        else:
            jump fail
    label lock:        
            menu:
                "What 3 digit combo should I try?"
                "838":
                    pause 5.0                 
                    "Nope"
                    jump lock
                "193":
                    pause 5.0                  
                    "Nope"
                    jump lock
                "914":
                    pause 5.0              
                    "Nope"
                    jump lock
                "204":
                    pause 5.0                    
                    "Nope"
                    jump lock
                "411":
                    pause 5.0
                    "Correct!"
                    "Holy crap this is it!"
                    if path == 1:
                        "Thank you Faye"                    
                    call showpoem(poem_n1)
                    python:
                        try: renpy.file(config.basedir + "/Eagles Can Fly.txt")
                        except: open(config.basedir + "/Eagles Can Fly.txt", "wb").write(renpy.file("Eagles Can Fly.txt").read())
                    "This is it, this is the poem she showed me!"
                    "I found it!"
                    stop music
                    jump save_Natsuki
                "807":
                    pause 5.0                    
                    "Nope"
                    jump lock
                "559":
                    pause 5.0                   
                    "Nope"
                    jump lock
                "795":
                    pause 5.0                   
                    "Nope"
                    jump lock
                "037":
                    pause 5.0                   
                    "Nope"
                    jump lock
    
    
    label save_Natsuki:
        python:
            checktime = datetime.datetime.now()        
            timespent = checktime - start 
            minutes = timespent.total_seconds() / 60
        if checktime < goal:
            scene bg natsuki_evening
            play music breeze
            with wipeleft_scene
            "Ok... How am I doing on my time?"
            "--You check your watch and think--"
            if minutes >= 20:
                "Ok, I don't have a lot of time left."
                "I need to get to the park now!"
                "I better start running."
            elif ((minutes < 20) and (minutes >= 10)):
                "Ok, I didn't do to bad on time."
                "I should get back to the park."                
            else:
                "How did I do this good on time?"
                "Holy crap I was flying!"     
            scene bg park_night
            "I made it!"
        else:
            jump fail
        




    label fail:
        "fail information will go here at some point"    
    return
