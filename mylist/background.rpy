label background_my_list:
    menu:
        "Фоны"
        "Лагерные здания":
            jump background_my_list_lz
        "Лагерные окрестности":
            jump background_my_list_lo
        "Автобус":
            jump background_my_list_bus_start
        "Город":
            jump background_my_list_town
        ">>Назад<<":
            jump start_my_list

label background_my_list_town:
    menu:
        "Город"
        "Вид из окна автобуса":
            scene bg intro_xx
            "bg intro_xx"
            scene black
            jump background_my_list_town
        "Комната Семёна":
            jump background_my_list_semen
        "Автобусная остановка":
            scene bg bus_stop
            "bg bus_stop"
            scene black
            jump background_my_list_town
        ">>Назад<<":
            jump background_my_list

label background_my_list_lz:
    menu:
        "Лагерные здания"
        "Медпункт":
            jump background_my_list_aidpost
        "Баня":
            scene bg ext_bathhouse_night
            "bg ext_bathhouse_night"
            scene black
            jump background_my_list_lz
        "Пристань":
            scene bg ext_boathouse_day
            "bg ext_boathouse_day"
            scene bg ext_boathouse_night
            "bg ext_boathouse_night"
            scene black
            jump background_my_list_lz
        "Клубы":
            jump background_my_list_clubs
        "Столовая":
            jump background_my_list_dining_hall
        "Домики персонажей":
            jump background_my_list_pioneers
        "Библиотека":
            jump background_my_list_library
        "Музыкальный клуб":
            jump background_my_list_musclub
        ">>Назад<<":
            jump background_my_list

    label background_my_list_lo:
        menu:
            "Лагерные окрестности"
            "Автобусная остановка":
                scene bg ext_no_bus
                "bg ext_no_bus"
                scene bg ext_no_bus_sunset
                "bg ext_no_bus_sunset"
                scene bg ext_no_bus_night
                "bg ext_no_bus_night"
                scene black
                jump background_my_list_lo
            "Пляж":
                scene bg ext_beach_day
                "bg ext_beach_day"
                scene bg ext_beach_sunset
                "bg ext_beach_sunset"
                scene bg ext_beach_night
                "bg ext_beach_night"
                scene black
                jump background_my_list_lo
            "Вход в лагерь":
                scene bg ext_camp_entrance_day
                "bg ext_camp_entrance_day"
                scene bg ext_camp_entrance_night
                "bg ext_camp_entrance_night"
                scene black
                jump background_my_list_lo
            "Домики":
                jump background_my_list_houses
            "Остров Ближний":
                jump background_my_list_island
            "Сцена":
                jump background_my_list_stage
            "Площадь":
                jump background_my_list_square
            "Старый корпус":
                jump background_my_list_old_building_main
            "Проходы":
                jump background_my_list_path
            "Спортивная площадка":
                jump background_my_list_playground
            "Поляна":
                jump background_my_list_polyana
            "Дорога":
                jump background_my_list_road
            "Умывальники":
                jump background_my_list_washstand
            ">>Назад<<":
                jump background_my_list

label background_my_list_bus_start:
    menu:
        "Автобус"
        "Лагерный автобус":
            jump background_my_list_bus
        "Лиаз":
            scene bg int_liaz
            "bg int_liaz"
            scene black
            jump background_my_list_bus_start
        ">>Назад<<":
            jump background_my_list

label background_my_list_aidpost:
    menu:
        "Медпункт"
        "Снаружи":
            jump background_my_list_aidpost_ext
        "Внутри":
            jump background_my_list_aidpost_int
        ">>Назад<<":
            jump background_my_list_lz

label background_my_list_aidpost_int:
    scene bg int_aidpost_day
    "bg int_aidpost_day"
    scene bg int_aidpost_day_apple
    "bg int_aidpost_day_apple"
    scene bg int_aidpost_night
    "bg int_aidpost_night"
    scene black
    jump background_my_list_aidpost

label background_my_list_aidpost_ext:
    scene bg ext_aidpost_day
    "bg ext_aidpost_day"
    scene bg ext_aidpost_night
    "bg ext_aidpost_night"
    scene black
    jump background_my_list_aidpost

label background_my_list_bus:
    menu:
        "Лагерный автобус"
        "Снаружи":
            scene bg ext_bus
            "bg ext_bus"
            scene bg ext_bus_night
            "bg ext_bus_night"
            scene black
            jump background_my_list_bus
        "Внутри":
            jump background_my_list_bus_int
        ">>Назад<<":
            jump background_my_list
