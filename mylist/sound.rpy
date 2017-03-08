label sound_my_list:
    menu:
        "Звуковые эфекты"
        "Звуки связанные с огнём":
            jump sound_my_list_fire
        "Звуки техники":
            jump sound_my_list_tech
        "Звуки связанные с жидкостью":
            jump sound_my_list_liq
        "Звуки природы":
            jump sound_my_list_animalsEnviron
        "Звуки связанные с человеком":
            jump sound_my_list_characters
        "Звуки открытия и закрытия":
            jump sound_my_list_openingClosing
        "Звуки удара и ломания":
            jump sound_my_list_hitBreak
        "Скрип":
            jump sound_my_list_squeak
        "Остальные звуки":
            jump sound_my_list_rest
        ">>Назад<<":
            jump start_my_list

label sound_my_list_fire:
    menu:
        "Звуки связанные с огнём"
        "Зажигалка":
            play sound sfx_alisa_lighter
            "sfx_alisa_lighter"
            stop sound
            jump sound_my_list_fire
        "Взрыв":
            play sound sfx_muffled_explosion
            "sfx_muffled_explosion"
            stop sound
            jump sound_my_list_fire
        "Факел":
            play sound sfx_ignite_torch
            "sfx_ignite_torch"
            play sound sfx_torch
            "sfx_torch"
            stop sound
            jump sound_my_list_fire
        "Свеча":
            play sound sfx_blow_out_candle
            "sfx_blow_out_candle"
            play sound sfx_light_candle
            "sfx_light_candle"
            play sound sfx_match_candle
            "sfx_match_candle"
            stop sound
            jump sound_my_list_fire
        "Костёр":
            play sound sfx_forest_fireplace
            "sfx_forest_fireplace"
            stop sound
            jump sound_my_list_fire
        ">>Назад<<":
            jump sound_my_list

label sound_my_list_tech:
    menu:
        "Звуки техники"
        "Телефон":
            play sound sfx_cellular_phone_error
            "sfx_cellular_phone_error"
            play sound sfx_home_phone_ring
            "sfx_home_phone_ring"
            play sound sfx_home_phone_take
            "sfx_home_phone_take"
            stop sound
            jump sound_my_list_tech
        "Компьютер":
            play sound sfx_computer_noise
            "sfx_computer_noise"
            play sound sfx_keyboard_mouse
            "sfx_keyboard_mouse"
            play sound sfx_keyboard_mouse_computer_noise
            "sfx_keyboard_mouse_computer_noise"
            stop sound
            jump sound_my_list_tech
        "Клик":
            play sound sfx_click_1
            "sfx_click_1"
            play sound sfx_click_2
            "sfx_click_2"
            play sound sfx_click_3
            "sfx_click_3"
            stop sound
            jump sound_my_list_tech
        "Радио":
            play sound sfx_radio_squelch_1
            "sfx_radio_squelch_1"
            play sound sfx_radio_squelch_2
            "sfx_radio_squelch_2"
            play sound sfx_radio_tune
            "sfx_radio_tune"
            stop sound
            jump sound_my_list_tech
        "Дверной звонок":
            play sound sfx_door_bell
            "sfx_door_bell"
            stop sound
            jump sound_my_list_tech
        "Адский будильник":
            play sound sfx_hell_alarm_clock
            "sfx_hell_alarm_clock"
            stop sound
            jump sound_my_list_tech
        "Горн":
            play sound sfx_dinner_horn_processed
            "sfx_dinner_horn_processed"
            play sound sfx_dinner_jingle_normal
            "sfx_dinner_jingle_normal"
            play sound sfx_dinner_jingle_speaker
            "sfx_dinner_jingle_speaker"
            play sound sfx_dinner_jingle_speaker_tape
            "sfx_dinner_jingle_speaker_tape"
            stop sound
            jump sound_my_list_fire
        "Чайник":
            play sound sfx_angry_ulyana
            "sfx_angry_ulyana"
            stop sound
            jump sound_my_list_tech
        "Сигнальный пистолет":
            play sound sfx_signal_pistol
            "sfx_signal_pistol"
            stop sound
            jump sound_my_list_tech
        "Автобус":
            play sound sfx_bus_honk
            "sfx_bus_honk"
            play sound sfx_bus_idle
            "sfx_bus_idle"
            play sound sfx_bus_interior_moving
            "sfx_bus_interior_moving"
            play sound sfx_bus_loop
            "sfx_bus_loop"
            play sound sfx_bus_out
            "sfx_bus_out"
            play sound sfx_bus_stop
            "sfx_bus_stop"
            play sound sfx_cooling_bus_motor
            "sfx_cooling_bus_motor"
            play sound sfx_cooling_engine_loop
            "sfx_cooling_engine_loop"
            play sound sfx_intro_bus_door_open
            "sfx_intro_bus_door_open"
            play sound sfx_intro_bus_engine_loop
            "sfx_intro_bus_engine_loop"
            play sound sfx_intro_bus_engine_start
            "sfx_intro_bus_engine_start"
            play sound sfx_ikarus_arrive
            "sfx_ikarus_arrive"
            stop sound
            jump sound_my_list_tech
        ">>Назад<<":
            jump sound_my_list

label sound_my_list_liq:
    menu:
        "Звуки связанные с жидкостью"
        "Лодка":
            play sound sfx_rowboat_loop
            "sfx_rowboat_loop"
            play sound sfx_boat_impact
            "sfx_boat_impact"
            stop sound
            jump sound_my_list_liq
        "Жидкости":
            jump sound_my_list_liq2
        "Плавание":
            play sound sfx_swimming
            "sfx_swimming"
            stop sound
            jump sound_my_list_liq
        "Раковина":
            play sound sfx_close_water_sink
            "sfx_close_water_sink"
            play sound sfx_open_water_sink
            "sfx_open_water_sink"
            stop sound
            jump sound_my_list_liq
        ">>Назад<<":
            jump sound_my_list

