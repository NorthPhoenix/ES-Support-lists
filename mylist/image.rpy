label image_my_list:
    menu:
        "Страница 1"
        "Славя":
            jump image_my_list_sl
        "Лена":
            jump image_my_list_un
        "Алиса":
            jump image_my_list_dv
        "Мику":
            jump image_my_list_mi
        "Ульяна":
            jump image_my_list_us
        "Юля":
            jump image_my_list_uv
        "Семён":
            jump image_my_list_me
        "Еда":
            show cg d1_food_normal
            "cg d1_food_normal"
            show cg d1_food_skolop
            "cg d1_food_skolop"
            hide cg
            jump image_my_list
        "Кузнечик":
            show cg d1_grasshopper
            "cg d1_grasshopper"
            hide cg
            jump image_my_list
        "Рена":
            show cg d1_rena_sunset
            "cg d1_rena_sunset"
            hide cg
            jump image_my_list
        "Линейка":
            show cg d2_lineup
            "cg d2_lineup"
            hide cg
            jump image_my_list
        "Женя":
            show cg d2_micu_lib
            "cg d2_micu_lib"
            hide cg
            jump image_my_list
        "Переодевающаяся Ольга (хентай)" if (persistent.hentai == True):
            show cg d2_mt_undressed
            "cg d2_mt_undressed"
            show cg d2_mt_undressed_2
            "cg d2_mt_undressed_2"
            hide cg
            jump image_my_list
        "Страница 2":
            jump image_my_list2
        "Страница 3":
            jump image_my_list3
        ">>Назад<<":
            jump start_my_list

label image_my_list2:
    menu:
        "Страница 2"
        "Дискотека":
            show cg d3_disco
            "cg d3_disco"
            hide cg
            jump image_my_list2
        "Элестроник":
            show cg d4_el_wash
            "cg d4_el_wash"
            hide cg
            jump image_my_list2
        "Сидящий Шурик":
            show cg d4_sh_sit
            "cg d4_sh_sit"
            hide cg
            jump image_my_list2
        "Шурик с куском арматуры":
            show cg d4_sh_stay
            "cg d4_sh_stay"
            hide cg
            jump image_my_list2
        "В лодке":
            show cg d5_boat
            "cg d5_boat"
            show cg d5_boat_2
            "cg d5_boat_2"
            hide cg
            jump image_my_list2
        "Торт":
            show cg d5_cake
            "cg d5_cake"
            hide cg
            jump image_my_list2
        "Робот":
            show cg d5_clubs_robot
            "cg d5_clubs_robot"
            hide cg
            jump image_my_list2
        "Виола":
            show cg d5_cs
            "cg d5_cs"
            hide cg
            jump image_my_list2
        "Курьёз у умывальников (хентай)" if (persistent.hentai == True):
            show cg d5_dv_us_wash
            "cg d5_dv_us_wash"
            show cg d5_dv_us_wash_2
            "cg d5_dv_us_wash_2"
            show cg d5_dv_us_wash_3
            "cg d5_dv_us_wash_3"
            show cg d5_dv_us_wash_4
            "cg d5_dv_us_wash_4"
            hide cg
            jump image_my_list2
        "Драка":
            show cg d6_dv_fight
            "cg d6_dv_fight"
            show cg d6_dv_fight_2
            "cg d6_dv_fight_2"
            show cg d6_dv_fight_3
            "cg d6_dv_fight_3"
            hide cg
            jump image_my_list2
        "Удар":
            show cg d6_un_punch
            "cg d6_un_punch"
            hide cg
            jump image_my_list2
        "Прощание":
            show cg d7_pioneers_leaving
            "cg d7_pioneers_leaving"
            show cg d7_pioneers_leaving_without_us
            "cg d7_pioneers_leaving_without_us"
            hide cg
            jump image_my_list2
        "Все вместе":
            show cg final_all_2
            "cg final_all_2"
            hide cg
            jump image_my_list2
        "Страница 1":
            jump image_my_list
        "Страница 3":
            jump image_my_list3
        ">>Назад<<":
            jump start_my_list