label background_my_list_bus_int:
    menu:
        "Внутри"
        "Пустой":
            scene bg int_bus
            "bg int_bus"
            scene bg int_bus_night
            "bg int_bus_night"
            scene black
            jump background_my_list_bus_int
        "Людный":
            scene bg int_bus_people_day
            "bg int_bus_people_day"
            scene bg int_bus_people_night
            "bg bg int_bus_people_night"
            scene bg int_bus_black
            "bg int_bus_black"
            scene black
            jump background_my_list_bus_int
        ">>Назад<<":
            jump background_my_list_bus

label background_my_list_clubs:
    menu:
        "Клубы"
        "Снаружи":
            scene bg ext_clubs_day
            "bg ext_clubs_day"
            scene bg ext_clubs_night
            "bg ext_clubs_night"
            scene black
            jump background_my_list_clubs
        "Внутри":
            scene bg int_clubs_male_day
            "bg int_clubs_male_day"
            scene bg int_clubs_male_sunset
            "bg int_clubs_male_sunset"
            scene bg int_clubs_male2_night
            "bg int_clubs_male2_night"
            scene bg int_clubs_male2_night_nolight
            "bg int_clubs_male2_night_nolight"
            scene black
            jump background_my_list_clubs
        ">>Назад<<":
            jump background_my_list_lz

label background_my_list_dining_hall:
    menu:
        "Столовая"
        "Снаружи":
            jump background_my_list_dining_hall_ext
        "Внутри":
            jump background_my_list_dining_hall_int
        ">>Назад<<":
            jump background_my_list_lz

label background_my_list_dining_hall_ext:
    menu:
        "Снаружи"
        "Вдали":
            scene bg ext_dining_hall_away_day
            "bg ext_dining_hall_away_day"
            scene bg ext_dining_hall_away_sunset
            "bg ext_dining_hall_away_sunset"
            scene bg ext_dining_hall_away_night
            "bg ext_dining_hall_away_night"
            scene black
            jump background_my_list_dining_hall_ext
        "Вблизи":
            scene bg ext_dining_hall_near_day
            "bg ext_dining_hall_near_day"
            scene bg ext_dining_hall_near_sunset
            "bg ext_dining_hall_near_sunset"
            scene bg ext_dining_hall_near_night
            "bg ext_dining_hall_near_night"
            scene black
            jump background_my_list_dining_hall_ext
        ">>Назад<<":
            jump background_my_list_dining_hall

label background_my_list_dining_hall_int:
    menu:
        "Внутри"
        "Пустая":
            scene bg int_dining_hall_day
            "bg int_dining_hall_day"
            scene bg int_dining_hall_sunset
            "bg int_dining_hall_sunset"
            scene bg int_dining_hall_night
            "bg int_dining_hall_night"
            scene black
            jump background_my_list_dining_hall_int
        "Людная":
            scene bg int_dining_hall_people_day
            "bg int_dining_hall_people_day"
            scene black
            jump background_my_list_dining_hall_int
        ">>Назад<<":
            jump background_my_list_dining_hall

label background_my_list_pioneers:
    menu:
        "Домики персонажей"
        "Домик Слави и Жени":
            jump background_my_list_pioneers_sl
        "Домик Алисы и Ульяны":
            jump background_my_list_pioneers_dv
        "Домик Ольги Дмитриевны":
            jump background_my_list_pioneers_mt
        "Домик Лены и Мику":
            jump background_my_list_pioneers_un
        ">>Назад<<":
            jump background_my_list_lz

label background_my_list_pioneers_sl:
    menu:
        "Домик Слави и Жени"
        "Снаружи":
            scene bg ext_house_of_sl_day
            "bg ext_house_of_sl_day"
            scene black
            jump background_my_list_pioneers_sl
        "Внутри":
            scene bg int_house_of_sl_day
            "bg int_house_of_sl_day"
            scene black
            jump background_my_list_pioneers_sl
        ">>Назад<<":
            jump background_my_list_pioneers

label background_my_list_pioneers_dv:
    menu:
        "Домик Алисы и Ульяны"
        "Снаружи":
            scene bg ext_house_of_dv_day
            "bg ext_house_of_dv_day"
            scene bg ext_house_of_dv_night
            "bg ext_house_of_dv_night"
            scene black
            jump background_my_list_pioneers_dv
        "Внутри":
            scene bg int_house_of_dv_day
            "bg int_house_of_dv_day"
            scene bg int_house_of_dv_night
            "bg int_house_of_dv_night"
            scene black
            jump background_my_list_pioneers_dv
        ">>Назад<<":
            jump background_my_list_pioneers

