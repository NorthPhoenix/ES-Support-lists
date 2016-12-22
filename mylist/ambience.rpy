label ambience_my_list:
    menu:
        "Звуки окружающей среды"
        "Пристань":
            jump ambience_my_list_bs
        "Лагерь":
            jump ambience_my_list_c
        "Вход в лагерь":
            jump ambience_my_list_ce
        "Катакомбы":
            jump ambience_my_list_catac
        "Клубы":
            play ambience ambience_clubs_inside_day fadein 1
            "ambience_clubs_inside_day"
            stop ambience
            jump ambience_my_list
        "Ветер":
            play ambience ambience_cold_wind_loop fadein 1
            "ambience_cold_wind_loop"
            stop ambience
            jump ambience_my_list
        "Сельская местность":
            play ambience ambience_day_countryside_ambience fadein 1
            "ambience_day_countryside_ambience"
            stop ambience
            jump ambience_my_list
        "Столовая":
            jump ambience_my_list_dh
        "Дорога":
            jump ambience_my_list_r
        "Лес":
            jump ambience_my_list_f
        "Кузнечики":
            play ambience ambience_grasshoper_clean fadein 1
            "ambience_grasshoper_clean"
            stop ambience
            jump ambience_my_list
        "Внутри дома":
            jump ambience_my_list_cab
        "Берег озера":
            jump ambience_my_list_ls
        "Библиотека":
            play ambience ambience_library_day fadein 1
            "ambience_library_day"
            stop ambience
            jump ambience_my_list
        "Средняя толпа":
            jump ambience_my_list_crowd
        "Медпункт":
            jump ambience_my_list_med
        "Музыкальный клуб":
            jump ambience_my_list_mc
        "Старый корпус":
            play ambience ambience_old_camp_outside fadein 1
            "ambience_old_camp_outside"
            stop ambience
            jump ambience_my_list
        "Игра в футбол":
            play ambience ambience_soccer_play_background fadein 1
            "ambience_soccer_play_background"
            stop ambience
            jump ambience_my_list
        ">>Назад<<":
            jump start_my_list

label ambience_my_list_bs:
    menu:
        "Пристань"
        "День":
            play ambience ambience_boat_station_day fadein 1
            "ambience_boat_station_day"
            stop ambience
            jump ambience_my_list_bs
        "Ночь":
            play ambience ambience_boat_station_night fadein 1
            "ambience_boat_station_night"
            stop ambience
            jump ambience_my_list_bs
        ">>Назад<<":
            jump ambience_my_list

label ambience_my_list_c:
    menu:
        "Лагерь"
        "День":
            play ambience ambience_camp_center_day fadein 1
            "ambience_camp_center_day"
            stop ambience
            jump ambience_my_list_c
        "Вечер":
            play ambience ambience_camp_center_evening fadein 1
            "ambience_camp_center_evening"
            stop ambience
            jump ambience_my_list_c
        "Ночь":
            play ambience ambience_camp_center_night fadein 1
            "ambience_camp_center_night"
            stop ambience
            jump ambience_my_list_c
        ">>Назад<<":
            jump ambience_my_list

label ambience_my_list_ce:
    menu:
        "Вход в лагерь"
        "День":
            play ambience ambience_camp_entrance_day fadein 1
            "ambience_camp_entrance_day"
            stop ambience
            jump ambience_my_list_ce
        "Людный день":
            play ambience ambience_camp_entrance_day_people fadein 1
            "ambience_camp_entrance_day_people"
            stop ambience
            jump ambience_my_list_ce
        "Вечер":
            play ambience ambience_camp_entrance_evening fadein 1
            "ambience_camp_entrance_evening"
            stop ambience
            jump ambience_my_list_ce
        "Ночь":
            play ambience ambience_camp_entrance_night fadein 1
            "ambience_camp_entrance_night"
            stop ambience
            jump ambience_my_list_ce
        ">>Назад<<":
            jump ambience_my_list

label ambience_my_list_catac:
    menu:
        "Катакомбы"
        "Катакомбы":
            play ambience ambience_catacombs fadein 1
            "ambience_catacombs"
            stop ambience
            jump ambience_my_list_catac
        "Камни":
            play ambience ambience_catacombs_stones fadein 1
            "ambience_catacombs_stones"
            stop ambience
            jump ambience_my_list_catac
        ">>Назад<<":
            jump ambience_my_list