label image_my_list3:
    menu:
        "Страница 3"
        "Дисклеймер":
            show disclaimer
            "disclaimer"
            hide disclaimer
            jump image_my_list3
        "Soviet Games":
            show soviet_games
            "soviet_games"
            hide soviet_games
            jump image_my_list3
        "Заставка":
            jump image_my_list3_splashscreen
        "Лого":
            show logo_day
            "logo_day"
            hide logo_day
            show logo_sunset
            "logo_sunset"
            hide logo_sunset
            show logo_night
            "logo_night"
            hide logo_night
            jump image_my_list3
        "Иконка":
            show icon_large
            "icon_large"
            hide icon_large
            show icon
            "icon"
            hide icon
            show icon16
            "icon16"
            hide icon16
            jump image_my_list3
        "Достижения":
            show achievement
            "achievement"
            hide achievement
            show achievement3
            "achievement3"
            hide achievement3
            show collector
            "collector"
            hide collector
            show dv_bad
            "dv_bad"
            hide dv_bad
            show dv_good
            "dv_good"
            hide dv_good
            show un_bad
            "un_bad"
            hide un_bad
            show un_good
            "un_good"
            hide un_good
            show sl_bad
            "sl_bad"
            hide sl_bad
            show sl_good
            "sl_good"
            hide sl_good
            show us_bad
            "us_bad"
            hide us_bad
            show us_good
            "us_good"
            hide us_good
            show main_bad
            "main_bad"
            hide main_bad
            show main_good
            "main_good"
            hide main_good
            show mi
            "mi"
            hide mi
            show uv_city
            "uv_city"
            hide uv_city
            show uv_good
            "uv_good"
            hide uv_good
            show void
            "void"
            hide void
            jump image_my_list3
        "Автобус":
            show op_back
            "op_back"
            hide op_back
            show op_sl
            "op_sl"
            hide op_sl
            show op_un
            "op_un"
            hide op_un
            show op_us
            "op_us"
            hide op_us
            show op_dv
            "op_dv"
            hide op_dv
            show op_mi
            "op_mi"
            hide op_mi
            show op_uv1
            "op_uv1"
            hide op_uv1
            show op_uv2
            "op_uv2"
            hide op_uv2
            show op_uv3
            "op_uv3"
            hide op_uv3
            jump image_my_list3
        "Текст":
            show backdrop_text (u"Любой текст"):
                xpos 0.5
                ypos 0.5
            pause
            $ set_mode_nvl()
            "backdrop_text (u\"Любой текст\")\n....xpos 0.5\n....ypos 0.5\n\n(\"....\" - четыре пробела)"
            $ set_mode_adv()
            hide backdrop_text
            jump image_my_list3
        "Карточный турнир":
            show cg lvl_1
            "cg lvl_1"
            show cg lvl_2_lena_win
            "cg lvl_2_lena_win"
            show cg lvl_2_semen_win
            "cg lvl_2_semen_win"
            show cg lvl_4_semen_win
            "cg lvl_4_semen_win"
            hide cg
            jump image_my_list3
        "Страница 1":
            jump image_my_list
        "Страница 2":
            jump image_my_list2
        ">>Назад<<":
            jump start_my_list

label image_my_list3_splashscreen:
    menu:
        "Заставка"
        "День":
            scene splashscreen_day:
                pos (0,0)
                linear 4.0pos (0,-1080)
            pause
            $ set_mode_nvl()
            "scene splashscreen_day:\n....pos (0,0)\n....linear 4.0pos (0,-1080)\n$ renpy.pause(4)\n\n(\"....\" - четыре пробела)"
            $ set_mode_adv()
            scene black
            jump image_my_list3_splashscreen
        "Закат/Восход":
            scene splashscreen_sunset:
                pos (0,0)
                linear 4.0pos (0,-1080)
            pause
            $ set_mode_nvl()
            "scene splashscreen_sunset:\n....pos (0,0)\n....linear 4.0pos (0,-1080)\n\n(\"....\" - четыре пробела)"
            $ set_mode_adv()
            scene black
            jump image_my_list3_splashscreen
        "Ночь":
            scene splashscreen_night:
                pos (0,0)
                linear 4.0pos (0,-1080)
            pause
            $ set_mode_nvl()
            "scene splashscreen_night:\n....pos (0,0)\n....linear 4.0pos (0,-1080)\n\n(\"....\" - четыре пробела)"
            $ set_mode_adv()
            scene black
            jump image_my_list3_splashscreen
        ">>Назад<<":
            jump image_my_list3

label image_my_list_sl:
    menu:
        "Славя"
        "Ужин со Славей":
            show cg d1_sl_dinner
            "cg d1_sl_dinner"
            show cg d1_sl_dinner_0
            "cg d1_sl_dinner_0"
            hide cg
            jump image_my_list_sl
        "В лесу":
            show cg d2_slavya_forest
            "cg d2_slavya_forest"
            show cg d6_sl_forest
            "cg d6_sl_forest"
            show cg d6_sl_forest_2
            "cg d6_sl_forest_2"
            hide cg
            jump image_my_list_sl
        "В бане (хентай)" if (persistent.hentai == True):
            show cg d3_sl_bathhouse
            "cg d3_sl_bathhouse"
            hide cg
            jump image_my_list_sl
        "Танец":
            show cg d3_sl_dance
            "cg d3_sl_dance"
            hide cg
            jump image_my_list_sl
        "Вечер":
            show cg d3_sl_evening
            "cg d3_sl_evening"
            hide cg
            jump image_my_list_sl
        "В библиотеке":
            show cg d3_sl_library
            "cg d3_sl_library"
            hide cg
            jump image_my_list_sl
        "Катакомбы":
            show cg d4_catac_sl
            "cg d4_catac_sl"
            hide cg
            jump image_my_list_sl
        "В медпункте":
            show cg d5_sl_sleep
            "cg d5_sl_sleep"
            show cg d5_sl_sleep_2
            "cg d5_sl_sleep_2"
            hide cg
            jump image_my_list_sl
        "Славя на озере (хентай)" if (persistent.hentai == True):
            show cg d6_sl_swim
            "cg d6_sl_swim"
            show cg d2_sl_swim
            "cg d2_sl_swim"
            hide cg
            jump image_my_list_sl
        "Славя (хентай)" if (persistent.hentai == True):
            show cg d6_sl_hentai_1
            "cg d6_sl_hentai_1"
            show cg d6_sl_hentai_2
            "cg d6_sl_hentai_2"
            hide cg
            jump image_my_list_sl
        "Утро (хентай)" if (persistent.hentai == True):
            show cg d7_sl_morning
            "cg d7_sl_morning"
            show cg d7_sl_morning_2
            "cg d7_sl_morning_2"
            hide cg
            jump image_my_list_sl
        "Эпилог Слави":
            show cg epilogue_uv_sl
            "cg epilogue_uv_sl"
            show cg epilogue_sl
            "cg epilogue_sl"
            show cg epilogue_sl_2
            "cg epilogue_sl_2"
            hide cg
            jump image_my_list_sl
        ">>Назад<<":
            jump image_my_list