label sound_my_list_liq2:
    menu:
        "Жидкости"
        "Вода":
            play sound sfx_draw_water
            "sfx_draw_water"
            play sound sfx_shoulder_dive_water
            "sfx_shoulder_dive_water"
            play sound sfx_water_emerge
            "sfx_water_emerge"
            play sound sfx_water_sink_stream
            "sfx_water_sink_stream"
            play sound sfx_water_splash
            "sfx_water_splash"
            play sound sfx_underwater_dive
            "sfx_underwater_dive"
            play sound sfx_scoop_water_cup
            "sfx_scoop_water_cup"
            stop sound
            jump sound_my_list_liq2
        "Борщ":
            play sound sfx_borshtch
            "sfx_borshtch"
            stop sound
            jump sound_my_list_liq2
        "Кампот":
            play sound sfx_throw_compote
            "sfx_throw_compote"
            stop sound
            jump sound_my_list_liq2
        ">>Назад<<":
            jump sound_my_list_liq

label sound_my_list_animalsEnviron:
    menu:
        "Звуки природы"
        "Ветер":
            play sound sfx_gusty_wind
            "sfx_gusty_wind"
            play sound sfx_wind_gust
            "sfx_wind_gust"
            stop sound
            jump sound_my_list_animalsEnviron
        "Адские кузнечики":
            play sound sfx_hell_crickets_1
            "sfx_hell_crickets_1"
            play sound sfx_hell_crickets_2
            "sfx_hell_crickets_2"
            play sound sfx_hell_crickets_3
            "sfx_hell_crickets_3"
            stop sound
            jump sound_my_list_animalsEnviron
        "Сова":
            play sound sfx_owl_far
            "sfx_owl_far"
            stop sound
            jump sound_my_list_animalsEnviron
        "Буря":
            play sound sfx_thunder_crack
            "sfx_thunder_crack"
            play sound sfx_thunder_rumble
            "sfx_thunder_rumble"
            play sound sfx_thunder_wood
            "sfx_thunder_wood"
            stop sound
            jump sound_my_list_animalsEnviron
        "Шорох листьев":
            play sound sfx_bush_leaves
            "sfx_bush_leaves"
            play sound sfx_hiding_in_bush
            "sfx_hiding_in_bush"
            play sound sfx_tree_branches
            "sfx_tree_branches"
            stop sound
            jump sound_my_list_animalsEnviron
        ">>Назад<<":
            jump sound_my_list

label sound_my_list_characters:
    menu:
        "Звуки связанные с человеком"
        "Физиологические процессы":
            jump sound_my_list_characters_fiz
        "Шаги":
            play sound sfx_alisa_masha_enter
            "sfx_alisa_masha_enter"
            play sound sfx_steps_clubs_nextroom
            "sfx_steps_clubs_nextroom"
            play sound sfx_far_steps
            "sfx_far_steps"
            play sound sfx_slavya_run
            "sfx_slavya_run"
            play sound sfx_intro_bus_stop_steps
            "sfx_intro_bus_stop_steps"
            play sound sfx_run_forest
            "sfx_run_forest"
            play sound sfx_shurik_mines_far
            "sfx_shurik_mines_far"
            stop sound
            jump sound_my_list_characters
        "Аплодисменты":
            play sound sfx_concert_applause
            "sfx_concert_applause"
            play sound sfx_simon_applause
            "sfx_simon_applause"
            stop sound
            jump sound_my_list_characters
        "Призрачный детский смех":
            play sound sfx_ghost_children_laugh
            "sfx_ghost_children_laugh"
            stop sound
            jump sound_my_list_characters
        ">>Назад<<":
            jump sound_my_list

label sound_my_list_characters_fiz:
    menu:
        "Физиологические процессы"
        "Дыхание":
            play sound sfx_inhale
            "sfx_inhale"
            play sound sfx_shurik_snore
            "sfx_shurik_snore"
            stop sound
            jump sound_my_list_characters_fiz
        "Урчание желудка":
            play sound sfx_stomach_growl
            "sfx_stomach_growl"
            stop sound
            jump sound_my_list_characters_fiz
        "Взрыв головы":
            play sound sfx_head_explode
            "sfx_head_explode"
            stop sound
            jump sound_my_list_characters_fiz
        "Сердцебиение":
            play sound sfx_head_heartbeat
            "sfx_head_heartbeat"
            stop sound
            jump sound_my_list_characters_fiz
        ">>Назад<<":
            jump sound_my_list_characters

label sound_my_list_openingClosing:
    menu:
        "Звуки открытия и закрытия"
        "Открытие":
            jump sound_my_list_openingClosing_op
        "Закрытие":
            jump sound_my_list_openingClosing_cl
        "Замок":
            jump sound_my_list_openingClosing_lock
        ">>Назад<<":
            jump sound_my_list

label sound_my_list_openingClosing_op:
    play sound sfx_slavya_gets_out
    "sfx_slavya_gets_out"
    play sound sfx_ikarus_open_doors
    "sfx_ikarus_open_doors"
    play sound sfx_shurik_opens_door
    "sfx_shurik_opens_door"
    play sound sfx_key_drawer
    "sfx_key_drawer"
    play sound sfx_cellar_open
    "sfx_cellar_open"
    play sound sfx_grate_open_hand
    "sfx_grate_open_hand"
    play sound sfx_medpunkt_door_open
    "sfx_medpunkt_door_open"
    play sound sfx_open_cabinet_1
    "sfx_open_cabinet_1"
    play sound sfx_open_cabinet_2
    "sfx_open_cabinet_2"
    play sound sfx_open_cupboard
    "sfx_open_cupboard"
    play sound sfx_open_dooor_campus_1
    "sfx_open_dooor_campus_1"
    play sound sfx_open_dooor_campus_2
    "sfx_open_dooor_campus_2"
    play sound sfx_open_door_1
    "sfx_open_door_1"
    play sound sfx_open_door_2
    "sfx_open_door_2"
    play sound sfx_open_door_clubs
    "sfx_open_door_clubs"
    play sound sfx_open_door_clubs_2
    "sfx_open_door_clubs_2"
    play sound sfx_open_door_clubs_nextroom
    "sfx_open_door_clubs_nextroom"
    play sound sfx_open_door_kick
    "sfx_open_door_kick"
    play sound sfx_open_door_mines
    "sfx_open_door_mines"
    play sound sfx_open_door_mines_metal
    "sfx_open_door_mines_metal"
    play sound sfx_open_door_strong
    "sfx_open_door_strong"
    play sound sfx_open_drapes
    "sfx_open_drapes"
    play sound sfx_open_journal
    "sfx_open_journal"
    play sound sfx_open_metal_door
    "sfx_open_metal_door"
    play sound sfx_open_metal_hatch
    "sfx_open_metal_hatch"
    play sound sfx_open_window
    "sfx_open_window"
    play sound sfx_open_table
    "sfx_open_table"
    play sound sfx_unzip_sleepbag
    "sfx_unzip_sleepbag"
    stop sound
    jump sound_my_list_openingClosing

