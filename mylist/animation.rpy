#init:
#    image owl:
#        "anim owl_1" with dissolve
#        0.5
#        "anim owl_2" with dissolve
#        0.5
#        repeat
#    image candle_my_list:
#        "anim candle_1" with dissolve
#        0.7
#        "anim candle_2" with dissolve
#        0.7
#        repeat
#    image ripple:
#        "anim prologue_1"
#        0.1
#        "anim prologue_2"
#        0.1
#        "anim prologue_3"
#        0.1
#        "anim prologue_2"
#        0.1
#        repeat
#    image keyboard:
#        "anim prologue_keyboard_1" with dissolve
#        0.1
#        "anim prologue_keyboard_2" with dissolve
#        0.1
#        "anim prologue_keyboard_3" with dissolve
#        0.1
#        "anim prologue_keyboard_4" with dissolve
#        0.1
#    image keyboard_monitor:
#        "anim prologue_keyboard_monitor_1" with dissolve
#        0.1
#        "anim prologue_keyboard_monitor_2" with dissolve
#        0.1
#        "anim prologue_keyboard_monitor_3" with dissolve
#        0.1
#        "anim prologue_keyboard_monitor_4" with dissolve
#        0.1
#    image monitor:
#        "anim prologue_monitor_1" with dissolve
#        0.1
#        "anim prologue_monitor_2" with dissolve
#        0.1
#        "anim prologue_monitor_3" with dissolve
#        0.1
#        "anim prologue_monitor_4" with dissolve
#        0.1
#    image stars:
#        "anim stars_1" with dissolve
#        0.5
#        "anim stars_3" with dissolve
#        0.5
#        repeat

label animation_my_list:
    menu:
        "Анимации"
        "По кадрам":
            jump animation_my_list_frame
        "Работающая":
            jump animation_my_list_together
        ">>Назад<<":
            jump start_my_list

label animation_my_list_frame:
    menu:
        "Раскадровка"
        "Моргание":
            show bg white
            show anim blink_down
            "anim blink_down (black)"
            show anim blink_up
            "anim blink_up (black)"
            hide anim
            show bg black
            jump animation_my_list_frame
        "Свеча":
            show anim candle_1
            "anim candle_1"
            show anim candle_2
            "anim candle_2"
            hide anim
            jump animation_my_list_frame
        "Интро":
            show anim intro_1
            "anim intro_1"
            show anim intro_2
            "anim intro_2"
            show anim intro_3
            "anim intro_3"
            show anim intro_4
            "anim intro_4"
            show anim intro_5
            "anim intro_5"
            show anim intro_6
            "anim intro_6"
            show anim intro_7
            "anim intro_7"
            show anim intro_8
            "anim intro_8"
            show anim intro_9
            "anim intro_9"
            show anim intro_10
            "anim intro_10"
            show anim intro_11
            "anim intro_11"
            show anim intro_12
            "anim intro_12"
            show anim intro_13
            "anim intro_13"
            show anim intro_14
            "anim intro_14"
            show anim intro_15
            "anim intro_15"
            show anim intro_16
            "anim intro_16"
            hide anim
            jump animation_my_list_frame
        "Сова":
            show anim owl_1
            "anim owl_1"
            show anim owl_2
            "anim owl_2"
            hide anim
            jump animation_my_list_frame
        "Пролог":
            show anim prolog_1
            "anim prolog_1"
            show anim prolog_2
            "anim prolog_2"
            show anim prolog_3
            "anim prolog_3"
            show anim prolog_4
            "anim prolog_4"
            show anim prolog_5
            "anim prolog_5"
            show anim prolog_10
            "anim prolog_10"
            show anim prolog_11
            "anim prolog_11"
            show anim prolog_14
            "anim prolog_14"
            show anim prolog_15
            "anim prolog_15"
            hide anim
            jump animation_my_list_frame
        "Рябь":
            show anim prologue_1
            "anim prologue_1"
            show anim prologue_2
            "anim prologue_2"
            show anim prologue_3
            "anim prologue_3"
            hide anim
            jump animation_my_list_frame
        "Клавиатура":
            show anim prologue_keyboard_1
            "anim prologue_keyboard_1"
            show anim prologue_keyboard_2
            "anim prologue_keyboard_2"
            show anim prologue_keyboard_3
            "anim prologue_keyboard_3"
            show anim prologue_keyboard_4
            "anim prologue_keyboard_4"
            hide anim
            jump animation_my_list_frame
        "Монитор и клавиатура":
            show anim prologue_keyboard_monitor_1
            "anim prologue_keyboard_monitor_1"
            show anim prologue_keyboard_monitor_2
            "anim prologue_keyboard_monitor_2"
            show anim prologue_keyboard_monitor_3
            "anim prologue_keyboard_monitor_3"
            show anim prologue_keyboard_monitor_4
            "anim prologue_keyboard_monitor_4"
            hide anim
            jump animation_my_list_frame
        "Монитор":
            show anim prologue_monitor_1
            "anim prologue_monitor_1"
            show anim prologue_monitor_2
            "anim prologue_monitor_2"
            show anim prologue_monitor_3
            "anim prologue_monitor_3"
            show anim prologue_monitor_4
            "anim prologue_monitor_4"
            hide anim
            jump animation_my_list_frame
        "Снег":
            show anim snow
            "anim snow"
            hide anim
            jump animation_my_list_frame
        "Звёзды":
            show anim stars_1
            "anim stars_1"
            show anim stars_3
            "anim stars_3"
            hide anim
            jump animation_my_list_frame
        ">>Назад<<":
            jump animation_my_list