label ambience_my_list_dh:
    menu:
        "Столовая"
        "Пустая":
            play ambience ambience_dining_hall_empty fadein 1
            "ambience_dining_hall_empty"
            stop ambience
            jump ambience_my_list_dh
        "Полная":
            play ambience ambience_dining_hall_full fadein 1
            "ambience_dining_hall_full"
            stop ambience
            jump ambience_my_list_dh
        ">>Назад<<":
            jump ambience_my_list

label ambience_my_list_r:
    menu:
        "Дорога"
        "День":
            play ambience ambience_ext_road_day fadein 1
            "ambience_ext_road_day"
            stop ambience
            jump ambience_my_list_r
        "Вечер":
            play ambience ambience_ext_road_evening fadein 1
            "ambience_ext_road_evening"
            stop ambience
            jump ambience_my_list_r
        "Ночь":
            play ambience ambience_ext_road_night fadein 1
            "ambience_ext_road_night"
            stop ambience
            jump ambience_my_list_r
        ">>Назад<<":
            jump ambience_my_list

label ambience_my_list_f:
    menu:
        "Лес"
        "День":
            play ambience ambience_forest_day fadein 1
            "ambience_forest_day"
            stop ambience
            jump ambience_my_list_f
        "Вечер":
            play ambience ambience_forest_evening fadein 1
            "ambience_forest_evening"
            stop ambience
            jump ambience_my_list_f
        "Ночь":
            play ambience ambience_forest_night fadein 1
            "ambience_forest_night"
            stop ambience
            jump ambience_my_list_f
        ">>Назад<<":
            jump ambience_my_list

label ambience_my_list_cab:
    menu:
        "Внутри дома"
        "День":
            play ambience ambience_int_cabin_day fadein 1
            "ambience_int_cabin_day"
            stop ambience
            jump ambience_my_list_cab
        "Вечер":
            play ambience ambience_int_cabin_evening fadein 1
            "ambience_int_cabin_evening"
            stop ambience
            jump ambience_my_list_cab
        "Ночь":
            play ambience ambience_int_cabin_night fadein 1
            "ambience_int_cabin_night"
            stop ambience
            jump ambience_my_list_cab
        ">>Назад<<":
            jump ambience_my_list

label ambience_my_list_ls:
    menu:
        "Берег озера"
        "День":
            play ambience ambience_lake_shore_day fadein 1
            "ambience_lake_shore_day"
            stop ambience
            jump ambience_my_list_ls
        "Вечер":
            play ambience ambience_lake_shore_evening fadein 1
            "ambience_lake_shore_evening"
            stop ambience
            jump ambience_my_list_ls
        "Ночь":
            play ambience ambience_lake_shore_night fadein 1
            "ambience_lake_shore_night"
            stop ambience
            jump ambience_my_list_ls
        ">>Назад<<":
            jump ambience_my_list

label ambience_my_list_crowd:
    menu:
        "Толпа"
        "В помещении":
            play ambience ambience_medium_crowd_indoors_1 fadein 1
            "ambience_medium_crowd_indoors_1"
            stop ambience
            jump ambience_my_list_crowd
        "На улице":
            play ambience ambience_medium_crowd_outdoors fadein 1
            "ambience_medium_crowd_outdoors"
            stop ambience
            jump ambience_my_list_crowd
        ">>Назад<<":
            jump ambience_my_list

label ambience_my_list_med:
    menu:
        "Медпункт"
        "День":
            play ambience ambience_medstation_inside_day fadein 1
            "ambience_medstation_inside_day"
            stop ambience
            jump ambience_my_list_med
        "Ночь":
            play ambience ambience_medstation_inside_night fadein 1
            "ambience_medstation_inside_night"
            stop ambience
            jump ambience_my_list_med
        ">>Назад<<":
            jump ambience_my_list

label ambience_my_list_mc:
    menu:
        "Музыкальный клуб"
        "День":
            play ambience ambience_music_club_day fadein 1
            "ambience_music_club_day"
            stop ambience
            jump ambience_my_list_mc
        "Ночь":
            play ambience ambience_music_club_night fadein 1
            "ambience_music_club_night"
            stop ambience
            jump ambience_my_list_mc
        ">>Назад<<":
            jump ambience_my_list