label sound_my_list_openingClosing_cl:
    play sound sfx_close_cabinet
    "sfx_close_cabinet"
    play sound sfx_close_door_1
    "sfx_close_door_1"
    play sound sfx_close_door_campus_1
    "sfx_close_door_campus_1"
    play sound sfx_close_door_clubs_nextroom
    "sfx_close_door_clubs_nextroom"
    play sound sfx_metal_door_heavy_close
    "sfx_metal_door_heavy_close"
    play sound sfx_metal_door_large_close_basement
    "sfx_metal_door_large_close_basement"
    play sound sfx_slam_door_campus
    "sfx_slam_door_campus"
    stop sound
    jump sound_my_list_openingClosing

label sound_my_list_openingClosing_lock:
    play sound sfx_lock_open_close_1
    "sfx_lock_open_close_1"
    play sound sfx_alisa_picklock
    "sfx_alisa_picklock"
    play sound sfx_unlock_door_campus
    "sfx_unlock_door_campus"
    play sound sfx_unlock_medpunkt_door
    "sfx_unlock_medpunkt_door"
    play sound sfx_lock_close
    "sfx_lock_close"
    play sound sfx_lock_open
    "sfx_lock_open"
    play sound sfx_lock_click
    "sfx_lock_click"
    stop sound
    jump sound_my_list_openingClosing

label sound_my_list_hitBreak:
    menu:
        "Звуки удара и ломания"
        "Удары":
            play sound sfx_face_slap
            "sfx_face_slap"
            play sound sfx_pat_shoulder_hard
            "sfx_pat_shoulder_hard"
            play sound sfx_bus_window_hit
            "sfx_bus_window_hit"
            play sound sfx_energy_door_bus
            "sfx_energy_door_bus"
            play sound sfx_lena_hits_alisa
            "sfx_lena_hits_alisa"
            play sound sfx_piano_head_bump
            "sfx_piano_head_bump"
            play sound sfx_salt_impact
            "sfx_salt_impact"
            play sound sfx_punch_medium
            "sfx_punch_medium"
            play sound sfx_table_hit
            "sfx_table_hit"
            play sound sfx_punch_washstand
            "sfx_punch_washstand"
            stop sound
            jump sound_my_list_hitBreak
        "Стук":
            play sound sfx_campus_door_rattle
            "sfx_campus_door_rattle"
            play sound sfx_knock_door2
            "sfx_knock_door2"
            play sound sfx_knock_door3_dull
            "sfx_knock_door3_dull"
            play sound sfx_knock_door6_closed
            "sfx_knock_door6_closed"
            play sound sfx_knock_door7_polite
            "sfx_knock_door7_polite"
            play sound sfx_knock_door_closed_hard1
            "sfx_knock_door_closed_hard1"
            play sound sfx_knock_door_closed_hard2
            "sfx_knock_door_closed_hard2"
            play sound sfx_knocking_door_outside
            "sfx_knocking_door_outside"
            play sound sfx_knock_glass
            "sfx_knock_glass"
            play sound sfx_knocking_door_2
            "sfx_knocking_door_2"
            stop sound
            jump sound_my_list_hitBreak
        "Ломания":
            play sound sfx_bones_breaking
            "sfx_bones_breaking"
            play sound sfx_break_flashlight
            "sfx_break_flashlight"
            play sound sfx_break_flashlight_alisa
            "sfx_break_flashlight_alisa"
            play sound sfx_break_cupboard
            "sfx_break_cupboard"
            play sound sfx_break_grid
            "sfx_break_grid"
            play sound sfx_home_phone_break
            "sfx_home_phone_break"
            play sound sfx_break_monitor
            "sfx_break_monitor"
            play sound sfx_broken_dish
            "sfx_broken_dish"
            stop sound
            jump sound_my_list_hitBreak
        "Падение":
            play sound sfx_alisa_falls
            "sfx_alisa_falls"
            play sound sfx_body_bump
            "sfx_body_bump"
            play sound sfx_bodyfall_1
            "sfx_bodyfall_1"
            play sound sfx_bush_body_fall
            "sfx_bush_body_fall"
            play sound sfx_simon_fall_1
            "sfx_simon_fall_1"
            play sound sfx_simon_fall_2
            "sfx_simon_fall_2"
            play sound sfx_fall_metal_door
            "sfx_fall_metal_door"
            play sound sfx_fall_grass
            "sfx_fall_grass"
            play sound sfx_fall_wood_floor
            "sfx_fall_wood_floor"
            play sound sfx_chair_fall
            "sfx_chair_fall"
            play sound sfx_grate_hand_fall
            "sfx_grate_hand_fall"
            play sound sfx_uliana_jumps_down
            "sfx_uliana_jumps_down"
            play sound sfx_brass_drop
            "sfx_brass_drop"
            play sound sfx_hatch_drop
            "sfx_hatch_drop"
            play sound sfx_drop_pipe
            "sfx_drop_pipe"
            play sound sfx_drop_alisa_bag
            "sfx_drop_alisa_bag"
            play sound sfx_dropped_chair
            "sfx_dropped_chair"
            play sound sfx_put_sugar_cart
            "sfx_put_sugar_cart"
            stop sound
            jump sound_my_list_hitBreak
        "Прыжок":
            play sound sfx_jump_into_hole_2
            "sfx_jump_into_hole_2"
            play sound sfx_jump_over_hole
            "sfx_jump_over_hole"
            stop sound
            jump sound_my_list_hitBreak
        "Хлопок":
            play sound sfx_clench2
            "sfx_clench2"
            stop sound
            jump sound_my_list_hitBreak
        ">>Назад<<":
            jump sound_my_list

label sound_my_list_squeak:
    play sound sfx_bed_squeak1
    "sfx_bed_squeak1"
    play sound sfx_bed_squeak2
    "sfx_bed_squeak2"
    play sound sfx_wood_floor_squeak
    "sfx_wood_floor_squeak"
    play sound sfx_door_squeak_light
    "sfx_door_squeak_light"
    play sound sfx_metal_door_handle_rattle
    "sfx_metal_door_handle_rattle"
    play sound sfx_carousel_squeak
    "sfx_carousel_squeak"
    play sound sfx_open_door_squeak_2
    "sfx_open_door_squeak_2"
    stop sound
    jump sound_my_list