label background_my_list_pioneers_mt:
    menu:
        "Домик Ольги Дмитриевны"
        "Снаружи":
            scene bg ext_house_of_mt_day
            "bg ext_house_of_mt_day"
            scene bg ext_house_of_mt_sunset
            "bg ext_house_of_mt_sunset"
            scene bg ext_house_of_mt_night
            "bg ext_house_of_mt_night"
            scene bg ext_house_of_mt_night_without_light
            "bg ext_house_of_mt_night_without_light"
            scene black
            jump background_my_list_pioneers_mt
        "Внутри":
            scene bg int_house_of_mt_day
            "bg int_house_of_mt_day"
            scene bg int_house_of_mt_sunset
            "bg int_house_of_mt_sunset"
            scene bg int_house_of_mt_night
            "bg int_house_of_mt_night"
            scene bg int_house_of_mt_night2
            "bg int_house_of_mt_night2"
            scene bg int_house_of_mt_noitem_night
            "bg int_house_of_mt_noitem_night"
            scene black
            jump background_my_list_pioneers_mt
        ">>Назад<<":
            jump background_my_list_pioneers

label background_my_list_pioneers_un:
    menu:
        "Домик Лены и Мику"
        "Снаружи":
            scene bg ext_house_of_un_day
            "bg ext_house_of_un_day"
            scene black
            jump background_my_list_pioneers_un
        "Внутри":
            scene bg int_house_of_un_day
            "bg int_house_of_un_day"
            scene bg int_house_of_un_night
            "bg int_house_of_un_night"
            scene black
            jump background_my_list_pioneers_un
        ">>Назад<<":
            jump background_my_list_pioneers

label background_my_list_houses:
    scene bg ext_houses_day
    "bg ext_houses_day"
    scene bg ext_houses_sunset
    "bg ext_houses_sunset"
    scene black
    jump background_my_list_lo

label background_my_list_island:
    scene bg ext_island_day
    "bg ext_island_day"
    scene bg ext_island_night
    "bg ext_island_night"
    scene black
    jump background_my_list_lo

label background_my_list_semen:
    scene bg semen_room
    "bg semen_room"
    scene bg semen_room_window
    "bg semen_room_window"
    scene black
    jump background_my_list_town

label background_my_list_stage:
    menu:
        "Сцена"
        "Вдали":
            scene bg ext_stage_big_night
            "bg ext_stage_big_night"
            scene black
            jump background_my_list_stage
        "Вблизи":
            scene bg ext_stage_normal_day
            "bg ext_stage_normal_day"
            scene bg ext_stage_normal_night
            "bg ext_stage_normal_night"
            scene black
            jump background_my_list_stage
        ">>Назад<<":
            jump background_my_list_lo

label background_my_list_library:
    menu:
        "Библиотека"
        "Снаружи":
            scene bg ext_library_day
            "bg ext_library_day"
            scene bg ext_library_night
            "bg ext_library_night"
            scene black
            jump background_my_list_library
        "Внутри":
            scene bg int_library_day
            "bg int_library_day"
            scene bg int_library_night
            "bg int_library_night"
            scene bg int_library_night2
            "bg int_library_night2"
            scene black
            jump background_my_list_library
        ">>Назад<<":
            jump background_my_list_lz

label background_my_list_square:
    menu:
        "Площадь"
        "Обычная":
            scene bg ext_square_day
            "bg ext_square_day"
            scene bg ext_square_sunset
            "bg ext_square_sunset"
            scene bg ext_square_night
            "bg ext_square_night"
            scene black
            jump background_my_list_square
        "Дискотека":
            scene bg ext_square_night_party
            "bg ext_square_night_party"
            scene bg ext_square_night_party2
            "bg ext_square_night_party2"
            scene black
            jump background_my_list_square
        "Город":
            scene bg ext_square_day_city
            "bg ext_square_day_city"
            scene black
            jump background_my_list_square
        ">>Назад<<":
            jump background_my_list_lo

label background_my_list_musclub:
    menu:
        "Музыкальный клуб"
        "Снаружи":
            scene bg ext_musclub_day
            "bg ext_musclub_day"
            scene black
            jump background_my_list_musclub
        "Внутри":
            scene bg int_musclub_day
            "bg int_musclub_day"
            scene black
            jump background_my_list_musclub
        ">>Назад<<":
            jump background_my_list_lz

