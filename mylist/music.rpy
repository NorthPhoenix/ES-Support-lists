label music_my_list:
    show ss serious casual with dissolve
    ss "Я должна тебя предупредить!"
    show ss nosmile casual with dspr
    ss "В разделе \"Музыка\" вместо квадратных скобок написаны, круглые скобки."
    ss "Так сделано потому, что в RenPy я не могу писать квадратные скобки."
    show ss smile2 casual with dspr
    ss "Так что, если ты видишь \"(\" или \")\"{w}, помни, это - квадратные скобки. "
    hide ss
    menu:
        "Музыка"
        "ES: Dark Side":
            jump music_my_list_dark_side
        "ES: Bright Side":
            jump music_my_list_bright_side
        "Экстра":
            jump music_my_list_extra
        ">>Назад<<":
            jump start_my_list

label music_my_list_dark_side:
    menu:
        "ES: Dark Side"
        "410":
            play music music_list["410"] fadein 1
            "music_list(\"410\")"
            stop music fadeout 1
            jump music_my_list_dark_side
        "Blow With The Fires":
            play music music_list["blow_with_the_fires"] fadein 1
            "music_list(\"blow_with_the_fires\")"
            stop music fadeout 1
            jump music_my_list_dark_side
        "Orchid":
            play music music_list["orchid"] fadein 1
            "music_list(\"orchid\")"
            stop music fadeout 1
            jump music_my_list_dark_side
        "You Won\'t Let Me Down":
            play music music_list["you_won_t_let_me_down"] fadein 1
            "music_list(\"you_won_t_let_me_down\")"
            stop music fadeout 1
            jump music_my_list_dark_side
        "Awakening Power":
            play music music_list["awakening_power"] fadein 1
            "music_list(\"awakening_power\")"
            stop music fadeout 1
            jump music_my_list_dark_side
        "Into The Unknown":
            play music music_list["into_the_unknown"] fadein 1
            "music_list(\"into_the_unknown\")"
            stop music fadeout 1
            jump music_my_list_dark_side
        "Doomed To Be Defeated":
            play music music_list["doomed_to_be_defeated"] fadein 1
            "music_list(\"doomed_to_be_defeated\")"
            stop music fadeout 1
            jump music_my_list_dark_side
        "Drown":
            play music music_list["drown"] fadein 1
            "music_list(\"drown\")"
            stop music fadeout 1
            jump music_my_list_dark_side
        "Faceless":
            play music music_list["faceless"] fadein 1
            "music_list(\"faceless\")"
            stop music fadeout 1
            jump music_my_list_dark_side
        "That's Our Madhouse":
            play music music_list["that_s_our_madhouse"] fadein 1
            "music_list(\"that_s_our_madhouse\")"
            stop music fadeout 1
            jump music_my_list_dark_side
        "Eternal Longing":
            play music music_list["eternal_longing"] fadein 1
            "music_list(\"eternal_longing\")"
            stop music fadeout 1
            jump music_my_list_dark_side
        "Glimmering Coals":
            play music music_list["glimmering_coals"] fadein 1
            "music_list(\"glimmering_coals\")"
            stop music fadeout 1
            jump music_my_list_dark_side
        "Lightness":
            play music music_list["lightness"] fadein 1
            "music_list(\"lightness\")"
            stop music fadeout 1
            jump music_my_list_dark_side
        "Lightness Radio Bus":
            play music music_list["lightness_radio_bus"] fadein 1
            "music_list(\"lightness_radio_bus\")"
            stop music fadeout 1
            jump music_my_list_dark_side
        "Gentle Predator":
            play music music_list["gentle_predator"] fadein 1
            "music_list(\"gentle_predator\")"
            stop music fadeout 1
            jump music_my_list_dark_side
        "Heather":
            play music music_list["heather"] fadein 1
            "music_list(\"heather\")"
            stop music fadeout 1
            jump music_my_list_dark_side
        "Pile":
            play music music_list["pile"] fadein 1
            "music_list(\"pile\")"
            stop music fadeout 1
            jump music_my_list_dark_side
        "Scarytale":
            play music music_list["scarytale"] fadein 1
            "music_list(\"scarytale\")"
            stop music fadeout 1
            jump music_my_list_dark_side
        "Torture":
            play music music_list["torture"] fadein 1
            "music_list(\"torture\")"
            stop music fadeout 1
            jump music_my_list_dark_side
        "Sunny Day":
            play music music_list["sunny_day"] fadein 1
            "music_list(\"sunny_day\")"
            stop music fadeout 1
            jump music_my_list_dark_side
        ">>Назад<<":
            jump music_my_list