label sound_my_list_rest:
    menu:
        "Остальные звуки"
        "Достижение":
            play sound sfx_achievement
            "sfx_achievement"
            stop sound
            jump sound_my_list_rest
        "Конами":
            play sound sfx_konami_on
            "sfx_konami_on"
            play sound sfx_konami_off
            "sfx_konami_off"
            stop sound
            jump sound_my_list_rest
        "Теннис":
            play sound sfx_lena_plays_tennis_fail
            "sfx_lena_plays_tennis_fail"
            play sound sfx_tennis_serve_1
            "sfx_tennis_serve_1"
            play sound sfx_tennis_serve_2
            "sfx_tennis_serve_2"
            stop sound
            jump sound_my_list_rest
        "Футбол":
            play sound sfx_soccer_ball_catch
            "sfx_soccer_ball_catch"
            play sound sfx_soccer_ball_gate
            "sfx_soccer_ball_gate"
            play sound sfx_soccer_ball_kick
            "sfx_soccer_ball_kick"
            stop sound
            jump sound_my_list_rest
        "Гитара":
            play sound sfx_miku_song_learn1
            "sfx_miku_song_learn1"
            play sound sfx_miku_song_learn2
            "sfx_miku_song_learn2"
            stop sound
            jump sound_my_list_rest
        "Ключи":
            play sound sfx_keys_rattle
            "sfx_keys_rattle"
            stop sound
            jump sound_my_list_rest
        "Ящик":
            play sound sfx_drawer_rattle
            "sfx_drawer_rattle"
            stop sound
            jump sound_my_list_rest
        "Арматура":
            play sound sfx_armature_swish
            "sfx_armature_swish"
            play sound sfx_insert_crowbar_door
            "sfx_insert_crowbar_door"
            stop sound
            jump sound_my_list_rest
        "Хруст":
            play sound sfx_cigarette_pack_crumple
            "sfx_cigarette_pack_crumple"
            play sound sfx_paper_bag
            "sfx_paper_bag"
            stop sound
            jump sound_my_list_rest
        "Метла":
            play sound sfx_broom_sweep
            "sfx_broom_sweep"
            stop sound
            jump sound_my_list_rest
        "Скример":
            play sound sfx_scary_sting
            "sfx_scary_sting"
            stop sound
            jump sound_my_list_rest
        "Яйца":
            play sound sfx_cooking_eggs_1
            "sfx_cooking_eggs_1"
            play sound sfx_cooking_eggs_2
            "sfx_cooking_eggs_2"
            stop sound
            jump sound_my_list_rest
        "Яблоко":
            play sound sfx_eat_apple
            "sfx_eat_apple"
            stop sound
            jump sound_my_list_rest
        "Дорожный трафик":
            play sound sfx_street_traffic_outside
            "sfx_street_traffic_outside"
            stop sound
            jump sound_my_list_rest
        "Терминатор":
            play sound sfx_terminator
            "sfx_terminator"
            play sound sfx_terminator_parody
            "sfx_terminator_parody"
            stop sound
            jump sound_my_list_rest
        "Трение об дерево":
            play sound sfx_wood_friction
            "sfx_wood_friction"
            stop sound
            jump sound_my_list_rest
        "Неожиданность":
            play sound sfx_suspence_bang
            "sfx_suspence_bang"
            stop sound
            jump sound_my_list_rest
        "Неопознанные звуки":
            play sound sfx_intro_bus_stop_sigh
            "sfx_intro_bus_stop_sigh"
            play sound sfx_intro_bus_transition
            "sfx_intro_bus_transition"
            play sound sfx_mystery_movement
            "sfx_mystery_movement"
            play sound sfx_blanket_off_stand
            "sfx_blanket_off_stand"
            stop sound
            jump sound_my_list_rest
        ">>Назад<<":
            jump sound_my_list

#Start of English translation

label sound_my_list_eng:
    menu:
        "Break":
            jump sound_my_list_breaking_eng
        "Characters":
            jump sound_my_list_characters_eng
        "Drop":
            jump sound_my_list_dropped_eng
        "Environment":
            jump sound_my_list_animalsEnviron_eng
        "Fall & Impact":
            jump sound_my_list_impactFall_eng
        "Food":
            jump sound_my_list_food_eng
        "Movement":
            jump sound_my_list_movenment_eng
        "Rattle":
            jump sound_my_list_rattle_eng
        "Squeak":
            jump sound_my_list_squeak_eng
        "Tech":
            jump sound_my_list_tech_eng
        "Misc. sounds":
            jump sound_my_list_miscSound_eng
        "<<Back>>":
            jump start_my_list_eng
label sound_my_list_breaking_eng:
    menu:
        "Bones breaking":
            play sound sfx_bones_breaking
            "sfx_bones_breaking"
            stop sound
            jump sound_my_list_breaking_eng
        "Cupboard breaking":
            play sound sfx_break_cupboard
            "sfx_break_cupboard"
            stop sound
            jump sound_my_list_breaking_eng
        "Dish breaking":
            play sound sfx_broken_dish
            "sfx_broken_dish"
            stop sound
            jump sound_my_list_breaking_eng
        "Flashlight breaking":
            play sound sfx_break_flashlight
            "sfx_break_flashlight"
            play sound sfx_break_flashlight_alisa
            "sfx_break_flashlight_alisa"
            stop sound
            jump sound_my_list_breaking_eng
        "Grid breaking":
            play sound sfx_break_grid
            "sfx_break_grid"
            stop sound
            jump sound_my_list_breaking_eng
        "Monitor breaking":
            play sound sfx_break_monitor
            "sfx_break_monitor"
            stop sound
            jump sound_my_list_breaking_eng
        "<<Back>>":
            jump sound_my_list_eng