label background_my_list_old_building_main:
    menu:
        "Старый корпус"
        "Здание":
            jump background_my_list_old_building
        "Шахта":
            jump background_my_list_mine
        "Катакомбы":
            jump background_my_list_catacombs
        ">>Назад<<":
            jump background_my_list_lo

label background_my_list_old_building:
    menu:
        "Здание"
        "Снаружи":
            scene bg ext_old_building_night
            "bg ext_old_building_night"
            scene bg ext_old_building_night_moonlight
            "bg ext_old_building_night_moonlight"
            scene black
            jump background_my_list_old_building
        "Внутри":
            scene bg int_old_building_night
            "bg int_old_building_night"
            scene black
            jump background_my_list_old_building
        ">>Назад<<":
            jump background_my_list_old_building_main

label background_my_list_path:
    menu:
        "Проходы"
        "Проход 1":
            scene bg ext_path_day
            "bg ext_path_day"
            scene bg ext_path_sunset
            "bg ext_path_sunset"
            scene bg ext_path_night
            "bg ext_path_night"
            scene black
            jump background_my_list_path
        "Проход 2":
            scene bg ext_path2_day
            "bg ext_path2_day"
            scene bg ext_path2_night
            "bg ext_path2_night"
            scene black
            jump background_my_list_path
        ">>Назад<<":
            jump background_my_list_lo

label background_my_list_playground:
    scene bg ext_playground_day
    "bg ext_playground_day"
    scene bg ext_playground_night
    "bg ext_playground_night"
    scene black
    jump background_my_list_lo

label background_my_list_polyana:
    scene bg ext_polyana_day
    "bg ext_polyana_day"
    scene bg ext_polyana_sunset
    "bg ext_polyana_sunset"
    scene bg ext_polyana_night
    "bg ext_polyana_night"
    scene black
    jump background_my_list_lo

label background_my_list_road:
    scene bg ext_road_day
    "bg ext_road_day"
    scene bg ext_road_sunset
    "bg ext_road_sunset"
    scene bg ext_road_night2
    "bg ext_road_night2"
    scene bg ext_road_night
    "bg ext_road_night"
    scene black
    jump background_my_list_lo

label background_my_list_washstand:
    scene bg ext_washstand_day
    "bg ext_washstand_day"
    scene bg ext_washstand2_day
    "bg ext_washstand2_day"
    scene black
    jump background_my_list_lo

label background_my_list_mine:
    menu:
        "Шахта"
        "Пещера":
            scene bg int_mine_coalface
            "bg int_mine_coalface"
            scene black
            jump background_my_list_mine
        "Шахта":
            scene bg int_mine
            "bg int_mine"
            scene black
            jump background_my_list_mine
        "Перекрёсток":
            scene bg int_mine_crossroad
            "bg int_mine_crossroad"
            scene black
            jump background_my_list_mine
        "Дверь":
            scene bg int_mine_door
            "bg int_mine_door"
            scene black
            jump background_my_list_mine
        "Выход":
            scene bg int_mine_exit_night_light
            "bg int_mine_exit_night_light"
            scene bg int_mine_exit_night_torch
            "bg int_mine_exit_night_torch"
            scene bg int_mine_exit_night_nolight
            "bg int_mine_exit_night_nolight"
            scene black
            jump background_my_list_mine
        "Поворот":
            scene bg int_mine_halt
            "bg int_mine_halt"
            scene black
            jump background_my_list_mine
        "Комната":
            scene bg int_mine_room
            "bg int_mine_room"
            scene bg int_mine_room_red
            "bg int_mine_room_red"
            scene black
            jump background_my_list_mine
        ">>Назад<<":
            jump background_my_list_old_building_main

label background_my_list_catacombs:
    menu:
        "Катакомбы"
        "Комната":
            scene bg int_catacombs_living
            "bg int_catacombs_living"
            scene bg int_catacombs_living_nodoor
            "bg int_catacombs_living_nodoor"
            scene black
            jump background_my_list_catacombs
        "Проход":
            scene bg int_catacombs_entrance
            "bg int_catacombs_entrance"
            scene bg int_catacombs_entrance_red
            "bg int_catacombs_entrance_red"
            scene black
            jump background_my_list_catacombs
        "Дверь":
            scene bg int_catacombs_door
            "bg int_catacombs_door"
            scene black
            jump background_my_list_catacombs
        "Дыра":
            scene bg int_catacombs_hole
            "bg int_catacombs_hole"
            scene black
            jump background_my_list_catacombs
        ">>Назад<<":
            jump background_my_list_old_building_main

#Start og English version

