define a = Character("Amandine")
define d = Character("Demon", color="#0051ff")
define nar = Character("", color="#ffffff")

image bg amandine = im.Scale("amandine back.jpg", config.screen_width, config.screen_height)

image bg laptop = im.Scale("laptop.jpg", config.screen_width, config.screen_height)

define long_fade = Fade(1,1.5,1)

label start:
    #scene amandine back
    scene bg amandine

    d "*comes closely and watches Amandine*"

    d "What are you doing?"

    a "*silence*"

    show demon stretched_hand:
        pos (0,400)
        yzoom 3
        xzoom 3
        linear 3 alpha .2

    d "*The Demon's hand has attempted to touch Amandine's shoulder but passed through it instead*"
    
    d "Just a moment ago I was busy with work and then this happened... Why am I suddenly here? Why doesn't she hear me?"

    a "*silence*"

    a "*silence...*"

    a "I miss him..."

    scene bg laptop
    with long_fade

    d "What was that?"

    show phone at right
    with moveinbottom

    d "*takes out the phone from the pocket and starts typing hurriedly*"

    nar " \"Demon: I love you.\""

    nar " \"Demon: I love you.\"\n\
\"Demon: I'll be with you whenever you think about me.\""

    nar " \"Demon: I love you.\"\n\
\"Demon: I'll be with you whenever you think about me.\"\n\
\"Demon: Even when you think I'm not there, I am.\""

    nar " \"Demon: I'll be with you whenever you think about me.\"\n\
\"Demon: Even when you think I'm not there, I am.\"\n
\"Demon: My mind and body can be busy with work, yet my soul always, *always* will be with you.\""

    nar "..."

    nar "\"I love you. With all my heart.\""

    scene bg amandine

    show phone at right    

    d "Hng?"

    a "Demon?"

    nar "Amandine felt a sudden hug from behind, which almost made her drop her phone."
    
    nar "She turned around and saw the Demon, smiling and happy."

    d "I missed you too, my love."

    nar "The End"
    return