label music_my_list_bright_side:
    menu:
        "ES: Bright Side (1)"
        "Everlasting Summer":
            play music music_list["everlasting_summer"] fadein 1
            "music_list(\"everlasting_summer\")"
            stop music fadeout 1
            jump music_my_list_bright_side
        "Door To Nightmare":
            play music music_list["door_to_nightmare"] fadein 1
            "music_list(\"door_to_nightmare\")"
            stop music fadeout 1
            jump music_my_list_bright_side
        "A Promise From Distant Days":
            play music music_list["a_promise_from_distant_days"] fadein 1
            "music_list(\"a_promise_from_distant_days\")"
            stop music fadeout 1
            jump music_my_list_bright_side
        "A Promise From Distant Days V.2":
            play music music_list["a_promise_from_distant_days_v2"] fadein 1
            "music_list(\"a_promise_from_distant_days_v2\")"
            stop music fadeout 1
            jump music_my_list_bright_side
        "I Want To Play":
            play music music_list["i_want_to_play"] fadein 1
            "music_list(\"i_want_to_play\")"
            stop music fadeout 1
            jump music_my_list_bright_side
        "Raindrops":
            play music music_list["raindrops"] fadein 1
            "music_list(\"raindrops\")"
            stop music fadeout 1
            jump music_my_list_bright_side
        "Let's Be Friends":
            play music music_list["lets_be_friends"] fadein 1
            "music_list(\"lets_be_friends\")"
            stop music fadeout 1
            jump music_my_list_bright_side
        "So Good To Be Careless":
            play music music_list["so_good_to_be_careless"] fadein 1
            "music_list(\"so_good_to_be_careless\")"
            stop music fadeout 1
            jump music_my_list_bright_side
        "Trapped In Dreams":
            play music music_list["trapped_in_dreams"] fadein 1
            "music_list(\"trapped_in_dreams\")"
            stop music fadeout 1
            jump music_my_list_bright_side
        "Dance Of Fireflies":
            play music music_list["dance_of_fireflies"] fadein 1
            "music_list(\"dance_of_fireflies\")"
            stop music fadeout 1
            jump music_my_list_bright_side
        "Timid Girl":
            play music music_list["timid_girl"] fadein 1
            "music_list(\"timid_girl\")"
            stop music fadeout 1
            jump music_my_list_bright_side
        "I Don't Blame You":
            play music music_list["i_dont_blame_you"] fadein 1
            "music_list(\"i_dont_blame_you\")"
            stop music fadeout 1
            jump music_my_list_bright_side
        "What Do You Think Of Me":
            play music music_list["what_do_you_think_of_me"] fadein 1
            "music_list(\"what_do_you_think_of_me\")"
            stop music fadeout 1
            jump music_my_list_bright_side
        "Eat Some Trouble":
            play music music_list["eat_some_trouble"] fadein 1
            "music_list(\"eat_some_trouble\")"
            stop music fadeout 1
            jump music_my_list_bright_side
        "Farewell To The Past (Edit)":
            play music music_list["farewell_to_the_past_edit"] fadein 1
            "music_list(\"farewell_to_the_past_edit\")"
            stop music fadeout 1
            jump music_my_list_bright_side
        "Farewell To The Past (Full)":
            play music music_list["farewell_to_the_past_full"] fadein 1
            "music_list(\"farewell_to_the_past_full\")"
            stop music fadeout 1
            jump music_my_list_bright_side
        "Afterword":
            play music music_list["afterword"] fadein 1
            "music_list(\"afterword\")"
            stop music fadeout 1
            jump music_my_list_bright_side
        "Two Glasses Of Melancholy":
            play music music_list["everlasting_summer"] fadein 1
            "music_list(\"everlasting_summer\")"
            stop music fadeout 1
            jump music_my_list_bright_side
        "Waltz Of Doubts":
            play music music_list["waltz_of_doubts"] fadein 1
            "music_list(\"waltz_of_doubts\")"
            stop music fadeout 1
            jump music_my_list_bright_side
        "ES: Bright Side (2)":
            jump music_my_list_bright_side2
        "ES: Bright Side (3)":
            jump music_my_list_bright_side3
        ">>Назад<<":
            jump music_my_list