#Start of English translation
label ambience_my_list_eng:
    menu:
        "Звуки окружающей среды"
        "Пристань":
            jump ambience_my_list_bs_eng
        "Лагерь":
            jump ambience_my_list_c_eng
        "Вход в лагерь":
            jump ambience_my_list_ce_eng
        "Катакомбы":
            jump ambience_my_list_catac_eng
        "Клубы":
            play ambience ambience_clubs_inside_day fadein 1
            "ambience_clubs_inside_day"
            stop ambience
            jump ambience_my_list_eng
        "Ветер":
            play ambience ambience_cold_wind_loop fadein 1
            "ambience_cold_wind_loop"
            stop ambience
            jump ambience_my_list_eng
        "Сельская местность":
            play ambience ambience_day_countryside_ambience fadein 1
            "ambience_day_countryside_ambience"
            stop ambience
            jump ambience_my_list_eng
        "Столовая":
            jump ambience_my_list_dh_eng
        "Дорога":
            jump ambience_my_list_r_eng
        "Лес":
            jump ambience_my_list_f_eng
        "Кузнечики":
            play ambience ambience_grasshoper_clean fadein 1
            "ambience_grasshoper_clean"
            stop ambience
            jump ambience_my_list_eng
        "Внутри дома":
            jump ambience_my_list_cab_eng
        "Берег озера":
            jump ambience_my_list_ls_eng
        "Библиотека":
            play ambience ambience_library_day fadein 1
            "ambience_library_day"
            stop ambience
            jump ambience_my_list_eng
        "Средняя толпа":
            jump ambience_my_list_crowd_eng
        "Медпункт":
            jump ambience_my_list_med_eng
        "Музыкальный клуб":
            jump ambience_my_list_mc_eng
        "Старый корпус":
            play ambience ambience_old_camp_outside fadein 1
            "ambience_old_camp_outside"
            stop ambience
            jump ambience_my_list_eng
        "Игра в футбол":
            play ambience ambience_soccer_play_background fadein 1
            "ambience_soccer_play_background"
            stop ambience
            jump ambience_my_list_eng
        ">>Back<<":
            jump start_my_list_eng

label ambience_my_list_bs_eng:
    menu:
        "Boat station"
        "Day":
            play ambience ambience_boat_station_day fadein 1
            "ambience_boat_station_day"
            stop ambience
            jump ambience_my_list_bs_eng
        "Night":
            play ambience ambience_boat_station_night fadein 1
            "ambience_boat_station_night"
            stop ambience
            jump ambience_my_list_bs_eng
        ">>Back<<":
            jump ambience_my_list_eng

label ambience_my_list_c_eng:
    menu:
        "Camp"
        "Day":
            play ambience ambience_camp_center_day fadein 1
            "ambience_camp_center_day"
            stop ambience
            jump ambience_my_list_c_eng
        "Evening":
            play ambience ambience_camp_center_evening fadein 1
            "ambience_camp_center_evening"
            stop ambience
            jump ambience_my_list_c_eng
        "Night":
            play ambience ambience_camp_center_night fadein 1
            "ambience_camp_center_night"
            stop ambience
            jump ambience_my_list_c_eng
        ">>Back<<":
            jump ambience_my_list_eng

label ambience_my_list_ce_eng:
    menu:
        "Camp entrance"
        "Day":
            play ambience ambience_camp_entrance_day fadein 1
            "ambience_camp_entrance_day"
            stop ambience
            jump ambience_my_list_ce_eng
        "Crowded day":
            play ambience ambience_camp_entrance_day_people fadein 1
            "ambience_camp_entrance_day_people"
            stop ambience
            jump ambience_my_list_ce_eng
        "Evening":
            play ambience ambience_camp_entrance_evening fadein 1
            "ambience_camp_entrance_evening"
            stop ambience
            jump ambience_my_list_ce_eng
        "Night":
            play ambience ambience_camp_entrance_night fadein 1
            "ambience_camp_entrance_night"
            stop ambience
            jump ambience_my_list_ce_eng
        ">>Back<<":
            jump ambience_my_list_eng

label ambience_my_list_catac_eng:
    menu:
        "Catacombs"
        "Catacombs":
            play ambience ambience_catacombs fadein 1
            "ambience_catacombs"
            stop ambience
            jump ambience_my_list_catac_eng
        "Stones":
            play ambience ambience_catacombs_stones fadein 1
            "ambience_catacombs_stones"
            stop ambience
            jump ambience_my_list_catac_eng
        ">>Back<<":
            jump ambience_my_list_eng