label sound_my_list_characters_eng:
    menu:
        "Alisa":
            play sound sfx_alisa_falls
            "sfx_alisa_falls"
            play sound sfx_alisa_lighter
            "sfx_alisa_lighter"
            play sound sfx_alisa_masha_enter
            "sfx_alisa_masha_enter"
            play sound sfx_alisa_picklock
            "sfx_alisa_picklock"
            stop sound
            jump sound_my_list_characters_eng
        "Alisa's bag dropping":
            play sound sfx_drop_alisa_bag
            "sfx_drop_alisa_bag"
            stop sound
            jump sound_my_list_characters_eng
        "Ikarus":
            play sound sfx_ikarus_arrive
            "sfx_ikarus_arrive"
            play sound sfx_ikarus_open_doors
            "sfx_ikarus_open_doors"
            stop sound
            jump sound_my_list_characters_eng
        "Lena hits alisa":
            play sound sfx_lena_hits_alisa
            "sfx_lena_hits_alisa"
            stop sound
            jump sound_my_list_characters_eng
        "Lena tennis fail":
            play sound sfx_lena_plays_tennis_fail
            "sfx_lena_plays_tennis_fail"
            stop sound
            jump sound_my_list_characters_eng
        "Miku's song":
            play sound sfx_miku_song_learn1
            "sfx_miku_song_learn1"
            play sound sfx_miku_song_learn2
            "sfx_miku_song_learn2"
            stop sound
            jump sound_my_list_characters_eng
        "Shurik":
            play sound sfx_shurik_mines_far
            "sfx_shurik_mines_far"
            play sound sfx_shurik_opens_door
            "sfx_shurik_opens_door"
            play sound sfx_shurik_snore
            "sfx_shurik_snore"
            stop sound
            jump sound_my_list_characters_eng
        "Semen":
            play sound sfx_simon_applause
            "sfx_simon_applause"
            play sound sfx_simon_fall_1
            "sfx_simon_fall_1"
            play sound sfx_simon_fall_2
            "sfx_simon_fall_2"
            stop sound
            jump sound_my_list_characters_eng
        "Slavya":
            play sound sfx_slavya_gets_out
            "sfx_slavya_gets_out"
            play sound sfx_slavya_run
            "sfx_slavya_run"
            stop sound
            jump sound_my_list_characters_eng
        "Ulyana angry":
            play sound sfx_angry_ulyana
            "sfx_angry_ulyana"
            stop sound
            jump sound_my_list_characters_eng
        "Ulyana jumps":
            play sound sfx_uliana_jumps_down
            "sfx_uliana_jumps_down"
            stop sound
            jump sound_my_list_characters_eng
        "<<Back>>":
            jump sound_my_list_eng
label sound_my_list_squeak_eng:
    menu:
        "Bed squeak":
            play sound sfx_bed_squeak1
            "sfx_bed_squeak1"
            play sound sfx_bed_squeak2
            "sfx_bed_squeak2"
            stop sound
            jump sound_my_list_squeak_eng
        "Carousel squeak":
            play sound sfx_carousel_squeak
            "sfx_carousel_squeak"
            stop sound
            jump sound_my_list_squeak_eng
        "Door squeak":
            play sound sfx_door_squeak_light
            "sfx_door_squeak_light"
            stop sound
            jump sound_my_list_squeak_eng
        "Wooden floor squeak":
            play sound sfx_wood_floor_squeak
            "sfx_wood_floor_squeak"
            stop sound
            jump sound_my_list_squeak_eng
        "Steps":
            play sound sfx_steps_clubs_nextroom
            "sfx_steps_clubs_nextroom"
            stop sound
            jump sound_my_list_squeak_eng
        "<<Back>>":
            jump sound_my_list_eng
label sound_my_list_impactFall_eng:
    menu:
        "Boat impact":
            play sound sfx_boat_impact
            "sfx_boat_impact"
            stop sound
            jump sound_my_list_impactFall_eng
        "Salt impact":
            play sound sfx_salt_impact
            "sfx_salt_impact"
            stop sound
            jump sound_my_list_impactFall_eng
        "Tennis":
            play sound sfx_tennis_serve_1
            "sfx_tennis_serve_1"
            play sound sfx_tennis_serve_2
            "sfx_tennis_serve_2"
            stop sound
            jump sound_my_list_impactFall_eng
        "Hiding in bush":
            play sound sfx_hiding_in_bush
            "sfx_hiding_in_bush"
            stop sound
            jump sound_my_list_impactFall_eng
        "Body bump":
            play sound sfx_body_bump
            "sfx_body_bump"
            stop sound
            jump sound_my_list_impactFall_eng
        "Piano head bump":
            play sound sfx_piano_head_bump
            "sfx_piano_head_bump"
            stop sound
            jump sound_my_list_impactFall_eng
        "Body fall":
            play sound sfx_bodyfall_1
            "sfx_bodyfall_1"
            stop sound
            jump sound_my_list_impactFall_eng
        "Chair fall":
            play sound sfx_chair_fall
            "sfx_chair_fall"
            stop sound
            jump sound_my_list_impactFall_eng
        "Grass falling":
            play sound sfx_fall_grass
            "sfx_fall_grass"
            stop sound
            jump sound_my_list_impactFall_eng
        "Metal door falling":
            play sound sfx_fall_metal_door
            "sfx_fall_metal_door"
            stop sound
            jump sound_my_list_impactFall_eng
        "Wooden floor falling":
            play sound sfx_fall_wood_floor
            "sfx_fall_wood_floor"
            stop sound
            jump sound_my_list_impactFall_eng
        "Armature swish":
            play sound sfx_armature_swish
            "sfx_armature_swish"
            stop sound
            jump sound_my_list_impactFall_eng
        "Wood friction":
            play sound sfx_wood_friction
            "sfx_wood_friction"
            stop sound
            jump sound_my_list_impactFall_eng
        "<<Back>>":
            jump sound_my_list_eng
label sound_my_list_dropped_eng:
    menu:
        "Brass drop":
            play sound sfx_brass_drop
            "sfx_brass_drop"
            stop sound
            jump sound_my_list_dropped_eng
        "Pipe drop":
            play sound sfx_drop_pipe
            "sfx_drop_pipe"
            stop sound
            jump sound_my_list_dropped_eng
        "Chair drop":
            play sound sfx_dropped_chair
            "sfx_dropped_chair"
            stop sound
            jump sound_my_list_dropped_eng
        "Hatch dropped":
            play sound sfx_hatch_drop
            "sfx_hatch_drop"
            stop sound
            jump sound_my_list_dropped_eng
        "Table":
            play sound sfx_table_hit
            "sfx_table_hit"
            stop sound
            jump sound_my_list_dropped_eng
        "<<Back>>":
            jump sound_my_list_eng