label music_my_list_bright_side2:
    menu:
        "ES: Bright Side (2)"
        "I Tried To Bring It Back":
            play music music_list["tried_to_bring_it_back"] fadein 1
            "music_list(\"tried_to_bring_it_back\")"
            stop music fadeout 1
            jump music_my_list_bright_side2
        "You Lost Me":
            play music music_list["you_lost_me"] fadein 1
            "music_list(\"you_lost_me\")"
            stop music fadeout 1
            jump music_my_list_bright_side2
        "Went Fishing, Caught A Girl":
            play music music_list["went_fishing_caught_a_girl"] fadein 1
            "music_list(\"went_fishing_caught_a_girl\")"
            stop music fadeout 1
            jump music_my_list_bright_side2
        "Mystery Girl":
            play music music_list["mystery_girl_v2"] fadein 1
            "music_list(\"mystery_girl_v2\")"
            stop music fadeout 1
            jump music_my_list_bright_side2
        "Forest Maiden":
            play music music_list["forest_maiden"] fadein 1
            "music_list(\"forest_maiden\")"
            stop music fadeout 1
            jump music_my_list_bright_side2
        "Always Ready":
            play music music_list["always_ready"] fadein 1
            "music_list(\"always_ready\")"
            stop music fadeout 1
            jump music_my_list_bright_side2
        "Get To Know Me Better":
            play music music_list["get_to_know_me_better"] fadein 1
            "music_list(\"get_to_know_me_better\")"
            stop music fadeout 1
            jump music_my_list_bright_side2
        "Goodbye Home Shores":
            play music music_list["goodbye_home_shores"] fadein 1
            "music_list(\"goodbye_home_shores\")"
            stop music fadeout 1
            jump music_my_list_bright_side2
        "Silhouette In Sunset":
            play music music_list["silhouette_in_sunset"] fadein 1
            "music_list(\"silhouette_in_sunset\")"
            stop music fadeout 1
            jump music_my_list_bright_side2
        "No Tresspassing":
            play music music_list["no_tresspassing"] fadein 1
            "music_list(\"no_tresspassing\")"
            stop music fadeout 1
            jump music_my_list_bright_side2
        "Meet Me There":
            play music music_list["meet_me_there"] fadein 1
            "music_list(\"meet_me_there\")"
            stop music fadeout 1
            jump music_my_list_bright_side2
        "Memories":
            play music music_list["memories"] fadein 1
            "music_list(\"memories\")"
            stop music fadeout 1
            jump music_my_list_bright_side2
        "Memories (Piano Outdoors)":
            play music music_list["memories_piano_outdoors"] fadein 1
            "music_list(\"memories_piano_outdoors\")"
            stop music fadeout 1
            jump music_my_list_bright_side2
        "Miku Song (Flute)":
            play music music_list["miku_song_flute"] fadein 1
            "music_list(\"miku_song_flute\")"
            stop music fadeout 1
            jump music_my_list_bright_side2
        "Miku Song (Voice)":
            play music music_list["miku_song_voice"] fadein 1
            "music_list(\"miku_song_voice\")"
            stop music fadeout 1
            jump music_my_list_bright_side2
        "My Daily Life":
            play music music_list["my_daily_life"] fadein 1
            "music_list(\"my_daily_life\")"
            stop music fadeout 1
            jump music_my_list_bright_side2
        "Reflection On Water":
            play music music_list["reflection_on_water"] fadein 1
            "music_list(\"reflection_on_water\")"
            stop music fadeout 1
            jump music_my_list_bright_side2
        "Reminiscences":
            play music music_list["reminiscences"] fadein 1
            "music_list(\"reminiscences\")"
            stop music fadeout 1
            jump music_my_list_bright_side2
        "ES: Bright Side (1)":
            jump music_my_list_bright_side
        "ES: Bright Side (3)":
            jump music_my_list_bright_side3
        ">>Назад<<":
            jump music_my_list

