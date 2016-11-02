
label background_my_list:
    menu:
        "Автобусная остановка":
            jump background_my_list_bus_stop
        "Медпункт":
            jump background_my_list_aidpost
        "Баня":
            scene bg ext_bathhouse_night
            "bg ext_bathhouse_night"
            scene black
            jump background_my_list
        "Пляж":
            scene bg ext_beach_day
            "bg ext_beach_day"
            scene bg ext_beach_sunset
            "bg ext_beach_sunset"
            scene bg ext_beach_night
            "bg ext_beach_night"
            scene black
            jump background_my_list
        "Автобус":
            jump background_my_list_bus
        "Пристань":
            scene bg ext_boathouse_day
            "bg ext_boathouse_day"
            scene bg ext_boathouse_night
            "bg ext_boathouse_night"
            scene black
            jump background_my_list
        "Вход в лагерь":
            scene bg ext_camp_entrance_day
            "bg ext_camp_entrance_day"
            scene bg ext_camp_entrance_night
            "bg ext_camp_entrance_night"
            scene black
            jump background_my_list
        "Клубы":
            jump background_my_list_clubs
        "Столовая":
            jump background_my_list_dining_hall
#        "Домики персонажей":
#        "Домики":
#        "Остров Ближний":
#        "Комната Семёна":
#        "Сцена":
#        "Библиотека":
#        "Площадь":
#        "Музыкальный клуб":
#        "Лиаз":
#       "Старый корпус":
#        "Путь":
#        "Спортивная площадка":
#        "Поляна":
#       "Дорога":
#       "Умывальники":
#        "Шахта":
#        "Катакомбы":
#        "intro xx":
        ">>Назад<<":
            jump start_my_list
        
label background_my_list_bus_stop:
    menu:
        "Совёнок":
            scene bg ext_no_bus
            "bg ext_no_bus"
            scene bg ext_no_bus_sunset
            "bg ext_no_bus_sunset"
            scene bg ext_no_bus_night
            "bg ext_no_bus_night"
            scene black
            jump background_my_list_bus_stop
        "Город":
            scene bg bus_stop 
            "bg bus_stop"
            scene black
            jump background_my_list_bus_stop
        ">>Назад<<":
            jump background_my_list
    
label background_my_list_aidpost:
    menu:
        "Снаружи":
            jump background_my_list_aidpost_ext
        "Внутри":
            jump background_my_list_aidpost_int
        
        ">>Назад<<":
            jump background_my_list
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
        "Снаружи":
            scene bg ext_bus
            "bg ext_bus"
            scene bg ext_bus_night
            "bg ext_bus_night"
            scene black
            jump background_my_list_bus
        "Внутри":
            scene bg int_bus
            "bg int_bus"
            scene bg int_bus_night
            "bg int_bus_night"
            scene black
            jump background_my_list_bus
        "Люди":
            scene bg int_bus_people_day
            "bg int_bus_people_day"
            scene bg int_bus_people_night
            "bg bg int_bus_people_night"
            scene bg int_bus_black
            "bg int_bus_black"
            scene black
            jump background_my_list_bus
        ">>Назад<<":
            jump background_my_list
            
label background_my_list_clubs:
    menu:
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
            jump background_my_list
            
label background_my_list_clubs_male:
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

label background_my_list_dining_hall:
    menu:
        "Снаружи":
            jump background_my_list_dining_hall_ext
        "Внутри":
            jump background_my_list_dining_hall_int
        ">>Назад<<":
            jump background_my_list
            
label background_my_list_dining_hall_ext:
    menu:
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
        "Пустой":
            scene bg int_dining_hall_day
            "bg int_dining_hall_day"
            scene bg int_dining_hall_sunset
            "bg int_dining_hall_sunset"
            scene bg int_dining_hall_night
            "bg int_dining_hall_night"
            scene black
            jump background_my_list_dining_hall_int
        "Люди":
            scene bg int_dining_hall_people_day
            "bg int_dining_hall_people_day"
            scene black
            jump background_my_list_dining_hall_int
        ">>Назад<<":
            jump background_my_list_dining_hall
            