label sound_my_list_nocked_eng:
    menu:
        "Door nocked":
            play sound sfx_knock_door2
            "sfx_knock_door2"
            play sound sfx_knock_door3_dull
            "sfx_knock_door3_dull"
            play sound sfx_knock_door6_closed
            "sfx_knock_door6_closed"
            play sound sfx_knock_door7_polite
            "sfx_knock_door7_polite"
            play sound sfx_knock_door_closed_hard1
            "sfx_knock_door_closed_hard1"
            play sound sfx_knock_door_closed_hard2
            "sfx_knock_door_closed_hard2"
            play sound sfx_knocking_door_2
            "sfx_knocking_door_2"
            play sound sfx_knocking_door_outside
            "sfx_knocking_door_outside"
            stop sound
            jump sound_my_list_nocked_eng
        "Glass nocked":
            play sound sfx_knock_glass
            "sfx_knock_glass"
            stop sound
            jump sound_my_list_nocked_eng
        "<<Back>>":
            jump sound_my_list_eng
label sound_my_list_rattle_eng:
    menu:
        "Campus door rattle":
            play sound sfx_campus_door_rattle
            "sfx_campus_door_rattle"
            stop sound
            jump sound_my_list_rattle_eng
        "Drawer rattle":
            play sound sfx_drawer_rattle
            "sfx_drawer_rattle"
            stop sound
            jump sound_my_list_rattle_eng
        "Keys rattle":
            play sound sfx_keys_rattle
            "sfx_keys_rattle"
            stop sound
            jump sound_my_list_rattle_eng
        "Drawer key":
            play sound sfx_key_drawer
            "sfx_key_drawer"
            stop sound
            jump sound_my_list_rattle_eng
        "Cigarette pack crumple":
            play sound sfx_cigarette_pack_crumple
            "sfx_cigarette_pack_crumple"
            stop sound
            jump sound_my_list_rattle_eng
        "Paper bag":
            play sound sfx_paper_bag
            "sfx_paper_bag"
            stop sound
            jump sound_my_list_rattle_eng
        "Clench":
            play sound sfx_clench2
            "sfx_clench2"
            stop sound
            jump sound_my_list_rattle_eng
        "<<Back>>":
            jump sound_my_list_eng
label sound_my_list_tech_eng:
    menu:
        "Alarm":
            play sound sfx_hell_alarm_clock
            "sfx_hell_alarm_clock"
            stop sound
            jump sound_my_list_tech_eng
        "Bus":
            play sound sfx_bus_honk
            "sfx_bus_honk"
            play sound sfx_bus_idle
            "sfx_bus_idle"
            play sound sfx_bus_interior_moving
            "sfx_bus_interior_moving"
            play sound sfx_bus_loop
            "sfx_bus_loop"
            play sound sfx_bus_out
            "sfx_bus_out"
            play sound sfx_bus_stop
            "sfx_bus_stop"
            play sound sfx_bus_window_hit
            "sfx_bus_window_hit"
            play sound sfx_cooling_bus_motor
            "sfx_cooling_bus_motor"
            play sound sfx_cooling_engine_loop
            "sfx_cooling_engine_loop"
            play sound sfx_intro_bus_door_open
            "sfx_intro_bus_door_open"
            play sound sfx_intro_bus_engine_loop
            "sfx_intro_bus_engine_loop"
            play sound sfx_intro_bus_engine_start
            "sfx_intro_bus_engine_start"
            play sound sfx_intro_bus_stop_sigh
            "sfx_intro_bus_stop_sigh"
            play sound sfx_intro_bus_stop_steps
            "sfx_intro_bus_stop_steps"
            play sound sfx_intro_bus_transition
            "sfx_intro_bus_transition"
            play sound sfx_energy_door_bus
            "sfx_energy_door_bus"
            stop sound
            jump sound_my_list_tech_eng
        "Cellphone":
            play sound sfx_cellular_phone_error
            "sfx_cellular_phone_error"
            stop sound
            jump sound_my_list_tech_eng
        "Computer":
            play sound sfx_computer_noise
            "sfx_computer_noise"
            play sound sfx_keyboard_mouse
            "sfx_keyboard_mouse"
            play sound sfx_keyboard_mouse_computer_noise
            "sfx_keyboard_mouse_computer_noise"
            stop sound
            jump sound_my_list_tech_eng
        "Home phone":
            play sound sfx_home_phone_break
            "sfx_home_phone_break"
            play sound sfx_home_phone_ring
            "sfx_home_phone_ring"
            play sound sfx_home_phone_take
            "sfx_home_phone_take"
            stop sound
            jump sound_my_list_tech_eng
        "Konami":
            play sound sfx_konami_off
            "sfx_konami_off"
            play sound sfx_konami_on
            "sfx_konami_on"
            stop sound
            jump sound_my_list_tech_eng
        "Radio":
            play sound sfx_radio_squelch_1
            "sfx_radio_squelch_1"
            play sound sfx_radio_squelch_2
            "sfx_radio_squelch_2"
            play sound sfx_radio_tune
            "sfx_radio_tune"
            stop sound
            jump sound_my_list_tech_eng
        "Signal pistol":
            play sound sfx_signal_pistol
            "sfx_signal_pistol"
            stop sound
            jump sound_my_list_tech_eng
        "Street traffic":
            play sound sfx_street_traffic_outside
            "sfx_street_traffic_outside"
            stop sound
            jump sound_my_list_tech_eng
        "<<Back>>":
            jump sound_my_list_eng