label music_my_list_bright_side3:
    menu:
        "ES: Bright Side (3)"
        "She Is Kind":
            play music music_list["she_is_kind"] fadein 1
            "music_list(\"she_is_kind\")"
            stop music fadeout 1
            jump music_my_list_bright_side3
        "Smooth Machine":
            play music music_list["smooth_machine"] fadein 1
            "music_list(\"smooth_machine\")"
            stop music fadeout 1
            jump music_my_list_bright_side3
        "Sweet Darkness":
            play music music_list["sweet_darkness"] fadein 1
            "music_list(\"sweet_darkness\")"
            stop music fadeout 1
            jump music_my_list_bright_side3
        "Take Me Beautifully":
            play music music_list["take_me_beautifully"] fadein 1
            "music_list(\"take_me_beautifully\")"
            stop music fadeout 1
            jump music_my_list_bright_side3
        "Your Bright Side":
            play music music_list["your_bright_side"] fadein 1
            "music_list(\"your_bright_side\")"
            stop music fadeout 1
            jump music_my_list_bright_side3
        "Just Think":
            play music music_list["just_think"] fadein 1
            "music_list(\"just_think\")"
            stop music fadeout 1
            jump music_my_list_bright_side3
        "Feeling Good":
            play music music_list["everyday_theme"] fadein 1
            "music_list(\"everyday_theme\")"
            stop music fadeout 1
            jump music_my_list_bright_side3
        "Confession":
            play music music_list["confession_oboe"] fadein 1
            "music_list(\"confession_oboe\")"
            stop music fadeout 1
            jump music_my_list_bright_side3
        "ES: Bright Side (1)":
            jump music_my_list_bright_side
        "ES: Bright Side (2)":
            jump music_my_list_bright_side2
        ">>Назад<<":
            jump music_my_list

    label music_my_list_extra:
        menu:
            "Экстра"
            "Kostry":
                play music music_list["kostry"] fadein 1
                "music_list(\"kostry\")"
                stop music fadeout 1
                jump music_my_list_extra
            "Opening":
                play music music_list["opening"] fadein 1
                "music_list(\"opening\")"
                stop music fadeout 1
                jump music_my_list_extra
            "Revenga":
                play music music_list["revenga"] fadein 1
                "music_list(\"revenga\")"
                stop music fadeout 1
                jump music_my_list_extra
            "Sparkles":
                play music music_list["sparkles"] fadein 1
                "music_list(\"sparkles\")"
                stop music fadeout 1
                jump music_my_list_extra
            "Dinner Horn Processed":
                play music music_list["dinner_horn_processed"] fadein 1
                "music_list(\"dinner_horn_processed\")"
                stop music fadeout 1
                jump music_my_list_extra
            ">>Назад<<":
                jump music_my_list