label image_my_list_un:
    menu:
        "Лена"
        "Сова":
            show cg d2_sovenok
            "cg d2_sovenok"
            hide cg
            jump image_my_list_un
        "Танец":
            show cg d3_un_dance
            "cg d3_un_dance"
            hide cg
            jump image_my_list_un
        "В лесу":
            show cg d3_un_forest
            "cg d3_un_forest"
            hide cg
            jump image_my_list_un
        "Катакомбы":
            show cg d4_catac_un
            "cg d4_catac_un"
            hide cg
            jump image_my_list_un
        "На острове":
            show cg d5_un_island
            "cg d5_un_island"
            show cg d5_un_sleep
            "cg d5_un_sleep"
            hide cg
            jump image_my_list_un
        "Вечер":
            show cg d6_un_evening_1
            "cg d6_un_evening_1"
            show cg d6_un_evening_2
            "cg d6_un_evening_2"
            hide cg
            jump image_my_list_un
        "Лена (хентай)" if (persistent.hentai == True):
            show cg d7_un_hentai
            "cg d7_un_hentai"
            show cg d7_un_hentai_3
            "cg d7_un_hentai_3"
            hide cg
            jump image_my_list_un
        "Суицид":
            show cg d7_un_suicide :
                pos (0,-360)
                linear 10.0pos (0,0)
            pause
            $ set_mode_nvl()
            "show cg d7_un_suicide:\n....pos (0,-360)\n....linear 10.0pos (0,0)\n\n(\"....\" - четыре пробела)"
            $ set_mode_adv()
            hide cg
            jump image_my_list_un
        "Эпилог Лены":
            show cg epilogue_uv_un
            "cg epilogue_uv_un"
            show cg epilogue_un
            "cg epilogue_un"
            show cg epilogue_un_good
            "cg epilogue_un_good"
            hide cg
            jump image_my_list_un
        ">>Назад<<":
            jump image_my_list

label image_my_list_dv:
    menu:
        "Алиса"
        "Пляж":
            show cg d2_2ch_beach  with dissolve:
                pos (0,-1920)
                linear 10.0pos (0,0)
                linear 2.0pos (0, -250)
            pause
            $ set_mode_nvl()
            "show cg d2_2ch_beach:\n....pos (0,-1920)\n....linear 10.0pos (0,0)\n....linear 2.0pos (0, -250)\n\n(\"....\" - четыре пробела)"
            hide cg
            $ set_mode_adv()
            jump image_my_list_dv
        "На реке":
            show cg d2_water_dan
            "cg d2_water_dan"
            hide cg
            jump image_my_list_dv
        "С электро гитарой":
            show cg d3_dv_guitar
            "cg d3_dv_guitar"
            hide cg
            jump image_my_list_dv
        "На сцене":
            show cg d3_dv_scene_1
            "cg d3_dv_scene_1"
            show cg d3_dv_scene_2
            "cg d3_dv_scene_2"
            hide cg
            jump image_my_list_dv
        "Катакомбы":
            show cg d4_catac_dv
            "cg d4_catac_dv"
            hide cg
            jump image_my_list_dv
        "Виновна":
            show cg d4_dv_mt
            "cg d4_dv_mt"
            hide cg
            jump image_my_list_dv
        "Спор с Алисой":
            show cg d5_dv_argue
            "cg d5_dv_argue"
            show cg d5_dv_argue_2
            "cg d5_dv_argue_2"
            show cg d5_dv_argue_3
            "cg d5_dv_argue_3"
            hide cg
            jump image_my_list_dv
        "В лесу":
            show cg d5_dv_island
            "cg d5_dv_island"
            hide cg
            jump image_my_list_dv
        "Алиса (хентай)" if (persistent.hentai == True):
            show cg d6_dv_hentai
            "cg d6_dv_hentai"
            show cg d6_dv_hentai_2
            "cg d6_dv_hentai_2"
            hide cg
            jump image_my_list_dv
        "Привал":
            show cg d7_dv
            "cg d7_dv"
            show cg d7_dv_2
            "cg d7_dv_2"
            hide cg
            jump image_my_list_dv
        "Эпилог Алисы":
            show cg epilogue_uv_dv
            "cg epilogue_uv_dv"
            show cg epilogue_dv_2
            "cg epilogue_dv_2"
            show cg epilogue_dv_3
            "cg epilogue_dv_3"
            hide cg
            jump image_my_list_dv
        ">>Назад<<":
            jump image_my_list