label sound_my_list_food_eng:
    menu:
        "Borshtch":
            play sound sfx_borshtch
            "sfx_borshtch"
            stop sound
            jump sound_my_list_food_eng
        "Cooking eggs":
            play sound sfx_cooking_eggs_1
            "sfx_cooking_eggs_1"
            play sound sfx_cooking_eggs_2
            "sfx_cooking_eggs_2"
            stop sound
            jump sound_my_list_food_eng
        "Compote":
            play sound sfx_throw_compote
            "sfx_throw_compote"
            stop sound
            jump sound_my_list_food_eng
        "Eating apple":
            play sound sfx_eat_apple
            "sfx_eat_apple"
            stop sound
            jump sound_my_list_food_eng
        "Dinner":
            play sound sfx_dinner_horn_processed
            "sfx_dinner_horn_processed"
            play sound sfx_dinner_jingle_normal
            "sfx_dinner_jingle_normal"
            play sound sfx_dinner_jingle_speaker
            "sfx_dinner_jingle_speaker"
            play sound sfx_dinner_jingle_speaker_tape
            "sfx_dinner_jingle_speaker_tape"
            stop sound
            jump sound_my_list_food_eng
        "Draw water":
            play sound sfx_draw_water
            "sfx_draw_water"
            stop sound
            jump sound_my_list_food_eng
        "Sugar cart":
            play sound sfx_put_sugar_cart
            "sfx_put_sugar_cart"
            stop sound
            jump sound_my_list_food_eng
        "Stomach growl":
            play sound sfx_stomach_growl
            "sfx_stomach_growl"
            stop sound
            jump sound_my_list_food_eng
        "Water cup scoop":
            play sound sfx_scoop_water_cup
            "sfx_scoop_water_cup"
            stop sound
            jump sound_my_list_food_eng
        "<<Back>>":
            jump sound_my_list_eng
label sound_my_list_openingClosing_eng:
    menu:
        "Cellar":
            play sound sfx_cellar_open
            "sfx_cellar_open"
            stop sound
            jump sound_my_list_openingClosing_eng
        "Closing":
            play sound sfx_close_cabinet
            "sfx_close_cabinet"
            play sound sfx_close_door_1
            "sfx_close_door_1"
            play sound sfx_close_door_campus_1
            "sfx_close_door_campus_1"
            play sound sfx_close_door_clubs_nextroom
            "sfx_close_door_clubs_nextroom"
            stop sound
            jump sound_my_list_openingClosing_eng
        "Faucet":
            play sound sfx_close_water_sink
            "sfx_close_water_sink"
            play sound sfx_open_water_sink
            "sfx_open_water_sink"
            stop sound
            jump sound_my_list_openingClosing_eng
        "Grate":
            play sound sfx_grate_hand_fall
            "sfx_grate_hand_fall"
            play sound sfx_grate_open_hand
            "sfx_grate_open_hand"
            stop sound
            jump sound_my_list_openingClosing_eng
        "Crowbar door":
            play sound sfx_insert_crowbar_door
            "sfx_insert_crowbar_door"
            stop sound
            jump sound_my_list_openingClosing_eng
        "Campus door unlocking":
            play sound sfx_unlock_door_campus
            "sfx_unlock_door_campus"
            play sound sfx_unlock_medpunkt_door
            "sfx_unlock_medpunkt_door"
            stop sound
            jump sound_my_list_openingClosing_eng
        "Lock":
            play sound sfx_lock_click
            "sfx_lock_click"
            play sound sfx_lock_close
            "sfx_lock_close"
            play sound sfx_lock_open
            "sfx_lock_open"
            play sound sfx_lock_open_close_1
            "sfx_lock_open_close_1"
            stop sound
            jump sound_my_list_openingClosing_eng
        "Door":
            play sound sfx_medpunkt_door_open
            "sfx_medpunkt_door_open"
            play sound sfx_metal_door_handle_rattle
            "sfx_metal_door_handle_rattle"
            play sound sfx_metal_door_heavy_close
            "sfx_metal_door_heavy_close"
            play sound sfx_metal_door_large_close_basement
            "sfx_metal_door_large_close_basement"
            play sound sfx_open_cabinet_1
            "sfx_open_cabinet_1"
            play sound sfx_open_cabinet_2
            "sfx_open_cabinet_2"
            play sound sfx_open_cupboard
            "sfx_open_cupboard"
            play sound sfx_open_dooor_campus_1
            "sfx_open_dooor_campus_1"
            play sound sfx_open_dooor_campus_2
            "sfx_open_dooor_campus_2"
            play sound sfx_open_door_1
            "sfx_open_door_1"
            play sound sfx_open_door_2
            "sfx_open_door_2"
            play sound sfx_open_door_clubs
            "sfx_open_door_clubs"
            play sound sfx_open_door_clubs_2
            "sfx_open_door_clubs_2"
            play sound sfx_open_door_clubs_nextroom
            "sfx_open_door_clubs_nextroom"
            play sound sfx_open_door_kick
            "sfx_open_door_kick"
            play sound sfx_open_door_mines
            "sfx_open_door_mines"
            play sound sfx_open_door_mines_metal
            "sfx_open_door_mines_metal"
            play sound sfx_open_door_squeak_2
            "sfx_open_door_squeak_2"
            play sound sfx_open_door_strong
            "sfx_open_door_strong"
            play sound sfx_open_drapes
            "sfx_open_drapes"
            play sound sfx_open_journal
            "sfx_open_journal"
            play sound sfx_open_metal_door
            "sfx_open_metal_door"
            play sound sfx_open_metal_hatch
            "sfx_open_metal_hatch"
            play sound sfx_slam_door_campus
            "sfx_slam_door_campus"
            stop sound
            jump sound_my_list_openingClosing_eng
        "Sleepbag unzipping":
            play sound sfx_unzip_sleepbag
            "sfx_unzip_sleepbag"
            stop sound
            jump sound_my_list_openingClosing_eng
        "Table opening":
            play sound sfx_open_table
            "sfx_open_table"
            stop sound
            jump sound_my_list_openingClosing_eng
        "Window opening":
            play sound sfx_open_window
            "sfx_open_window"
            stop sound
            jump sound_my_list_openingClosing_eng
        "<<Back>>":
            jump sound_my_list_eng