#Start of English version
label music_my_list_eng:
    menu:
        "Music"
        "ES: Dark Side":
            jump music_my_list_dark_side_eng
        "ES: Bright Side":
            jump music_my_list_bright_side_eng
        "Extra":
            jump music_my_list_extra_eng
        ">>Back<<":
            jump start_my_list_eng

label music_my_list_dark_side_eng:
    menu:
        "ES: Dark Side"
        "410":
            play music music_list["410"] fadein 1
            "music_list(\"410\")"
            stop music fadeout 1
            jump music_my_list_dark_side_eng
        "Blow With The Fires":
            play music music_list["blow_with_the_fires"] fadein 1
            "music_list(\"blow_with_the_fires\")"
            stop music fadeout 1
            jump music_my_list_dark_side_eng
        "Orchid":
            play music music_list["orchid"] fadein 1
            "music_list(\"orchid\")"
            stop music fadeout 1
            jump music_my_list_dark_side_eng
        "You Won\'t Let Me Down":
            play music music_list["you_won_t_let_me_down"] fadein 1
            "music_list(\"you_won_t_let_me_down\")"
            stop music fadeout 1
            jump music_my_list_dark_side_eng
        "Awakening Power":
            play music music_list["awakening_power"] fadein 1
            "music_list(\"awakening_power\")"
            stop music fadeout 1
            jump music_my_list_dark_side_eng
        "Into The Unknown":
            play music music_list["into_the_unknown"] fadein 1
            "music_list(\"into_the_unknown\")"
            stop music fadeout 1
            jump music_my_list_dark_side_eng
        "Doomed To Be Defeated":
            play music music_list["doomed_to_be_defeated"] fadein 1
            "music_list(\"doomed_to_be_defeated\")"
            stop music fadeout 1
            jump music_my_list_dark_side_eng
        "Drown":
            play music music_list["drown"] fadein 1
            "music_list(\"drown\")"
            stop music fadeout 1
            jump music_my_list_dark_side_eng
        "Faceless":
            play music music_list["faceless"] fadein 1
            "music_list(\"faceless\")"
            stop music fadeout 1
            jump music_my_list_dark_side_eng
        "That's Our Madhouse":
            play music music_list["that_s_our_madhouse"] fadein 1
            "music_list(\"that_s_our_madhouse\")"
            stop music fadeout 1
            jump music_my_list_dark_side
        "Eternal Longing":
            play music music_list["eternal_longing"] fadein 1
            "music_list(\"eternal_longing\")"
            stop music fadeout 1
            jump music_my_list_dark_side_eng
        "Glimmering Coals":
            play music music_list["glimmering_coals"] fadein 1
            "music_list(\"glimmering_coals\")"
            stop music fadeout 1
            jump music_my_list_dark_side_eng
        "Lightness":
            play music music_list["lightness"] fadein 1
            "music_list(\"lightness\")"
            stop music fadeout 1
            jump music_my_list_dark_side_eng
        "Lightness Radio Bus":
            play music music_list["lightness_radio_bus"] fadein 1
            "music_list(\"lightness_radio_bus\")"
            stop music fadeout 1
            jump music_my_list_dark_side_eng
        "Gentle Predator":
            play music music_list["gentle_predator"] fadein 1
            "music_list(\"gentle_predator\")"
            stop music fadeout 1
            jump music_my_list_dark_side_eng
        "Heather":
            play music music_list["heather"] fadein 1
            "music_list(\"heather\")"
            stop music fadeout 1
            jump music_my_list_dark_side_eng
        "Pile":
            play music music_list["pile"] fadein 1
            "music_list(\"pile\")"
            stop music fadeout 1
            jump music_my_list_dark_side_eng
        "Scarytale":
            play music music_list["scarytale"] fadein 1
            "music_list(\"scarytale\")"
            stop music fadeout 1
            jump music_my_list_dark_side_eng
        "Torture":
            play music music_list["torture"] fadein 1
            "music_list(\"torture\")"
            stop music fadeout 1
            jump music_my_list_dark_side_eng
        "Sunny Day":
            play music music_list["sunny_day"] fadein 1
            "music_list(\"sunny_day\")"
            stop music fadeout 1
            jump music_my_list_dark_side_eng
        ">>Back<<":
            jump music_my_list_eng