label animation_my_list_together:
    menu:
        "Работающая анимация"
        "Моргание":
            show bg white
            show blinking
            "blinking"
            hide blinking
            show bg black
            jump animation_my_list_together
        "Свеча":
            show candle
            "candle"
            hide candle
            jump animation_my_list_together
        "Рябь":
            show prologue_dream
            "prologue_dream"
            hide prologue_dream
            jump animation_my_list_together
        "Сова":
            show owl
            "owl"
            hide owl
            jump animation_my_list_together
        "Клавиатура":
            show anim 1_prologue
            "anim 1_prologue"
            hide anim
            jump animation_my_list_together
        "Монитор и клавиатура":
            show anim 2_prologue
            "anim 2_prologue"
            hide anim
            jump animation_my_list_together
        "Монитор":
            show anim 3_prologue
            "anim 3_prologue"
            hide anim
            jump animation_my_list_together
        "Снег":
            show snow
            "snow"
            hide snow
            jump animation_my_list_together
        "Звёзды":
            show stars
            "stars"
            hide stars
            jump animation_my_list_together
        ">>Назад<<":
            jump animation_my_list

#Start of English translation

label animation_my_list_eng:
    menu:
        "Animations"
        "By frames":
            jump animation_my_list_eng_frame_eng
        "Working animation":
            jump animation_my_list_eng_together_eng
        ">>Back<<":
            jump start_my_list_eng