label background_my_list_eng:
    menu:
        "Backgraunds"
        "Camp buildings":
            jump background_my_list_lz_eng
        "Camp surroundings":
            jump background_my_list_lo_eng
        "Bus":
            jump background_my_list_bus_start_eng
        "Town":
            jump background_my_list_town_eng
        ">>Назад<<":
            jump start_my_list_eng

label background_my_list_town_eng:
    menu:
        "Town"
        "View from the bus window":
            scene bg intro_xx
            "bg intro_xx"
            scene black
            jump background_my_list_town_eng
        "Semyon's room":
            jump background_my_list_semen_eng
        "Bus stop":
            scene bg bus_stop
            "bg bus_stop"
            scene black
            jump background_my_list_town_eng
        ">>Back<<":
            jump background_my_list_eng

label background_my_list_lz_eng:
    menu:
        "Camp buildings"
        "Aid post":
            jump background_my_list_aidpost_eng
        "Bathhouse":
            scene bg ext_bathhouse_night
            "bg ext_bathhouse_night"
            scene black
            jump background_my_list_lz_eng
        "Boathouse":
            scene bg ext_boathouse_day
            "bg ext_boathouse_day"
            scene bg ext_boathouse_night
            "bg ext_boathouse_night"
            scene black
            jump background_my_list_lz_eng
        "Clubs":
            jump background_my_list_clubs_eng
        "Dining hall":
            jump background_my_list_dining_hall_eng
        "Pioneer cabins":
            jump background_my_list_pioneers_eng
        "Library":
            jump background_my_list_library_eng
        "Music club":
            jump background_my_list_musclub_eng
        ">>Back<<":
            jump background_my_list_eng

    label background_my_list_lo_eng:
        menu:
            "Camp surroundings"
            "Bus stop":
                scene bg ext_no_bus
                "bg ext_no_bus"
                scene bg ext_no_bus_sunset
                "bg ext_no_bus_sunset"
                scene bg ext_no_bus_night
                "bg ext_no_bus_night"
                scene black
                jump background_my_list_lo_eng
            "Beach":
                scene bg ext_beach_day
                "bg ext_beach_day"
                scene bg ext_beach_sunset
                "bg ext_beach_sunset"
                scene bg ext_beach_night
                "bg ext_beach_night"
                scene black
                jump background_my_list_lo_eng
            "Camp entrance":
                scene bg ext_camp_entrance_day
                "bg ext_camp_entrance_day"
                scene bg ext_camp_entrance_night
                "bg ext_camp_entrance_night"
                scene black
                jump background_my_list_lo_eng
            "Houses":
                jump background_my_list_houses_eng
            "Island":
                jump background_my_list_island_eng
            "Stage":
                jump background_my_list_stage_eng
            "Square":
                jump background_my_list_square_eng
            "Old building":
                jump background_my_list_old_building_main_eng
            "Paths":
                jump background_my_list_path_eng
            "Playground":
                jump background_my_list_playground_eng
            "Meadow":
                jump background_my_list_polyana_eng
            "Road":
                jump background_my_list_road_eng
            "Wash stand":
                jump background_my_list_washstand_eng
            ">>Back<<":
                jump background_my_list_eng

label background_my_list_bus_start_eng:
    menu:
        "Bus"
        "Camp bus":
            jump background_my_list_bus_eng
        "Liaz":
            scene bg int_liaz
            "bg int_liaz"
            scene black
            jump background_my_list_bus_start_eng
        ">>Back<<":
            jump background_my_list_eng

label background_my_list_aidpost_eng:
    menu:
        "Outside":
            jump background_my_list_aidpost_ext_eng
        "Inside":
            jump background_my_list_aidpost_int_eng
        ">>Back<<":
            jump background_my_list_lz_eng

label background_my_list_aidpost_int_eng:
    scene bg int_aidpost_day
    "bg int_aidpost_day"
    scene bg int_aidpost_day_apple
    "bg int_aidpost_day_apple"
    scene bg int_aidpost_night
    "bg int_aidpost_night"
    scene black
    jump background_my_list_aidpost_eng

label background_my_list_aidpost_ext_eng:
    scene bg ext_aidpost_day
    "bg ext_aidpost_day"
    scene bg ext_aidpost_night
    "bg ext_aidpost_night"
    scene black
    jump background_my_list_aidpost_eng