label ambience_my_list_dh_eng:
    menu:
        "Dining hall"
        "Empty":
            play ambience ambience_dining_hall_empty fadein 1
            "ambience_dining_hall_empty"
            stop ambience
            jump ambience_my_list_dh_eng
        "Full":
            play ambience ambience_dining_hall_full fadein 1
            "ambience_dining_hall_full"
            stop ambience
            jump ambience_my_list_dh_eng
        ">>Back<<":
            jump ambience_my_list_eng

label ambience_my_list_r_eng:
    menu:
        "Дорога"
        "Day":
            play ambience ambience_ext_road_day fadein 1
            "ambience_ext_road_day"
            stop ambience
            jump ambience_my_list_r_eng
        "Вечер":
            play ambience ambience_ext_road_evening fadein 1
            "ambience_ext_road_evening"
            stop ambience
            jump ambience_my_list_r_eng
        "Ночь":
            play ambience ambience_ext_road_night fadein 1
            "ambience_ext_road_night"
            stop ambience
            jump ambience_my_list_r_eng
        ">>Back<<":
            jump ambience_my_list_eng

label ambience_my_list_f_eng:
    menu:
        "Лес"
        "Day":
            play ambience ambience_forest_day fadein 1
            "ambience_forest_day"
            stop ambience
            jump ambience_my_list_f_eng
        "Вечер":
            play ambience ambience_forest_evening fadein 1
            "ambience_forest_evening"
            stop ambience
            jump ambience_my_list_f_eng
        "Ночь":
            play ambience ambience_forest_night fadein 1
            "ambience_forest_night"
            stop ambience
            jump ambience_my_list_f_eng
        ">>Back<<":
            jump ambience_my_list_eng

label ambience_my_list_cab_eng:
    menu:
        "Внутри дома"
        "Day":
            play ambience ambience_int_cabin_day fadein 1
            "ambience_int_cabin_day"
            stop ambience
            jump ambience_my_list_cab_eng
        "Вечер":
            play ambience ambience_int_cabin_evening fadein 1
            "ambience_int_cabin_evening"
            stop ambience
            jump ambience_my_list_cab_eng
        "Ночь":
            play ambience ambience_int_cabin_night fadein 1
            "ambience_int_cabin_night"
            stop ambience
            jump ambience_my_list_cab_eng
        ">>Back<<":
            jump ambience_my_list_eng

label ambience_my_list_ls_eng:
    menu:
        "Берег озера"
        "Day":
            play ambience ambience_lake_shore_day fadein 1
            "ambience_lake_shore_day"
            stop ambience
            jump ambience_my_list_ls_eng
        "Evening":
            play ambience ambience_lake_shore_evening fadein 1
            "ambience_lake_shore_evening"
            stop ambience
            jump ambience_my_list_ls_eng
        "Ночь":
            play ambience ambience_lake_shore_night fadein 1
            "ambience_lake_shore_night"
            stop ambience
            jump ambience_my_list_ls_eng
        ">>Back<<":
            jump ambience_my_list_eng

label ambience_my_list_crowd_eng:
    menu:
        "Толпа"
        "В помещении":
            play ambience ambience_medium_crowd_indoors_1 fadein 1
            "ambience_medium_crowd_indoors_1"
            stop ambience
            jump ambience_my_list_crowd_eng
        "На улице":
            play ambience ambience_medium_crowd_outdoors fadein 1
            "ambience_medium_crowd_outdoors"
            stop ambience
            jump ambience_my_list_crowd_eng
        ">>Back<<":
            jump ambience_my_list_eng

label ambience_my_list_med_eng:
    menu:
        "Med. station"
        "Day":
            play ambience ambience_medstation_inside_day fadein 1
            "ambience_medstation_inside_day"
            stop ambience
            jump ambience_my_list_med_eng
        "Night":
            play ambience ambience_medstation_inside_night fadein 1
            "ambience_medstation_inside_night"
            stop ambience
            jump ambience_my_list_med_eng
        ">>Back<<":
            jump ambience_my_list_eng

label ambience_my_list_mc_eng:
    menu:
        "Music club"
        "Day":
            play ambience ambience_music_club_day fadein 1
            "ambience_music_club_day"
            stop ambience
            jump ambience_my_list_mc_eng
        "Night":
            play ambience ambience_music_club_night fadein 1
            "ambience_music_club_night"
            stop ambience
            jump ambience_my_list_mc_eng
        ">>Back<<":
            jump ambience_my_list_eng