label music_my_list_bright_side_eng:
    menu:
        "ES: Bright Side (1)"
        "Everlasting Summer":
            play music music_list["everlasting_summer"] fadein 1
            "music_list(\"everlasting_summer\")"
            stop music fadeout 1
            jump music_my_list_bright_side_eng
        "Door To Nightmare":
            play music music_list["door_to_nightmare"] fadein 1
            "music_list(\"door_to_nightmare\")"
            stop music fadeout 1
            jump music_my_list_bright_side_eng
        "A Promise From Distant Days":
            play music music_list["a_promise_from_distant_days"] fadein 1
            "music_list(\"a_promise_from_distant_days\")"
            stop music fadeout 1
            jump music_my_list_bright_side
        "A Promise From Distant Days V.2":
            play music music_list["a_promise_from_distant_days_v2"] fadein 1
            "music_list(\"a_promise_from_distant_days_v2\")"
            stop music fadeout 1
            jump music_my_list_bright_side_eng
        "I Want To Play":
            play music music_list["i_want_to_play"] fadein 1
            "music_list(\"i_want_to_play\")"
            stop music fadeout 1
            jump music_my_list_bright_side_eng
        "Raindrops":
            play music music_list["raindrops"] fadein 1
            "music_list(\"raindrops\")"
            stop music fadeout 1
            jump music_my_list_bright_side_eng
        "Let's Be Friends":
            play music music_list["lets_be_friends"] fadein 1
            "music_list(\"lets_be_friends\")"
            stop music fadeout 1
            jump music_my_list_bright_side_eng
        "So Good To Be Careless":
            play music music_list["so_good_to_be_careless"] fadein 1
            "music_list(\"so_good_to_be_careless\")"
            stop music fadeout 1
            jump music_my_list_bright_side_eng
        "Trapped In Dreams":
            play music music_list["trapped_in_dreams"] fadein 1
            "music_list(\"trapped_in_dreams\")"
            stop music fadeout 1
            jump music_my_list_bright_side_eng
        "Dance Of Fireflies":
            play music music_list["dance_of_fireflies"] fadein 1
            "music_list(\"dance_of_fireflies\")"
            stop music fadeout 1
            jump music_my_list_bright_side_eng
        "Timid Girl":
            play music music_list["timid_girl"] fadein 1
            "music_list(\"timid_girl\")"
            stop music fadeout 1
            jump music_my_list_bright_side_eng
        "I Don't Blame You":
            play music music_list["i_dont_blame_you"] fadein 1
            "music_list(\"i_dont_blame_you\")"
            stop music fadeout 1
            jump music_my_list_bright_side_eng
        "What Do You Think Of Me":
            play music music_list["what_do_you_think_of_me"] fadein 1
            "music_list(\"what_do_you_think_of_me\")"
            stop music fadeout 1
            jump music_my_list_bright_side_eng
        "Eat Some Trouble":
            play music music_list["eat_some_trouble"] fadein 1
            "music_list(\"eat_some_trouble\")"
            stop music fadeout 1
            jump music_my_list_bright_side_eng
        "Farewell To The Past (Edit)":
            play music music_list["farewell_to_the_past_edit"] fadein 1
            "music_list(\"farewell_to_the_past_edit\")"
            stop music fadeout 1
            jump music_my_list_bright_side_eng
        "Farewell To The Past (Full)":
            play music music_list["farewell_to_the_past_full"] fadein 1
            "music_list(\"farewell_to_the_past_full\")"
            stop music fadeout 1
            jump music_my_list_bright_side_eng
        "Afterword":
            play music music_list["afterword"] fadein 1
            "music_list(\"afterword\")"
            stop music fadeout 1
            jump music_my_list_bright_side_eng
        "Two Glasses Of Melancholy":
            play music music_list["everlasting_summer"] fadein 1
            "music_list(\"everlasting_summer\")"
            stop music fadeout 1
            jump music_my_list_bright_side_eng
        "Waltz Of Doubts":
            play music music_list["waltz_of_doubts"] fadein 1
            "music_list(\"waltz_of_doubts\")"
            stop music fadeout 1
            jump music_my_list_bright_side_eng
        "ES: Bright Side (2)":
            jump music_my_list_bright_side2_eng
        "ES: Bright Side (3)":
            jump music_my_list_bright_side3_eng
        ">>Back<<":
            jump music_my_list_eng