label image_my_list_mi:
    menu:
        "Мику"
        "Мику под пианино":
            show cg d2_miku_piano
            "cg d2_miku_piano"
            show cg d2_miku_piano2
            "cg d2_miku_piano2"
            hide cg
            jump image_my_list_mi
        "Мику с гитарой":
            show cg d4_mi_guitar
            "cg d4_mi_guitar"
            hide cg
            jump image_my_list_mi
        "Поющая Мику":
            show cg d4_mi_sing
            "cg d4_mi_sing"
            hide cg
            jump image_my_list_mi
        "Мику":
            show cg d5_mi
            "cg d5_mi"
            hide cg
            jump image_my_list_mi
        "Эпилог Мику":
            show cg epilogue_uv_mi
            "cg epilogue_uv_mi"
            show cg epilogue_mi_1
            "cg epilogue_mi_1"
            show cg epilogue_mi_2
            "cg epilogue_mi_2"
            show cg epilogue_mi_3
            "cg epilogue_mi_3"
            show cg epilogue_mi_4
            "cg epilogue_mi_4"
            show cg epilogue_mi_5
            "cg epilogue_mi_5"
            show cg epilogue_mi_6
            "cg epilogue_mi_6"
            show cg epilogue_mi_7
            "cg epilogue_mi_7"
            show cg epilogue_mi_8
            "cg epilogue_mi_8"
            show cg epilogue_mi_9
            "cg epilogue_mi_9"
            hide cg
            jump image_my_list_mi
        "Мику (хентай)" if (persistent.hentai == True):
            show cg miku_h_1_cenz
            "cg miku_h_1_cenz"
            show cg miku_h_2_cenz
            "cg miku_h_2_cenz"
            hide cg
            jump image_my_list_mi
        ">>Назад<<":
            jump image_my_list

label image_my_list_us:
    menu:
        "Ульяна"
        "Падающая Ульяна":
            show cg d2_ussr_falling
            "cg d2_ussr_falling"
            hide cg
            jump image_my_list_us
        "Футбол":
            show cg d3_soccer
            "cg d3_soccer"
            hide cg
            jump image_my_list_us
        "Ульяна в столовой":
            show cg d3_us_dinner
            "cg d3_us_dinner"
            hide cg
            jump image_my_list_us
        "Ульяна в библиотеке":
            show cg d3_us_library_1
            "cg d3_us_library_1"
            show cg d3_us_library_2
            "cg d3_us_library_2"
            show cg d3_us_library_3
            "cg d3_us_library_3"
            show cg d3_us_library_4
            "cg d3_us_library_4"
            show cg d4_us_morning
            "cg d4_us_morning"
            show cg day4_us_morning
            "cg day4_us_morning"
            show cg d6_us_night_2
            "cg d6_us_night_2"
            show cg d5_us_sit
            "cg d5_us_sit"
            hide cg
            jump image_my_list_us
        "Фильм":
            show cg d6_us_film
            "cg d6_us_film"
            hide cg
            jump image_my_list_us
        "Ульяна в лесу":
            show cg d3_ussr_catched
            "cg d3_ussr_catched"
            hide cg
            jump image_my_list_us
        "Катакомбы":
            show cg d4_catac_us
            "cg d4_catac_us"
            show cg d4_catac_us_2
            "cg d4_catac_us_2"
            hide cg
            jump image_my_list_us
        "Рак":
            show cg d4_us_cancer
            "cg d4_us_cancer"
            hide cg
            jump image_my_list_us
        "Ульяна с проволокой":
            show cg d5_sh_us
            "cg d5_sh_us"
            hide cg
            jump image_my_list_us
        "Ульяна-призрак":
            show cg d5_us_ghost
            "cg d5_us_ghost"
            show cg d5_us_ghost_2
            "cg d5_us_ghost_2"
            hide cg
            jump image_my_list_us
        "Поцелуй от Ульяны":
            show cg d5_us_kiss
            "cg d5_us_kiss"
            hide cg
            jump image_my_list_us
        "Эпилог Ульяны":
            show cg epilogue_uv_us
            "cg epilogue_uv_us"
            show cg epilogue_us
            "cg epilogue_us"
            show cg epilogue_us_3_a
            "cg epilogue_us_3_a"
            show cg epilogue_us_alone
            "cg epilogue_us_alone"
            hide cg
            jump image_my_list_us
        ">>Назад<<":
            jump image_my_list

label image_my_list_uv:
    menu:
        "Юля"
        "Незнакомка":
            show cg d1_uv
            "cg d1_uv"
            show cg d1_uv_2
            "cg d1_uv_2"
            hide cg
            jump image_my_list_uv
        "День 4":
            show cg d4_uv_1
            "cg d4_uv_1"
            show cg d4_uv
            "cg d4_uv"
            hide cg
            jump image_my_list_uv
        "День 5":
            show cg d5_uv
            "cg d5_uv"
            show cg d5_uv_2
            "cg d5_uv_2"
            hide cg
            jump image_my_list_uv
        "День 6":
            show cg d6_uv
            "cg d6_uv"
            show cg d6_uv_2
            "cg d6_uv_2"
            hide cg
            jump image_my_list_uv
        "День 7":
            show cg d7_uv
            "cg d7_uv"
            hide cg
            jump image_my_list_uv
        "Эпилог Юли":
            show cg epilogue_uv_2
            "cg epilogue_uv_2"
            show cg epilogue_uv_uv
            "cg epilogue_uv_uv"
            hide cg
            jump image_my_list_uv
        "Юля (хентай)" if (persistent.hentai == True):
            show cg uvao_h_cenz
            "cg uvao_h_cenz"
            hide cg
            jump image_my_list_uv
        ">>Назад<<":
            jump image_my_list