label background_my_list_bus_eng:
    menu:
        "Outside":
            scene bg ext_bus
            "bg ext_bus"
            scene bg ext_bus_night
            "bg ext_bus_night"
            scene black
            jump background_my_list_bus_eng
        "Inside":
            scene bg int_bus
            "bg int_bus"
            scene bg int_bus_night
            "bg int_bus_night"
            scene black
            jump background_my_list_bus_eng
        "With passengers":
            scene bg int_bus_people_day
            "bg int_bus_people_day"
            scene bg int_bus_people_night
            "bg bg int_bus_people_night"
            scene bg int_bus_black
            "bg int_bus_black"
            scene black
            jump background_my_list_bus_eng
        ">>Back<<":
            jump background_my_list_bus_start_eng

label background_my_list_clubs_eng:
    menu:
        "Outside":
            scene bg ext_clubs_day
            "bg ext_clubs_day"
            scene bg ext_clubs_night
            "bg ext_clubs_night"
            scene black
            jump background_my_list_clubs_eng
        "Inside":
            scene bg int_clubs_male_day
            "bg int_clubs_male_day"
            scene bg int_clubs_male_sunset
            "bg int_clubs_male_sunset"
            scene bg int_clubs_male2_night
            "bg int_clubs_male2_night"
            scene bg int_clubs_male2_night_nolight
            "bg int_clubs_male2_night_nolight"
            scene black
            jump background_my_list_clubs_eng
        ">>Back<<":
            jump background_my_list_lz_eng

label background_my_list_dining_hall_eng:
    menu:
        "Outside":
            jump background_my_list_dining_hall_ext_eng
        "Inside":
            jump background_my_list_dining_hall_int_eng
        ">>Back<<":
            jump background_my_list_lz_eng

label background_my_list_dining_hall_ext_eng:
    menu:
        "Away":
            scene bg ext_dining_hall_away_day
            "bg ext_dining_hall_away_day"
            scene bg ext_dining_hall_away_sunset
            "bg ext_dining_hall_away_sunset"
            scene bg ext_dining_hall_away_night
            "bg ext_dining_hall_away_night"
            scene black
            jump background_my_list_dining_hall_ext_eng
        "Near":
            scene bg ext_dining_hall_near_day
            "bg ext_dining_hall_near_day"
            scene bg ext_dining_hall_near_sunset
            "bg ext_dining_hall_near_sunset"
            scene bg ext_dining_hall_near_night
            "bg ext_dining_hall_near_night"
            scene black
            jump background_my_list_dining_hall_ext_eng
        ">>Back<<":
            jump background_my_list_dining_hall_eng

label background_my_list_dining_hall_int_eng:
    menu:
        "Empty":
            scene bg int_dining_hall_day
            "bg int_dining_hall_day"
            scene bg int_dining_hall_sunset
            "bg int_dining_hall_sunset"
            scene bg int_dining_hall_night
            "bg int_dining_hall_night"
            scene black
            jump background_my_list_dining_hall_int_eng
        "People":
            scene bg int_dining_hall_people_day
            "bg int_dining_hall_people_day"
            scene black
            jump background_my_list_dining_hall_int_eng
        ">>Back<<":
            jump background_my_list_dining_hall_eng

label background_my_list_pioneers_eng:
    menu:
        "Slavya and Zheni's cabin":
            jump background_my_list_pioneers_sl_eng
        "Alice and Uliana's cabin":
            jump background_my_list_pioneers_dv_eng
        "Olga Dmitrievna's cabin":
            jump background_my_list_pioneers_mt_eng
        "Lena and Miku's cabin":
            jump background_my_list_pioneers_un_eng
        ">>Back<<":
            jump background_my_list_lz_eng

label background_my_list_pioneers_sl_eng:
    menu:
        "Outside":
            scene bg ext_house_of_sl_day
            "bg ext_house_of_sl_day"
            scene black
            jump background_my_list_pioneers_sl_eng
        "Inside":
            scene bg int_house_of_sl_day
            "bg int_house_of_sl_day"
            scene black
            jump background_my_list_pioneers_sl_eng
        ">>Back<<":
            jump background_my_list_pioneers_eng

label background_my_list_pioneers_dv_eng:
    menu:
        "Outside":
            scene bg ext_house_of_dv_day
            "bg ext_house_of_dv_day"
            scene bg ext_house_of_dv_night
            "bg ext_house_of_dv_night"
            scene black
            jump background_my_list_pioneers_dv_eng
        "Inside":
            scene bg int_house_of_dv_day
            "bg int_house_of_dv_day"
            scene bg int_house_of_dv_night
            "bg int_house_of_dv_night"
            scene black
            jump background_my_list_pioneers_dv_eng
        ">>Back<<":
            jump background_my_list_pioneers_eng