label music_my_list_bright_side2_eng:
    menu:
        "ES: Bright Side (2)"
        "I Tried To Bring It Back":
            play music music_list["tried_to_bring_it_back"] fadein 1
            "music_list(\"tried_to_bring_it_back\")"
            stop music fadeout 1
            jump music_my_list_bright_side2_eng
        "You Lost Me":
            play music music_list["you_lost_me"] fadein 1
            "music_list(\"you_lost_me\")"
            stop music fadeout 1
            jump music_my_list_bright_side2_eng
        "Went Fishing, Caught A Girl":
            play music music_list["went_fishing_caught_a_girl"] fadein 1
            "music_list(\"went_fishing_caught_a_girl\")"
            stop music fadeout 1
            jump music_my_list_bright_side2_eng
        "Mystery Girl":
            play music music_list["mystery_girl_v2"] fadein 1
            "music_list(\"mystery_girl_v2\")"
            stop music fadeout 1
            jump music_my_list_bright_side2_eng
        "Forest Maiden":
            play music music_list["forest_maiden"] fadein 1
            "music_list(\"forest_maiden\")"
            stop music fadeout 1
            jump music_my_list_bright_side2_eng
        "Always Ready":
            play music music_list["always_ready"] fadein 1
            "music_list(\"always_ready\")"
            stop music fadeout 1
            jump music_my_list_bright_side2_eng
        "Get To Know Me Better":
            play music music_list["get_to_know_me_better"] fadein 1
            "music_list(\"get_to_know_me_better\")"
            stop music fadeout 1
            jump music_my_list_bright_side2_eng
        "Goodbye Home Shores":
            play music music_list["goodbye_home_shores"] fadein 1
            "music_list(\"goodbye_home_shores\")"
            stop music fadeout 1
            jump music_my_list_bright_side2_eng
        "Silhouette In Sunset":
            play music music_list["silhouette_in_sunset"] fadein 1
            "music_list(\"silhouette_in_sunset\")"
            stop music fadeout 1
            jump music_my_list_bright_side2_eng
        "No Tresspassing":
            play music music_list["no_tresspassing"] fadein 1
            "music_list(\"no_tresspassing\")"
            stop music fadeout 1
            jump music_my_list_bright_side2_eng
        "Meet Me There":
            play music music_list["meet_me_there"] fadein 1
            "music_list(\"meet_me_there\")"
            stop music fadeout 1
            jump music_my_list_bright_side2_eng
        "Memories":
            play music music_list["memories"] fadein 1
            "music_list(\"memories\")"
            stop music fadeout 1
            jump music_my_list_bright_side2_eng
        "Memories (Piano Outdoors)":
            play music music_list["memories_piano_outdoors"] fadein 1
            "music_list(\"memories_piano_outdoors\")"
            stop music fadeout 1
            jump music_my_list_bright_side2_eng
        "Miku Song (Flute)":
            play music music_list["miku_song_flute"] fadein 1
            "music_list(\"miku_song_flute\")"
            stop music fadeout 1
            jump music_my_list_bright_side2_eng
        "Miku Song (Voice)":
            play music music_list["miku_song_voice"] fadein 1
            "music_list(\"miku_song_voice\")"
            stop music fadeout 1
            jump music_my_list_bright_side2_eng
        "My Daily Life":
            play music music_list["my_daily_life"] fadein 1
            "music_list(\"my_daily_life\")"
            stop music fadeout 1
            jump music_my_list_bright_side2_eng
        "Reflection On Water":
            play music music_list["reflection_on_water"] fadein 1
            "music_list(\"reflection_on_water\")"
            stop music fadeout 1
            jump music_my_list_bright_side2_eng
        "Reminiscences":
            play music music_list["reminiscences"] fadein 1
            "music_list(\"reminiscences\")"
            stop music fadeout 1
            jump music_my_list_bright_side2_eng
        "ES: Bright Side (1)":
            jump music_my_list_bright_side_eng
        "ES: Bright Side (3)":
            jump music_my_list_bright_side3_eng
        ">>Back<<":
            jump music_my_list_eng