label image_my_list_me:
    menu:
        "Семён"
        "Эпилог":
            show cg epilogue_uv
            "cg epilogue_uv"
            show cg epilogue_un_bad
            "cg epilogue_un_bad"
            hide cg
            jump image_my_list_me
        "Семён в зеркале":
            show cg d2_mirror
            "cg d2_mirror"
            hide cg
            jump image_my_list_me
        "Катакомбы":
            show cg d4_catac
            "cg d4_catac"
            hide cg
            jump image_my_list_me
        "Клубничный кошмар":
            show cg d5_strawberry_race
            "cg d5_strawberry_race"
            hide cg
            jump image_my_list_me
        "Пионер":
            show cg d6_pioneer
            "cg d6_pioneer"
            hide cg
            jump image_my_list_me
        ">>Назад<<":
            jump image_my_list


#Start of English translation
label image_my_list_eng:
    menu:
        "Page 1"
        "Slavya":
            jump image_my_list_sl_eng
        "Lena":
            jump image_my_list_un_eng
        "Alisa":
            jump image_my_list_dv_eng
        "Miku":
            jump image_my_list_mi_eng
        "Ulyana":
            jump image_my_list_us_eng
        "Yulya":
            jump image_my_list_uv_eng
        "Semyon":
            jump image_my_list_me_eng
        "Food":
            show cg d1_food_normal
            "cg d1_food_normal"
            show cg d1_food_skolop
            "cg d1_food_skolop"
            hide cg
            jump image_my_list_eng
        "Grasshoopers":
            show cg d1_grasshopper
            "cg d1_grasshopper"
            hide cg
            jump image_my_list_eng
        "Rena":
            show cg d1_rena_sunset
            "cg d1_rena_sunset"
            hide cg
            jump image_my_list_eng
        "Lineup":
            show cg d2_lineup
            "cg d2_lineup"
            hide cg
            jump image_my_list_eng
        "Zhenya":
            show cg d2_micu_lib
            "cg d2_micu_lib"
            hide cg
            jump image_my_list_eng
        "Undressed Olga (hentai)" if (persistent.hentai == True):
            show cg d2_mt_undressed
            "cg d2_mt_undressed"
            show cg d2_mt_undressed_2
            "cg d2_mt_undressed_2"
            hide cg
            jump image_my_list_eng
        "Page 2":
            jump image_my_list2_eng
        "Page 3":
            jump image_my_list3_eng
        ">>Back<<":
            jump start_my_list_eng

label image_my_list2_eng:
    menu:
        "Page 2"
        "Disco":
            show cg d3_disco
            "cg d3_disco"
            hide cg
            jump image_my_list2_eng
        "Elektronik":
            show cg d4_el_wash
            "cg d4_el_wash"
            hide cg
            jump image_my_list2_eng
        "Shurik sits":
            show cg d4_sh_sit
            "cg d4_sh_sit"
            hide cg
            jump image_my_list2_eng
        "Shurik with armature":
            show cg d4_sh_stay
            "cg d4_sh_stay"
            hide cg
            jump image_my_list2_eng
        "In boat":
            show cg d5_boat
            "cg d5_boat"
            show cg d5_boat_2
            "cg d5_boat_2"
            hide cg
            jump image_my_list2_eng
        "Cake":
            show cg d5_cake
            "cg d5_cake"
            hide cg
            jump image_my_list2_eng
        "Robot":
            show cg d5_clubs_robot
            "cg d5_clubs_robot"
            hide cg
            jump image_my_list2_eng
        "Viola":
            show cg d5_cs
            "cg d5_cs"
            hide cg
            jump image_my_list2_eng
        "Case near to washstand (hentai)" if (persistent.hentai == True):
            show cg d5_dv_us_wash
            "cg d5_dv_us_wash"
            show cg d5_dv_us_wash_2
            "cg d5_dv_us_wash_2"
            show cg d5_dv_us_wash_3
            "cg d5_dv_us_wash_3"
            show cg d5_dv_us_wash_4
            "cg d5_dv_us_wash_4"
            hide cg
            jump image_my_list2_eng
        "Fight":
            show cg d6_dv_fight
            "cg d6_dv_fight"
            show cg d6_dv_fight_2
            "cg d6_dv_fight_2"
            show cg d6_dv_fight_3
            "cg d6_dv_fight_3"
            hide cg
            jump image_my_list2_eng
        "Punch":
            show cg d6_un_punch
            "cg d6_un_punch"
            hide cg
            jump image_my_list2_eng
        "Pioneers leaving":
            show cg d7_pioneers_leaving
            "cg d7_pioneers_leaving"
            show cg d7_pioneers_leaving_without_us
            "cg d7_pioneers_leaving_without_us"
            hide cg
            jump image_my_list2_eng
        "Together":
            show cg final_all_2
            "cg final_all_2"
            hide cg
            jump image_my_list2_eng
        "Page 1":
            jump image_my_list_eng
        "Page 3":
            jump image_my_list3_eng
        ">>Back<<":
            jump start_my_list_eng