label background_my_list_pioneers_mt_eng:
    menu:
        "Outside":
            scene bg ext_house_of_mt_day
            "bg ext_house_of_mt_day"
            scene bg ext_house_of_mt_sunset
            "bg ext_house_of_mt_sunset"
            scene bg ext_house_of_mt_night
            "bg ext_house_of_mt_night"
            scene bg ext_house_of_mt_night_without_light
            "bg ext_house_of_mt_night_without_light"
            scene black
            jump background_my_list_pioneers_mt_eng
        "Inside":
            scene bg int_house_of_mt_day
            "bg int_house_of_mt_day"
            scene bg int_house_of_mt_sunset
            "bg int_house_of_mt_sunset"
            scene bg int_house_of_mt_night
            "bg int_house_of_mt_night"
            scene bg int_house_of_mt_night2
            "bg int_house_of_mt_night2"
            scene bg int_house_of_mt_noitem_night
            "bg int_house_of_mt_noitem_night"
            scene black
            jump background_my_list_pioneers_mt_eng
        ">>Back<<":
            jump background_my_list_pioneers_eng

label background_my_list_pioneers_un_eng:
    menu:
        "Outside":
            scene bg ext_house_of_un_day
            "bg ext_house_of_un_day"
            scene black
            jump background_my_list_pioneers_un_eng
        "Inside":
            scene bg int_house_of_un_day
            "bg int_house_of_un_day"
            scene bg int_house_of_un_night
            "bg int_house_of_un_night"
            scene black
            jump background_my_list_pioneers_un_eng
        ">>Back<<":
            jump background_my_list_pioneers_eng

label background_my_list_houses_eng:
    scene bg ext_houses_day
    "bg ext_houses_day"
    scene bg ext_houses_sunset
    "bg ext_houses_sunset"
    scene black
    jump background_my_list_lo_eng

label background_my_list_island_eng:
    scene bg ext_island_day
    "bg ext_island_day"
    scene bg ext_island_night
    "bg ext_island_night"
    scene black
    jump background_my_list_lo_eng

label background_my_list_semen_eng:
    scene bg semen_room
    "bg semen_room"
    scene bg semen_room_window
    "bg semen_room_window"
    scene black
    jump background_my_list_town_eng

label background_my_list_stage_eng:
    menu:
        "Away":
            scene bg ext_stage_big_night
            "bg ext_stage_big_night"
            scene black
            jump background_my_list_stage_eng
        "Near":
            scene bg ext_stage_normal_day
            "bg ext_stage_normal_day"
            scene bg ext_stage_normal_night
            "bg ext_stage_normal_night"
            scene black
            jump background_my_list_stage_eng
        ">>Back<<":
            jump background_my_list_lo_eng

label background_my_list_library_eng:
    menu:
        "Outside":
            scene bg ext_library_day
            "bg ext_library_day"
            scene bg ext_library_night
            "bg ext_library_night"
            scene black
            jump background_my_list_library_eng
        "Inside":
            scene bg int_library_day
            "bg int_library_day"
            scene bg int_library_night
            "bg int_library_night"
            scene bg int_library_night2
            "bg int_library_night2"
            scene black
            jump background_my_list_library_eng
        ">>Back<<":
            jump background_my_list_lz_eng

label background_my_list_square_eng:
    menu:
        "Normal":
            scene bg ext_square_day
            "bg ext_square_day"
            scene bg ext_square_sunset
            "bg ext_square_sunset"
            scene bg ext_square_night
            "bg ext_square_night"
            scene black
            jump background_my_list_square_eng
        "Party":
            scene bg ext_square_night_party
            "bg ext_square_night_party"
            scene bg ext_square_night_party2
            "bg ext_square_night_party2"
            scene black
            jump background_my_list_square_eng
        "City":
            scene bg ext_square_day_city
            "bg ext_square_day_city"
            scene black
            jump background_my_list_square_eng
        ">>Back<<":
            jump background_my_list_lo_eng

label background_my_list_musclub_eng:
    menu:
        "Outside":
            scene bg ext_musclub_day
            "bg ext_musclub_day"
            scene black
            jump background_my_list_musclub_eng
        "Inside":
            scene bg int_musclub_day
            "bg int_musclub_day"
            scene black
            jump background_my_list_musclub_eng
        ">>Back<<":
            jump background_my_list_lz_eng