label music_my_list_bright_side3_eng:
    menu:
        "ES: Bright Side (3)"
        "She Is Kind":
            play music music_list["she_is_kind"] fadein 1
            "music_list(\"she_is_kind\")"
            stop music fadeout 1
            jump music_my_list_bright_side3_eng
        "Smooth Machine":
            play music music_list["smooth_machine"] fadein 1
            "music_list(\"smooth_machine\")"
            stop music fadeout 1
            jump music_my_list_bright_side3_eng
        "Sweet Darkness":
            play music music_list["sweet_darkness"] fadein 1
            "music_list(\"sweet_darkness\")"
            stop music fadeout 1
            jump music_my_list_bright_side3_eng
        "Take Me Beautifully":
            play music music_list["take_me_beautifully"] fadein 1
            "music_list(\"take_me_beautifully\")"
            stop music fadeout 1
            jump music_my_list_bright_side3_eng
        "Your Bright Side":
            play music music_list["your_bright_side"] fadein 1
            "music_list(\"your_bright_side\")"
            stop music fadeout 1
            jump music_my_list_bright_side3_eng
        "Just Think":
            play music music_list["just_think"] fadein 1
            "music_list(\"just_think\")"
            stop music fadeout 1
            jump music_my_list_bright_side3_eng
        "ES: Bright Side (1)":
            jump music_my_list_bright_side_eng
        "ES: Bright Side (2)":
            jump music_my_list_bright_side2_eng
        ">>Back<<":
            jump music_my_list_eng

    label music_my_list_extra_eng:
        menu:
            "Extra"
            "Confession":
                play music music_list["confession_oboe"] fadein 1
                "music_list(\"confession_oboe\")"
                stop music fadeout 1
                jump music_my_list_extra
            "Kostry":
                play music music_list["kostry"] fadein 1
                "music_list(\"kostry\")"
                stop music fadeout 1
                jump music_my_list_extra_eng
            "Opening":
                play music music_list["opening"] fadein 1
                "music_list(\"opening\")"
                stop music fadeout 1
                jump music_my_list_extra_eng
            "Revenga":
                play music music_list["revenga"] fadein 1
                "music_list(\"revenga\")"
                stop music fadeout 1
                jump music_my_list_extra_eng
            "Sparkles":
                play music music_list["sparkles"] fadein 1
                "music_list(\"sparkles\")"
                stop music fadeout 1
                jump music_my_list_extra_eng
            "Feeling Good":
                play music music_list["everyday_theme"] fadein 1
                "music_list(\"everyday_theme\")"
                stop music fadeout 1
                jump music_my_list_extra_eng
            "Dinner Horn Processed":
                play music music_list["dinner_horn_processed"] fadein 1
                "music_list(\"dinner_horn_processed\")"
                stop music fadeout 1
                jump music_my_list_extra_eng
            ">>Back<<":
                jump music_my_list_eng