label image_my_list3_eng:
    menu:
        "Page 3"
        "Disclaimer":
            show disclaimer
            "disclaimer"
            hide disclaimer
            jump image_my_list3_eng
        "Soviet Games":
            show soviet_games
            "soviet_games"
            hide soviet_games
            jump image_my_list3_eng
        "Splashscreen":
            show splashscreen_day
            "splashscreen_day"
            hide splashscreen_day
            show splashscreen_sunset
            "splashscreen_sunset"
            hide splashscreen_sunset
            show splashscreen_night
            "splashscreen_night"
            hide splashscreen_night
            jump image_my_list3_eng
        "Logo":
            show logo_day
            "logo_day"
            hide logo_day
            show logo_sunset
            "logo_sunset"
            hide logo_sunset
            show logo_night
            "logo_night"
            hide logo_night
            jump image_my_list3_eng
        "Achievement":
            show achievement
            "achievement"
            hide achievement
            show achievement3
            "achievement3"
            hide achievement3
            show dv_bad
            "dv_bad"
            hide dv_bad
            show dv_good
            "dv_good"
            hide dv_good
            show un_bad
            "un_bad"
            hide un_bad
            show un_good
            "un_good"
            hide un_good
            show sl_bad
            "sl_bad"
            hide sl_bad
            show sl_good
            "sl_good"
            hide sl_good
            show us_bad
            "us_bad"
            hide us_bad
            show us_good
            "us_good"
            hide us_good
            show main_bad
            "main_bad"
            hide main_bad
            show main_good
            "main_good"
            hide main_good
            show mi
            "mi"
            hide mi
            show uv_city
            "uv_city"
            hide uv_city
            jump image_my_list3_eng
        "Bus":
            show op_back
            "op_back"
            hide op_back
            show op_sl
            "op_sl"
            hide op_sl
            show op_un
            "op_un"
            hide op_un
            show op_us
            "op_us"
            hide op_us
            show op_dv
            "op_dv"
            hide op_dv
            show op_mi
            "op_mi"
            hide op_mi
            show op_uv1
            "op_uv1"
            hide op_uv1
            show op_uv2
            "op_uv2"
            hide op_uv2
            show op_uv3
            "op_uv3"
            hide op_uv3
            jump image_my_list3_eng
        "Text":
            show backdrop_text (u"Любой текст")
            "backdrop_text (u\"Любой текст\",параметры...)"
            hide backdrop_text
            jump image_my_list3_eng
        "Cards tournament":
            show cg lvl_1
            "cg lvl_1"
            show cg lvl_2_lena_win
            "cg lvl_2_lena_win"
            show cg lvl_2_semen_win
            "cg lvl_2_semen_win"
            show cg lvl_4_semen_win
            "cg lvl_4_semen_win"
            hide cg
            jump image_my_list3_eng
        "Page 1":
            jump image_my_list_eng
        "Page 2":
            jump image_my_list2_eng
        ">>Back<<":
            jump start_my_list_eng

label image_my_list_sl_eng:
    menu:
        "Slavya"
        "Dinner":
            show cg d1_sl_dinner
            "cg d1_sl_dinner"
            show cg d1_sl_dinner_0
            "cg d1_sl_dinner_0"
            hide cg
            jump image_my_list_sl_eng
        "In the forest":
            show cg d2_slavya_forest
            "cg d2_slavya_forest"
            show cg d6_sl_forest
            "cg d6_sl_forest"
            show cg d6_sl_forest_2
            "cg d6_sl_forest_2"
            hide cg
            jump image_my_list_sl_eng
        "In bathhouse (hentai)" if (persistent.hentai == True):
            show cg d3_sl_bathhouse
            "cg d3_sl_bathhouse"
            hide cg
            jump image_my_list_sl_eng
        "Dance":
            show cg d3_sl_dance
            "cg d3_sl_dance"
            hide cg
            jump image_my_list_sl_eng
        "Evening":
            show cg d3_sl_evening
            "cg d3_sl_evening"
            hide cg
            jump image_my_list_sl_eng
        "In the library":
            show cg d3_sl_library
            "cg d3_sl_library"
            hide cg
            jump image_my_list_sl_eng
        "Catacombs":
            show cg d4_catac_sl
            "cg d4_catac_sl"
            hide cg
            jump image_my_list_sl_eng
        "In the aid post":
            show cg d5_sl_sleep
            "cg d5_sl_sleep"
            show cg d5_sl_sleep_2
            "cg d5_sl_sleep_2"
            hide cg
            jump image_my_list_sl_eng
        "Slavya in the lake (hentai)" if (persistent.hentai == True):
            show cg d6_sl_swim
            "cg d6_sl_swim"
            show cg d2_sl_swim
            "cg d2_sl_swim"
            hide cg
            jump image_my_list_sl_eng
        "Slavya (hentai)" if (persistent.hentai == True):
            show cg d6_sl_hentai_1
            "cg d6_sl_hentai_1"
            show cg d6_sl_hentai_2
            "cg d6_sl_hentai_2"
            hide cg
            jump image_my_list_sl_eng
        "Morning (hentai)" if (persistent.hentai == True):
            show cg d7_sl_morning
            "cg d7_sl_morning"
            show cg d7_sl_morning_2
            "cg d7_sl_morning_2"
            hide cg
            jump image_my_list_sl_eng
        "Slavya's epilogue":
            show cg epilogue_uv_sl
            "cg epilogue_uv_sl"
            show cg epilogue_sl
            "cg epilogue_sl"
            show cg epilogue_sl_2
            "cg epilogue_sl_2"
            hide cg
            jump image_my_list_sl_eng
        ">>Back<<":
            jump image_my_list_eng