label sound_my_list_animalsEnviron_eng:
    menu:
        "Cricket":
            play sound sfx_hell_crickets_1
            "sfx_hell_crickets_1"
            play sound sfx_hell_crickets_2
            "sfx_hell_crickets_2"
            play sound sfx_hell_crickets_3
            "sfx_hell_crickets_3"
            stop sound
            jump sound_my_list_animalsEnviron_eng
        "Owl":
            play sound sfx_owl_far
            "sfx_owl_far"
            stop sound
            jump sound_my_list_animalsEnviron_eng
        "Bush leaves":
            play sound sfx_bush_leaves
            "sfx_bush_leaves"
            stop sound
            jump sound_my_list_animalsEnviron_eng
        "Fireplace in forest":
            play sound sfx_forest_fireplace
            "sfx_forest_fireplace"
            stop sound
            jump sound_my_list_animalsEnviron_eng
        "Gusty wind":
            play sound sfx_gusty_wind
            "sfx_gusty_wind"
            stop sound
            jump sound_my_list_animalsEnviron_eng
        "Run into forest":
            play sound sfx_run_forest
            "sfx_run_forest"
            stop sound
            jump sound_my_list_animalsEnviron_eng
        "Thunder":
            play sound sfx_thunder_crack
            "sfx_thunder_crack"
            play sound sfx_thunder_rumble
            "sfx_thunder_rumble"
            play sound sfx_thunder_wood
            "sfx_thunder_wood"
            stop sound
            jump sound_my_list_animalsEnviron_eng
        "Water":
            play sound sfx_water_emerge
            "sfx_water_emerge"
            play sound sfx_water_sink_stream
            "sfx_water_sink_stream"
            play sound sfx_water_splash
            "sfx_water_splash"
            stop sound
            jump sound_my_list_animalsEnviron_eng
        "Wind gust":
            play sound sfx_wind_gust
            "sfx_wind_gust"
            stop sound
            jump sound_my_list_animalsEnviron_eng
        "Tree branches":
            play sound sfx_tree_branches
            "sfx_tree_branches"
            stop sound
            jump sound_my_list_animalsEnviron_eng
        "<<Back>>":
            jump sound_my_list_eng

label sound_my_list_inWater_eng:
    menu:
        "Rowboat loop":
            play sound sfx_rowboat_loop
            "sfx_rowboat_loop"
            stop sound
            jump sound_my_list_inWater_eng
        "Swimming":
            play sound sfx_swimming
            "sfx_swimming"
            stop sound
            jump sound_my_list_inWater_eng
        "Underwater dive":
            play sound sfx_underwater_dive
            "sfx_underwater_dive"
            stop sound
            jump sound_my_list_inWater_eng
        "Water dive shoulder":
            play sound sfx_shoulder_dive_water
            "sfx_shoulder_dive_water"
            stop sound
            jump sound_my_list_inWater_eng
        "<<Back>>":
            jump sound_my_list_eng
label sound_my_list_movenment_eng:
    menu:
        "Soccer ball":
            play sound sfx_soccer_ball_catch
            "sfx_soccer_ball_catch"
            play sound sfx_soccer_ball_gate
            "sfx_soccer_ball_gate"
            play sound sfx_soccer_ball_kick
            "sfx_soccer_ball_kick"
            stop sound
            jump sound_my_list_movenment_eng
        "Misterty movement":
            play sound sfx_mystery_movement
            "sfx_mystery_movement"
            stop sound
            jump sound_my_list_movenment_eng
        "Pat on shoulder":
            play sound sfx_pat_shoulder_hard
            "sfx_pat_shoulder_hard"
            stop sound
            jump sound_my_list_movenment_eng
        "Punch":
            play sound sfx_punch_medium
            "sfx_punch_medium"
            play sound sfx_punch_washstand
            "sfx_punch_washstand"
            stop sound
            jump sound_my_list_movenment_eng
        "Inhale":
            play sound sfx_inhale
            "sfx_inhale"
            stop sound
            jump sound_my_list_movenment_eng
        "Jump into hole":
            play sound sfx_jump_into_hole_2
            "sfx_jump_into_hole_2"
            stop sound
            jump sound_my_list_movenment_eng
        "Jump over hole":
            play sound sfx_jump_over_hole
            "sfx_jump_over_hole"
            stop sound
            jump sound_my_list_movenment_eng
        "Face slap":
            play sound sfx_face_slap
            "sfx_face_slap"
            stop sound
            jump sound_my_list_movenment_eng
        "Far steps":
            play sound sfx_far_steps
            "sfx_far_steps"
            stop sound
            jump sound_my_list_movenment_eng
        "Applause":
            play sound sfx_concert_applause
            "sfx_concert_applause"
            stop sound
            jump sound_my_list_movenment_eng
        "<<Back>>":
            jump sound_my_list_eng
label sound_my_list_miscSound_eng:
    menu:
        "Achiеvement":
            play sound sfx_achievement
            "sfx_achievement"
            stop sound
            jump sound_my_list_miscSound_eng
        "Blanket":
            play sound sfx_blanket_off_stand
            "sfx_blanket_off_stand"
            stop sound
            jump sound_my_list_miscSound_eng
        "Candle":
            play sound sfx_blow_out_candle
            "sfx_blow_out_candle"
            play sound sfx_light_candle
            "sfx_light_candle"
            play sound sfx_match_candle
            "sfx_match_candle"
            stop sound
            jump sound_my_list_miscSound_eng
        "Broom sweep":
            play sound sfx_broom_sweep
            "sfx_broom_sweep"
            stop sound
            jump sound_my_list_miscSound_eng
        "Click":
            play sound sfx_click_1
            "sfx_click_1"
            play sound sfx_click_2
            "sfx_click_2"
            play sound sfx_click_3
            "sfx_click_3"
            stop sound
            jump sound_my_list_miscSound_eng
        "Door bell":
            play sound sfx_door_bell
            "sfx_door_bell"
            stop sound
            jump sound_my_list_miscSound_eng
        "Ghost children's laughter":
            play sound sfx_ghost_children_laugh
            "sfx_ghost_children_laugh"
            stop sound
            jump sound_my_list_miscSound_eng
        "Head explosion":
            play sound sfx_head_explode
            "sfx_head_explode"
            stop sound
            jump sound_my_list_miscSound_eng
        "Heartbeat":
            play sound sfx_head_heartbeat
            "sfx_head_heartbeat"
            stop sound
            jump sound_my_list_miscSound_eng
        "Torch":
            play sound sfx_ignite_torch
            "sfx_ignite_torch"
            stop sound
            jump sound_my_list_miscSound_eng
        "Muffled explosion":
            play sound sfx_muffled_explosion
            "sfx_muffled_explosion"
            stop sound
            jump sound_my_list_miscSound_eng
        "Scary sting":
            play sound sfx_scary_sting
            "sfx_scary_sting"
            stop sound
            jump sound_my_list_miscSound_eng
        "Suspence bang":
            play sound sfx_suspence_bang
            "sfx_suspence_bang"
            stop sound
            jump sound_my_list_miscSound_eng
        "Terminator":
            play sound sfx_terminator
            "sfx_terminator"
            play sound sfx_terminator_parody
            "sfx_terminator_parody"
            stop sound
            jump sound_my_list_miscSound_eng
        "<<Back>>":
            jump sound_my_list_eng