label background_my_list_old_building_main_eng:
    menu:
        "Building":
            jump background_my_list_old_building_eng
        "Mine":
            jump background_my_list_mine_eng
        "Catacombs":
            jump background_my_list_catacombs_eng
        ">>Back<<":
            jump background_my_list_lo_eng

label background_my_list_old_building_eng:
    menu:
        "Outside":
            scene bg ext_old_building_night
            "bg ext_old_building_night"
            scene bg ext_old_building_night_moonlight
            "bg ext_old_building_night_moonlight"
            scene black
            jump background_my_list_old_building_eng
        "Inside":
            scene bg int_old_building_night
            "bg int_old_building_night"
            scene black
            jump background_my_list_old_building_eng
        ">>Back<<":
            jump background_my_list_old_building_main_eng

label background_my_list_path_eng:
    menu:
        "Path 1":
            scene bg ext_path_day
            "bg ext_path_day"
            scene bg ext_path_sunset
            "bg ext_path_sunset"
            scene bg ext_path_night
            "bg ext_path_night"
            scene black
            jump background_my_list_path_eng
        "Path 2":
            scene bg ext_path2_day
            "bg ext_path2_day"
            scene bg ext_path2_night
            "bg ext_path2_night"
            scene black
            jump background_my_list_path_eng
        ">>Back<<":
            jump background_my_list_lo_eng

label background_my_list_playground_eng:
    scene bg ext_playground_day
    "bg ext_playground_day"
    scene bg ext_playground_night
    "bg ext_playground_night"
    scene black
    jump background_my_list_lo_eng

label background_my_list_polyana_eng:
    scene bg ext_polyana_day
    "bg ext_polyana_day"
    scene bg ext_polyana_sunset
    "bg ext_polyana_sunset"
    scene bg ext_polyana_night
    "bg ext_polyana_night"
    scene black
    jump background_my_list_lo_eng

label background_my_list_road_eng:
    scene bg ext_road_day
    "bg ext_road_day"
    scene bg ext_road_sunset
    "bg ext_road_sunset"
    scene bg ext_road_night2
    "bg ext_road_night2"
    scene bg ext_road_night
    "bg ext_road_night"
    scene black
    jump background_my_list_lo_eng

label background_my_list_washstand_eng:
    scene bg ext_washstand_day
    "bg ext_washstand_day"
    scene bg ext_washstand2_day
    "bg ext_washstand2_day"
    scene black
    jump background_my_list_lo_eng

label background_my_list_mine_eng:
    menu:
        "Cave":
            scene bg int_mine_coalface
            "bg int_mine_coalface"
            scene black
            jump background_my_list_mine_eng
        "Mine":
            scene bg int_mine
            "bg int_mine"
            scene black
            jump background_my_list_mine_eng
        "Crossroad":
            scene bg int_mine_crossroad
            "bg int_mine_crossroad"
            scene black
            jump background_my_list_mine_eng
        "Door":
            scene bg int_mine_door
            "bg int_mine_door"
            scene black
            jump background_my_list_mine_eng
        "Exit":
            scene bg int_mine_exit_night_light
            "bg int_mine_exit_night_light"
            scene bg int_mine_exit_night_torch
            "bg int_mine_exit_night_torch"
            scene bg int_mine_exit_night_nolight
            "bg int_mine_exit_night_nolight"
            scene black
            jump background_my_list_mine_eng
        "Turn":
            scene bg int_mine_halt
            "bg int_mine_halt"
            scene black
            jump background_my_list_mine_eng
        "Room":
            scene bg int_mine_room
            "bg int_mine_room"
            scene bg int_mine_room_red
            "bg int_mine_room_red"
            scene black
            jump background_my_list_mine_eng
        ">>Back<<":
            jump background_my_list_old_building_main_eng

label background_my_list_catacombs_eng:
    menu:
        "Room":
            scene bg int_catacombs_living
            "bg int_catacombs_living"
            scene bg int_catacombs_living_nodoor
            "bg int_catacombs_living_nodoor"
            scene black
            jump background_my_list_catacombs_eng
        "Entrance":
            scene bg int_catacombs_entrance
            "bg int_catacombs_entrance"
            scene bg int_catacombs_entrance_red
            "bg int_catacombs_entrance_red"
            scene black
            jump background_my_list_catacombs_eng
        "Door":
            scene bg int_catacombs_door
            "bg int_catacombs_door"
            scene black
            jump background_my_list_catacombs_eng
        "Hole":
            scene bg int_catacombs_hole
            "bg int_catacombs_hole"
            scene black
            jump background_my_list_catacombs_eng
        ">>Back<<":
            jump background_my_list_old_building_main_eng