label image_my_list_un_eng:
    menu:
        "Lena"
        "Owl":
            show cg d2_sovenok
            "cg d2_sovenok"
            hide cg
            jump image_my_list_un_eng
        "Dance":
            show cg d3_un_dance
            "cg d3_un_dance"
            hide cg
            jump image_my_list_un_eng
        "In the forest":
            show cg d3_un_forest
            "cg d3_un_forest"
            hide cg
            jump image_my_list_un_eng
        "Catacombs":
            show cg d4_catac_un
            "cg d4_catac_un"
            hide cg
            jump image_my_list_un_eng
        "On the island":
            show cg d5_un_island
            "cg d5_un_island"
            show cg d5_un_sleep
            "cg d5_un_sleep"
            hide cg
            jump image_my_list_un_eng
        "Evening":
            show cg d6_un_evening_1
            "cg d6_un_evening_1"
            show cg d6_un_evening_2
            "cg d6_un_evening_2"
            hide cg
            jump image_my_list_un_eng
        "Lena (hentai)" if (persistent.hentai == True):
            show cg d7_un_hentai
            "cg d7_un_hentai"
            show cg d7_un_hentai_3
            "cg d7_un_hentai_3"
            hide cg
            jump image_my_list_un_eng
        "Suicide":
            show cg d7_un_suicide
            "cg d7_un_suicide"
            hide cg
            jump image_my_list_un_eng
        "Lena's epilogue":
            show cg epilogue_uv_un
            "cg epilogue_uv_un"
            show cg epilogue_un
            "cg epilogue_un"
            show cg epilogue_un_good
            "cg epilogue_un_good"
            hide cg
            jump image_my_list_un_eng
        ">>Back<<":
            jump image_my_list_eng

label image_my_list_dv_eng:
    menu:
        "Alisa"
        "Beach":
            show cg d2_2ch_beach
            "cg d2_2ch_beach"
            hide cg
            jump image_my_list_dv_eng
        "In the water":
            show cg d2_water_dan
            "cg d2_water_dan"
            hide cg
            jump image_my_list_dv_eng
        "Electric guitar":
            show cg d3_dv_guitar
            "cg d3_dv_guitar"
            hide cg
            jump image_my_list_dv_eng
        "Scene":
            show cg d3_dv_scene_1
            "cg d3_dv_scene_1"
            show cg d3_dv_scene_2
            "cg d3_dv_scene_2"
            hide cg
            jump image_my_list_dv_eng
        "Catacombs":
            show cg d4_catac_dv
            "cg d4_catac_dv"
            hide cg
            jump image_my_list_dv_eng
        "Guilty":
            show cg d4_dv_mt
            "cg d4_dv_mt"
            hide cg
            jump image_my_list_dv_eng
        "Argue":
            show cg d5_dv_argue
            "cg d5_dv_argue"
            show cg d5_dv_argue_2
            "cg d5_dv_argue_2"
            show cg d5_dv_argue_3
            "cg d5_dv_argue_3"
            hide cg
            jump image_my_list_dv_eng
        "In the forest":
            show cg d5_dv_island
            "cg d5_dv_island"
            hide cg
            jump image_my_list_dv
        "Alisa (hentai)" if (persistent.hentai == True):
            show cg d6_dv_hentai
            "cg d6_dv_hentai"
            show cg d6_dv_hentai_2
            "cg d6_dv_hentai_2"
            hide cg
            jump image_my_list_dv_eng
        "Halt":
            show cg d7_dv
            "cg d7_dv"
            show cg d7_dv_2
            "cg d7_dv_2"
            hide cg
            jump image_my_list_dv_eng
        "Alisa's epilogue":
            show cg epilogue_uv_dv
            "cg epilogue_uv_dv"
            show cg epilogue_dv_2
            "cg epilogue_dv_2"
            show cg epilogue_dv_3
            "cg epilogue_dv_3"
            hide cg
            jump image_my_list_dv_eng
        ">>Back<<":
            jump image_my_list_eng

label image_my_list_mi_eng:
    menu:
        "Miku"
        "Miku under the piano":
            show cg d2_miku_piano
            "cg d2_miku_piano"
            show cg d2_miku_piano2
            "cg d2_miku_piano2"
            hide cg
            jump image_my_list_mi_eng
        "Miku with guitar":
            show cg d4_mi_guitar
            "cg d4_mi_guitar"
            hide cg
            jump image_my_list_mi_eng
        "Singing Miku":
            show cg d4_mi_sing
            "cg d4_mi_sing"
            hide cg
            jump image_my_list_mi_eng
        "Miku":
            show cg d5_mi
            "cg d5_mi"
            hide cg
            jump image_my_list_mi_eng
        "Miku's epilogue":
            show cg epilogue_uv_mi
            "cg epilogue_uv_mi"
            show cg epilogue_mi_1
            "cg epilogue_mi_1"
            show cg epilogue_mi_2
            "cg epilogue_mi_2"
            show cg epilogue_mi_3
            "cg epilogue_mi_3"
            show cg epilogue_mi_4
            "cg epilogue_mi_4"
            show cg epilogue_mi_5
            "cg epilogue_mi_5"
            show cg epilogue_mi_6
            "cg epilogue_mi_6"
            show cg epilogue_mi_7
            "cg epilogue_mi_7"
            show cg epilogue_mi_8
            "cg epilogue_mi_8"
            show cg epilogue_mi_9
            "cg epilogue_mi_9"
            hide cg
            jump image_my_list_mi_eng
        "Miku (hentai)" if (persistent.hentai == True):
            show cg miku_h_1_cenz
            "cg miku_h_1_cenz"
            show cg miku_h_2_cenz
            "cg miku_h_2_cenz"
            hide cg
            jump image_my_list_mi_eng
        ">>Back<<":
            jump image_my_list_eng