label animation_my_list_eng_frame_eng:
    menu:
        "Frames"
        "Blinking":
            show bg white
            show anim blink_down
            "anim blink_down (black)"
            show anim blink_up
            "anim blink_up (black)"
            hide anim
            show bg black
            jump animation_my_list_eng_frame_eng
        "Candle":
            show anim candle_1
            "anim candle_1"
            show anim candle_2
            "anim candle_2"
            hide anim
            jump animation_my_list_eng_frame_eng
        "Intro":
            show anim intro_1
            "anim intro_1"
            show anim intro_2
            "anim intro_2"
            show anim intro_3
            "anim intro_3"
            show anim intro_4
            "anim intro_4"
            show anim intro_5
            "anim intro_5"
            show anim intro_6
            "anim intro_6"
            show anim intro_7
            "anim intro_7"
            show anim intro_8
            "anim intro_8"
            show anim intro_9
            "anim intro_9"
            show anim intro_10
            "anim intro_10"
            show anim intro_11
            "anim intro_11"
            show anim intro_12
            "anim intro_12"
            show anim intro_13
            "anim intro_13"
            show anim intro_14
            "anim intro_14"
            show anim intro_15
            "anim intro_15"
            show anim intro_16
            "anim intro_16"
            hide anim
            jump animation_my_list_eng_frame_eng
        "Owl":
            show anim owl_1
            "anim owl_1"
            show anim owl_2
            "anim owl_2"
            hide anim
            jump animation_my_list_eng_frame_eng
        "Prologue":
            show anim prolog_1
            "anim prolog_1"
            show anim prolog_2
            "anim prolog_2"
            show anim prolog_3
            "anim prolog_3"
            show anim prolog_4
            "anim prolog_4"
            show anim prolog_5
            "anim prolog_5"
            show anim prolog_10
            "anim prolog_10"
            show anim prolog_11
            "anim prolog_11"
            show anim prolog_14
            "anim prolog_14"
            show anim prolog_15
            "anim prolog_15"
            hide anim
            jump animation_my_list_eng_frame_eng
        "Rippling":
            show anim prologue_1
            "anim prologue_1"
            show anim prologue_2
            "anim prologue_2"
            show anim prologue_3
            "anim prologue_3"
            hide anim
            jump animation_my_list_eng_frame_eng
        "Keyboard":
            show anim prologue_keyboard_1
            "anim prologue_keyboard_1"
            show anim prologue_keyboard_2
            "anim prologue_keyboard_2"
            show anim prologue_keyboard_3
            "anim prologue_keyboard_3"
            show anim prologue_keyboard_4
            "anim prologue_keyboard_4"
            hide anim
            jump animation_my_list_eng_frame_eng
        "Monitor and keyboard":
            show anim prologue_keyboard_monitor_1
            "anim prologue_keyboard_monitor_1"
            show anim prologue_keyboard_monitor_2
            "anim prologue_keyboard_monitor_2"
            show anim prologue_keyboard_monitor_3
            "anim prologue_keyboard_monitor_3"
            show anim prologue_keyboard_monitor_4
            "anim prologue_keyboard_monitor_4"
            hide anim
            jump animation_my_list_eng_frame_eng
        "Monitor":
            show anim prologue_monitor_1
            "anim prologue_monitor_1"
            show anim prologue_monitor_2
            "anim prologue_monitor_2"
            show anim prologue_monitor_3
            "anim prologue_monitor_3"
            show anim prologue_monitor_4
            "anim prologue_monitor_4"
            hide anim
            jump animation_my_list_eng_frame_eng
        "Snow":
            show anim snow
            "anim snow"
            hide anim
            jump animation_my_list_eng_frame_eng
        "Stars":
            show anim stars_1
            "anim stars_1"
            show anim stars_3
            "anim stars_3"
            show anim stars_3o
            "anim stars_3o"
            hide anim
            jump animation_my_list_eng_frame_eng
        ">>Back<<":
            jump animation_my_list_eng

label animation_my_list_eng_together_eng:
    menu:
        "Working animation"
        "Blinking":
            show bg white
            show blinking
            "blinking"
            hide blinking
            show bg black
            jump animation_my_list_eng_together_eng
        "Candle":
            show candle
            pause
            hide candle
            jump animation_my_list_eng_together_eng
        "Rippling":
            show prologue_dream
            pause
            hide prologue_dream
            jump animation_my_list_eng_together_eng
        "Owl":
            show owl
            pause
            hide owl
            jump animation_my_list_eng_together_eng
        "Keyboard":
            show anim 1_prologue
            pause
            hide anim
            jump animation_my_list_eng_together_eng
        "Monitor and keyboard":
            show anim 2_prologue
            pause
            hide anim
            jump animation_my_list_eng_together_eng
        "Monitor":
            show anim 3_prologue
            pause
            hide anim
            jump animation_my_list_eng_together_eng
        "Snow":
            show snow
            "snow"
            hide snow
            jump animation_my_list_together
        "Stars":
            show stars
            pause
            hide stars
            jump animation_my_list_eng_together_eng
        ">>Back<<":
            jump animation_my_list_eng