label image_my_list_us_eng:
    menu:
        "Ulyana"
        "Falling Ulyana":
            show cg d2_ussr_falling
            "cg d2_ussr_falling"
            hide cg
            jump image_my_list_us_eng
        "Soccer":
            show cg d3_soccer
            "cg d3_soccer"
            hide cg
            jump image_my_list_us_eng
        "Ulyana in dining room":
            show cg d3_us_dinner
            "cg d3_us_dinner"
            hide cg
            jump image_my_list_us_eng
        "Ulyana in the library":
            show cg d3_us_library_1
            "cg d3_us_library_1"
            show cg d3_us_library_2
            "cg d3_us_library_2"
            show cg d3_us_library_3
            "cg d3_us_library_3"
            show cg d3_us_library_4
            "cg d3_us_library_4"
            show cg d4_us_morning
            "cg d4_us_morning"
            show cg day4_us_morning
            "cg day4_us_morning"
            show cg d6_us_night_2
            "cg d6_us_night_2"
            show cg d5_us_sit
            "cg d5_us_sit"
            hide cg
            jump image_my_list_us_eng
        "Film":
            show cg d6_us_film
            "cg d6_us_film"
            hide cg
            jump image_my_list_us_eng
        "Ulyana in the forest":
            show cg d3_ussr_catched
            "cg d3_ussr_catched"
            hide cg
            jump image_my_list_us_eng
        "Catacombs":
            show cg d4_catac_us
            "cg d4_catac_us"
            show cg d4_catac_us_2
            "cg d4_catac_us_2"
            hide cg
            jump image_my_list_us_eng
        "Cancer":
            show cg d4_us_cancer
            "cg d4_us_cancer"
            hide cg
            jump image_my_list_us_eng
        "Ulyana с проволокой":
            show cg d5_sh_us
            "cg d5_sh_us"
            hide cg
            jump image_my_list_us_eng
        "Ulyana-gost":
            show cg d5_us_ghost
            "cg d5_us_ghost"
            show cg d5_us_ghost_2
            "cg d5_us_ghost_2"
            hide cg
            jump image_my_list_us_eng
        "Ulyana's kiss":
            show cg d5_us_kiss
            "cg d5_us_kiss"
            hide cg
            jump image_my_list_us_eng
        "Ulyana's epilogue":
            show cg epilogue_uv_us
            "cg epilogue_uv_us"
            show cg epilogue_us
            "cg epilogue_us"
            show cg epilogue_us_3_a
            "cg epilogue_us_3_a"
            show cg epilogue_us_alone
            "cg epilogue_us_alone"
            hide cg
            jump image_my_list_us_eng
        ">>Back<<":
            jump image_my_list_eng

label image_my_list_uv_eng:
    menu:
        "Yulya"
        "Stranger":
            show cg d1_uv
            "cg d1_uv"
            show cg d1_uv_2
            "cg d1_uv_2"
            hide cg
            jump image_my_list_uv_eng
        "Day 4":
            show cg d4_uv_1
            "cg d4_uv_1"
            show cg d4_uv
            "cg d4_uv"
            hide cg
            jump image_my_list_uv_eng
        "Day 5":
            show cg d5_uv
            "cg d5_uv"
            show cg d5_uv_2
            "cg d5_uv_2"
            hide cg
            jump image_my_list_uv_eng
        "Day 6":
            show cg d6_uv
            "cg d6_uv"
            show cg d6_uv_2
            "cg d6_uv_2"
            hide cg
            jump image_my_list_uv_eng
        "Day 7":
            show cg d7_uv
            "cg d7_uv"
            hide cg
            jump image_my_list_uv_eng
        "Yulya's epilogue":
            show cg epilogue_uv_2
            "cg epilogue_uv_2"
            show cg epilogue_uv_uv
            "cg epilogue_uv_uv"
            hide cg
            jump image_my_list_uv_eng
        "Yulya (hentai)" if (persistent.hentai == True):
            show cg uvao_h_cenz
            "cg uvao_h_cenz"
            hide cg
            jump image_my_list_uv_eng
        ">>Back<<":
            jump image_my_list_eng

label image_my_list_me_eng:
    menu:
        "Semyon"
        "Epilogue":
            show cg epilogue_uv
            "cg epilogue_uv"
            show cg epilogue_un_bad
            "cg epilogue_un_bad"
            hide cg
            jump image_my_list_me_eng
        "Semyon in the mirror":
            show cg d2_mirror
            "cg d2_mirror"
            hide cg
            jump image_my_list_me_eng
        "Catacombs":
            show cg d4_catac
            "cg d4_catac"
            hide cg
            jump image_my_list_me_eng
        "Strawberry race":
            show cg d5_strawberry_race
            "cg d5_strawberry_race"
            hide cg
            jump image_my_list_me_eng
        "Pioneer":
            show cg d6_pioneer
            "cg d6_pioneer"
            hide cg
            jump image_my_list_me_eng
        ">>Back<<":
            jump image_my_list_eng
