init:

    $ mods["my_list"]=u"How to make a mod: Support list for modders"

    $ ss = Character(u'Саманта', color="#c8ffc8", what_color="E2C778", drop_shadow = [ (-1, -1), (1, -1), (-1, 1), (1, 1) ], drop_shadow_color = "#000")

    $ ca = Character(u'Samantha', color="#c8ffc8", what_color="E2C778", drop_shadow = [ (-1, -1), (1, -1), (-1, 1), (1, 1) ], drop_shadow_color = "#000")

    image names = "mods/mylist/image/names.jpg"

label my_list:
    if _preferences.language == None:
        jump my_list_ru
    else:
        jump my_list_eng
label my_list_ru:
    scene black
    show ss smile casual with dissolve
    ss "Привет, я тебя ждала."
    show ss grin_smile casual with dspr
    ss "Меня зовут Саманта.{w} И я здесь, что бы показать тебе все возможные спрайты, бэкграунды, картинки, музыку, эмбриенты и конечно же звуки."
    show ss grin casual with dspr
    ss "Что ж, давай посмотрим."
label start_my_list_ru:
    scene black
    menu:
        "Спрайты":
            jump sprites_my_list
        "Бэкграунды":
            jump background_my_list
        "Картинки":
            jump image_my_list
        "Анимации":
            jump exit
        "Музыка":
            jump music_my_list
        "Звуки":
            jump exit
        "Эмбиенты":
            jump exit
        ">>Выход<<":
            jump exit

label exit:
    show ss surprise casual with dspr
    ss "Ты правда хочешь выйти?"
    hide ss with dspr
    menu:
        "Да, хочу":
            show ss sad casual with dissolve
            ss "Хорошо..."
            $ renpy.pause (1)
            show ss serious casual with dspr
            ss "Только возвращайся поскорее!"
            return
        "Нет":
            show ss smile casual with dspr
            $ renpy.pause (1)
            hide ss with dissolve
            jump start_my_list_ru

label sprites_my_list:
    menu:
        "Алиса":
            jump sprites_my_list_dv
        "Славя":
            jump sprites_my_list_sl
        "Лена":
            jump sprites_my_list_un
        "Мику":
            jump sprites_my_list_mi
        "Ульяна":
            jump sprites_my_list_us
        "Ольга Дмитриевна":
            jump sprites_my_list_mt
        "Юля":
            jump sprites_my_list_uv
        "Женя":
            jump sprites_my_list_mz
        "Виола":
            jump sprites_my_list_cs
        "Электроник":
            jump sprites_my_list_el
        "Шурик":
            jump sprites_my_list_sh
        "Пионер":
            jump sprites_my_list_pi
        "Саманта":
            show ss sad casual with dspr
            ss "Меня нет в спрайтах {i}Бесконечного Лета.{/i}"
            show ss normal casual with dspr
            ss "Но ты можешь дабавить меня в свой мод самостоятельно."
            show ss laugh casual with dspr
            ss "Вот мои спрайты."
            hide ss with dspr
            jump sprites_my_list_ss
        ">>Назад<<":
            show ss serious casual with dspr
            ss "Уже налюбовался?"
            jump start_my_list

label sprites_my_list_ss:
    menu:
        "Обычная":
            jump sprites_my_list_ss_casual
        "С хвостиками":
            jump sprites_my_list_ss_fancy
        ">>Назад<<":
            jump sprites_my_list

label sprites_my_list_ss_casual:
    menu:
        "Грустная":
            show ss sad casual with dspr
            "(имя переменной) sad casual"
            hide ss sad casual with dspr
            jump sprites_my_list_ss_casual
        "Испуганная":
            show ss scared casual with dspr
            "(имя переменной) scared casual"
            hide ss scared casual with dspr
            jump sprites_my_list_ss_casual
        "Плачущая(1)":
            show ss cry casual with dspr
            "(имя переменной) cry casual"
            hide ss with dspr
            jump sprites_my_list_ss_casual
        "Плачущая(2)":
            show ss cry2 casual with dspr
            "(имя переменной) cry2 casual"
            hide ss cry2 casual with dspr
            jump sprites_my_list_ss_casual
        "Стесняущаяся(1)":
            show ss shy casual with dspr
            "(имя переменной) shy casual"
            hide ss shy casual with dspr
            jump sprites_my_list_ss_casual
        "Стесняущаяся(2)":
            show ss shy2 casual with dspr
            "(имя переменной) shy2 casual"
            hide ss shy2 casual with dspr
            jump sprites_my_list_ss_casual
        "Неулыбающаяся":
            show ss nosmile casual with dspr
            "(имя переменной) nosmile casual"
            hide ss with dspr
            jump sprites_my_list_ss_casual
        "Улыбка сквозь слёзы(1)":
            show ss crysmile casual with dspr
            "(имя переменной) crysmile casual"
            hide ss with dspr
            jump sprites_my_list_ss_casual
        "Улыбка сквозь слёзы(2)":
            show ss crysmile2 casual with dspr
            "(имя переменной) crysmile2 casual"
            hide ss with dspr
            jump sprites_my_list_ss_casual
        "Обычная":
            show ss normal casual with dspr
            "(имя переменной) normal casual"
            hide ss with dspr
            jump sprites_my_list_ss_casual
        "Неуверенная":
            show ss unsure casual with dspr
            "(имя переменной) unsure casual"
            hide ss with dspr
            jump sprites_my_list_ss_casual
        "Удивлённая":
            show ss surprise casual with dspr
            "(имя переменной) surprise casual"
            hide ss with dspr
            jump sprites_my_list_ss_casual
        "Усмешка":
            show ss grin_smile casual with dspr
            "(имя переменной) grin casual"
            hide ss with dspr
            jump sprites_my_list_ss_casual
        "Усмешка с подмигиванием":
            show ss grin casual with dspr
            "(имя переменной) grin casual"
            hide ss with dspr
            jump sprites_my_list_ss_casual
        "Смех":
            show ss laugh casual with dspr
            "(имя переменной) laugh casual"
            hide ss with dspr
            jump sprites_my_list_ss_casual
        "Улыбка(1)":
            show ss smile casual with dspr
            "(имя переменной) smile casual"
            hide ss with dspr
            jump sprites_my_list_ss_casual
        "Улыбка(2)":
            show ss smile2 casual with dspr
            "(имя переменной) smile2 casual"
            hide ss with dspr
            jump sprites_my_list_ss_casual
        "Злость":
            show ss vangry casual with dspr
            "(имя переменной) vangry casual"
            hide ss with dspr
            jump sprites_my_list_ss_casual
        "Хмурая":
            show ss angry casual with dspr
            "(имя переменной) angry casual"
            hide ss with dspr
            jump sprites_my_list_ss_casual
        "Серьёзная":
            show ss serious casual with dspr
            "(имя переменной) serious casual"
            hide ss with dspr
            jump sprites_my_list_ss_casual
        ">>Назад<<":
            jump sprites_my_list_ss

label sprites_my_list_ss_fancy:
    menu:
        "Грустная":
            show ss sad fancy with dspr
            "(имя переменной) sad fancy"
            hide ss sad fancy with dspr
            jump sprites_my_list_ss_fancy
        "Испуганная":
            show ss scared fancy with dspr
            "(имя переменной) scared fancy"
            hide ss scared fancy with dspr
            jump sprites_my_list_ss_fancy
        "Плачущая(1)":
            show ss cry fancy with dspr
            "(имя переменной) cry fancy"
            hide ss with dspr
            jump sprites_my_list_ss_fancy
        "Плачущая(2)":
            show ss cry2 fancy with dspr
            "(имя переменной) cry2 fancy"
            hide ss cry2 fancy with dspr
            jump sprites_my_list_ss_fancy
        "Стесняущаяся(1)":
            show ss shy fancy with dspr
            "(имя переменной) shy fancy"
            hide ss shy fancy with dspr
            jump sprites_my_list_ss_fancy
        "Стесняущаяся(2)":
            show ss shy2 fancy with dspr
            "(имя переменной) shy2 fancy"
            hide ss shy2 fancy with dspr
            jump sprites_my_list_ss_fancy
        "Неулыбающаяся":
            show ss nosmile fancy with dspr
            "(имя переменной) nosmile fancy"
            hide ss with dspr
            jump sprites_my_list_ss_fancy
        "Улыбка сквозь слёзы(1)":
            show ss crysmile fancy with dspr
            "(имя переменной) crysmile fancy"
            hide ss with dspr
            jump sprites_my_list_ss_fancy
        "Улыбка сквозь слёзы(2)":
            show ss crysmile2 fancy with dspr
            "(имя переменной) crysmile2 fancy"
            hide ss with dspr
            jump sprites_my_list_ss_fancy
        "Обычная":
            show ss normal fancy with dspr
            "(имя переменной) normal fancy"
            hide ss with dspr
            jump sprites_my_list_ss_fancy
        "Неуверенная":
            show ss unsure fancy with dspr
            "(имя переменной) unsure fancy"
            hide ss with dspr
            jump sprites_my_list_ss_fancy
        "Удивлённая":
            show ss surprise fancy with dspr
            "(имя переменной) surprise fancy"
            hide ss with dspr
            jump sprites_my_list_ss_fancy
        "Усмешка":
            show ss grin_smile fancy with dspr
            "(имя переменной) grin fancy"
            hide ss with dspr
            jump sprites_my_list_ss_fancy
        "Усмешка с подмигиванием":
            show ss grin fancy with dspr
            "(имя переменной) grin fancy"
            hide ss with dspr
            jump sprites_my_list_ss_fancy
        "Смех":
            show ss laugh fancy with dspr
            "(имя переменной) laugh fancy"
            hide ss with dspr
            jump sprites_my_list_ss_fancy
        "Улыбка(1)":
            show ss smile fancy with dspr
            "(имя переменной) smile fancy"
            hide ss with dspr
            jump sprites_my_list_ss_fancy
        "Улыбка(2)":
            show ss smile2 fancy with dspr
            "(имя переменной) smile2 fancy"
            hide ss with dspr
            jump sprites_my_list_ss_fancy
        "Злость":
            show ss vangry fancy with dspr
            "(имя переменной) vangry fancy"
            hide ss with dspr
            jump sprites_my_list_ss_fancy
        "Хмурая":
            show ss angry fancy with dspr
            "(имя переменной) angry fancy"
            hide ss with dspr
            jump sprites_my_list_ss_fancy
        "Серьёзная":
            show ss serious fancy with dspr
            "(имя переменной) serious fancy"
            hide ss with dspr
            jump sprites_my_list_ss_fancy
        ">>Назад<<":
            jump sprites_my_list_ss

label sprites_my_list_dv:
    menu:
        "Пионерская форма":
            jump sprites_my_list_dv_pioneer
        "Пионерская форма с узлом":
            jump sprites_my_list_dv_pioneer2
        "Купальник":
            jump sprites_my_list_dv_swim
        "Голая" if (persistent.hentai == True):
            jump sprites_my_list_dv_extra
        ">>Назад<<":
            jump sprites_my_list

label sprites_my_list_dv_pioneer:
    menu:
        "Хмурая":
            show dv angry pioneer far with dspr
            "dv angry pioneer far"
            show dv angry pioneer with dspr
            "dv angry pioneer"
            show dv angry pioneer close with dspr
            "dv angry pioneer close"
            hide dv with dspr
            jump sprites_my_list_dv_pioneer
        "Плачущая":
            show dv cry pioneer far with dspr
            "dv cry pioneer far"
            show dv cry pioneer with dspr
            "dv cry pioneer"
            show dv cry pioneer close with dspr
            "dv cry pioneer close"
            hide dv with dspr
            jump sprites_my_list_dv_pioneer
        "Усмешка":
            show dv grin pioneer far with dspr
            "dv grin pioneer far"
            show dv grin pioneer with dspr
            "dv grin pioneer"
            show dv grin pioneer close with dspr
            "dv grin pioneer close"
            hide dv with dspr
            jump sprites_my_list_dv_pioneer
        "Виноватая":
            show dv guilty pioneer far with dspr
            "dv guilty pioneer far"
            show dv guilty pioneer with dspr
            "dv guilty pioneer"
            show dv guilty pioneer close with dspr
            "dv guilty pioneer close"
            hide dv with dspr
            jump sprites_my_list_dv_pioneer
        "Смех":
            show dv laugh pioneer far with dspr
            "dv laugh pioneer far"
            show dv laugh pioneer with dspr
            "dv laugh pioneer"
            show dv laugh pioneer close with dspr
            "dv laugh pioneer close"
            hide dv with dspr
            jump sprites_my_list_dv_pioneer
        "Обычная":
            show dv normal pioneer far with dspr
            "dv normal pioneer far"
            show dv normal pioneer with dspr
            "dv normal pioneer"
            show dv normal pioneer close with dspr
            "dv normal pioneer close"
            hide dv with dspr
            jump sprites_my_list_dv_pioneer
        "Злость":
            show dv rage pioneer far with dspr
            "dv rage pioneer far"
            show dv rage pioneer with dspr
            "dv rage pioneer"
            show dv rage pioneer close with dspr
            "dv rage pioneer close"
            hide dv with dspr
            jump sprites_my_list_dv_pioneer
        "Испуганная":
            show dv scared pioneer far with dspr
            "dv scared pioneer far"
            show dv scared pioneer with dspr
            "dv scared pioneer"
            show dv scared pioneer close with dspr
            "dv scared pioneer close"
            hide dv with dspr
            jump sprites_my_list_dv_pioneer
        "Грустная":
            show dv sad pioneer far with dspr
            "dv sad pioneer far"
            show dv sad pioneer with dspr
            "dv sad pioneer"
            show dv sad pioneer close with dspr
            "dv sad pioneer close"
            hide dv with dspr
            jump sprites_my_list_dv_pioneer
        "Шокированная":
            show dv shocked pioneer far with dspr
            "dv shocked pioneer far"
            show dv shocked pioneer with dspr
            "dv shocked pioneer"
            show dv shocked pioneer close with dspr
            "dv shocked pioneer close"
            hide dv with dspr
            jump sprites_my_list_dv_pioneer
        "Стесняущаяся":
            show dv shy pioneer far with dspr
            "dv shy pioneer far"
            show dv shy pioneer with dspr
            "dv shy pioneer"
            show dv shy pioneer close with dspr
            "dv shy pioneer close"
            hide dv with dspr
            jump sprites_my_list_dv_pioneer
        "Улыбка":
            show dv smile pioneer far with dspr
            "dv smile pioneer far"
            show dv smile pioneer with dspr
            "dv smile pioneer"
            show dv smile pioneer close with dspr
            "dv smile pioneer close"
            hide dv with dspr
            jump sprites_my_list_dv_pioneer
        "Удивлённая":
            show dv surprise pioneer far with dspr
            "dv surprise pioneer far"
            show dv surprise pioneer with dspr
            "dv surprise pioneer"
            show dv surprise pioneer close with dspr
            "dv surprise pioneer close"
            hide dv with dspr
            jump sprites_my_list_dv_pioneer
        ">>Назад<<":
            jump sprites_my_list_dv

label sprites_my_list_dv_pioneer2:
    menu:
        "Хмурая":
            show dv angry pioneer2 far with dspr
            "dv angry pioneer2 far"
            show dv angry pioneer2 with dspr
            "dv angry pioneer2"
            show dv angry pioneer2 close with dspr
            "dv angry pioneer2 close"
            hide dv with dspr
            jump sprites_my_list_dv_pioneer2
        "Плачущая":
            show dv cry pioneer2 far with dspr
            "dv cry pioneer2 far"
            show dv cry pioneer2 with dspr
            "dv cry pioneer2"
            show dv cry pioneer2 close with dspr
            "dv cry pioneer2 close"
            hide dv with dspr
            jump sprites_my_list_dv_pioneer2
        "Усмешка":
            show dv grin pioneer2 far with dspr
            "dv grin pioneer2 far"
            show dv grin pioneer2 with dspr
            "dv grin pioneer2"
            show dv grin pioneer2 close with dspr
            "dv grin pioneer2 close"
            hide dv with dspr
            jump sprites_my_list_dv_pioneer2
        "Виноватая":
            show dv guilty pioneer2 far with dspr
            "dv guilty pioneer2 far"
            show dv guilty pioneer2 with dspr
            "dv guilty pioneer2"
            show dv guilty pioneer2 close with dspr
            "dv guilty pioneer2 close"
            hide dv with dspr
            jump sprites_my_list_dv_pioneer2
        "Смех":
            show dv laugh pioneer2 far with dspr
            "dv laugh pioneer2 far"
            show dv laugh pioneer2 with dspr
            "dv laugh pioneer2"
            show dv laugh pioneer2 close with dspr
            "dv laugh pioneer2 close"
            hide dv with dspr
            jump sprites_my_list_dv_pioneer2
        "Обычная":
            show dv normal pioneer2 far with dspr
            "dv normal pioneer2 far"
            show dv normal pioneer2 with dspr
            "dv normal pioneer2"
            show dv normal pioneer2 close with dspr
            "dv normal pioneer2 close"
            hide dv with dspr
            jump sprites_my_list_dv_pioneer2
        "Злость":
            show dv rage pioneer2 far with dspr
            "dv rage pioneer2 far"
            show dv rage pioneer2 with dspr
            "dv rage pioneer2"
            show dv rage pioneer2 close with dspr
            "dv rage pioneer2 close"
            hide dv with dspr
            jump sprites_my_list_dv_pioneer2
        "Испуганная":
            show dv scared pioneer2 far with dspr
            "dv scared pioneer2 far"
            show dv scared pioneer2 with dspr
            "dv scared pioneer2"
            show dv scared pioneer2 close with dspr
            "dv scared pioneer2 close"
            hide dv with dspr
            jump sprites_my_list_dv_pioneer2
        "Грустная":
            show dv sad pioneer2 far with dspr
            "dv sad pioneer2 far"
            show dv sad pioneer2 with dspr
            "dv sad pioneer2"
            show dv sad pioneer2 close with dspr
            "dv sad pioneer2 close"
            hide dv with dspr
            jump sprites_my_list_dv_pioneer2
        "Шокированная":
            show dv shocked pioneer2 far with dspr
            "dv shocked pioneer2 far"
            show dv shocked pioneer2 with dspr
            "dv shocked pioneer2"
            show dv shocked pioneer2 close with dspr
            "dv shocked pioneer2 close"
            hide dv with dspr
            jump sprites_my_list_dv_pioneer2
        "Стесняущаяся":
            show dv shy pioneer2 far with dspr
            "dv shy pioneer2 far"
            show dv shy pioneer2 with dspr
            "dv shy pioneer2"
            show dv shy pioneer2 close with dspr
            "dv shy pioneer2 close"
            hide dv with dspr
            jump sprites_my_list_dv_pioneer2
        "Улыбка":
            show dv smile pioneer2 far with dspr
            "dv smile pioneer2 far"
            show dv smile pioneer2 with dspr
            "dv smile pioneer2"
            show dv smile pioneer2 close with dspr
            "dv smile pioneer2 close"
            hide dv with dspr
            jump sprites_my_list_dv_pioneer2
        "Удивлённая":
            show dv surprise pioneer2 far with dspr
            "dv surprise pioneer2 far"
            show dv surprise pioneer2 with dspr
            "dv surprise pioneer2"
            show dv surprise pioneer2 close with dspr
            "dv surprise pioneer2 close"
            hide dv with dspr
            jump sprites_my_list_dv_pioneer2
        ">>Назад<<":
            jump sprites_my_list_dv

label sprites_my_list_dv_swim:
        menu:
            "Плачущая":
                show dv cry swim far with dspr
                "dv cry swim far"
                show dv cry swim with dspr
                "dv cry swim"
                show dv cry swim close with dspr
                "dv cry swim close"
                hide dv with dspr
                jump sprites_my_list_dv_swim
            "Усмешка":
                show dv grin swim far with dspr
                "dv grin swim far"
                show dv grin swim with dspr
                "dv grin swim"
                show dv grin swim close with dspr
                "dv grin swim close"
                hide dv with dspr
                jump sprites_my_list_dv_swim
            "Смех":
                show dv laugh swim far with dspr
                "dv laugh swim far"
                show dv laugh swim with dspr
                "dv laugh swim"
                show dv laugh swim close with dspr
                "dv laugh swim close"
                hide dv with dspr
                jump sprites_my_list_dv_swim
            "Обычная":
                show dv normal swim far with dspr
                "dv normal swim far"
                show dv normal swim with dspr
                "dv normal swim"
                show dv normal swim close with dspr
                "dv normal swim close"
                hide dv with dspr
                jump sprites_my_list_dv_swim
            "Испуганная":
                show dv scared swim far with dspr
                "dv scared swim far"
                show dv scared swim with dspr
                "dv scared swim"
                show dv scared swim close with dspr
                "dv scared swim close"
                hide dv with dspr
                jump sprites_my_list_dv_swim
            "Шокированная":
                show dv shocked swim far with dspr
                "dv shocked swim far"
                show dv shocked swim with dspr
                "dv shocked swim"
                show dv shocked swim close with dspr
                "dv shocked swim close"
                hide dv with dspr
                jump sprites_my_list_dv_swim
            "Улыбка":
                show dv smile swim far with dspr
                "dv smile swim far"
                show dv smile swim with dspr
                "dv smile swim"
                show dv smile swim close with dspr
                "dv smile swim close"
                hide dv with dspr
                jump sprites_my_list_dv_swim
            "Удивлённая":
                show dv surprise swim far with dspr
                "dv surprise swim far"
                show dv surprise swim with dspr
                "dv surprise swim"
                show dv surprise swim close with dspr
                "dv surprise swim close"
                hide dv with dspr
                jump sprites_my_list_dv_swim
            ">>Назад<<":
                jump sprites_my_list_dv

label sprites_my_list_sl:
   menu:
        "Пионерская форма":
            jump sprites_my_list_sl_pioneer
        "Платье":
            jump sprites_my_list_sl_dress
        "Споривная форма":
            jump sprites_my_list_sl_sport
        "Купальник":
            jump sprites_my_list_sl_swim
        ">>Назад<<":
            jump sprites_my_list

label sprites_my_list_sl_pioneer:
    menu:
        "Злость":
            show sl angry pioneer far with dspr
            "sl angry pioneer far"
            show sl angry pioneer with dspr
            "sl angry pioneer"
            show sl angry pioneer close with dspr
            "sl angry pioneer close"
            hide sl with dspr
            jump sprites_my_list_sl_pioneer
        "Счастье":
            show sl happy pioneer far with dspr
            "sl happy pioneer far"
            show sl happy pioneer with dspr
            "sl happy pioneer"
            show sl happy pioneer close with dspr
            "sl happy pioneer close"
            hide sl with dspr
            jump sprites_my_list_sl_pioneer
        "Смех":
            show sl laugh pioneer far with dspr
            "sl laugh pioneer far"
            show sl laugh pioneer with dspr
            "sl laugh pioneer"
            show sl laugh pioneer close with dspr
            "sl laugh pioneer close"
            hide sl with dspr
            jump sprites_my_list_sl_pioneer
        "Обычная":
            show sl normal pioneer far with dspr
            "sl normal pioneer far"
            show sl normal pioneer with dspr
            "sl normal pioneer"
            show sl normal pioneer close with dspr
            "sl normal pioneer close"
            hide sl with dspr
            jump sprites_my_list_sl_pioneer
        "Грустная":
            show sl sad pioneer far with dspr
            "sl sad pioneer far"
            show sl sad pioneer with dspr
            "sl sad pioneer"
            show sl sad pioneer close with dspr
            "sl sad pioneer close"
            hide sl with dspr
            jump sprites_my_list_sl_pioneer
        "Испуганная":
            show sl scared pioneer far with dspr
            "sl scared pioneer far"
            show sl scared pioneer with dspr
            "sl scared pioneer"
            show sl scared pioneer close with dspr
            "sl scared pioneer close"
            hide sl with dspr
            jump sprites_my_list_sl_pioneer
        "Серьёзная":
            show sl serious pioneer far with dspr
            "sl serious pioneer far"
            show sl serious pioneer with dspr
            "sl serious pioneer"
            show sl serious pioneer close with dspr
            "sl serious pioneer close"
            hide sl with dspr
            jump sprites_my_list_sl_pioneer
        "Стесняущаяся":
            show sl shy pioneer far with dspr
            "sl shy pioneer far"
            show sl shy pioneer with dspr
            "sl shy pioneer"
            show sl shy pioneer close with dspr
            "sl shy pioneer close"
            hide sl with dspr
            jump sprites_my_list_sl_pioneer
        "Улыбка":
            show sl smile pioneer far with dspr
            "sl smile pioneer far"
            show sl smile pioneer with dspr
            "sl smile pioneer"
            show sl smile pioneer close with dspr
            "sl smile pioneer close"
            hide sl with dspr
            jump sprites_my_list_sl_pioneer
        "Улыбка(2)":
            show sl smile2 pioneer far with dspr
            "sl smile2 pioneer far"
            show sl smile2 pioneer with dspr
            "sl smile2 pioneer"
            show sl smile2 pioneer close with dspr
            "sl smile2 pioneer close"
            hide sl with dspr
            jump sprites_my_list_sl_pioneer
        "Удивлённая":
            show sl surprise pioneer far with dspr
            "sl surprise pioneer far"
            show sl surprise pioneer with dspr
            "sl surprise pioneer"
            show sl surprise pioneer close with dspr
            "sl surprise pioneer close"
            hide sl with dspr
            jump sprites_my_list_sl_pioneer
        "Нежность":
            show sl tender pioneer far with dspr
            "sl tender pioneer far"
            show sl tender pioneer with dspr
            "sl tender pioneer"
            show sl tender pioneer close with dspr
            "sl tender pioneer close"
            hide sl with dspr
            jump sprites_my_list_sl_pioneer
        ">>Назад<<":
            jump sprites_my_list_sl

label sprites_my_list_sl_dress:
    menu:
        "Злость":
            show sl angry dress far with dspr
            "sl angry dress far"
            show sl angry dress with dspr
            "sl angry dress"
            show sl angry dress close with dspr
            "sl angry dress close"
            hide sl with dspr
            jump sprites_my_list_sl_dress
        "Счастье":
            show sl happy dress far with dspr
            "sl happy dress far"
            show sl happy dress with dspr
            "sl happy dress"
            show sl happy dress close with dspr
            "sl happy dress close"
            hide sl with dspr
            jump sprites_my_list_sl_dress
        "Смех":
            show sl laugh dress far with dspr
            "sl laugh dress far"
            show sl laugh dress with dspr
            "sl laugh dress"
            show sl laugh dress close with dspr
            "sl laugh dress close"
            hide sl with dspr
            jump sprites_my_list_sl_dress
        "Обычная":
            show sl normal dress far with dspr
            "sl normal dress far"
            show sl normal dress with dspr
            "sl normal dress"
            show sl normal dress close with dspr
            "sl normal dress close"
            hide sl with dspr
            jump sprites_my_list_sl_dress
        "Грустная":
            show sl sad dress far with dspr
            "sl sad dress far"
            show sl sad dress with dspr
            "sl sad dress"
            show sl sad dress close with dspr
            "sl sad dress close"
            hide sl with dspr
            jump sprites_my_list_sl_dress
        "Испуганная":
            show sl scared dress far with dspr
            "sl scared dress far"
            show sl scared dress with dspr
            "sl scared dress"
            show sl scared dress close with dspr
            "sl scared dress close"
            hide sl with dspr
            jump sprites_my_list_sl_dress
        "Серьёзная":
            show sl serious dress far with dspr
            "sl serious dress far"
            show sl serious dress with dspr
            "sl serious dress"
            show sl serious dress close with dspr
            "sl serious dress close"
            hide sl with dspr
            jump sprites_my_list_sl_dress
        "Стесняущаяся":
            show sl shy dress far with dspr
            "sl shy dress far"
            show sl shy dress with dspr
            "sl shy dress"
            show sl shy dress close with dspr
            "sl shy dress close"
            hide sl with dspr
            jump sprites_my_list_sl_dress
        "Улыбка":
            show sl smile dress far with dspr
            "sl smile dress far"
            show sl smile dress with dspr
            "sl smile dress"
            show sl smile dress close with dspr
            "sl smile dress close"
            hide sl with dspr
            jump sprites_my_list_sl_dress
        "Улыбка(2)":
            show sl smile2 dress far with dspr
            "sl smile2 dress far"
            show sl smile2 dress with dspr
            "sl smile2 dress"
            show sl smile2 dress close with dspr
            "sl smile2 dress close"
            hide sl with dspr
            jump sprites_my_list_sl_dress
        "Удивлённая":
            show sl surprise dress far with dspr
            "sl surprise dress far"
            show sl surprise dress with dspr
            "sl surprise dress"
            show sl surprise dress close with dspr
            "sl surprise dress close"
            hide sl with dspr
            jump sprites_my_list_sl_dress
        "Нежность":
            show sl tender dress far with dspr
            "sl tender dress far"
            show sl tender dress with dspr
            "sl tender dress"
            show sl tender dress close with dspr
            "sl tender dress close"
            hide sl with dspr
            jump sprites_my_list_sl_dress
        ">>Назад<<":
            jump sprites_my_list_sl

label sprites_my_list_sl_sport:
    menu:
        "Злость":
            show sl angry sport far with dspr
            "sl angry sport far"
            show sl angry sport with dspr
            "sl angry sport"
            show sl angry sport close with dspr
            "sl angry sport close"
            hide sl with dspr
            jump sprites_my_list_sl_sport
        "Счастье":
            show sl happy sport far with dspr
            "sl happy sport far"
            show sl happy sport with dspr
            "sl happy sport"
            show sl happy sport close with dspr
            "sl happy sport close"
            hide sl with dspr
            jump sprites_my_list_sl_sport
        "Смех":
            show sl laugh sport far with dspr
            "sl laugh sport far"
            show sl laugh sport with dspr
            "sl laugh sport"
            show sl laugh sport close with dspr
            "sl laugh sport close"
            hide sl with dspr
            jump sprites_my_list_sl_sport
        "Обычная":
            show sl normal sport far with dspr
            "sl normal sport far"
            show sl normal sport with dspr
            "sl normal sport"
            show sl normal sport close with dspr
            "sl normal sport close"
            hide sl with dspr
            jump sprites_my_list_sl_sport
        "Грустная":
            show sl sad sport far with dspr
            "sl sad sport far"
            show sl sad sport with dspr
            "sl sad sport"
            show sl sad sport close with dspr
            "sl sad sport close"
            hide sl with dspr
            jump sprites_my_list_sl_sport
        "Испуганная":
            show sl scared sport far with dspr
            "sl scared sport far"
            show sl scared sport with dspr
            "sl scared sport"
            show sl scared sport close with dspr
            "sl scared sport close"
            hide sl with dspr
            jump sprites_my_list_sl_sport
        "Серьёзная":
            show sl serious sport far with dspr
            "sl serious sport far"
            show sl serious sport with dspr
            "sl serious sport"
            show sl serious sport close with dspr
            "sl serious sport close"
            hide sl with dspr
            jump sprites_my_list_sl_sport
        "Стесняущаяся":
            show sl shy sport far with dspr
            "sl shy sport far"
            show sl shy sport with dspr
            "sl shy sport"
            show sl shy sport close with dspr
            "sl shy sport close"
            hide sl with dspr
            jump sprites_my_list_sl_sport
        "Улыбка":
            show sl smile sport far with dspr
            "sl smile sport far"
            show sl smile sport with dspr
            "sl smile sport"
            show sl smile sport close with dspr
            "sl smile sport close"
            hide sl with dspr
            jump sprites_my_list_sl_sport
        "Улыбка(2)":
            show sl smile2 sport far with dspr
            "sl smile2 sport far"
            show sl smile2 sport with dspr
            "sl smile2 sport"
            show sl smile2 sport close with dspr
            "sl smile2 sport close"
            hide sl with dspr
            jump sprites_my_list_sl_sport
        "Удивлённая":
            show sl surprise sport far with dspr
            "sl surprise sport far"
            show sl surprise sport with dspr
            "sl surprise sport"
            show sl surprise sport close with dspr
            "sl surprise sport close"
            hide sl with dspr
            jump sprites_my_list_sl_sport
        "Нежность":
            show sl tender sport far with dspr
            "sl tender sport far"
            show sl tender sport with dspr
            "sl tender sport"
            show sl tender sport close with dspr
            "sl tender sport close"
            hide sl with dspr
            jump sprites_my_list_sl_sport
        ">>Назад<<":
            jump sprites_my_list_sl

label sprites_my_list_sl_swim:
    menu:
        "Злость":
            show sl angry swim far with dspr
            "sl angry swim far"
            show sl angry swim with dspr
            "sl angry swim"
            show sl angry swim close with dspr
            "sl angry swim close"
            hide sl with dspr
            jump sprites_my_list_sl_swim
        "Счастье":
            show sl happy swim far with dspr
            "sl happy swim far"
            show sl happy swim with dspr
            "sl happy swim"
            show sl happy swim close with dspr
            "sl happy swim close"
            hide sl with dspr
            jump sprites_my_list_sl_swim
        "Смех":
            show sl laugh swim far with dspr
            "sl laugh swim far"
            show sl laugh swim with dspr
            "sl laugh swim"
            show sl laugh swim close with dspr
            "sl laugh swim close"
            hide sl with dspr
            jump sprites_my_list_sl_swim
        "Обычная":
            show sl normal swim far with dspr
            "sl normal swim far"
            show sl normal swim with dspr
            "sl normal swim"
            show sl normal swim close with dspr
            "sl normal swim close"
            hide sl with dspr
            jump sprites_my_list_sl_swim
        "Грустная":
            show sl sad swim far with dspr
            "sl sad swim far"
            show sl sad swim with dspr
            "sl sad swim"
            show sl sad swim close with dspr
            "sl sad swim close"
            hide sl with dspr
            jump sprites_my_list_sl_swim
        "Испуганная":
            show sl scared swim far with dspr
            "sl scared swim far"
            show sl scared swim with dspr
            "sl scared swim"
            show sl scared swim close with dspr
            "sl scared swim close"
            hide sl with dspr
            jump sprites_my_list_sl_swim
        "Серьёзная":
            show sl serious swim far with dspr
            "sl serious swim far"
            show sl serious swim with dspr
            "sl serious swim"
            show sl serious swim close with dspr
            "sl serious swim close"
            hide sl with dspr
            jump sprites_my_list_sl_swim
        "Стесняущаяся":
            show sl shy swim far with dspr
            "sl shy swim far"
            show sl shy swim with dspr
            "sl shy swim"
            show sl shy swim close with dspr
            "sl shy swim close"
            hide sl with dspr
            jump sprites_my_list_sl_swim
        "Улыбка":
            show sl smile swim far with dspr
            "sl smile swim far"
            show sl smile swim with dspr
            "sl smile swim"
            show sl smile swim close with dspr
            "sl smile swim close"
            hide sl with dspr
            jump sprites_my_list_sl_swim
        "Улыбка(2)":
            show sl smile2 swim far with dspr
            "sl smile2 swim far"
            show sl smile2 swim with dspr
            "sl smile2 swim"
            show sl smile2 swim close with dspr
            "sl smile2 swim close"
            hide sl with dspr
            jump sprites_my_list_sl_swim
        "Удивлённая":
            show sl surprise swim far with dspr
            "sl surprise swim far"
            show sl surprise swim with dspr
            "sl surprise swim"
            show sl surprise swim close with dspr
            "sl surprise swim close"
            hide sl with dspr
            jump sprites_my_list_sl_swim
        "Нежность":
            show sl tender swim far with dspr
            "sl tender swim far"
            show sl tender swim with dspr
            "sl tender swim"
            show sl tender swim close with dspr
            "sl tender swim close"
            hide sl with dspr
            jump sprites_my_list_sl_swim
        ">>Назад<<":
            jump sprites_my_list_sl

label sprites_my_list_un:
    menu:
        "Пионерская форма":
            jump sprites_my_list_un_pioner
        "Платье":
            jump sprites_my_list_un_dress
        "Спортивная форма":
            jump sprites_my_list_un_sport
        "Купальник":
            jump sprites_my_list_un_swim
        ">>Назад<<":
            jump sprites_my_list

label sprites_my_list_un_pioner:
    menu:
        "Злость":
            show un angry pioneer far with dspr
            "un angry pioneer far"
            show un angry pioneer with dspr
            "un angry pioneer"
            show un angry pioneer close with dspr
            "un angry pioneer close"
            hide un with dspr
            jump sprites_my_list_un_pioner
        "Хмурая":
            show un angry2 pioneer far with dspr
            "un angry2 pioneer far"
            show un angry2 pioneer with dspr
            "un angry2 pioneer"
            show un angry2 pioneer close with dspr
            "un angry2 pioneer close"
            hide un with dspr
            jump sprites_my_list_un_pioner
        "Улыбка сквозь слёзы":
            show un cry_smile pioneer far with dspr
            "un cry_smile pioneer far"
            show un cry_smile pioneer with dspr
            "un cry_smile pioneer"
            show un cry_smile pioneer close with dspr
            "un cry_smile pioneer close"
            hide un with dspr
            jump sprites_my_list_un_pioner
        "Плачущая":
            show un cry pioneer far with dspr
            "un cry pioneer far"
            show un cry pioneer with dspr
            "un cry pioneer"
            show un cry pioneer close with dspr
            "un cry pioneer close"
            hide un with dspr
            jump sprites_my_list_un_pioner
        "Evil smile":
            show un evil_smile pioneer far with dspr
            "un evil_smile pioneer far"
            show un evil_smile pioneer with dspr
            "un evil_smile pioneer"
            show un evil_smile pioneer close with dspr
            "un evil_smile pioneer close"
            hide un with dspr
            jump sprites_my_list_un_pioner
        "Усмешка":
            show un grin pioneer far with dspr
            "un grin pioneer far"
            show un grin pioneer with dspr
            "un grin pioneer"
            show un grin pioneer close with dspr
            "un grin pioneer close"
            hide un with dspr
            jump sprites_my_list_un_pioner
        "Смех":
            show un laugh pioneer far with dspr
            "un laugh pioneer far"
            show un laugh pioneer with dspr
            "un laugh pioneer"
            show un laugh pioneer close with dspr
            "un laugh pioneer close"
            hide un with dspr
            jump sprites_my_list_un_pioner
        "Обычная":
            show un normal pioneer far with dspr
            "un normal pioneer far"
            show un normal pioneer with dspr
            "un normal pioneer"
            show un normal pioneer close with dspr
            "un normal pioneer close"
            hide un with dspr
            jump sprites_my_list_un_pioner
        "Ярость":
            show un rage pioneer far with dspr
            "un rage pioneer far"
            show un rage pioneer with dspr
            "un rage pioneer"
            show un rage pioneer close with dspr
            "un rage pioneer close"
            hide un with dspr
            jump sprites_my_list_un_pioner
        "Грустная":
            show un sad pioneer far with dspr
            "un sad pioneer far"
            show un sad pioneer with dspr
            "un sad pioneer"
            show un sad pioneer close with dspr
            "un sad pioneer close"
            hide un with dspr
            jump sprites_my_list_un_pioner
        "Испуганная":
            show un scared pioneer far with dspr
            "un scared pioneer far"
            show un scared pioneer with dspr
            "un scared pioneer"
            show un scared pioneer close with dspr
            "un scared pioneer close"
            hide un with dspr
            jump sprites_my_list_un_pioner
        "Серьёзная":
            show un serious pioneer far with dspr
            "un serious pioneer far"
            show un serious pioneer with dspr
            "un serious pioneer"
            show un serious pioneer close with dspr
            "un serious pioneer close"
            hide un with dspr
            jump sprites_my_list_un_pioner
        "Шокированная":
            show un shocked pioneer far with dspr
            "un shocked pioneer far"
            show un shocked pioneer with dspr
            "un shocked pioneer"
            show un shocked pioneer close with dspr
            "un shocked pioneer close"
            hide un with dspr
            jump sprites_my_list_un_pioner
        "Застенчивая":
            show un shy pioneer far with dspr
            "un shy pioneer far"
            show un shy pioneer with dspr
            "un shy pioneer"
            show un shy pioneer close with dspr
            "un shy pioneer close"
            hide un with dspr
            jump sprites_my_list_un_pioner
        "Улыбка(1)":
            show un smile pioneer far with dspr
            "un smile pioneer far"
            show un smile pioneer with dspr
            "un smile pioneer"
            show un smile pioneer close with dspr
            "un smile pioneer close"
            hide un with dspr
            jump sprites_my_list_un_pioner
        "Улыбка(2)":
            show un smile2 pioneer far with dspr
            "un smile2 pioneer far"
            show un smile2 pioneer with dspr
            "un smile2 pioneer"
            show un smile2 pioneer close with dspr
            "un smile2 pioneer close"
            hide un with dspr
            jump sprites_my_list_un_pioner
        "Улыбка(3)":
            show un smile3 pioneer far with dspr
            "un smile3 pioneer far"
            show un smile3 pioneer with dspr
            "un smile3 pioneer"
            show un smile3 pioneer close with dspr
            "un smile3 pioneer close"
            hide un with dspr
            jump sprites_my_list_un_pioner
        "Удивлённая":
            show un surprise pioneer far with dspr
            "un surprise pioneer far"
            show un surprise pioneer with dspr
            "un surprise pioneer"
            show un surprise pioneer close with dspr
            "un surprise pioneer close"
            hide un with dspr
            jump sprites_my_list_un_pioner
        ">>Назад<<":
            jump sprites_my_list_un

label sprites_my_list_un_dress:
    menu:
        "Злость":
            show un angry dress far with dspr
            "un angry dress far"
            show un angry dress with dspr
            "un angry dress"
            show un angry dress close with dspr
            "un angry dress close"
            hide un with dspr
            jump sprites_my_list_un_dress
        "Хмурая":
            show un angry2 dress far with dspr
            "un angry2 dress far"
            show un angry2 dress with dspr
            "un angry2 dress"
            show un angry2 dress close with dspr
            "un angry2 dress close"
            hide un with dspr
            jump sprites_my_list_un_dress
        "Улыбка сквозь слёзы":
            show un cry_smile dress far with dspr
            "un cry_smile dress far"
            show un cry_smile dress with dspr
            "un cry_smile dress"
            show un cry_smile dress close with dspr
            "un cry_smile dress close"
            hide un with dspr
            jump sprites_my_list_un_dress
        "Плачущая":
            show un cry dress far with dspr
            "un cry dress far"
            show un cry dress with dspr
            "un cry dress"
            show un cry dress close with dspr
            "un cry dress close"
            hide un with dspr
            jump sprites_my_list_un_dress
        "Дьявольская улыбка":
            show un evil_smile dress far with dspr
            "un evil_smile dress far"
            show un evil_smile dress with dspr
            "un evil_smile dress"
            show un evil_smile dress close with dspr
            "un evil_smile dress close"
            hide un with dspr
            jump sprites_my_list_un_dress
        "Усмешка":
            show un grin dress far with dspr
            "un grin dress far"
            show un grin dress with dspr
            "un grin dress"
            show un grin dress close with dspr
            "un grin dress close"
            hide un with dspr
            jump sprites_my_list_un_dress
        "Смех":
            show un laugh dress far with dspr
            "un laugh dress far"
            show un laugh dress with dspr
            "un laugh dress"
            show un laugh dress close with dspr
            "un laugh dress close"
            hide un with dspr
            jump sprites_my_list_un_dress
        "Обычная":
            show un normal dress far with dspr
            "un normal dress far"
            show un normal dress with dspr
            "un normal dress"
            show un normal dress close with dspr
            "un normal dress close"
            hide un with dspr
            jump sprites_my_list_un_dress
        "Ярость":
            show un rage dress far with dspr
            "un rage dress far"
            show un rage dress with dspr
            "un rage dress"
            show un rage dress close with dspr
            "un rage dress close"
            hide un with dspr
            jump sprites_my_list_un_dress
        "Грустная":
            show un sad dress far with dspr
            "un sad dress far"
            show un sad dress with dspr
            "un sad dress"
            show un sad dress close with dspr
            "un sad dress close"
            hide un with dspr
            jump sprites_my_list_un_dress
        "Испуганная":
            show un scared dress far with dspr
            "un scared dress far"
            show un scared dress with dspr
            "un scared dress"
            show un scared dress close with dspr
            "un scared dress close"
            hide un with dspr
            jump sprites_my_list_un_dress
        "Серьёзная":
            show un serious dress far with dspr
            "un serious dress far"
            show un serious dress with dspr
            "un serious dress"
            show un serious dress close with dspr
            "un serious dress close"
            hide un with dspr
            jump sprites_my_list_un_dress
        "Шокированная":
            show un shocked dress far with dspr
            "un shocked dress far"
            show un shocked dress with dspr
            "un shocked dress"
            show un shocked dress close with dspr
            "un shocked dress close"
            hide un with dspr
            jump sprites_my_list_un_dress
        "Застенчивая":
            show un shy dress far with dspr
            "un shy dress far"
            show un shy dress with dspr
            "un shy dress"
            show un shy dress close with dspr
            "un shy dress close"
            hide un with dspr
            jump sprites_my_list_un_dress
        "Улыбка(1)":
            show un smile dress far with dspr
            "un smile dress far"
            show un smile dress with dspr
            "un smile dress"
            show un smile dress close with dspr
            "un smile dress close"
            hide un with dspr
            jump sprites_my_list_un_dress
        "Улыбка(2)":
            show un smile2 dress far with dspr
            "un smile2 dress far"
            show un smile2 dress with dspr
            "un smile2 dress"
            show un smile2 dress close with dspr
            "un smile2 dress close"
            hide un with dspr
            jump sprites_my_list_un_dress
        "Улыбка(3)":
            show un smile3 dress far with dspr
            "un smile3 dress far"
            show un smile3 dress with dspr
            "un smile3 dress"
            show un smile3 dress close with dspr
            "un smile3 dress close"
            hide un with dspr
            jump sprites_my_list_un_dress
        "Удивлённая":
            show un surprise dress far with dspr
            "un surprise dress far"
            show un surprise dress with dspr
            "un surprise dress"
            show un surprise dress close with dspr
            "un surprise dress close"
            hide un with dspr
            jump sprites_my_list_un_dress
        ">>Назад<<":
            jump sprites_my_list_un

label sprites_my_list_un_sport:
    menu:
        "Злость":
            show un angry sport far with dspr
            "un angry sport far"
            show un angry sport with dspr
            "un angry sport"
            show un angry sport close with dspr
            "un angry sport close"
            hide un with dspr
            jump sprites_my_list_un_sport
        "Хмурая":
            show un angry2 sport far with dspr
            "un angry2 sport far"
            show un angry2 sport with dspr
            "un angry2 sport"
            show un angry2 sport close with dspr
            "un angry2 sport close"
            hide un with dspr
            jump sprites_my_list_un_sport
        "Улыбка сквозь слёзы":
            show un cry_smile sport far with dspr
            "un cry_smile sport far"
            show un cry_smile sport with dspr
            "un cry_smile sport"
            show un cry_smile sport close with dspr
            "un cry_smile sport close"
            hide un with dspr
            jump sprites_my_list_un_sport
        "Плачущая":
            show un cry sport far with dspr
            "un cry sport far"
            show un cry sport with dspr
            "un cry sport"
            show un cry sport close with dspr
            "un cry sport close"
            hide un with dspr
            jump sprites_my_list_un_sport
        "Дьявольская улыбка":
            show un evil_smile sport far with dspr
            "un evil_smile sport far"
            show un evil_smile sport with dspr
            "un evil_smile sport"
            show un evil_smile sport close with dspr
            "un evil_smile sport close"
            hide un with dspr
            jump sprites_my_list_un_sport
        "Усмешка":
            show un grin sport far with dspr
            "un grin sport far"
            show un grin sport with dspr
            "un grin sport"
            show un grin sport close with dspr
            "un grin sport close"
            hide un with dspr
            jump sprites_my_list_un_sport
        "Смех":
            show un laugh sport far with dspr
            "un laugh sport far"
            show un laugh sport with dspr
            "un laugh sport"
            show un laugh sport close with dspr
            "un laugh sport close"
            hide un with dspr
            jump sprites_my_list_un_sport
        "Обычная":
            show un normal sport far with dspr
            "un normal sport far"
            show un normal sport with dspr
            "un normal sport"
            show un normal sport close with dspr
            "un normal sport close"
            hide un with dspr
            jump sprites_my_list_un_sport
        "Ярость":
            show un rage sport far with dspr
            "un rage sport far"
            show un rage sport with dspr
            "un rage sport"
            show un rage sport close with dspr
            "un rage sport close"
            hide un with dspr
            jump sprites_my_list_un_sport
        "Грустная":
            show un sad sport far with dspr
            "un sad sport far"
            show un sad sport with dspr
            "un sad sport"
            show un sad sport close with dspr
            "un sad sport close"
            hide un with dspr
            jump sprites_my_list_un_sport
        "Испуганная":
            show un scared sport far with dspr
            "un scared sport far"
            show un scared sport with dspr
            "un scared sport"
            show un scared sport close with dspr
            "un scared sport close"
            hide un with dspr
            jump sprites_my_list_un_sport
        "Серьёзная":
            show un serious sport far with dspr
            "un serious sport far"
            show un serious sport with dspr
            "un serious sport"
            show un serious sport close with dspr
            "un serious sport close"
            hide un with dspr
            jump sprites_my_list_un_sport
        "Шокированная":
            show un shocked sport far with dspr
            "un shocked sport far"
            show un shocked sport with dspr
            "un shocked sport"
            show un shocked sport close with dspr
            "un shocked sport close"
            hide un with dspr
            jump sprites_my_list_un_sport
        "Застенчивая":
            show un shy sport far with dspr
            "un shy sport far"
            show un shy sport with dspr
            "un shy sport"
            show un shy sport close with dspr
            "un shy sport close"
            hide un with dspr
            jump sprites_my_list_un_sport
        "Улыбка(1)":
            show un smile sport far with dspr
            "un smile sport far"
            show un smile sport with dspr
            "un smile sport"
            show un smile sport close with dspr
            "un smile sport close"
            hide un with dspr
            jump sprites_my_list_un_sport
        "Улыбка(2)":
            show un smile2 sport far with dspr
            "un smile2 sport far"
            show un smile2 sport with dspr
            "un smile2 sport"
            show un smile2 sport close with dspr
            "un smile2 sport close"
            hide un with dspr
            jump sprites_my_list_un_sport
        "Улыбка(3)":
            show un smile3 sport far with dspr
            "un smile3 sport far"
            show un smile3 sport with dspr
            "un smile3 sport"
            show un smile3 sport close with dspr
            "un smile3 sport close"
            hide un with dspr
            jump sprites_my_list_un_sport
        "Удивлённая":
            show un surprise sport far with dspr
            "un surprise sport far"
            show un surprise sport with dspr
            "un surprise sport"
            show un surprise sport close with dspr
            "un surprise sport close"
            hide un with dspr
            jump sprites_my_list_un_sport
        ">>Назад<<":
            jump sprites_my_list_un

label sprites_my_list_un_swim:
    menu:
        "Злость":
            show un angry swim far with dspr
            "un angry swim far"
            show un angry swim with dspr
            "un angry swim"
            show un angry swim close with dspr
            "un angry swim close"
            hide un with dspr
            jump sprites_my_list_un_swim
        "Улыбка сквозь слёзы":
            show un cry_smile swim far with dspr
            "un cry_smile swim far"
            show un cry_smile swim with dspr
            "un cry_smile swim"
            show un cry_smile swim close with dspr
            "un cry_smile swim close"
            hide un with dspr
            jump sprites_my_list_un_swim
        "Плачущая":
            show un cry swim far with dspr
            "un cry swim far"
            show un cry swim with dspr
            "un cry swim"
            show un cry swim close with dspr
            "un cry swim close"
            hide un with dspr
            jump sprites_my_list_un_swim
        "Дьявольская улыбка":
            show un evil_smile swim far with dspr
            "un evil_smile swim far"
            show un evil_smile swim with dspr
            "un evil_smile swim"
            show un evil_smile swim close with dspr
            "un evil_smile swim close"
            hide un with dspr
            jump sprites_my_list_un_swim
        "Обычная":
            show un normal swim far with dspr
            "un normal swim far"
            show un normal swim with dspr
            "un normal swim"
            show un normal swim close with dspr
            "un normal swim close"
            hide un with dspr
            jump sprites_my_list_un_swim
        "Грустная":
            show un sad swim far with dspr
            "un sad swim far"
            show un sad swim with dspr
            "un sad swim"
            show un sad swim close with dspr
            "un sad swim close"
            hide un with dspr
            jump sprites_my_list_un_swim
        "Испуганная":
            show un scared swim far with dspr
            "un scared swim far"
            show un scared swim with dspr
            "un scared swim"
            show un scared swim close with dspr
            "un scared swim close"
            hide un with dspr
            jump sprites_my_list_un_swim
        "Шокированная":
            show un shocked swim far with dspr
            "un shocked swim far"
            show un shocked swim with dspr
            "un shocked swim"
            show un shocked swim close with dspr
            "un shocked swim close"
            hide un with dspr
            jump sprites_my_list_un_swim
        "Застенчивая":
            show un shy swim far with dspr
            "un shy swim far"
            show un shy swim with dspr
            "un shy swim"
            show un shy swim close with dspr
            "un shy swim close"
            hide un with dspr
            jump sprites_my_list_un_swim
        "Улыбка(1)":
            show un smile swim far with dspr
            "un smile swim far"
            show un smile swim with dspr
            "un smile swim"
            show un smile swim close with dspr
            "un smile swim close"
            hide un with dspr
            jump sprites_my_list_un_swim
        "Улыбка(2)":
            show un smile2 swim far with dspr
            "un smile2 swim far"
            show un smile2 swim with dspr
            "un smile2 swim"
            show un smile2 swim close with dspr
            "un smile2 swim close"
            hide un with dspr
            jump sprites_my_list_un_swim
        "Удивлённая":
            show un surprise swim far with dspr
            "un surprise swim far"
            show un surprise swim with dspr
            "un surprise swim"
            show un surprise swim close with dspr
            "un surprise swim close"
            hide un with dspr
            jump sprites_my_list_un_swim
        ">>Назад<<":
            jump sprites_my_list_un

label sprites_my_list_mi:
    menu:
        "Пионерская форма":
            jump sprites_my_list_mi_pioneer
        "Купальник":
            jump sprites_my_list_mi_swim
        ">>Назад<<":
            jump sprites_my_list

label sprites_my_list_mi_pioneer:
    menu:
        "Хмурая":
            show mi angry pioneer far with dspr
            "mi angry pioneer far"
            show mi angry pioneer with dspr
            "mi angry pioneer"
            show mi angry pioneer close with dspr
            "mi angry pioneer close"
            hide mi with dspr
            jump sprites_my_list_mi_pioneer
        "Плачущая":
            show mi cry pioneer far with dspr
            "mi cry pioneer far"
            show mi cry pioneer with dspr
            "mi cry pioneer"
            show mi cry pioneer close with dspr
            "mi cry pioneer close"
            hide mi with dspr
            jump sprites_my_list_mi_pioneer
        "Улыбка сквозь слёзы":
            show mi cry_smile pioneer far with dspr
            "mi cry_smile pioneer far"
            show mi cry_smile pioneer with dspr
            "mi cry_smile pioneer"
            show mi cry_smile pioneer close with dspr
            "mi cry_smile pioneer close"
            hide mi with dspr
            jump sprites_my_list_mi_pioneer
        "Неприязнь":
            show mi dontlike pioneer far with dspr
            "mi dontlike pioneer far"
            show mi dontlike pioneer with dspr
            "mi dontlike pioneer"
            show mi dontlike pioneer close with dspr
            "mi dontlike pioneer close"
            hide mi with dspr
            jump sprites_my_list_mi_pioneer
        "Усмешка":
            show mi grin pioneer far with dspr
            "mi grin pioneer far"
            show mi grin pioneer with dspr
            "mi grin pioneer"
            show mi grin pioneer close with dspr
            "mi grin pioneer close"
            hide mi with dspr
            jump sprites_my_list_mi_pioneer
        "Счастье":
            show mi happy pioneer far with dspr
            "mi happy pioneer far"
            show mi happy pioneer with dspr
            "mi happy pioneer"
            show mi happy pioneer close with dspr
            "mi happy pioneer close"
            hide mi with dspr
            jump sprites_my_list_mi_pioneer
        "Смех":
            show mi laugh pioneer far with dspr
            "mi laugh pioneer far"
            show mi laugh pioneer with dspr
            "mi laugh pioneer"
            show mi laugh pioneer close with dspr
            "mi laugh pioneer close"
            hide mi with dspr
            jump sprites_my_list_mi_pioneer
        "Обычная":
            show mi normal pioneer far with dspr
            "mi normal pioneer far"
            show mi normal pioneer with dspr
            "mi normal pioneer"
            show mi normal pioneer close with dspr
            "mi normal pioneer close"
            hide mi with dspr
            jump sprites_my_list_mi_pioneer
        "Злость":
            show mi rage pioneer far with dspr
            "mi rage pioneer far"
            show mi rage pioneer with dspr
            "mi rage pioneer"
            show mi rage pioneer close with dspr
            "mi rage pioneer close"
            hide mi with dspr
            jump sprites_my_list_mi_pioneer
        "Грустная":
            show mi sad pioneer far with dspr
            "mi sad pioneer far"
            show mi sad pioneer with dspr
            "mi sad pioneer"
            show mi sad pioneer close with dspr
            "mi sad pioneer close"
            hide mi with dspr
            jump sprites_my_list_mi_pioneer
        "Испуганная":
            show mi scared pioneer far with dspr
            "mi scared pioneer far"
            show mi scared pioneer with dspr
            "mi scared pioneer"
            show mi scared pioneer close with dspr
            "mi scared pioneer close"
            hide mi with dspr
            jump sprites_my_list_mi_pioneer
        "Серьёзная":
            show mi serious pioneer far with dspr
            "mi serious pioneer far"
            show mi serious pioneer with dspr
            "mi serious pioneer"
            show mi serious pioneer close with dspr
            "mi serious pioneer close"
            hide mi with dspr
            jump sprites_my_list_mi_pioneer
        "Шокированная":
            show mi shocked pioneer far with dspr
            "mi shocked pioneer far"
            show mi shocked pioneer with dspr
            "mi shocked pioneer"
            show mi shocked pioneer close with dspr
            "mi shocked pioneer close"
            hide mi with dspr
            jump sprites_my_list_mi_pioneer
        "Стесняущаяся":
            show mi shy pioneer far with dspr
            "mi shy pioneer far"
            show mi shy pioneer with dspr
            "mi shy pioneer"
            show mi shy pioneer close with dspr
            "mi shy pioneer close"
            hide mi with dspr
            jump sprites_my_list_mi_pioneer
        "Улыбка":
            show mi smile pioneer far with dspr
            "mi smile pioneer far"
            show mi smile pioneer with dspr
            "mi smile pioneer"
            show mi smile pioneer close with dspr
            "mi smile pioneer close"
            hide mi with dspr
            jump sprites_my_list_mi_pioneer
        "Удивлённая":
            show mi surprise pioneer far with dspr
            "mi surprise pioneer far"
            show mi surprise pioneer with dspr
            "mi surprise pioneer"
            show mi surprise pioneer close with dspr
            "mi surprise pioneer close"
            hide mi with dspr
            jump sprites_my_list_mi_pioneer
        "Расстроенная":
            show mi upset pioneer far with dspr
            "mi upset pioneer far"
            show mi upset pioneer with dspr
            "mi upset pioneer"
            show mi upset pioneer close with dspr
            "mi upset pioneer close"
            hide mi with dspr
            jump sprites_my_list_mi_pioneer
        ">>Назад<<":
            jump sprites_my_list_mi

label sprites_my_list_mi_swim:
    menu:
        "Хмурая":
            show mi angry swim far with dspr
            "mi angry swim far"
            show mi angry swim with dspr
            "mi angry swim"
            show mi angry swim close with dspr
            "mi angry swim close"
            hide mi with dspr
            jump sprites_my_list_mi_swim
        "Плачущая":
            show mi cry swim far with dspr
            "mi cry swim far"
            show mi cry swim with dspr
            "mi cry swim"
            show mi cry swim close with dspr
            "mi cry swim close"
            hide mi with dspr
            jump sprites_my_list_mi_swim
        "Улыбка сквозь слёзы":
            show mi cry_smile swim far with dspr
            "mi cry_smile swim far"
            show mi cry_smile swim with dspr
            "mi cry_smile swim"
            show mi cry_smile swim close with dspr
            "mi cry_smile swim close"
            hide mi with dspr
            jump sprites_my_list_mi_swim
        "Неприязнь":
            show mi dontlike swim far with dspr
            "mi dontlike swim far"
            show mi dontlike swim with dspr
            "mi dontlike swim"
            show mi dontlike swim close with dspr
            "mi dontlike swim close"
            hide mi with dspr
            jump sprites_my_list_mi_swim
        "Усмешка":
            show mi grin swim far with dspr
            "mi grin swim far"
            show mi grin swim with dspr
            "mi grin swim"
            show mi grin swim close with dspr
            "mi grin swim close"
            hide mi with dspr
            jump sprites_my_list_mi_swim
        "Счастье":
            show mi happy swim far with dspr
            "mi happy swim far"
            show mi happy swim with dspr
            "mi happy swim"
            show mi happy swim close with dspr
            "mi happy swim close"
            hide mi with dspr
            jump sprites_my_list_mi_swim
        "Смех":
            show mi laugh swim far with dspr
            "mi laugh swim far"
            show mi laugh swim with dspr
            "mi laugh swim"
            show mi laugh swim close with dspr
            "mi laugh swim close"
            hide mi with dspr
            jump sprites_my_list_mi_swim
        "Обычная":
            show mi normal swim far with dspr
            "mi normal swim far"
            show mi normal swim with dspr
            "mi normal swim"
            show mi normal swim close with dspr
            "mi normal swim close"
            hide mi with dspr
            jump sprites_my_list_mi_swim
        "Злость":
            show mi rage swim far with dspr
            "mi rage swim far"
            show mi rage swim with dspr
            "mi rage swim"
            show mi rage swim close with dspr
            "mi rage swim close"
            hide mi with dspr
            jump sprites_my_list_mi_swim
        "Грустная":
            show mi sad swim far with dspr
            "mi sad swim far"
            show mi sad swim with dspr
            "mi sad swim"
            show mi sad swim close with dspr
            "mi sad swim close"
            hide mi with dspr
            jump sprites_my_list_mi_swim
        "Испуганная":
            show mi scared swim far with dspr
            "mi scared swim far"
            show mi scared swim with dspr
            "mi scared swim"
            show mi scared swim close with dspr
            "mi scared swim close"
            hide mi with dspr
            jump sprites_my_list_mi_swim
        "Серьёзная":
            show mi serious swim far with dspr
            "mi serious swim far"
            show mi serious swim with dspr
            "mi serious swim"
            show mi serious swim close with dspr
            "mi serious swim close"
            hide mi with dspr
            jump sprites_my_list_mi_swim
        "Шокированная":
            show mi shocked swim far with dspr
            "mi shocked swim far"
            show mi shocked swim with dspr
            "mi shocked swim"
            show mi shocked swim close with dspr
            "mi shocked swim close"
            hide mi with dspr
            jump sprites_my_list_mi_swim
        "Стесняущаяся":
            show mi shy swim far with dspr
            "mi shy swim far"
            show mi shy swim with dspr
            "mi shy swim"
            show mi shy swim close with dspr
            "mi shy swim close"
            hide mi with dspr
            jump sprites_my_list_mi_swim
        "Улыбка":
            show mi smile swim far with dspr
            "mi smile swim far"
            show mi smile swim with dspr
            "mi smile swim"
            show mi smile swim close with dspr
            "mi smile swim close"
            hide mi with dspr
            jump sprites_my_list_mi_swim
        "Удивлённая":
            show mi surprise swim far with dspr
            "mi surprise swim far"
            show mi surprise swim with dspr
            "mi surprise swim"
            show mi surprise swim close with dspr
            "mi surprise swim close"
            hide mi with dspr
            jump sprites_my_list_mi_swim
        "Расстроенная":
            show mi upset swim far with dspr
            "mi upset swim far"
            show mi upset swim with dspr
            "mi upset swim"
            show mi upset swim close with dspr
            "mi upset swim close"
            hide mi with dspr
            jump sprites_my_list_mi_swim
        ">>Назад<<":
            jump sprites_my_list_mi

label sprites_my_list_us:
    menu:
        "Пионерская форма":
            jump sprites_my_list_us_pioneer
        "Платье":
            jump sprites_my_list_us_dress
        "Споривная форма":
            jump sprites_my_list_us_sport
        "Купальник":
            jump sprites_my_list_us_swim
        ">>Назад<<":
            jump sprites_my_list

label sprites_my_list_us_pioneer:
    menu:
        "Хмурая":
            show us angry pioneer far with dspr
            "us angry pioneer far"
            show us angry pioneer with dspr
            "us angry pioneer"
            show us angry pioneer close with dspr
            "us angry pioneer close"
            hide us with dspr
            jump sprites_my_list_us_pioneer
        "Спокойная":
            show us calml pioneer far with dspr
            "us calml pioneer far"
            show us calml pioneer with dspr
            "us calml pioneer"
            show us calml pioneer close with dspr
            "us calml pioneer close"
            hide us with dspr
            jump sprites_my_list_us_pioneer
        "Плачущая(1)":
            show us cry pioneer far with dspr
            "us cry pioneer far"
            show us cry pioneer with dspr
            "us cry pioneer"
            show us cry pioneer close with dspr
            "us cry pioneer close"
            hide us with dspr
            jump sprites_my_list_us_pioneer
        "Плачущая(2)":
            show us cry2 pioneer far with dspr
            "us cry2 pioneer far"
            show us cry2 pioneer with dspr
            "us cry2 pioneer"
            show us cry2 pioneer close with dspr
            "us cry2 pioneer close"
            hide us with dspr
            jump sprites_my_list_us_pioneer
        "Неприязнь":
            show us dontlike pioneer far with dspr
            "us dontlike pioneer far"
            show us dontlike pioneer with dspr
            "us dontlike pioneer"
            show us dontlike pioneer close with dspr
            "us dontlike pioneer close"
            hide us with dspr
            jump sprites_my_list_us_pioneer
        "Страх":
            show us fear pioneer far with dspr
            "us fear pioneer far"
            show us fear pioneer with dspr
            "us fear pioneer"
            show us fear pioneer close with dspr
            "us fear pioneer close"
            hide us with dspr
            jump sprites_my_list_us_pioneer
        "Усмешка":
            show us grin pioneer far with dspr
            "us grin pioneer far"
            show us grin pioneer with dspr
            "us grin pioneer"
            show us grin pioneer close with dspr
            "us grin pioneer close"
            hide us with dspr
            jump sprites_my_list_us_pioneer
        "Смех(1)":
            show us laugh pioneer far with dspr
            "us laugh pioneer far"
            show us laugh pioneer with dspr
            "us laugh pioneer"
            show us laugh pioneer close with dspr
            "us laugh pioneer close"
            hide us with dspr
            jump sprites_my_list_us_pioneer
        "Смех(2)":
            show us laugh2 pioneer far with dspr
            "us laugh2 pioneer far"
            show us laugh2 pioneer with dspr
            "us laugh2 pioneer"
            show us laugh2 pioneer close with dspr
            "us laugh2 pioneer close"
            hide us with dspr
            jump sprites_my_list_us_pioneer
        "Обычная":
            show us normal pioneer far with dspr
            "us normal pioneer far"
            show us normal pioneer with dspr
            "us normal pioneer"
            show us normal pioneer close with dspr
            "us normal pioneer close"
            hide us with dspr
            jump sprites_my_list_us_pioneer
        "Грустная":
            show us sad pioneer far with dspr
            "us sad pioneer far"
            show us sad pioneer with dspr
            "us sad pioneer"
            show us sad pioneer close with dspr
            "us sad pioneer close"
            hide us with dspr
            jump sprites_my_list_us_pioneer
        "Стесняущаяся(1)":
            show us shy pioneer far with dspr
            "us shy pioneer far"
            show us shy pioneer with dspr
            "us shy pioneer"
            show us shy pioneer close with dspr
            "us shy pioneer close"
            hide us with dspr
            jump sprites_my_list_us_pioneer
        "Стесняущаяся(2)":
            show us shy2 pioneer far with dspr
            "us shy2 pioneer far"
            show us shy2 pioneer with dspr
            "us shy2 pioneer"
            show us shy2 pioneer close with dspr
            "us shy2 pioneer close"
            hide us with dspr
            jump sprites_my_list_us_pioneer
        "Улыбка":
            show us smile pioneer far with dspr
            "us smile pioneer far"
            show us smile pioneer with dspr
            "us smile pioneer"
            show us smile pioneer close with dspr
            "us smile pioneer close"
            hide us with dspr
            jump sprites_my_list_us_pioneer
        "Удивлённая(1)":
            show us surp1 pioneer far with dspr
            "us surp1 pioneer far"
            show us surp1 pioneer with dspr
            "us surp1 pioneer"
            show us surp1 pioneer close with dspr
            "us surp1 pioneer close"
            hide us with dspr
            jump sprites_my_list_us_pioneer
        "Удивлённая(2)":
            show us surp2 pioneer far with dspr
            "us surp2 pioneer far"
            show us surp2 pioneer with dspr
            "us surp2 pioneer"
            show us surp2 pioneer close with dspr
            "us surp2 pioneer close"
            hide us with dspr
            jump sprites_my_list_us_pioneer
        "Удивлённая(3)":
            show us surp3 pioneer far with dspr
            "us surp3 pioneer far"
            show us surp3 pioneer with dspr
            "us surp3 pioneer"
            show us surp3 pioneer close with dspr
            "us surp3 pioneer close"
            hide us with dspr
            jump sprites_my_list_us_pioneer
        "Расстроенная":
            show us upset pioneer far with dspr
            "us upset pioneer far"
            show us upset pioneer with dspr
            "us upset pioneer"
            show us upset pioneer close with dspr
            "us upset pioneer close"
            hide us with dspr
            jump sprites_my_list_us_pioneer
        ">>Назад<<":
            jump sprites_my_list_us

label sprites_my_list_us_dress:
    menu:
        "Хмурая":
            show us angry dress far with dspr
            "us angry dress far"
            show us angry dress with dspr
            "us angry dress"
            show us angry dress close with dspr
            "us angry dress close"
            hide us with dspr
            jump sprites_my_list_us_dress
        "Спокойная":
            show us calml dress far with dspr
            "us calml dress far"
            show us calml dress with dspr
            "us calml dress"
            show us calml dress close with dspr
            "us calml dress close"
            hide us with dspr
            jump sprites_my_list_us_dress
        "Плачущая(1)":
            show us cry dress far with dspr
            "us cry dress far"
            show us cry dress with dspr
            "us cry dress"
            show us cry dress close with dspr
            "us cry dress close"
            hide us with dspr
            jump sprites_my_list_us_dress
        "Плачущая(2)":
            show us cry2 dress far with dspr
            "us cry2 dress far"
            show us cry2 dress with dspr
            "us cry2 dress"
            show us cry2 dress close with dspr
            "us cry2 dress close"
            hide us with dspr
            jump sprites_my_list_us_dress
        "Неприязнь":
            show us dontlike dress far with dspr
            "us dontlike dress far"
            show us dontlike dress with dspr
            "us dontlike dress"
            show us dontlike dress close with dspr
            "us dontlike dress close"
            hide us with dspr
            jump sprites_my_list_us_dress
        "Страх":
            show us fear dress far with dspr
            "us fear dress far"
            show us fear dress with dspr
            "us fear dress"
            show us fear dress close with dspr
            "us fear dress close"
            hide us with dspr
            jump sprites_my_list_us_dress
        "Усмешка":
            show us grin dress far with dspr
            "us grin dress far"
            show us grin dress with dspr
            "us grin dress"
            show us grin dress close with dspr
            "us grin dress close"
            hide us with dspr
            jump sprites_my_list_us_dress
        "Смех(1)":
            show us laugh dress far with dspr
            "us laugh dress far"
            show us laugh dress with dspr
            "us laugh dress"
            show us laugh dress close with dspr
            "us laugh dress close"
            hide us with dspr
            jump sprites_my_list_us_dress
        "Смех(2)":
            show us laugh2 dress far with dspr
            "us laugh2 dress far"
            show us laugh2 dress with dspr
            "us laugh2 dress"
            show us laugh2 dress close with dspr
            "us laugh2 dress close"
            hide us with dspr
            jump sprites_my_list_us_dress
        "Обычная":
            show us normal dress far with dspr
            "us normal dress far"
            show us normal dress with dspr
            "us normal dress"
            show us normal dress close with dspr
            "us normal dress close"
            hide us with dspr
            jump sprites_my_list_us_dress
        "Грустная":
            show us sad dress far with dspr
            "us sad dress far"
            show us sad dress with dspr
            "us sad dress"
            show us sad dress close with dspr
            "us sad dress close"
            hide us with dspr
            jump sprites_my_list_us_dress
        "Стесняущаяся(1)":
            show us shy dress far with dspr
            "us shy dress far"
            show us shy dress with dspr
            "us shy dress"
            show us shy dress close with dspr
            "us shy dress close"
            hide us with dspr
            jump sprites_my_list_us_dress
        "Стесняущаяся(2)":
            show us shy2 dress far with dspr
            "us shy2 dress far"
            show us shy2 dress with dspr
            "us shy2 dress"
            show us shy2 dress close with dspr
            "us shy2 dress close"
            hide us with dspr
            jump sprites_my_list_us_dress
        "Улыбка":
            show us smile dress far with dspr
            "us smile dress far"
            show us smile dress with dspr
            "us smile dress"
            show us smile dress close with dspr
            "us smile dress close"
            hide us with dspr
            jump sprites_my_list_us_dress
        "Удивлённая(1)":
            show us surp1 dress far with dspr
            "us surp1 dress far"
            show us surp1 dress with dspr
            "us surp1 dress"
            show us surp1 dress close with dspr
            "us surp1 dress close"
            hide us with dspr
            jump sprites_my_list_us_dress
        "Удивлённая(2)":
            show us surp2 dress far with dspr
            "us surp2 dress far"
            show us surp2 dress with dspr
            "us surp2 dress"
            show us surp2 dress close with dspr
            "us surp2 dress close"
            hide us with dspr
            jump sprites_my_list_us_dress
        "Удивлённая(3)":
            show us surp3 dress far with dspr
            "us surp3 dress far"
            show us surp3 dress with dspr
            "us surp3 dress"
            show us surp3 dress close with dspr
            "us surp3 dress close"
            hide us with dspr
            jump sprites_my_list_us_dress
        "Расстроенная":
            show us upset dress far with dspr
            "us upset dress far"
            show us upset dress with dspr
            "us upset dress"
            show us upset dress close with dspr
            "us upset dress close"
            hide us with dspr
            jump sprites_my_list_us_dress
        ">>Назад<<":
            jump sprites_my_list_us

label sprites_my_list_us_sport:
    menu:
        "Хмурая":
            show us angry sport far with dspr
            "us angry sport far"
            show us angry sport with dspr
            "us angry sport"
            show us angry sport close with dspr
            "us angry sport close"
            hide us with dspr
            jump sprites_my_list_us_sport
        "Спокойная":
            show us calml sport far with dspr
            "us calml sport far"
            show us calml sport with dspr
            "us calml sport"
            show us calml sport close with dspr
            "us calml sport close"
            hide us with dspr
            jump sprites_my_list_us_sport
        "Плачущая(1)":
            show us cry sport far with dspr
            "us cry sport far"
            show us cry sport with dspr
            "us cry sport"
            show us cry sport close with dspr
            "us cry sport close"
            hide us with dspr
            jump sprites_my_list_us_sport
        "Плачущая(2)":
            show us cry2 sport far with dspr
            "us cry2 sport far"
            show us cry2 sport with dspr
            "us cry2 sport"
            show us cry2 sport close with dspr
            "us cry2 sport close"
            hide us with dspr
            jump sprites_my_list_us_sport
        "Неприязнь":
            show us dontlike sport far with dspr
            "us dontlike sport far"
            show us dontlike sport with dspr
            "us dontlike sport"
            show us dontlike sport close with dspr
            "us dontlike sport close"
            hide us with dspr
            jump sprites_my_list_us_sport
        "Страх":
            show us fear sport far with dspr
            "us fear sport far"
            show us fear sport with dspr
            "us fear sport"
            show us fear sport close with dspr
            "us fear sport close"
            hide us with dspr
            jump sprites_my_list_us_sport
        "Усмешка":
            show us grin sport far with dspr
            "us grin sport far"
            show us grin sport with dspr
            "us grin sport"
            show us grin sport close with dspr
            "us grin sport close"
            hide us with dspr
            jump sprites_my_list_us_sport
        "Смех(1)":
            show us laugh sport far with dspr
            "us laugh sport far"
            show us laugh sport with dspr
            "us laugh sport"
            show us laugh sport close with dspr
            "us laugh sport close"
            hide us with dspr
            jump sprites_my_list_us_sport
        "Смех(2)":
            show us laugh2 sport far with dspr
            "us laugh2 sport far"
            show us laugh2 sport with dspr
            "us laugh2 sport"
            show us laugh2 sport close with dspr
            "us laugh2 sport close"
            hide us with dspr
            jump sprites_my_list_us_sport
        "Обычная":
            show us normal sport far with dspr
            "us normal sport far"
            show us normal sport with dspr
            "us normal sport"
            show us normal sport close with dspr
            "us normal sport close"
            hide us with dspr
            jump sprites_my_list_us_sport
        "Грустная":
            show us sad sport far with dspr
            "us sad sport far"
            show us sad sport with dspr
            "us sad sport"
            show us sad sport close with dspr
            "us sad sport close"
            hide us with dspr
            jump sprites_my_list_us_sport
        "Стесняущаяся(1)":
            show us shy sport far with dspr
            "us shy sport far"
            show us shy sport with dspr
            "us shy sport"
            show us shy sport close with dspr
            "us shy sport close"
            hide us with dspr
            jump sprites_my_list_us_sport
        "Стесняущаяся(2)":
            show us shy2 sport far with dspr
            "us shy2 sport far"
            show us shy2 sport with dspr
            "us shy2 sport"
            show us shy2 sport close with dspr
            "us shy2 sport close"
            hide us with dspr
            jump sprites_my_list_us_sport
        "Улыбка":
            show us smile sport far with dspr
            "us smile sport far"
            show us smile sport with dspr
            "us smile sport"
            show us smile sport close with dspr
            "us smile sport close"
            hide us with dspr
            jump sprites_my_list_us_sport
        "Удивлённая(1)":
            show us surp1 sport far with dspr
            "us surp1 sport far"
            show us surp1 sport with dspr
            "us surp1 sport"
            show us surp1 sport close with dspr
            "us surp1 sport close"
            hide us with dspr
            jump sprites_my_list_us_sport
        "Удивлённая(2)":
            show us surp2 sport far with dspr
            "us surp2 sport far"
            show us surp2 sport with dspr
            "us surp2 sport"
            show us surp2 sport close with dspr
            "us surp2 sport close"
            hide us with dspr
            jump sprites_my_list_us_sport
        "Удивлённая(3)":
            show us surp3 sport far with dspr
            "us surp3 sport far"
            show us surp3 sport with dspr
            "us surp3 sport"
            show us surp3 sport close with dspr
            "us surp3 sport close"
            hide us with dspr
            jump sprites_my_list_us_sport
        "Расстроенная":
            show us upset sport far with dspr
            "us upset sport far"
            show us upset sport with dspr
            "us upset sport"
            show us upset sport close with dspr
            "us upset sport close"
            hide us with dspr
            jump sprites_my_list_us_sport
        ">>Назад<<":
            jump sprites_my_list_us

label sprites_my_list_us_swim:
    menu:
        "Хмурая":
            show us angry swim far with dspr
            "us angry swim far"
            show us angry swim with dspr
            "us angry swim"
            show us angry swim close with dspr
            "us angry swim close"
            hide us with dspr
            jump sprites_my_list_us_swim
        "Спокойная":
            show us calml swim far with dspr
            "us calml swim far"
            show us calml swim with dspr
            "us calml swim"
            show us calml swim close with dspr
            "us calml swim close"
            hide us with dspr
            jump sprites_my_list_us_swim
        "Плачущая(1)":
            show us cry swim far with dspr
            "us cry swim far"
            show us cry swim with dspr
            "us cry swim"
            show us cry swim close with dspr
            "us cry swim close"
            hide us with dspr
            jump sprites_my_list_us_swim
        "Плачущая(2)":
            show us cry2 swim far with dspr
            "us cry2 swim far"
            show us cry2 swim with dspr
            "us cry2 swim"
            show us cry2 swim close with dspr
            "us cry2 swim close"
            hide us with dspr
            jump sprites_my_list_us_swim
        "Неприязнь":
            show us dontlike swim far with dspr
            "us dontlike swim far"
            show us dontlike swim with dspr
            "us dontlike swim"
            show us dontlike swim close with dspr
            "us dontlike swim close"
            hide us with dspr
            jump sprites_my_list_us_swim
        "Страх":
            show us fear swim far with dspr
            "us fear swim far"
            show us fear swim with dspr
            "us fear swim"
            show us fear swim close with dspr
            "us fear swim close"
            hide us with dspr
            jump sprites_my_list_us_swim
        "Усмешка":
            show us grin swim far with dspr
            "us grin swim far"
            show us grin swim with dspr
            "us grin swim"
            show us grin swim close with dspr
            "us grin swim close"
            hide us with dspr
            jump sprites_my_list_us_swim
        "Смех(1)":
            show us laugh swim far with dspr
            "us laugh swim far"
            show us laugh swim with dspr
            "us laugh swim"
            show us laugh swim close with dspr
            "us laugh swim close"
            hide us with dspr
            jump sprites_my_list_us_swim
        "Смех(2)":
            show us laugh2 swim far with dspr
            "us laugh2 swim far"
            show us laugh2 swim with dspr
            "us laugh2 swim"
            show us laugh2 swim close with dspr
            "us laugh2 swim close"
            hide us with dspr
            jump sprites_my_list_us_swim
        "Обычная":
            show us normal swim far with dspr
            "us normal swim far"
            show us normal swim with dspr
            "us normal swim"
            show us normal swim close with dspr
            "us normal swim close"
            hide us with dspr
            jump sprites_my_list_us_swim
        "Грустная":
            show us sad swim far with dspr
            "us sad swim far"
            show us sad swim with dspr
            "us sad swim"
            show us sad swim close with dspr
            "us sad swim close"
            hide us with dspr
            jump sprites_my_list_us_swim
        "Стесняущаяся(1)":
            show us shy swim far with dspr
            "us shy swim far"
            show us shy swim with dspr
            "us shy swim"
            show us shy swim close with dspr
            "us shy swim close"
            hide us with dspr
            jump sprites_my_list_us_swim
        "Стесняущаяся(2)":
            show us shy2 swim far with dspr
            "us shy2 swim far"
            show us shy2 swim with dspr
            "us shy2 swim"
            show us shy2 swim close with dspr
            "us shy2 swim close"
            hide us with dspr
            jump sprites_my_list_us_swim
        "Улыбка":
            show us smile swim far with dspr
            "us smile swim far"
            show us smile swim with dspr
            "us smile swim"
            show us smile swim close with dspr
            "us smile swim close"
            hide us with dspr
            jump sprites_my_list_us_swim
        "Удивлённая(1)":
            show us surp1 swim far with dspr
            "us surp1 swim far"
            show us surp1 swim with dspr
            "us surp1 swim"
            show us surp1 swim close with dspr
            "us surp1 swim close"
            hide us with dspr
            jump sprites_my_list_us_swim
        "Удивлённая(2)":
            show us surp2 swim far with dspr
            "us surp2 swim far"
            show us surp2 swim with dspr
            "us surp2 swim"
            show us surp2 swim close with dspr
            "us surp2 swim close"
            hide us with dspr
            jump sprites_my_list_us_swim
        "Удивлённая(3)":
            show us surp3 swim far with dspr
            "us surp3 swim far"
            show us surp3 swim with dspr
            "us surp3 swim"
            show us surp3 swim close with dspr
            "us surp3 swim close"
            hide us with dspr
            jump sprites_my_list_us_swim
        "Расстроенная":
            show us upset swim far with dspr
            "us upset swim far"
            show us upset swim with dspr
            "us upset swim"
            show us upset swim close with dspr
            "us upset swim close"
            hide us with dspr
            jump sprites_my_list_us_swim
        ">>Назад<<":
            jump sprites_my_list_us

label sprites_my_list_mt:
    menu:
        "Обычная":
            jump sprites_my_list_mt_normal
        "С панамой":
            jump sprites_my_list_mt_panama
        ">>Назад<<":
            jump sprites_my_list

label sprites_my_list_mt_normal:
    menu:
        "Пионерская форма":
            jump sprites_my_list_mt_normal_pioneer
        "Платье":
            jump sprites_my_list_mt_normal_dress
        "Купальник":
            jump sprites_my_list_mt_normal_swim
        ">>Назад<<":
            jump sprites_my_list_mt

label sprites_my_list_mt_normal_pioneer:
    menu:
        "Плачущая":
            show mt cry pioneer far with dspr
            "mt cry pioneer far"
            show mt cry pioneer with dspr
            "mt cry pioneer"
            show mt cry pioneer close with dspr
            "mt cry pioneer close"
            hide mt with dspr
            jump sprites_my_list_mt_normal_pioneer
        "Хмурая":
            show mt angry pioneer far with dspr
            "mt angry pioneer far"
            show mt angry pioneer with dspr
            "mt angry pioneer"
            show mt angry pioneer close with dspr
            "mt angry pioneer close"
            hide mt with dspr
            jump sprites_my_list_mt_normal_pioneer
        "Усмешка":
            show mt grin pioneer far with dspr
            "mt grin pioneer far"
            show mt grin pioneer with dspr
            "mt grin pioneer"
            show mt grin pioneer close with dspr
            "mt grin pioneer close"
            hide mt with dspr
            jump sprites_my_list_mt_normal_pioneer
        "Смех":
            show mt laugh pioneer far with dspr
            "mt laugh pioneer far"
            show mt laugh pioneer with dspr
            "mt laugh pioneer"
            show mt laugh pioneer close with dspr
            "mt laugh pioneer close"
            hide mt with dspr
            jump sprites_my_list_mt_normal_pioneer
        "Обычная":
            show mt normal pioneer far with dspr
            "mt normal pioneer far"
            show mt normal pioneer with dspr
            "mt normal pioneer"
            show mt normal pioneer close with dspr
            "mt normal pioneer close"
            hide mt with dspr
            jump sprites_my_list_mt_normal_pioneer
        "Злость":
            show mt rage pioneer far with dspr
            "mt rage pioneer far"
            show mt rage pioneer with dspr
            "mt rage pioneer"
            show mt rage pioneer close with dspr
            "mt rage pioneer close"
            hide mt with dspr
            jump sprites_my_list_mt_normal_pioneer
        "Расстроенная":
            show mt sad pioneer far with dspr
            "mt sad pioneer far"
            show mt sad pioneer with dspr
            "mt sad pioneer"
            show mt sad pioneer close with dspr
            "mt sad pioneer close"
            hide mt with dspr
            jump sprites_my_list_mt_normal_pioneer
        "Испуганная":
            show mt scared pioneer far with dspr
            "mt scared pioneer"
            show mt scared pioneer with dspr
            "mt scared pioneer"
            show mt scared pioneer close with dspr
            "mt scared pioneer close"
            hide mt with dspr
            jump sprites_my_list_mt_normal_pioneer
        "Шокированная":
            show mt shocked pioneer far with dspr
            "mt shocked pioneer"
            show mt shocked pioneer with dspr
            "mt shocked pioneer"
            show mt shocked pioneer close with dspr
            "mt shocked pioneer"
            hide mt with dspr
            jump sprites_my_list_mt_normal_pioneer
        "Улыбка":
            show mt smile pioneer far with dspr
            "mt smile pioneer far"
            show mt smile pioneer with dspr
            "mt smile pioneer"
            show mt smile pioneer close with dspr
            "mt smile pioneer close"
            hide mt with dspr
            jump sprites_my_list_mt_normal_pioneer
        "Удивлённая":
            show mt surprise pioneer far with dspr
            "mt surprise pioneer far"
            show mt surprise pioneer with dspr
            "mt surprise pioneer"
            show mt surprise pioneer close with dspr
            "mt surprise pioneer close"
            hide mt with dspr
            jump sprites_my_list_mt_normal_pioneer
        ">>Назад<<":
            jump sprites_my_list_mt_normal

label sprites_my_list_mt_normal_dress:
    menu:
        "Хмурая":
            show mt angry dress far with dspr
            "mt angry dress far"
            show mt angry dress with dspr
            "mt angry dress"
            show mt angry dress close with dspr
            "mt angry dress close"
            hide mt with dspr
            jump sprites_my_list_mt_normal_dress
        "Обычная":
            show mt normal dress far with dspr
            "mt normal dress far"
            show mt normal dress with dspr
            "mt normal dress"
            show mt normal dress close with dspr
            "mt normal dress close"
            hide mt with dspr
            jump sprites_my_list_mt_normal_dress
        "Злость":
            show mt rage dress far with dspr
            "mt rage dress far"
            show mt rage dress with dspr
            "mt rage dress"
            show mt rage dress close with dspr
            "mt rage dress close"
            hide mt with dspr
            jump sprites_my_list_mt_normal_dress
        "Расстроенная":
            show mt sad dress far with dspr
            "mt sad dress far"
            show mt sad dress with dspr
            "mt sad dress"
            show mt sad dress close with dspr
            "mt sad dress close"
            hide mt with dspr
            jump sprites_my_list_mt_normal_dress
        "Испуганная":
            show mt scared dress far with dspr
            "mt scared dress"
            show mt scared dress with dspr
            "mt scared dress"
            show mt scared dress close with dspr
            "mt scared dress close"
            hide mt with dspr
            jump sprites_my_list_mt_normal_dress
        "Шокированная":
            show mt shocked dress far with dspr
            "mt shocked dress"
            show mt shocked dress with dspr
            "mt shocked dress"
            show mt shocked dress close with dspr
            "mt shocked dress"
            hide mt with dspr
            jump sprites_my_list_mt_normal_dress
        "Улыбка":
            show mt smile dress far with dspr
            "mt smile dress far"
            show mt smile dress with dspr
            "mt smile dress"
            show mt smile dress close with dspr
            "mt smile dress close"
            hide mt with dspr
            jump sprites_my_list_mt_normal_dress
        "Удивлённая":
            show mt surprise dress far with dspr
            "mt surprise dress far"
            show mt surprise dress with dspr
            "mt surprise dress"
            show mt surprise dress close with dspr
            "mt surprise dress close"
            hide mt with dspr
            jump sprites_my_list_mt_normal_dress
        ">>Назад<<":
            jump sprites_my_list_mt_normal

label sprites_my_list_mt_normal_swim:
    menu:
        "Хмурая":
            show mt angry swim far with dspr
            "mt angry swim far"
            show mt angry swim with dspr
            "mt angry swim"
            show mt angry swim close with dspr
            "mt angry swim close"
            hide mt with dspr
            jump sprites_my_list_mt_normal_swim
        "Обычная":
            show mt normal swim far with dspr
            "mt normal swim far"
            show mt normal swim with dspr
            "mt normal swim"
            show mt normal swim close with dspr
            "mt normal swim close"
            hide mt with dspr
            jump sprites_my_list_mt_normal_swim
        "Злость":
            show mt rage swim far with dspr
            "mt rage swim far"
            show mt rage swim with dspr
            "mt rage swim"
            show mt rage swim close with dspr
            "mt rage swim close"
            hide mt with dspr
            jump sprites_my_list_mt_normal_swim
        "Расстроенная":
            show mt sad swim far with dspr
            "mt sad swim far"
            show mt sad swim with dspr
            "mt sad swim"
            show mt sad swim close with dspr
            "mt sad swim close"
            hide mt with dspr
            jump sprites_my_list_mt_normal_swim
        "Испуганная":
            show mt scared swim far with dspr
            "mt scared swim"
            show mt scared swim with dspr
            "mt scared swim"
            show mt scared swim close with dspr
            "mt scared swim close"
            hide mt with dspr
            jump sprites_my_list_mt_normal_swim
        "Шокированная":
            show mt shocked swim far with dspr
            "mt shocked swim"
            show mt shocked swim with dspr
            "mt shocked swim"
            show mt shocked swim close with dspr
            "mt shocked swim"
            hide mt with dspr
            jump sprites_my_list_mt_normal_swim
        "Улыбка":
            show mt smile swim far with dspr
            "mt smile swim far"
            show mt smile swim with dspr
            "mt smile swim"
            show mt smile swim close with dspr
            "mt smile swim close"
            hide mt with dspr
            jump sprites_my_list_mt_normal_swim
        "Удивлённая":
            show mt surprise swim far with dspr
            "mt surprise swim far"
            show mt surprise swim with dspr
            "mt surprise swim"
            show mt surprise swim close with dspr
            "mt surprise swim close"
            hide mt with dspr
            jump sprites_my_list_mt_normal_swim
        ">>Назад<<":
            jump sprites_my_list_mt_normal

label sprites_my_list_mt_panama:
    menu:
        "Пионерская форма":
            jump sprites_my_list_mt_panama_pioneer
        "Платье":
            jump sprites_my_list_mt_panama_dress
        "Купальник":
            jump sprites_my_list_mt_panama_swim
        ">>Назад<<":
            jump sprites_my_list_mt

label sprites_my_list_mt_panama_pioneer:
    menu:
        "Хмурая":
            show mt angry panama pioneer far with dspr
            "mt angry panama pioneer far"
            show mt angry panama pioneer with dspr
            "mt angry panama pioneer"
            show mt angry panama pioneer close with dspr
            "mt angry panama pioneer close"
            hide mt with dspr
            jump sprites_my_list_mt_panama_pioneer
        "Усмешка":
            show mt grin panama pioneer far with dspr
            "mt grin panama pioneer far"
            show mt grin panama pioneer with dspr
            "mt grin panama pioneer"
            show mt grin panama pioneer close with dspr
            "mt grin panama pioneer close"
            hide mt with dspr
            jump sprites_my_list_mt_panama_pioneer
        "Смех":
            show mt laugh panama pioneer far with dspr
            "mt laugh panama pioneer far"
            show mt laugh panama pioneer with dspr
            "mt laugh panama pioneer"
            show mt laugh panama pioneer close with dspr
            "mt laugh panama pioneer close"
            hide mt with dspr
            jump sprites_my_list_mt_panama_pioneer
        "Обычная":
            show mt normal panama pioneer far with dspr
            "mt normal panama pioneer far"
            show mt normal panama pioneer with dspr
            "mt normal panama pioneer"
            show mt normal panama pioneer close with dspr
            "mt normal panama pioneer close"
            hide mt with dspr
            jump sprites_my_list_mt_panama_pioneer
        "Злость":
            show mt rage panama pioneer far with dspr
            "mt rage panama pioneer far"
            show mt rage panama pioneer with dspr
            "mt rage panama pioneer"
            show mt rage panama pioneer close with dspr
            "mt rage panama pioneer close"
            hide mt with dspr
            jump sprites_my_list_mt_panama_pioneer
        "Расстроенная":
            show mt sad panama pioneer far with dspr
            "mt sad panama pioneer far"
            show mt sad panama pioneer with dspr
            "mt sad panama pioneer"
            show mt sad panama pioneer close with dspr
            "mt sad panama pioneer close"
            hide mt with dspr
            jump sprites_my_list_mt_panama_pioneer
        "Испуганная":
            show mt scared panama pioneer far with dspr
            "mt scared panama pioneer"
            show mt scared panama pioneer with dspr
            "mt scared panama pioneer"
            show mt scared panama pioneer close with dspr
            "mt scared panama pioneer close"
            hide mt with dspr
            jump sprites_my_list_mt_panama_pioneer
        "Шокированная":
            show mt shocked panama pioneer far with dspr
            "mt shocked panama pioneer"
            show mt shocked panama pioneer with dspr
            "mt shocked panama pioneer"
            show mt shocked panama pioneer close with dspr
            "mt shocked panama pioneer"
            hide mt with dspr
            jump sprites_my_list_mt_panama_pioneer
        "Улыбка":
            show mt smile panama pioneer far with dspr
            "mt smile panama pioneer far"
            show mt smile panama pioneer with dspr
            "mt smile panama pioneer"
            show mt smile panama pioneer close with dspr
            "mt smile panama pioneer close"
            hide mt with dspr
            jump sprites_my_list_mt_panama_pioneer
        "Удивлённая":
            show mt surprise panama pioneer far with dspr
            "mt surprise panama pioneer far"
            show mt surprise panama pioneer with dspr
            "mt surprise panama pioneer"
            show mt surprise panama pioneer close with dspr
            "mt surprise panama pioneer close"
            hide mt with dspr
            jump sprites_my_list_mt_panama_pioneer

        ">>Назад<<":
            jump sprites_my_list_mt_normal

label sprites_my_list_mt_panama_dress:
    menu:
        "Хмурая":
            show mt angry panama dress far with dspr
            "mt angry panama dress far"
            show mt angry panama dress with dspr
            "mt angry panama dress"
            show mt angry panama dress close with dspr
            "mt angry panama dress close"
            hide mt with dspr
            jump sprites_my_list_mt_panama_dress
        "Обычная":
            show mt normal panama dress far with dspr
            "mt normal panama dress far"
            show mt normal panama dress with dspr
            "mt normal panama dress"
            show mt normal panama dress close with dspr
            "mt normal panama dress close"
            hide mt with dspr
            jump sprites_my_list_mt_panama_dress
        "Злость":
            show mt rage panama dress far with dspr
            "mt rage panama dress far"
            show mt rage panama dress with dspr
            "mt rage panama dress"
            show mt rage panama dress close with dspr
            "mt rage panama dress close"
            hide mt with dspr
            jump sprites_my_list_mt_panama_dress
        "Расстроенная":
            show mt sad panama dress far with dspr
            "mt sad panama dress far"
            show mt sad panama dress with dspr
            "mt sad panama dress"
            show mt sad panama dress close with dspr
            "mt sad panama dress close"
            hide mt with dspr
            jump sprites_my_list_mt_panama_dress
        "Испуганная":
            show mt scared panama dress far with dspr
            "mt scared panama dress"
            show mt scared panama dress with dspr
            "mt scared panama dress"
            show mt scared panama dress close with dspr
            "mt scared panama dress close"
            hide mt with dspr
            jump sprites_my_list_mt_panama_dress
        "Шокированная":
            show mt shocked panama dress far with dspr
            "mt shocked panama dress"
            show mt shocked panama dress with dspr
            "mt shocked panama dress"
            show mt shocked panama dress close with dspr
            "mt shocked panama dress"
            hide mt with dspr
            jump sprites_my_list_mt_panama_dress
        "Улыбка":
            show mt smile panama dress far with dspr
            "mt smile panama dress far"
            show mt smile panama dress with dspr
            "mt smile panama dress"
            show mt smile panama dress close with dspr
            "mt smile panama dress close"
            hide mt with dspr
            jump sprites_my_list_mt_panama_dress
        "Удивлённая":
            show mt surprise panama dress far with dspr
            "mt surprise panama dress far"
            show mt surprise panama dress with dspr
            "mt surprise panama dress"
            show mt surprise panama dress close with dspr
            "mt surprise panama dress close"
            hide mt with dspr
            jump sprites_my_list_mt_panama_dress
        ">>Назад<<":
            jump sprites_my_list_mt_normal

label sprites_my_list_mt_panama_swim:
    menu:
        "Хмурая":
            show mt angry panama swim far with dspr
            "mt angry panama swim far"
            show mt angry panama swim with dspr
            "mt angry panama swim"
            show mt angry panama swim close with dspr
            "mt angry panama swim close"
            hide mt with dspr
            jump sprites_my_list_mt_panama_swim
        "Обычная":
            show mt normal panama swim far with dspr
            "mt normal panama swim far"
            show mt normal panama swim with dspr
            "mt normal panama swim"
            show mt normal panama swim close with dspr
            "mt normal panama swim close"
            hide mt with dspr
            jump sprites_my_list_mt_panama_swim
        "Злость":
            show mt rage panama swim far with dspr
            "mt rage panama swim far"
            show mt rage panama swim with dspr
            "mt rage panama swim"
            show mt rage panama swim close with dspr
            "mt rage panama swim close"
            hide mt with dspr
            jump sprites_my_list_mt_panama_swim
        "Расстроенная":
            show mt sad panama swim far with dspr
            "mt sad panama swim far"
            show mt sad panama swim with dspr
            "mt sad panama swim"
            show mt sad panama swim close with dspr
            "mt sad panama swim close"
            hide mt with dspr
            jump sprites_my_list_mt_panama_swim
        "Испуганная":
            show mt scared panama swim far with dspr
            "mt scared panama swim"
            show mt scared panama swim with dspr
            "mt scared panama swim"
            show mt scared panama swim close with dspr
            "mt scared panama swim close"
            hide mt with dspr
            jump sprites_my_list_mt_panama_swim
        "Шокированная":
            show mt shocked panama swim far with dspr
            "mt shocked panama swim"
            show mt shocked panama swim with dspr
            "mt shocked panama swim"
            show mt shocked panama swim close with dspr
            "mt shocked panama swim"
            hide mt with dspr
            jump sprites_my_list_mt_panama_swim
        "Улыбка":
            show mt smile panama swim far with dspr
            "mt smile panama swim far"
            show mt smile panama swim with dspr
            "mt smile panama swim"
            show mt smile panama swim close with dspr
            "mt smile panama swim close"
            hide mt with dspr
            jump sprites_my_list_mt_panama_swim
        "Удивлённая":
            show mt surprise panama swim far with dspr
            "mt surprise panama swim far"
            show mt surprise panama swim with dspr
            "mt surprise panama swim"
            show mt surprise panama swim close with dspr
            "mt surprise panama swim close"
            hide mt with dspr
            jump sprites_my_list_mt_panama_swim
        ">>Назад<<":
            jump sprites_my_list_mt_normal

label sprites_my_list_uv:
    menu:
        "Неприязнь":
            show uv dontlike far with dspr
            "uv dontlike far"
            show uv dontlike with dspr
            "uv dontlike "
            show uv dontlike close with dspr
            "uv dontlike close"
            hide uv with dspr
            jump sprites_my_list_uv
        "Усмешка":
            show uv grin far with dspr
            "uv grin far"
            show uv grin with dspr
            "uv grin "
            show uv grin close with dspr
            "uv grin close"
            hide uv with dspr
            jump sprites_my_list_uv
        "Виноватая":
            show uv guilty far with dspr
            "uv guilty far"
            show uv guilty with dspr
            "uv guilty "
            show uv guilty close with dspr
            "uv guilty close"
            hide uv with dspr
            jump sprites_my_list_uv
        "Смех":
            show uv laugh far with dspr
            "uv laugh far"
            show uv laugh with dspr
            "uv laugh "
            show uv laugh close with dspr
            "uv laugh close"
            hide uv with dspr
            jump sprites_my_list_uv
        "Обычная":
            show uv normal far with dspr
            "uv normal far"
            show uv normal with dspr
            "uv normal "
            show uv normal close with dspr
            "uv normal close"
            hide uv with dspr
            jump sprites_my_list_uv
        "Злость":
            show uv rage far with dspr
            "uv rage far"
            show uv rage with dspr
            "uv rage "
            show uv rage close with dspr
            "uv rage close"
            hide uv with dspr
            jump sprites_my_list_uv
        "Грустная":
            show uv sad far with dspr
            "uv sad far"
            show uv sad with dspr
            "uv sad "
            show uv sad close with dspr
            "uv sad close"
            hide uv with dspr
            jump sprites_my_list_uv
        "Шокированная":
            show uv shocked far with dspr
            "uv shocked far"
            show uv shocked with dspr
            "uv shocked "
            show uv shocked close with dspr
            "uv shocked close"
            hide uv with dspr
            jump sprites_my_list_uv
        "Улыбка":
            show uv smile far with dspr
            "uv smile far"
            show uv smile with dspr
            "uv smile "
            show uv smile close with dspr
            "uv smile close"
            hide uv with dspr
            jump sprites_my_list_uv
        "Удивлённая":
            show uv surprise far with dspr
            "uv surprise far"
            show uv surprise with dspr
            "uv surprise "
            show uv surprise close with dspr
            "uv surprise close"
            hide uv with dspr
            jump sprites_my_list_uv
        "Удивлённая(2)":
            show uv surprise2 far with dspr
            "uv surprise2 far"
            show uv surprise2 with dspr
            "uv surprise2 "
            show uv surprise2 close with dspr
            "uv surprise2 close"
            hide uv with dspr
            jump sprites_my_list_uv
        "Расстроенная":
            show uv upset far with dspr
            "uv upset far"
            show uv upset with dspr
            "uv upset "
            show uv upset close with dspr
            "uv upset close"
            hide uv with dspr
            jump sprites_my_list_uv
        ">>Назад<<":
            jump sprites_my_list

label sprites_my_list_mz:
    menu:
        "Очки":
            jump sprites_my_list_mz_glasses
        "Без очков":
            jump sprites_my_list_mz_normal
        ">>Назад<<":
            jump sprites_my_list

label sprites_my_list_mz_glasses:
    menu:
        "Хмурая":
            show mz angry glasses pioneer far with dspr
            "mz angry glasses pioneer far"
            show mz angry glasses pioneer with dspr
            "mz angry glasses pioneer"
            show mz angry glasses pioneer close with dspr
            "mz angry glasses pioneer close"
            hide mz with dspr
            jump sprites_my_list_mz_glasses
        "Бука":
            show mz bukal glasses pioneer far with dspr
            "mz bukal glasses pioneer far"
            show mz bukal glasses pioneer with dspr
            "mz bukal glasses pioneer"
            show mz bukal glasses pioneer close with dspr
            "mz bukal glasses pioneer close"
            hide mz with dspr
            jump sprites_my_list_mz_glasses
        "Смех":
            show mz laugh glasses pioneer far with dspr
            "mz laugh glasses pioneer far"
            show mz laugh glasses pioneer with dspr
            "mz laugh glasses pioneer"
            show mz laugh glasses pioneer close with dspr
            "mz laugh glasses pioneer close"
            hide mz with dspr
            jump sprites_my_list_mz_glasses
        "Обычная":
            show mz normal glasses pioneer far with dspr
            "mz normal glasses pioneer far"
            show mz normal glasses pioneer with dspr
            "mz normal glasses pioneer"
            show mz normal glasses pioneer close with dspr
            "mz normal glasses pioneer close"
            hide mz with dspr
            jump sprites_my_list_mz_glasses
        "Злость":
            show mz rage glasses pioneer far with dspr
            "mz rage glasses pioneer far"
            show mz rage glasses pioneer with dspr
            "mz rage glasses pioneer"
            show mz rage glasses pioneer close with dspr
            "mz rage glasses pioneer close"
            hide mz with dspr
            jump sprites_my_list_mz_glasses
        "Застенчивая":
            show mz shy glasses pioneer far with dspr
            "mz shy glasses pioneer far"
            show mz shy glasses pioneer with dspr
            "mz shy glasses pioneer"
            show mz shy glasses pioneer close with dspr
            "mz shy glasses pioneer close"
            hide mz with dspr
            jump sprites_my_list_mz_glasses
        "Улыбка":
            show mz smile glasses pioneer far with dspr
            "mz smile glasses pioneer far"
            show mz smile glasses pioneer with dspr
            "mz smile glasses pioneer"
            show mz smile glasses pioneer close with dspr
            "mz smile glasses pioneer close"
            hide mz with dspr
            jump sprites_my_list_mz_glasses
        ">>Назад<<":
            jump sprites_my_list_mz

label sprites_my_list_mz_normal:
    menu:
        "Хмурая":
            show mz angry pioneer far with dspr
            "mz angry pioneer far"
            show mz angry pioneer with dspr
            "mz angry pioneer"
            show mz angry pioneer close with dspr
            "mz angry pioneer close"
            hide mz with dspr
            jump sprites_my_list_mz_normal
        "Бука":
            show mz bukal pioneer far with dspr
            "mz bukal pioneer far"
            show mz bukal pioneer with dspr
            "mz bukal pioneer"
            show mz bukal pioneer close with dspr
            "mz bukal pioneer close"
            hide mz with dspr
            jump sprites_my_list_mz_normal
        "Смех":
            show mz laugh pioneer far with dspr
            "mz laugh pioneer far"
            show mz laugh pioneer with dspr
            "mz laugh pioneer"
            show mz laugh pioneer close with dspr
            "mz laugh pioneer close"
            hide mz with dspr
            jump sprites_my_list_mz_normal
        "Обычная":
            show mz normal pioneer far with dspr
            "mz normal pioneer far"
            show mz normal pioneer with dspr
            "mz normal pioneer"
            show mz normal pioneer close with dspr
            "mz normal pioneer close"
            hide mz with dspr
            jump sprites_my_list_mz_normal
        "Злость":
            show mz rage pioneer far with dspr
            "mz rage pioneer far"
            show mz rage pioneer with dspr
            "mz rage pioneer"
            show mz rage pioneer close with dspr
            "mz rage pioneer close"
            hide mz with dspr
            jump sprites_my_list_mz_normal
        "Застенчивая":
            show mz shy pioneer far with dspr
            "mz shy pioneer far"
            show mz shy pioneer with dspr
            "mz shy pioneer"
            show mz shy pioneer close with dspr
            "mz shy pioneer close"
            hide mz with dspr
            jump sprites_my_list_mz_normal
        "Улыбка":
            show mz smile pioneer far with dspr
            "mz smile pioneer far"
            show mz smile pioneer with dspr
            "mz smile pioneer"
            show mz smile pioneer close with dspr
            "mz smile pioneer close"
            hide mz with dspr
            jump sprites_my_list_mz_normal
        ">>Назад<<":
            jump sprites_my_list_mz

label sprites_my_list_cs:
    menu:
        "Обычная":
            jump sprites_my_list_cs_normal
        "Очки":
            jump sprites_my_list_cs_glasses
        "Стетоскоп":
            jump sprites_my_list_cs_stethoscope
        ">>Назад<<":
            jump sprites_my_list

label sprites_my_list_cs_normal:
    menu:
        "Обычная":
            show cs normal far with dspr
            "cs normal far"
            show cs normal with dspr
            "cs normal"
            show cs normal close with dspr
            "cs normal close"
            hide cs with dspr
            jump sprites_my_list_cs_normal
        "Улыбка":
            show cs smile far with dspr
            "cs smile far"
            show cs smile with dspr
            "cs smile"
            show cs smile close with dspr
            "cs smile close"
            hide cs with dspr
            jump sprites_my_list_cs_normal
        "Застенчивая":
            show cs shy far with dspr
            "cs shy far"
            show cs shy with dspr
            "cs shy"
            show cs shy close with dspr
            "cs shy close"
            hide cs with dspr
            jump sprites_my_list_cs_normal
        ">>Назад<<":
            jump sprites_my_list_cs

label sprites_my_list_cs_glasses:
    menu:
        "Обычная":
            show cs normal glasses far with dspr
            "cs normal glasses far"
            show cs normal glasses with dspr
            "cs normal glasses"
            show cs normal glasses close with dspr
            "cs normal glasses close"
            hide cs with dspr
            jump sprites_my_list_cs_glasses
        "Улыбка":
            show cs smile glasses far with dspr
            "cs smile glasses far"
            show cs smile glasses with dspr
            "cs smile glasses"
            show cs smile glasses close with dspr
            "cs smile glasses close"
            hide cs with dspr
            jump sprites_my_list_cs_glasses
        "Застенчивая":
            show cs shy glasses far with dspr
            "cs shy glasses far"
            show cs shy glasses with dspr
            "cs shy glasses"
            show cs shy glasses close with dspr
            "cs shy glasses close"
            hide cs with dspr
            jump sprites_my_list_cs_glasses
        ">>Назад<<":
            jump sprites_my_list_cs

label sprites_my_list_cs_stethoscope:
    menu:
        "Обычная":
            show cs normal stethoscope far with dspr
            "cs normal stethoscope far"
            show cs normal stethoscope with dspr
            "cs normal stethoscope"
            show cs normal stethoscope close with dspr
            "cs normal stethoscope close"
            hide cs with dspr
            jump sprites_my_list_cs_stethoscope
        "Улыбка":
            show cs smile stethoscope far with dspr
            "cs smile stethoscope far"
            show cs smile stethoscope with dspr
            "cs smile stethoscope"
            show cs smile stethoscope close with dspr
            "cs smile stethoscope close"
            hide cs with dspr
            jump sprites_my_list_cs_stethoscope
        "Застенчивая":
            show cs shy stethoscope far with dspr
            "cs shy stethoscope far"
            show cs shy stethoscope with dspr
            "cs shy stethoscope"
            show cs shy stethoscope close with dspr
            "cs shy stethoscope close"
            hide cs with dspr
            jump sprites_my_list_cs_stethoscope
        ">>Назад<<":
            jump sprites_my_list_cs

label sprites_my_list_el:
    menu:
        "Фингал":
            show el fingal pioneer far with dspr
            "el fingal pioneer far"
            show el fingal pioneer with dspr
            "el fingal pioneer"
            show el fingal pioneer close with dspr
            "el fingal pioneer close"
            hide el with dspr
            jump sprites_my_list_el
        "Хмурый":
            show el angry pioneer far with dspr
            "el angry pioneer far"
            show el angry pioneer with dspr
            "el angry pioneer"
            show el angry pioneer close with dspr
            "el angry pioneer close"
            hide el with dspr
            jump sprites_my_list_el
        "Усмешка":
            show el grin pioneer far with dspr
            "el grin pioneer far"
            show el grin pioneer with dspr
            "el grin pioneer"
            show el grin pioneer close with dspr
            "el grin pioneer close"
            hide el with dspr
            jump sprites_my_list_el
        "Смех":
            show el laugh pioneer far with dspr
            "el laugh pioneer far"
            show el laugh pioneer with dspr
            "el laugh pioneer"
            show el laugh pioneer close with dspr
            "el laugh pioneer close"
            hide el with dspr
            jump sprites_my_list_el
        "Обычный":
            show el normal pioneer far with dspr
            "el normal pioneer far"
            show el normal pioneer with dspr
            "el normal pioneer"
            show el normal pioneer close with dspr
            "el normal pioneer close"
            hide el with dspr
            jump sprites_my_list_el
        "Грустный":
            show el sad pioneer far with dspr
            "el sad pioneer far"
            show el sad pioneer with dspr
            "el sad pioneer"
            show el sad pioneer close with dspr
            "el sad pioneer close"
            hide el with dspr
            jump sprites_my_list_el
        "Scared":
            show el scared pioneer far with dspr
            "el scared pioneer far"
            show el scared pioneer with dspr
            "el scared pioneer"
            show el scared pioneer close with dspr
            "el scared pioneer close"
            hide el with dspr
            jump sprites_my_list_el
        "Серьёзный":
            show el serious pioneer far with dspr
            "el serious pioneer far"
            show el serious pioneer with dspr
            "el serious pioneer"
            show el serious pioneer close with dspr
            "el serious pioneer close"
            hide el with dspr
            jump sprites_my_list_el
        "Шокированный":
            show el shocked pioneer far with dspr
            "el shocked pioneer far"
            show el shocked pioneer with dspr
            "el shocked pioneer"
            show el shocked pioneer close with dspr
            "el shocked pioneer close"
            hide el with dspr
            jump sprites_my_list_el
        "Улыбка":
            show el smile pioneer far with dspr
            "el smile pioneer far"
            show el smile pioneer with dspr
            "el smile pioneer"
            show el smile pioneer close with dspr
            "el smile pioneer close"
            hide el with dspr
            jump sprites_my_list_el
        "Удивлённый":
            show el surprise pioneer far with dspr
            "el surprise pioneer far"
            show el surprise pioneer with dspr
            "el surprise pioneer"
            show el surprise pioneer close with dspr
            "el surprise pioneer close"
            hide el with dspr
            jump sprites_my_list_el
        "Расстроенный":
            show el upset pioneer far with dspr
            "el angry pioneer far"
            show el angry pioneer with dspr
            "el angry pioneer"
            show el angry pioneer close with dspr
            "el angry pioneer close"
            hide el with dspr
            jump sprites_my_list_el
        ">>Назад<<":
            jump sprites_my_list

label sprites_my_list_sh:
    menu:
        "Обычный":
            jump sprites_my_list_sh_1
        "Очки":
            jump sprites_my_list_sh_2
        ">>Назад<<":
            jump sprites_my_list

label sprites_my_list_sh_1:
    menu:
        "Плачущий":
            show sh cry far with dspr
            "sh cry far"
            show sh cry with dspr
            "sh cry"
            show sh cry close with dspr
            "sh cry close"
            hide sh with dspr
            jump sprites_my_list_sh_1
        "Смех":
            show sh laugh far with dspr
            "sh laugh far"
            show sh laugh with dspr
            "sh laugh"
            show sh laugh close with dspr
            "sh laugh close"
            hide sh with dspr
            jump sprites_my_list_sh_1
        "Обычный":
            show sh normal far with dspr
            "sh normal far"
            show sh normal with dspr
            "sh normal"
            show sh normal close with dspr
            "sh normal close"
            hide sh with dspr
            jump sprites_my_list_sh_1
        "Дежурная улыбка":
            show sh normal_smile far with dspr
            "sh normal_smile far"
            show sh normal_smile with dspr
            "sh normal_smile"
            show sh normal_smile close with dspr
            "sh normal_smile close"
            hide sh with dspr
            jump sprites_my_list_sh_1
        "Злость":
            show sh rage far with dspr
            "sh rage far"
            show sh rage with dspr
            "sh rage"
            show sh rage close with dspr
            "sh rage close"
            hide sh with dspr
            jump sprites_my_list_sh_1
        "Испуганный":
            show sh scared far with dspr
            "sh scared far"
            show sh scared with dspr
            "sh scared"
            show sh scared close with dspr
            "sh scared close"
            hide sh with dspr
            jump sprites_my_list_sh_1
        "Серьёзный":
            show sh serious far with dspr
            "sh serious far"
            show sh serious with dspr
            "sh serious"
            show sh serious close with dspr
            "sh serious close"
            hide sh with dspr
            jump sprites_my_list_sh_1
        "Улыбка":
            show sh smile far with dspr
            "sh smile far"
            show sh smile with dspr
            "sh smile"
            show sh smile close with dspr
            "sh smile close"
            hide sh with dspr
            jump sprites_my_list_sh_1
        "Удивлённый":
            show sh surprise far with dspr
            "sh surprise far"
            show sh surprise with dspr
            "sh surprise"
            show sh surprise close with dspr
            "sh surprise close"
            hide sh with dspr
            jump sprites_my_list_sh_1
        "Расстроенный":
            show sh upset far with dspr
            "sh upset far"
            show sh upset with dspr
            "sh upset"
            show sh upset close with dspr
            "sh upset close"
            hide sh with dspr
            jump sprites_my_list_sh_1
        ">>Назад<<":
            jump sprites_my_list_sh

label sprites_my_list_sh_2:
    menu:
        "Плачущий":
            show sh cry pioneer far with dspr
            "sh cry pioneer far"
            show sh cry pioneer with dspr
            "sh cry pioneer"
            show sh cry pioneer close with dspr
            "sh cry pioneer close"
            hide sh with dspr
            jump sprites_my_list_sh_2
        "Смех":
            show sh laugh pioneer far with dspr
            "sh laugh pioneer far"
            show sh laugh pioneer with dspr
            "sh laugh pioneer"
            show sh laugh pioneer close with dspr
            "sh laugh pioneer close"
            hide sh with dspr
            jump sprites_my_list_sh_2
        "Обычный":
            show sh normal pioneer far with dspr
            "sh normal pioneer far"
            show sh normal pioneer with dspr
            "sh normal pioneer"
            show sh normal pioneer close with dspr
            "sh normal pioneer close"
            hide sh with dspr
            jump sprites_my_list_sh_2
        "Дежурная улыбка":
            show sh normal_smile pioneer far with dspr
            "sh normal_smile pioneer far"
            show sh normal_smile pioneer with dspr
            "sh normal_smile pioneer"
            show sh normal_smile pioneer close with dspr
            "sh normal_smile pioneer close"
            hide sh with dspr
            jump sprites_my_list_sh_2
        "Злость":
            show sh rage pioneer far with dspr
            "sh rage pioneer far"
            show sh rage pioneer with dspr
            "sh rage pioneer"
            show sh rage pioneer close with dspr
            "sh rage pioneer close"
            hide sh with dspr
            jump sprites_my_list_sh_2
        "Испуганный":
            show sh scared pioneer far with dspr
            "sh scared pioneer far"
            show sh scared pioneer with dspr
            "sh scared pioneer"
            show sh scared pioneer close with dspr
            "sh scared pioneer close"
            hide sh with dspr
            jump sprites_my_list_sh_2
        "Серьёзный":
            show sh serious pioneer far with dspr
            "sh serious pioneer far"
            show sh serious pioneer with dspr
            "sh serious pioneer"
            show sh serious pioneer close with dspr
            "sh serious pioneer close"
            hide sh with dspr
            jump sprites_my_list_sh_2
        "Улыбка":
            show sh smile pioneer far with dspr
            "sh smile pioneer far"
            show sh smile pioneer with dspr
            "sh smile pioneer"
            show sh smile pioneer close with dspr
            "sh smile pioneer close"
            hide sh with dspr
            jump sprites_my_list_sh_2
        "Удивлённый":
            show sh surprise pioneer far with dspr
            "sh surprise pioneer far"
            show sh surprise pioneer with dspr
            "sh surprise pioneer"
            show sh surprise pioneer close with dspr
            "sh surprise pioneer close"
            hide sh with dspr
            jump sprites_my_list_sh_2
        "Расстроенный":
            show sh upset pioneer far with dspr
            "sh upset pioneer far"
            show sh upset pioneer with dspr
            "sh upset pioneer"
            show sh upset pioneer close with dspr
            "sh upset pioneer close"
            hide sh with dspr
            jump sprites_my_list_sh_2
        ">>Назад<<":
            jump sprites_my_list_sh

label sprites_my_list_pi:
    menu:
        "Обычный":
            show pi far with dspr
            "pi far"
            show pi with dspr
            "pi"
            show pi close with dspr
            "pi close"
            hide pi with dspr
            jump sprites_my_list_pi
        "Улыбка":
            show pi smile far with dspr
            "pi smile far"
            show pi smile with dspr
            "pi smile"
            show pi smile close with dspr
            "pi smile close"
            hide pi with dspr
            jump sprites_my_list_pi
        ">>Назад<<":
            jump sprites_my_list

#Start of English version
label my_list_eng:
    scene black
    show ss smile casual with dissolve
    ca "Hi, I was waiting for you!"
    show ss grin_smile casual with dspr
    ca "My name is Samantha,{w} and I'm here to show you all the possible sprites, backgrounds, pictures, music, ambient and of course sounds of the game."
    show ss grin casual with dspr
    ca "Well, let's see."
label start_my_list_eng:
    scene black
    menu:
        "Sprites":
            jump sprites_my_list_eng
        "Background":
            jump background_my_list_eng
        "Images":
            jump image_my_list_eng
        "Animations":
            jump exit_eng
        "Music":
            jump music_my_list_eng
        "Sound":
            jump exit_eng
        "Ambient":
            jump exit_eng
        ">>Quit<<":
            jump exit_eng

label exit_eng:
    show ss surprise casual with dspr
    ca "Do you really want to quit?"
    hide ss with dspr
    menu:
        "Yes, I do":
            show ss sad casual with dissolve
            ca "Ok..."
            $ renpy.pause (1)
            show ss serious casual with dspr
            ss "Just come back soon!"
            return
        "No":
            show ss smile casual with dspr
            $ renpy.pause (1)
            hide ss with dissolve
            jump start_my_list_eng

label sprites_my_list_eng:
    menu:
        "Alisa":
            jump sprites_my_list_dv_eng
        "Slavya":
            jump sprites_my_list_sl_eng
        "Lena":
            jump sprites_my_list_un_eng
        "Miku":
            jump sprites_my_list_mi_eng
        "Ulyana":
            jump sprites_my_list_us_eng
        "Olga Dmitrievna":
            jump sprites_my_list_mt_eng
        "Yulya":
            jump sprites_my_list_uv_eng
        "Zhenya":
            jump sprites_my_list_mz_eng
        "Viola":
            jump sprites_my_list_cs_eng
        "Ell":
            jump sprites_my_list_el_eng
        "Shurik":
            jump sprites_my_list_sh_eng
        "Pioneer":
            jump sprites_my_list_pi_eng
        "Samantha":
            show ss sad casual with dspr
            ca "I'm not in the original sprites of {i}Everlasting Summer.{/i}"
            show ss normal casual with dspr
            ca "But you can add me in your mod independently."
            show ss laugh casual with dspr
            ca "Here are my sprites."
            hide ss with dspr
            jump sprites_my_list_ss_eng
        ">>Back<<":
            show ss serious casual with dspr
            ca "Already seen enough?"
            jump start_my_list_eng

label sprites_my_list_ss_eng:
    menu:
        "Casual":
            jump sprites_my_list_ss_casual_eng
        "Fancy":
            jump sprites_my_list_ss_fancy_eng
        ">>Back<<":
            jump sprites_my_list_eng

label sprites_my_list_ss_casual_eng:
    menu:
        "Sad":
            show ss sad casual with dspr
            "(variable name) sad casual"
            hide ss sad casual with dspr
            jump sprites_my_list_ss_casual_eng
        "Scared":
            show ss scared casual with dspr
            "(variable name) scared casual"
            hide ss scared casual with dspr
            jump sprites_my_list_ss_casual_eng
        "Cry(1)":
            show ss cry casual with dspr
            "(variable name) cry casual"
            hide ss with dspr
            jump sprites_my_list_ss_casual_eng
        "Cry(2)":
            show ss cry2 casual with dspr
            "(variable name) cry2 casual"
            hide ss cry2 casual with dspr
            jump sprites_my_list_ss_casual_eng
        "Shy(1)":
            show ss shy casual with dspr
            "(variable name) shy casual"
            hide ss shy casual with dspr
            jump sprites_my_list_ss_casual_eng
        "Shy(2)":
            show ss shy2 casual with dspr
            "(variable name) shy2 casual"
            hide ss shy2 casual with dspr
            jump sprites_my_list_ss_casual_eng
        "Unsmile":
            show ss nosmile casual with dspr
            "(variable name) nosmile casual"
            hide ss with dspr
            jump sprites_my_list_ss_casual_eng
        "Crysmile(1)":
            show ss crysmile casual with dspr
            "(variable name) crysmile casual"
            hide ss with dspr
            jump sprites_my_list_ss_casual_eng
        "Crysmile(2)":
            show ss crysmile2 casual with dspr
            "(variable name) crysmile2 casual"
            hide ss with dspr
            jump sprites_my_list_ss_casual_eng
        "Normal":
            show ss normal casual with dspr
            "(variable name) normal casual"
            hide ss with dspr
            jump sprites_my_list_ss_casual_eng
        "Unsure":
            show ss unsure casual with dspr
            "(variable name) unsure casual"
            hide ss with dspr
            jump sprites_my_list_ss_casual_eng
        "Surprised":
            show ss surprise casual with dspr
            "(variable name) surprise casual"
            hide ss with dspr
            jump sprites_my_list_ss_casual_eng
        "Grin":
            show ss grin_smile casual with dspr
            "(variable name) grin casual"
            hide ss with dspr
            jump sprites_my_list_ss_casual_eng
        "Grin":
            show ss grin casual with dspr
            "(variable name) grin casual"
            hide ss with dspr
            jump sprites_my_list_ss_casual_eng
        "Laugh":
            show ss laugh casual with dspr
            "(variable name) laugh casual"
            hide ss with dspr
            jump sprites_my_list_ss_casual_eng
        "Smile(1)":
            show ss smile casual with dspr
            "(variable name) smile casual"
            hide ss with dspr
            jump sprites_my_list_ss_casual_eng
        "Smile(2)":
            show ss smile2 casual with dspr
            "(variable name) smile2 casual"
            hide ss with dspr
            jump sprites_my_list_ss_casual_eng
        "Rage":
            show ss vangry casual with dspr
            "(variable name) vangry casual"
            hide ss with dspr
            jump sprites_my_list_ss_casual_eng
        "Angry":
            show ss angry casual with dspr
            "(variable name) angry casual"
            hide ss with dspr
            jump sprites_my_list_ss_casual_eng
        "Serious":
            show ss serious casual with dspr
            "(variable name) serious casual"
            hide ss with dspr
            jump sprites_my_list_ss_casual_eng
        ">>Back<<":
            jump sprites_my_list_ss_eng

label sprites_my_list_ss_fancy_eng:
    menu:
        "Sad":
            show ss sad fancy with dspr
            "(variable name) sad fancy"
            hide ss sad fancy with dspr
            jump sprites_my_list_ss_fancy_eng
        "Scared":
            show ss scared fancy with dspr
            "(variable name) scared fancy"
            hide ss scared fancy with dspr
            jump sprites_my_list_ss_fancy_eng
        "Cry(1)":
            show ss cry fancy with dspr
            "(variable name) cry fancy"
            hide ss with dspr
            jump sprites_my_list_ss_fancy_eng
        "Cry(2)":
            show ss cry2 fancy with dspr
            "(variable name) cry2 fancy"
            hide ss cry2 fancy with dspr
            jump sprites_my_list_ss_fancy_eng
        "Shy(1)":
            show ss shy fancy with dspr
            "(variable name) shy fancy"
            hide ss shy fancy with dspr
            jump sprites_my_list_ss_fancy_eng
        "Shy(2)":
            show ss shy2 fancy with dspr
            "(variable name) shy2 fancy"
            hide ss shy2 fancy with dspr
            jump sprites_my_list_ss_fancy_eng
        "Unsmiling":
            show ss nosmile fancy with dspr
            "(variable name) nosmile fancy"
            hide ss with dspr
            jump sprites_my_list_ss_fancy_eng
        "Crysmile(1)":
            show ss crysmile fancy with dspr
            "(variable name) crysmile fancy"
            hide ss with dspr
            jump sprites_my_list_ss_fancy_eng
        "Crysmile(2)":
            show ss crysmile2 fancy with dspr
            "(variable name) crysmile2 fancy"
            hide ss with dspr
            jump sprites_my_list_ss_fancy_eng
        "Normal":
            show ss normal fancy with dspr
            "(variable name) normal fancy"
            hide ss with dspr
            jump sprites_my_list_ss_fancy_eng
        "Unsure":
            show ss unsure fancy with dspr
            "(variable name) unsure fancy"
            hide ss with dspr
            jump sprites_my_list_ss_fancy_eng
        "Surprised":
            show ss surprise fancy with dspr
            "(variable name) surprise fancy"
            hide ss with dspr
            jump sprites_my_list_ss_fancy_eng
        "Grin":
            show ss grin_smile fancy with dspr
            "(variable name) grin fancy"
            hide ss with dspr
            jump sprites_my_list_ss_fancy_eng
        "Grin":
            show ss grin fancy with dspr
            "(variable name) grin fancy"
            hide ss with dspr
            jump sprites_my_list_ss_fancy_eng
        "Laugh":
            show ss laugh fancy with dspr
            "(variable name) laugh fancy"
            hide ss with dspr
            jump sprites_my_list_ss_fancy_eng
        "Smile(1)":
            show ss smile fancy with dspr
            "(variable name) smile fancy"
            hide ss with dspr
            jump sprites_my_list_ss_fancy_eng
        "Smile(2)":
            show ss smile2 fancy with dspr
            "(variable name) smile2 fancy"
            hide ss with dspr
            jump sprites_my_list_ss_fancy_eng
        "Rage":
            show ss vangry fancy with dspr
            "(variable name) vangry fancy"
            hide ss with dspr
            jump sprites_my_list_ss_fancy_eng
        "Angry":
            show ss angry fancy with dspr
            "(variable name) angry fancy"
            hide ss with dspr
            jump sprites_my_list_ss_fancy_eng
        "Serious":
            show ss serious fancy with dspr
            "(variable name) serious fancy"
            hide ss with dspr
            jump sprites_my_list_ss_fancy_eng
        ">>Back<<":
            jump sprites_my_list_ss_eng

label sprites_my_list_dv_eng:
    menu:
        "Pioneer Form":
            jump sprites_my_list_dv_pioneer_eng
        "Pioneer Form with knot":
            jump sprites_my_list_dv_pioneer2_eng
        "Swimsuit":
            jump sprites_my_list_dv_swim_eng
        "Naked" if (persistent.hentai == True):
            jump sprites_my_list_dv_extra_eng
        ">>Back<<":
            jump sprites_my_list_eng

label sprites_my_list_dv_pioneer_eng:
    menu:
        "Angry":
            show dv angry pioneer far with dspr
            "dv angry pioneer far"
            show dv angry pioneer with dspr
            "dv angry pioneer"
            show dv angry pioneer close with dspr
            "dv angry pioneer close"
            hide dv with dspr
            jump sprites_my_list_dv_pioneer_eng
        "Cry":
            show dv cry pioneer far with dspr
            "dv cry pioneer far"
            show dv cry pioneer with dspr
            "dv cry pioneer"
            show dv cry pioneer close with dspr
            "dv cry pioneer close"
            hide dv with dspr
            jump sprites_my_list_dv_pioneer_eng
        "Grin":
            show dv grin pioneer far with dspr
            "dv grin pioneer far"
            show dv grin pioneer with dspr
            "dv grin pioneer"
            show dv grin pioneer close with dspr
            "dv grin pioneer close"
            hide dv with dspr
            jump sprites_my_list_dv_pioneer_eng
        "Guilty":
            show dv guilty pioneer far with dspr
            "dv guilty pioneer far"
            show dv guilty pioneer with dspr
            "dv guilty pioneer"
            show dv guilty pioneer close with dspr
            "dv guilty pioneer close"
            hide dv with dspr
            jump sprites_my_list_dv_pioneer_eng
        "Laugh":
            show dv laugh pioneer far with dspr
            "dv laugh pioneer far"
            show dv laugh pioneer with dspr
            "dv laugh pioneer"
            show dv laugh pioneer close with dspr
            "dv laugh pioneer close"
            hide dv with dspr
            jump sprites_my_list_dv_pioneer_eng
        "Normal":
            show dv normal pioneer far with dspr
            "dv normal pioneer far"
            show dv normal pioneer with dspr
            "dv normal pioneer"
            show dv normal pioneer close with dspr
            "dv normal pioneer close"
            hide dv with dspr
            jump sprites_my_list_dv_pioneer_eng
        "Rage":
            show dv rage pioneer far with dspr
            "dv rage pioneer far"
            show dv rage pioneer with dspr
            "dv rage pioneer"
            show dv rage pioneer close with dspr
            "dv rage pioneer close"
            hide dv with dspr
            jump sprites_my_list_dv_pioneer_eng
        "Scared":
            show dv scared pioneer far with dspr
            "dv scared pioneer far"
            show dv scared pioneer with dspr
            "dv scared pioneer"
            show dv scared pioneer close with dspr
            "dv scared pioneer close"
            hide dv with dspr
            jump sprites_my_list_dv_pioneer_eng
        "Sad":
            show dv sad pioneer far with dspr
            "dv sad pioneer far"
            show dv sad pioneer with dspr
            "dv sad pioneer"
            show dv sad pioneer close with dspr
            "dv sad pioneer close"
            hide dv with dspr
            jump sprites_my_list_dv_pioneer_eng
        "Shocked":
            show dv shocked pioneer far with dspr
            "dv shocked pioneer far"
            show dv shocked pioneer with dspr
            "dv shocked pioneer"
            show dv shocked pioneer close with dspr
            "dv shocked pioneer close"
            hide dv with dspr
            jump sprites_my_list_dv_pioneer_eng
        "Shy":
            show dv shy pioneer far with dspr
            "dv shy pioneer far"
            show dv shy pioneer with dspr
            "dv shy pioneer"
            show dv shy pioneer close with dspr
            "dv shy pioneer close"
            hide dv with dspr
            jump sprites_my_list_dv_pioneer_eng
        "Smile":
            show dv smile pioneer far with dspr
            "dv smile pioneer far"
            show dv smile pioneer with dspr
            "dv smile pioneer"
            show dv smile pioneer close with dspr
            "dv smile pioneer close"
            hide dv with dspr
            jump sprites_my_list_dv_pioneer_eng
        "Surprised":
            show dv surprise pioneer far with dspr
            "dv surprise pioneer far"
            show dv surprise pioneer with dspr
            "dv surprise pioneer"
            show dv surprise pioneer close with dspr
            "dv surprise pioneer close"
            hide dv with dspr
            jump sprites_my_list_dv_pioneer_eng
        ">>Back<<":
            jump sprites_my_list_dv_eng

label sprites_my_list_dv_pioneer2_eng:
    menu:
        "Angry":
            show dv angry pioneer2 far with dspr
            "dv angry pioneer2 far"
            show dv angry pioneer2 with dspr
            "dv angry pioneer2"
            show dv angry pioneer2 close with dspr
            "dv angry pioneer2 close"
            hide dv with dspr
            jump sprites_my_list_dv_pioneer2_eng
        "Cry":
            show dv cry pioneer2 far with dspr
            "dv cry pioneer2 far"
            show dv cry pioneer2 with dspr
            "dv cry pioneer2"
            show dv cry pioneer2 close with dspr
            "dv cry pioneer2 close"
            hide dv with dspr
            jump sprites_my_list_dv_pioneer2_eng
        "Grin":
            show dv grin pioneer2 far with dspr
            "dv grin pioneer2 far"
            show dv grin pioneer2 with dspr
            "dv grin pioneer2"
            show dv grin pioneer2 close with dspr
            "dv grin pioneer2 close"
            hide dv with dspr
            jump sprites_my_list_dv_pioneer2_eng
        "Guilty":
            show dv guilty pioneer2 far with dspr
            "dv guilty pioneer2 far"
            show dv guilty pioneer2 with dspr
            "dv guilty pioneer2"
            show dv guilty pioneer2 close with dspr
            "dv guilty pioneer2 close"
            hide dv with dspr
            jump sprites_my_list_dv_pioneer2_eng
        "Laugh":
            show dv laugh pioneer2 far with dspr
            "dv laugh pioneer2 far"
            show dv laugh pioneer2 with dspr
            "dv laugh pioneer2"
            show dv laugh pioneer2 close with dspr
            "dv laugh pioneer2 close"
            hide dv with dspr
            jump sprites_my_list_dv_pioneer2_eng
        "Normal":
            show dv normal pioneer2 far with dspr
            "dv normal pioneer2 far"
            show dv normal pioneer2 with dspr
            "dv normal pioneer2"
            show dv normal pioneer2 close with dspr
            "dv normal pioneer2 close"
            hide dv with dspr
            jump sprites_my_list_dv_pioneer2_eng
        "Rage":
            show dv rage pioneer2 far with dspr
            "dv rage pioneer2 far"
            show dv rage pioneer2 with dspr
            "dv rage pioneer2"
            show dv rage pioneer2 close with dspr
            "dv rage pioneer2 close"
            hide dv with dspr
            jump sprites_my_list_dv_pioneer2_eng
        "Scared":
            show dv scared pioneer2 far with dspr
            "dv scared pioneer2 far"
            show dv scared pioneer2 with dspr
            "dv scared pioneer2"
            show dv scared pioneer2 close with dspr
            "dv scared pioneer2 close"
            hide dv with dspr
            jump sprites_my_list_dv_pioneer2_eng
        "Sad":
            show dv sad pioneer2 far with dspr
            "dv sad pioneer2 far"
            show dv sad pioneer2 with dspr
            "dv sad pioneer2"
            show dv sad pioneer2 close with dspr
            "dv sad pioneer2 close"
            hide dv with dspr
            jump sprites_my_list_dv_pioneer2_eng
        "Shocked":
            show dv shocked pioneer2 far with dspr
            "dv shocked pioneer2 far"
            show dv shocked pioneer2 with dspr
            "dv shocked pioneer2"
            show dv shocked pioneer2 close with dspr
            "dv shocked pioneer2 close"
            hide dv with dspr
            jump sprites_my_list_dv_pioneer2_eng
        "Shy":
            show dv shy pioneer2 far with dspr
            "dv shy pioneer2 far"
            show dv shy pioneer2 with dspr
            "dv shy pioneer2"
            show dv shy pioneer2 close with dspr
            "dv shy pioneer2 close"
            hide dv with dspr
            jump sprites_my_list_dv_pioneer2_eng
        "Smile":
            show dv smile pioneer2 far with dspr
            "dv smile pioneer2 far"
            show dv smile pioneer2 with dspr
            "dv smile pioneer2"
            show dv smile pioneer2 close with dspr
            "dv smile pioneer2 close"
            hide dv with dspr
            jump sprites_my_list_dv_pioneer2_eng
        "Surprised":
            show dv surprise pioneer2 far with dspr
            "dv surprise pioneer2 far"
            show dv surprise pioneer2 with dspr
            "dv surprise pioneer2"
            show dv surprise pioneer2 close with dspr
            "dv surprise pioneer2 close"
            hide dv with dspr
            jump sprites_my_list_dv_pioneer2_eng
        ">>Back<<":
            jump sprites_my_list_dv_eng

label sprites_my_list_dv_swim_eng:
        menu:
            "Cry":
                show dv cry swim far with dspr
                "dv cry swim far"
                show dv cry swim with dspr
                "dv cry swim"
                show dv cry swim close with dspr
                "dv cry swim close"
                hide dv with dspr
                jump sprites_my_list_dv_swim_eng
            "Grin":
                show dv grin swim far with dspr
                "dv grin swim far"
                show dv grin swim with dspr
                "dv grin swim"
                show dv grin swim close with dspr
                "dv grin swim close"
                hide dv with dspr
                jump sprites_my_list_dv_swim_eng
            "Laugh":
                show dv laugh swim far with dspr
                "dv laugh swim far"
                show dv laugh swim with dspr
                "dv laugh swim"
                show dv laugh swim close with dspr
                "dv laugh swim close"
                hide dv with dspr
                jump sprites_my_list_dv_swim_eng
            "Normal":
                show dv normal swim far with dspr
                "dv normal swim far"
                show dv normal swim with dspr
                "dv normal swim"
                show dv normal swim close with dspr
                "dv normal swim close"
                hide dv with dspr
                jump sprites_my_list_dv_swim_eng
            "Scared":
                show dv scared swim far with dspr
                "dv scared swim far"
                show dv scared swim with dspr
                "dv scared swim"
                show dv scared swim close with dspr
                "dv scared swim close"
                hide dv with dspr
                jump sprites_my_list_dv_swim_eng
            "Shocked":
                show dv shocked swim far with dspr
                "dv shocked swim far"
                show dv shocked swim with dspr
                "dv shocked swim"
                show dv shocked swim close with dspr
                "dv shocked swim close"
                hide dv with dspr
                jump sprites_my_list_dv_swim_eng
            "Smile":
                show dv smile swim far with dspr
                "dv smile swim far"
                show dv smile swim with dspr
                "dv smile swim"
                show dv smile swim close with dspr
                "dv smile swim close"
                hide dv with dspr
                jump sprites_my_list_dv_swim_eng
            "Surprised":
                show dv surprise swim far with dspr
                "dv surprise swim far"
                show dv surprise swim with dspr
                "dv surprise swim"
                show dv surprise swim close with dspr
                "dv surprise swim close"
                hide dv with dspr
                jump sprites_my_list_dv_swim_eng
            ">>Back<<":
                jump sprites_my_list_dv_eng

label sprites_my_list_sl_eng:
   menu:
        "Pioneer Form":
            jump sprites_my_list_sl_pioneer_eng
        "Dress":
            jump sprites_my_list_sl_dress_eng
        "Sport uniform":
            jump sprites_my_list_sl_sport_eng
        "Swimsuit":
            jump sprites_my_list_sl_swim_eng
        ">>Back<<":
            jump sprites_my_list_eng

label sprites_my_list_sl_pioneer_eng:
    menu:
        "Angry":
            show sl angry pioneer far with dspr
            "sl angry pioneer far"
            show sl angry pioneer with dspr
            "sl angry pioneer"
            show sl angry pioneer close with dspr
            "sl angry pioneer close"
            hide sl with dspr
            jump sprites_my_list_sl_pioneer_eng
        "Happy":
            show sl happy pioneer far with dspr
            "sl happy pioneer far"
            show sl happy pioneer with dspr
            "sl happy pioneer"
            show sl happy pioneer close with dspr
            "sl happy pioneer close"
            hide sl with dspr
            jump sprites_my_list_sl_pioneer_eng
        "Laugh":
            show sl laugh pioneer far with dspr
            "sl laugh pioneer far"
            show sl laugh pioneer with dspr
            "sl laugh pioneer"
            show sl laugh pioneer close with dspr
            "sl laugh pioneer close"
            hide sl with dspr
            jump sprites_my_list_sl_pioneer_eng
        "Normal":
            show sl normal pioneer far with dspr
            "sl normal pioneer far"
            show sl normal pioneer with dspr
            "sl normal pioneer"
            show sl normal pioneer close with dspr
            "sl normal pioneer close"
            hide sl with dspr
            jump sprites_my_list_sl_pioneer_eng
        "Sad":
            show sl sad pioneer far with dspr
            "sl sad pioneer far"
            show sl sad pioneer with dspr
            "sl sad pioneer"
            show sl sad pioneer close with dspr
            "sl sad pioneer close"
            hide sl with dspr
            jump sprites_my_list_sl_pioneer_eng
        "Scared":
            show sl scared pioneer far with dspr
            "sl scared pioneer far"
            show sl scared pioneer with dspr
            "sl scared pioneer"
            show sl scared pioneer close with dspr
            "sl scared pioneer close"
            hide sl with dspr
            jump sprites_my_list_sl_pioneer_eng_eng
        "Serious":
            show sl serious pioneer far with dspr
            "sl serious pioneer far"
            show sl serious pioneer with dspr
            "sl serious pioneer"
            show sl serious pioneer close with dspr
            "sl serious pioneer close"
            hide sl with dspr
            jump sprites_my_list_sl_pioneer_eng
        "Shy":
            show sl shy pioneer far with dspr
            "sl shy pioneer far"
            show sl shy pioneer with dspr
            "sl shy pioneer"
            show sl shy pioneer close with dspr
            "sl shy pioneer close"
            hide sl with dspr
            jump sprites_my_list_sl_pioneer_eng
        "Smile(1)":
            show sl smile pioneer far with dspr
            "sl smile pioneer far"
            show sl smile pioneer with dspr
            "sl smile pioneer"
            show sl smile pioneer close with dspr
            "sl smile pioneer close"
            hide sl with dspr
            jump sprites_my_list_sl_pioneer_eng
        "Smile(2)":
            show sl smile2 pioneer far with dspr
            "sl smile2 pioneer far"
            show sl smile2 pioneer with dspr
            "sl smile2 pioneer"
            show sl smile2 pioneer close with dspr
            "sl smile2 pioneer close"
            hide sl with dspr
            jump sprites_my_list_sl_pioneer_eng
        "Surprised":
            show sl surprise pioneer far with dspr
            "sl surprise pioneer far"
            show sl surprise pioneer with dspr
            "sl surprise pioneer"
            show sl surprise pioneer close with dspr
            "sl surprise pioneer close"
            hide sl with dspr
            jump sprites_my_list_sl_pioneer_eng
        "Tender":
            show sl tender pioneer far with dspr
            "sl tender pioneer far"
            show sl tender pioneer with dspr
            "sl tender pioneer"
            show sl tender pioneer close with dspr
            "sl tender pioneer close"
            hide sl with dspr
            jump sprites_my_list_sl_pioneer_eng
        ">>Back<<":
            jump sprites_my_list_sl_eng

label sprites_my_list_sl_dress_eng:
    menu:
        "Angry":
            show sl angry dress far with dspr
            "sl angry dress far"
            show sl angry dress with dspr
            "sl angry dress"
            show sl angry dress close with dspr
            "sl angry dress close"
            hide sl with dspr
            jump sprites_my_list_sl_dress_eng
        "Happy":
            show sl happy dress far with dspr
            "sl happy dress far"
            show sl happy dress with dspr
            "sl happy dress"
            show sl happy dress close with dspr
            "sl happy dress close"
            hide sl with dspr
            jump sprites_my_list_sl_dress_eng
        "Laugh":
            show sl laugh dress far with dspr
            "sl laugh dress far"
            show sl laugh dress with dspr
            "sl laugh dress"
            show sl laugh dress close with dspr
            "sl laugh dress close"
            hide sl with dspr
            jump sprites_my_list_sl_dress_eng
        "Normal":
            show sl normal dress far with dspr
            "sl normal dress far"
            show sl normal dress with dspr
            "sl normal dress"
            show sl normal dress close with dspr
            "sl normal dress close"
            hide sl with dspr
            jump sprites_my_list_sl_dress_eng
        "Sad":
            show sl sad dress far with dspr
            "sl sad dress far"
            show sl sad dress with dspr
            "sl sad dress"
            show sl sad dress close with dspr
            "sl sad dress close"
            hide sl with dspr
            jump sprites_my_list_sl_dress_eng
        "Scared":
            show sl scared dress far with dspr
            "sl scared dress far"
            show sl scared dress with dspr
            "sl scared dress"
            show sl scared dress close with dspr
            "sl scared dress close"
            hide sl with dspr
            jump sprites_my_list_sl_dress_eng
        "Serious":
            show sl serious dress far with dspr
            "sl serious dress far"
            show sl serious dress with dspr
            "sl serious dress"
            show sl serious dress close with dspr
            "sl serious dress close"
            hide sl with dspr
            jump sprites_my_list_sl_dress_eng
        "Shy":
            show sl shy dress far with dspr
            "sl shy dress far"
            show sl shy dress with dspr
            "sl shy dress"
            show sl shy dress close with dspr
            "sl shy dress close"
            hide sl with dspr
            jump sprites_my_list_sl_dress_eng
        "Smile(1)":
            show sl smile dress far with dspr
            "sl smile dress far"
            show sl smile dress with dspr
            "sl smile dress"
            show sl smile dress close with dspr
            "sl smile dress close"
            hide sl with dspr
            jump sprites_my_list_sl_dress_eng
        "Smile(2)":
            show sl smile2 dress far with dspr
            "sl smile2 dress far"
            show sl smile2 dress with dspr
            "sl smile2 dress"
            show sl smile2 dress close with dspr
            "sl smile2 dress close"
            hide sl with dspr
            jump sprites_my_list_sl_dress_eng
        "Surprised":
            show sl surprise dress far with dspr
            "sl surprise dress far"
            show sl surprise dress with dspr
            "sl surprise dress"
            show sl surprise dress close with dspr
            "sl surprise dress close"
            hide sl with dspr
            jump sprites_my_list_sl_dress_eng
        "Tender":
            show sl tender dress far with dspr
            "sl tender dress far"
            show sl tender dress with dspr
            "sl tender dress"
            show sl tender dress close with dspr
            "sl tender dress close"
            hide sl with dspr
            jump sprites_my_list_sl_dress_eng
        ">>Back<<":
            jump sprites_my_list_sl_eng

label sprites_my_list_sl_sport_eng:
    menu:
        "Angry":
            show sl angry sport far with dspr
            "sl angry sport far"
            show sl angry sport with dspr
            "sl angry sport"
            show sl angry sport close with dspr
            "sl angry sport close"
            hide sl with dspr
            jump sprites_my_list_sl_sport_eng
        "Happy":
            show sl happy sport far with dspr
            "sl happy sport far"
            show sl happy sport with dspr
            "sl happy sport"
            show sl happy sport close with dspr
            "sl happy sport close"
            hide sl with dspr
            jump sprites_my_list_sl_sport_eng
        "Laugh":
            show sl laugh sport far with dspr
            "sl laugh sport far"
            show sl laugh sport with dspr
            "sl laugh sport"
            show sl laugh sport close with dspr
            "sl laugh sport close"
            hide sl with dspr
            jump sprites_my_list_sl_sport_eng
        "Normal":
            show sl normal sport far with dspr
            "sl normal sport far"
            show sl normal sport with dspr
            "sl normal sport"
            show sl normal sport close with dspr
            "sl normal sport close"
            hide sl with dspr
            jump sprites_my_list_sl_sport_eng
        "Sad":
            show sl sad sport far with dspr
            "sl sad sport far"
            show sl sad sport with dspr
            "sl sad sport"
            show sl sad sport close with dspr
            "sl sad sport close"
            hide sl with dspr
            jump sprites_my_list_sl_sport_eng
        "Scared":
            show sl scared sport far with dspr
            "sl scared sport far"
            show sl scared sport with dspr
            "sl scared sport"
            show sl scared sport close with dspr
            "sl scared sport close"
            hide sl with dspr
            jump sprites_my_list_sl_sport_eng
        "Serious":
            show sl serious sport far with dspr
            "sl serious sport far"
            show sl serious sport with dspr
            "sl serious sport"
            show sl serious sport close with dspr
            "sl serious sport close"
            hide sl with dspr
            jump sprites_my_list_sl_sport_eng
        "Shy":
            show sl shy sport far with dspr
            "sl shy sport far"
            show sl shy sport with dspr
            "sl shy sport"
            show sl shy sport close with dspr
            "sl shy sport close"
            hide sl with dspr
            jump sprites_my_list_sl_sport_eng
        "Smile(1)":
            show sl smile sport far with dspr
            "sl smile sport far"
            show sl smile sport with dspr
            "sl smile sport"
            show sl smile sport close with dspr
            "sl smile sport close"
            hide sl with dspr
            jump sprites_my_list_sl_sport_eng
        "Smile(2)":
            show sl smile2 sport far with dspr
            "sl smile2 sport far"
            show sl smile2 sport with dspr
            "sl smile2 sport"
            show sl smile2 sport close with dspr
            "sl smile2 sport close"
            hide sl with dspr
            jump sprites_my_list_sl_sport_eng
        "Surprised":
            show sl surprise sport far with dspr
            "sl surprise sport far"
            show sl surprise sport with dspr
            "sl surprise sport"
            show sl surprise sport close with dspr
            "sl surprise sport close"
            hide sl with dspr
            jump sprites_my_list_sl_sport_eng
        "Tender":
            show sl tender sport far with dspr
            "sl tender sport far"
            show sl tender sport with dspr
            "sl tender sport"
            show sl tender sport close with dspr
            "sl tender sport close"
            hide sl with dspr
            jump sprites_my_list_sl_sport_eng
        ">>Back<<":
            jump sprites_my_list_sl_eng

label sprites_my_list_sl_swim_eng:
    menu:
        "Angry":
            show sl angry swim far with dspr
            "sl angry swim far"
            show sl angry swim with dspr
            "sl angry swim"
            show sl angry swim close with dspr
            "sl angry swim close"
            hide sl with dspr
            jump sprites_my_list_sl_swim_eng
        "Happy":
            show sl happy swim far with dspr
            "sl happy swim far"
            show sl happy swim with dspr
            "sl happy swim"
            show sl happy swim close with dspr
            "sl happy swim close"
            hide sl with dspr
            jump sprites_my_list_sl_swim_eng
        "Laugh":
            show sl laugh swim far with dspr
            "sl laugh swim far"
            show sl laugh swim with dspr
            "sl laugh swim"
            show sl laugh swim close with dspr
            "sl laugh swim close"
            hide sl with dspr
            jump sprites_my_list_sl_swim_eng
        "Normal":
            show sl normal swim far with dspr
            "sl normal swim far"
            show sl normal swim with dspr
            "sl normal swim"
            show sl normal swim close with dspr
            "sl normal swim close"
            hide sl with dspr
            jump sprites_my_list_sl_swim_eng
        "Sad":
            show sl sad swim far with dspr
            "sl sad swim far"
            show sl sad swim with dspr
            "sl sad swim"
            show sl sad swim close with dspr
            "sl sad swim close"
            hide sl with dspr
            jump sprites_my_list_sl_swim_eng
        "Scared":
            show sl scared swim far with dspr
            "sl scared swim far"
            show sl scared swim with dspr
            "sl scared swim"
            show sl scared swim close with dspr
            "sl scared swim close"
            hide sl with dspr
            jump sprites_my_list_sl_swim_eng
        "Serious":
            show sl serious swim far with dspr
            "sl serious swim far"
            show sl serious swim with dspr
            "sl serious swim"
            show sl serious swim close with dspr
            "sl serious swim close"
            hide sl with dspr
            jump sprites_my_list_sl_swim_eng
        "Shy":
            show sl shy swim far with dspr
            "sl shy swim far"
            show sl shy swim with dspr
            "sl shy swim"
            show sl shy swim close with dspr
            "sl shy swim close"
            hide sl with dspr
            jump sprites_my_list_sl_swim_eng
        "Smile(1)":
            show sl smile swim far with dspr
            "sl smile swim far"
            show sl smile swim with dspr
            "sl smile swim"
            show sl smile swim close with dspr
            "sl smile swim close"
            hide sl with dspr
            jump sprites_my_list_sl_swim_eng
        "Smile(2)":
            show sl smile2 swim far with dspr
            "sl smile2 swim far"
            show sl smile2 swim with dspr
            "sl smile2 swim"
            show sl smile2 swim close with dspr
            "sl smile2 swim close"
            hide sl with dspr
            jump sprites_my_list_sl_swim_eng
        "Surprised":
            show sl surprise swim far with dspr
            "sl surprise swim far"
            show sl surprise swim with dspr
            "sl surprise swim"
            show sl surprise swim close with dspr
            "sl surprise swim close"
            hide sl with dspr
            jump sprites_my_list_sl_swim_eng
        "Tender":
            show sl tender swim far with dspr
            "sl tender swim far"
            show sl tender swim with dspr
            "sl tender swim"
            show sl tender swim close with dspr
            "sl tender swim close"
            hide sl with dspr
            jump sprites_my_list_sl_swim_eng
        ">>Back<<":
            jump sprites_my_list_sl_eng

label sprites_my_list_un_eng:
    menu:
        "Pioneer Form":
            jump sprites_my_list_un_pioner_eng
        "Dress":
            jump sprites_my_list_un_dress_eng
        "Sport uniform":
            jump sprites_my_list_un_sport_eng
        "Swimsuit":
            jump sprites_my_list_un_swim_eng
        ">>Back<<":
            jump sprites_my_list_eng

label sprites_my_list_un_pioner_eng:
    menu:
        "Rage":
            show un angry pioneer far with dspr
            "un angry pioneer far"
            show un angry pioneer with dspr
            "un angry pioneer"
            show un angry pioneer close with dspr
            "un angry pioneer close"
            hide un with dspr
            jump sprites_my_list_un_pioner_eng
        "Angry":
            show un angry2 pioneer far with dspr
            "un angry2 pioneer far"
            show un angry2 pioneer with dspr
            "un angry2 pioneer"
            show un angry2 pioneer close with dspr
            "un angry2 pioneer close"
            hide un with dspr
            jump sprites_my_list_un_pioner_eng
        "Crysmile":
            show un cry_smile pioneer far with dspr
            "un cry_smile pioneer far"
            show un cry_smile pioneer with dspr
            "un cry_smile pioneer"
            show un cry_smile pioneer close with dspr
            "un cry_smile pioneer close"
            hide un with dspr
            jump sprites_my_list_un_pioner_eng
        "Cry":
            show un cry pioneer far with dspr
            "un cry pioneer far"
            show un cry pioneer with dspr
            "un cry pioneer"
            show un cry pioneer close with dspr
            "un cry pioneer close"
            hide un with dspr
            jump sprites_my_list_un_pioner_eng
        "Evil smile":
            show un evil_smile pioneer far with dspr
            "un evil_smile pioneer far"
            show un evil_smile pioneer with dspr
            "un evil_smile pioneer"
            show un evil_smile pioneer close with dspr
            "un evil_smile pioneer close"
            hide un with dspr
            jump sprites_my_list_un_pioner_eng
        "Grin":
            show un grin pioneer far with dspr
            "un grin pioneer far"
            show un grin pioneer with dspr
            "un grin pioneer"
            show un grin pioneer close with dspr
            "un grin pioneer close"
            hide un with dspr
            jump sprites_my_list_un_pioner_eng
        "Laugh":
            show un laugh pioneer far with dspr
            "un laugh pioneer far"
            show un laugh pioneer with dspr
            "un laugh pioneer"
            show un laugh pioneer close with dspr
            "un laugh pioneer close"
            hide un with dspr
            jump sprites_my_list_un_pioner_eng
        "Normal":
            show un normal pioneer far with dspr
            "un normal pioneer far"
            show un normal pioneer with dspr
            "un normal pioneer"
            show un normal pioneer close with dspr
            "un normal pioneer close"
            hide un with dspr
            jump sprites_my_list_un_pioner_eng
        "Rage":
            show un rage pioneer far with dspr
            "un rage pioneer far"
            show un rage pioneer with dspr
            "un rage pioneer"
            show un rage pioneer close with dspr
            "un rage pioneer close"
            hide un with dspr
            jump sprites_my_list_un_pioner_eng
        "Sad":
            show un sad pioneer far with dspr
            "un sad pioneer far"
            show un sad pioneer with dspr
            "un sad pioneer"
            show un sad pioneer close with dspr
            "un sad pioneer close"
            hide un with dspr
            jump sprites_my_list_un_pioner_eng
        "Scared":
            show un scared pioneer far with dspr
            "un scared pioneer far"
            show un scared pioneer with dspr
            "un scared pioneer"
            show un scared pioneer close with dspr
            "un scared pioneer close"
            hide un with dspr
            jump sprites_my_list_un_pioner_eng
        "Serious":
            show un serious pioneer far with dspr
            "un serious pioneer far"
            show un serious pioneer with dspr
            "un serious pioneer"
            show un serious pioneer close with dspr
            "un serious pioneer close"
            hide un with dspr
            jump sprites_my_list_un_pioner_eng
        "Shocked":
            show un shocked pioneer far with dspr
            "un shocked pioneer far"
            show un shocked pioneer with dspr
            "un shocked pioneer"
            show un shocked pioneer close with dspr
            "un shocked pioneer close"
            hide un with dspr
            jump sprites_my_list_un_pioner_eng
        "Shy":
            show un shy pioneer far with dspr
            "un shy pioneer far"
            show un shy pioneer with dspr
            "un shy pioneer"
            show un shy pioneer close with dspr
            "un shy pioneer close"
            hide un with dspr
            jump sprites_my_list_un_pioner_eng
        "Smile(1)":
            show un smile pioneer far with dspr
            "un smile pioneer far"
            show un smile pioneer with dspr
            "un smile pioneer"
            show un smile pioneer close with dspr
            "un smile pioneer close"
            hide un with dspr
            jump sprites_my_list_un_pioner_eng
        "Smile(2)":
            show un smile2 pioneer far with dspr
            "un smile2 pioneer far"
            show un smile2 pioneer with dspr
            "un smile2 pioneer"
            show un smile2 pioneer close with dspr
            "un smile2 pioneer close"
            hide un with dspr
            jump sprites_my_list_un_pioner_eng
        "Smile(3)":
            show un smile3 pioneer far with dspr
            "un smile3 pioneer far"
            show un smile3 pioneer with dspr
            "un smile3 pioneer"
            show un smile3 pioneer close with dspr
            "un smile3 pioneer close"
            hide un with dspr
            jump sprites_my_list_un_pioner_eng
        "Surprised":
            show un surprise pioneer far with dspr
            "un surprise pioneer far"
            show un surprise pioneer with dspr
            "un surprise pioneer"
            show un surprise pioneer close with dspr
            "un surprise pioneer close"
            hide un with dspr
            jump sprites_my_list_un_pioneer_eng
        ">>Back<<":
            jump sprites_my_list_un_eng

label sprites_my_list_un_dress_eng:
    menu:
        "Angry(1)":
            show un angry dress far with dspr
            "un angry dress far"
            show un angry dress with dspr
            "un angry dress"
            show un angry dress close with dspr
            "un angry dress close"
            hide un with dspr
            jump sprites_my_list_un_dress_eng
        "Angry(2)":
            show un angry2 dress far with dspr
            "un angry2 dress far"
            show un angry2 dress with dspr
            "un angry2 dress"
            show un angry2 dress close with dspr
            "un angry2 dress close"
            hide un with dspr
            jump sprites_my_list_un_dress_eng
        "Crysmile":
            show un cry_smile dress far with dspr
            "un cry_smile dress far"
            show un cry_smile dress with dspr
            "un cry_smile dress"
            show un cry_smile dress close with dspr
            "un cry_smile dress close"
            hide un with dspr
            jump sprites_my_list_un_dress_eng
        "Cry":
            show un cry dress far with dspr
            "un cry dress far"
            show un cry dress with dspr
            "un cry dress"
            show un cry dress close with dspr
            "un cry dress close"
            hide un with dspr
            jump sprites_my_list_un_dress_eng
        "Evil smile":
            show un evil_smile dress far with dspr
            "un evil_smile dress far"
            show un evil_smile dress with dspr
            "un evil_smile dress"
            show un evil_smile dress close with dspr
            "un evil_smile dress close"
            hide un with dspr
            jump sprites_my_list_un_dress_eng
        "Grin":
            show un grin dress far with dspr
            "un grin dress far"
            show un grin dress with dspr
            "un grin dress"
            show un grin dress close with dspr
            "un grin dress close"
            hide un with dspr
            jump sprites_my_list_un_dress_eng
        "Laugh":
            show un laugh dress far with dspr
            "un laugh dress far"
            show un laugh dress with dspr
            "un laugh dress"
            show un laugh dress close with dspr
            "un laugh dress close"
            hide un with dspr
            jump sprites_my_list_un_dress_eng
        "Normal":
            show un normal dress far with dspr
            "un normal dress far"
            show un normal dress with dspr
            "un normal dress"
            show un normal dress close with dspr
            "un normal dress close"
            hide un with dspr
            jump sprites_my_list_un_dress_eng
        "Rage":
            show un rage dress far with dspr
            "un rage dress far"
            show un rage dress with dspr
            "un rage dress"
            show un rage dress close with dspr
            "un rage dress close"
            hide un with dspr
            jump sprites_my_list_un_dress_eng
        "Sad":
            show un sad dress far with dspr
            "un sad dress far"
            show un sad dress with dspr
            "un sad dress"
            show un sad dress close with dspr
            "un sad dress close"
            hide un with dspr
            jump sprites_my_list_un_dress_eng
        "Scared":
            show un scared dress far with dspr
            "un scared dress far"
            show un scared dress with dspr
            "un scared dress"
            show un scared dress close with dspr
            "un scared dress close"
            hide un with dspr
            jump sprites_my_list_un_dress_eng
        "Serious":
            show un serious dress far with dspr
            "un serious dress far"
            show un serious dress with dspr
            "un serious dress"
            show un serious dress close with dspr
            "un serious dress close"
            hide un with dspr
            jump sprites_my_list_un_dress_eng
        "Shocked":
            show un shocked dress far with dspr
            "un shocked dress far"
            show un shocked dress with dspr
            "un shocked dress"
            show un shocked dress close with dspr
            "un shocked dress close"
            hide un with dspr
            jump sprites_my_list_un_dress_eng
        "Shy":
            show un shy dress far with dspr
            "un shy dress far"
            show un shy dress with dspr
            "un shy dress"
            show un shy dress close with dspr
            "un shy dress close"
            hide un with dspr
            jump sprites_my_list_un_dress_eng
        "Smile(1)":
            show un smile dress far with dspr
            "un smile dress far"
            show un smile dress with dspr
            "un smile dress"
            show un smile dress close with dspr
            "un smile dress close"
            hide un with dspr
            jump sprites_my_list_un_dress_eng
        "Smile(2)":
            show un smile2 dress far with dspr
            "un smile2 dress far"
            show un smile2 dress with dspr
            "un smile2 dress"
            show un smile2 dress close with dspr
            "un smile2 dress close"
            hide un with dspr
            jump sprites_my_list_un_dress_eng
        "Smile(3)":
            show un smile3 dress far with dspr
            "un smile3 dress far"
            show un smile3 dress with dspr
            "un smile3 dress"
            show un smile3 dress close with dspr
            "un smile3 dress close"
            hide un with dspr
            jump sprites_my_list_un_dress_eng
        "Surprised":
            show un surprise dress far with dspr
            "un surprise dress far"
            show un surprise dress with dspr
            "un surprise dress"
            show un surprise dress close with dspr
            "un surprise dress close"
            hide un with dspr
            jump sprites_my_list_un_dress_eng
        ">>Back<<":
            jump sprites_my_list_un_eng

label sprites_my_list_un_sport_eng:
    menu:
        "Rage":
            show un angry sport far with dspr
            "un angry sport far"
            show un angry sport with dspr
            "un angry sport"
            show un angry sport close with dspr
            "un angry sport close"
            hide un with dspr
            jump sprites_my_list_un_sport_eng
        "Angry":
            show un angry2 sport far with dspr
            "un angry2 sport far"
            show un angry2 sport with dspr
            "un angry2 sport"
            show un angry2 sport close with dspr
            "un angry2 sport close"
            hide un with dspr
            jump sprites_my_list_un_sport_eng
        "Crysmile":
            show un cry_smile sport far with dspr
            "un cry_smile sport far"
            show un cry_smile sport with dspr
            "un cry_smile sport"
            show un cry_smile sport close with dspr
            "un cry_smile sport close"
            hide un with dspr
            jump sprites_my_list_un_sport_eng
        "Cry":
            show un cry sport far with dspr
            "un cry sport far"
            show un cry sport with dspr
            "un cry sport"
            show un cry sport close with dspr
            "un cry sport close"
            hide un with dspr
            jump sprites_my_list_un_sport_eng
        "Evil smile":
            show un evil_smile sport far with dspr
            "un evil_smile sport far"
            show un evil_smile sport with dspr
            "un evil_smile sport"
            show un evil_smile sport close with dspr
            "un evil_smile sport close"
            hide un with dspr
            jump sprites_my_list_un_sport_eng
        "Grin":
            show un grin sport far with dspr
            "un grin sport far"
            show un grin sport with dspr
            "un grin sport"
            show un grin sport close with dspr
            "un grin sport close"
            hide un with dspr
            jump sprites_my_list_un_sport_eng
        "Laugh":
            show un laugh sport far with dspr
            "un laugh sport far"
            show un laugh sport with dspr
            "un laugh sport"
            show un laugh sport close with dspr
            "un laugh sport close"
            hide un with dspr
            jump sprites_my_list_un_sport_eng
        "Normal":
            show un normal sport far with dspr
            "un normal sport far"
            show un normal sport with dspr
            "un normal sport"
            show un normal sport close with dspr
            "un normal sport close"
            hide un with dspr
            jump sprites_my_list_un_sport_eng
        "Rage":
            show un rage sport far with dspr
            "un rage sport far"
            show un rage sport with dspr
            "un rage sport"
            show un rage sport close with dspr
            "un rage sport close"
            hide un with dspr
            jump sprites_my_list_un_sport_eng
        "Sad":
            show un sad sport far with dspr
            "un sad sport far"
            show un sad sport with dspr
            "un sad sport"
            show un sad sport close with dspr
            "un sad sport close"
            hide un with dspr
            jump sprites_my_list_un_sport_eng
        "Scared":
            show un scared sport far with dspr
            "un scared sport far"
            show un scared sport with dspr
            "un scared sport"
            show un scared sport close with dspr
            "un scared sport close"
            hide un with dspr
            jump sprites_my_list_un_sport_eng
        "Serious":
            show un serious sport far with dspr
            "un serious sport far"
            show un serious sport with dspr
            "un serious sport"
            show un serious sport close with dspr
            "un serious sport close"
            hide un with dspr
            jump sprites_my_list_un_sport_eng
        "Shocked":
            show un shocked sport far with dspr
            "un shocked sport far"
            show un shocked sport with dspr
            "un shocked sport"
            show un shocked sport close with dspr
            "un shocked sport close"
            hide un with dspr
            jump sprites_my_list_un_sport_eng
        "Shy":
            show un shy sport far with dspr
            "un shy sport far"
            show un shy sport with dspr
            "un shy sport"
            show un shy sport close with dspr
            "un shy sport close"
            hide un with dspr
            jump sprites_my_list_un_sport_eng
        "Smile":
            show un smile sport far with dspr
            "un smile sport far"
            show un smile sport with dspr
            "un smile sport"
            show un smile sport close with dspr
            "un smile sport close"
            hide un with dspr
            jump sprites_my_list_un_sport_eng
        "Smile(2)":
            show un smile2 sport far with dspr
            "un smile2 sport far"
            show un smile2 sport with dspr
            "un smile2 sport"
            show un smile2 sport close with dspr
            "un smile2 sport close"
            hide un with dspr
            jump sprites_my_list_un_sport_eng
        "Smile(3)":
            show un smile3 sport far with dspr
            "un smile3 sport far"
            show un smile3 sport with dspr
            "un smile3 sport"
            show un smile3 sport close with dspr
            "un smile3 sport close"
            hide un with dspr
            jump sprites_my_list_un_sport_eng
        "Surprised":
            show un surprise sport far with dspr
            "un surprise sport far"
            show un surprise sport with dspr
            "un surprise sport"
            show un surprise sport close with dspr
            "un surprise sport close"
            hide un with dspr
            jump sprites_my_list_un_sport_eng
        ">>Back<<":
            jump sprites_my_list_un_eng

label sprites_my_list_un_swim_eng:
    menu:
        "Rage":
            show un angry swim far with dspr
            "un angry swim far"
            show un angry swim with dspr
            "un angry swim"
            show un angry swim close with dspr
            "un angry swim close"
            hide un with dspr
            jump sprites_my_list_un_swim_eng
        "Crysmile":
            show un cry_smile swim far with dspr
            "un cry_smile swim far"
            show un cry_smile swim with dspr
            "un cry_smile swim"
            show un cry_smile swim close with dspr
            "un cry_smile swim close"
            hide un with dspr
            jump sprites_my_list_un_swim_eng
        "Cry":
            show un cry swim far with dspr
            "un cry swim far"
            show un cry swim with dspr
            "un cry swim"
            show un cry swim close with dspr
            "un cry swim close"
            hide un with dspr
            jump sprites_my_list_un_swim_eng
        "Evil smile":
            show un evil_smile swim far with dspr
            "un evil_smile swim far"
            show un evil_smile swim with dspr
            "un evil_smile swim"
            show un evil_smile swim close with dspr
            "un evil_smile swim close"
            hide un with dspr
            jump sprites_my_list_un_swim_eng
        "Normal":
            show un normal swim far with dspr
            "un normal swim far"
            show un normal swim with dspr
            "un normal swim"
            show un normal swim close with dspr
            "un normal swim close"
            hide un with dspr
            jump sprites_my_list_un_swim_eng
        "Sad":
            show un sad swim far with dspr
            "un sad swim far"
            show un sad swim with dspr
            "un sad swim"
            show un sad swim close with dspr
            "un sad swim close"
            hide un with dspr
            jump sprites_my_list_un_swim_eng
        "Scared":
            show un scared swim far with dspr
            "un scared swim far"
            show un scared swim with dspr
            "un scared swim"
            show un scared swim close with dspr
            "un scared swim close"
            hide un with dspr
            jump sprites_my_list_un_swim_eng
        "Shocked":
            show un shocked swim far with dspr
            "un shocked swim far"
            show un shocked swim with dspr
            "un shocked swim"
            show un shocked swim close with dspr
            "un shocked swim close"
            hide un with dspr
            jump sprites_my_list_un_swim_eng
        "Shy":
            show un shy swim far with dspr
            "un shy swim far"
            show un shy swim with dspr
            "un shy swim"
            show un shy swim close with dspr
            "un shy swim close"
            hide un with dspr
            jump sprites_my_list_un_swim_eng
        "Smile(1)":
            show un smile swim far with dspr
            "un smile swim far"
            show un smile swim with dspr
            "un smile swim"
            show un smile swim close with dspr
            "un smile swim close"
            hide un with dspr
            jump sprites_my_list_un_swim_eng
        "Smile(2)":
            show un smile2 swim far with dspr
            "un smile2 swim far"
            show un smile2 swim with dspr
            "un smile2 swim"
            show un smile2 swim close with dspr
            "un smile2 swim close"
            hide un with dspr
            jump sprites_my_list_un_swim_eng
        "Surprised":
            show un surprise swim far with dspr
            "un surprise swim far"
            show un surprise swim with dspr
            "un surprise swim"
            show un surprise swim close with dspr
            "un surprise swim close"
            hide un with dspr
            jump sprites_my_list_un_swim_eng
        ">>Back<<":
            jump sprites_my_list_un_eng

label sprites_my_list_mi_eng:
    menu:
        "Pioneer Form":
            jump sprites_my_list_mi_pioneer_eng
        "Swimsuit":
            jump sprites_my_list_mi_swim_eng
        ">>Back<<":
            jump sprites_my_list_eng

label sprites_my_list_mi_pioneer_eng:
    menu:
        "Angry":
            show mi angry pioneer far with dspr
            "mi angry pioneer far"
            show mi angry pioneer with dspr
            "mi angry pioneer"
            show mi angry pioneer close with dspr
            "mi angry pioneer close"
            hide mi with dspr
            jump sprites_my_list_mi_pioneer_eng
        "Cry":
            show mi cry pioneer far with dspr
            "mi cry pioneer far"
            show mi cry pioneer with dspr
            "mi cry pioneer"
            show mi cry pioneer close with dspr
            "mi cry pioneer close"
            hide mi with dspr
            jump sprites_my_list_mi_pioneer_eng
        "Crysmile":
            show mi cry_smile pioneer far with dspr
            "mi cry_smile pioneer far"
            show mi cry_smile pioneer with dspr
            "mi cry_smile pioneer"
            show mi cry_smile pioneer close with dspr
            "mi cry_smile pioneer close"
            hide mi with dspr
            jump sprites_my_list_mi_pioneer_eng
        "Dislike":
            show mi dontlike pioneer far with dspr
            "mi dontlike pioneer far"
            show mi dontlike pioneer with dspr
            "mi dontlike pioneer"
            show mi dontlike pioneer close with dspr
            "mi dontlike pioneer close"
            hide mi with dspr
            jump sprites_my_list_mi_pioneer_eng
        "Grin":
            show mi grin pioneer far with dspr
            "mi grin pioneer far"
            show mi grin pioneer with dspr
            "mi grin pioneer"
            show mi grin pioneer close with dspr
            "mi grin pioneer close"
            hide mi with dspr
            jump sprites_my_list_mi_pioneer_eng
        "Happy":
            show mi happy pioneer far with dspr
            "mi happy pioneer far"
            show mi happy pioneer with dspr
            "mi happy pioneer"
            show mi happy pioneer close with dspr
            "mi happy pioneer close"
            hide mi with dspr
            jump sprites_my_list_mi_pioneer_eng
        "Laugh":
            show mi laugh pioneer far with dspr
            "mi laugh pioneer far"
            show mi laugh pioneer with dspr
            "mi laugh pioneer"
            show mi laugh pioneer close with dspr
            "mi laugh pioneer close"
            hide mi with dspr
            jump sprites_my_list_mi_pioneer_eng
        "Normal":
            show mi normal pioneer far with dspr
            "mi normal pioneer far"
            show mi normal pioneer with dspr
            "mi normal pioneer"
            show mi normal pioneer close with dspr
            "mi normal pioneer close"
            hide mi with dspr
            jump sprites_my_list_mi_pioneer_eng
        "Rage":
            show mi rage pioneer far with dspr
            "mi rage pioneer far"
            show mi rage pioneer with dspr
            "mi rage pioneer"
            show mi rage pioneer close with dspr
            "mi rage pioneer close"
            hide mi with dspr
            jump sprites_my_list_mi_pioneer_eng
        "Sad":
            show mi sad pioneer far with dspr
            "mi sad pioneer far"
            show mi sad pioneer with dspr
            "mi sad pioneer"
            show mi sad pioneer close with dspr
            "mi sad pioneer close"
            hide mi with dspr
            jump sprites_my_list_mi_pioneer_eng
        "Scared":
            show mi scared pioneer far with dspr
            "mi scared pioneer far"
            show mi scared pioneer with dspr
            "mi scared pioneer"
            show mi scared pioneer close with dspr
            "mi scared pioneer close"
            hide mi with dspr
            jump sprites_my_list_mi_pioneer_eng
        "Serious":
            show mi serious pioneer far with dspr
            "mi serious pioneer far"
            show mi serious pioneer with dspr
            "mi serious pioneer"
            show mi serious pioneer close with dspr
            "mi serious pioneer close"
            hide mi with dspr
            jump sprites_my_list_mi_pioneer_eng
        "Shocked":
            show mi shocked pioneer far with dspr
            "mi shocked pioneer far"
            show mi shocked pioneer with dspr
            "mi shocked pioneer"
            show mi shocked pioneer close with dspr
            "mi shocked pioneer close"
            hide mi with dspr
            jump sprites_my_list_mi_pioneer_eng
        "Shy":
            show mi shy pioneer far with dspr
            "mi shy pioneer far"
            show mi shy pioneer with dspr
            "mi shy pioneer"
            show mi shy pioneer close with dspr
            "mi shy pioneer close"
            hide mi with dspr
            jump sprites_my_list_mi_pioneer_eng
        "Smile":
            show mi smile pioneer far with dspr
            "mi smile pioneer far"
            show mi smile pioneer with dspr
            "mi smile pioneer"
            show mi smile pioneer close with dspr
            "mi smile pioneer close"
            hide mi with dspr
            jump sprites_my_list_mi_pioneer_eng
        "Surprised":
            show mi surprise pioneer far with dspr
            "mi surprise pioneer far"
            show mi surprise pioneer with dspr
            "mi surprise pioneer"
            show mi surprise pioneer close with dspr
            "mi surprise pioneer close"
            hide mi with dspr
            jump sprites_my_list_mi_pioneer_eng
        "Upset":
            show mi upset pioneer far with dspr
            "mi upset pioneer far"
            show mi upset pioneer with dspr
            "mi upset pioneer"
            show mi upset pioneer close with dspr
            "mi upset pioneer close"
            hide mi with dspr
            jump sprites_my_list_mi_pioneer_eng
        ">>Back<<":
            jump sprites_my_list_mi_eng

label sprites_my_list_mi_swim_eng:
    menu:
        "Angry":
            show mi angry swim far with dspr
            "mi angry swim far"
            show mi angry swim with dspr
            "mi angry swim"
            show mi angry swim close with dspr
            "mi angry swim close"
            hide mi with dspr
            jump sprites_my_list_mi_swim_eng
        "Cry":
            show mi cry swim far with dspr
            "mi cry swim far"
            show mi cry swim with dspr
            "mi cry swim"
            show mi cry swim close with dspr
            "mi cry swim close"
            hide mi with dspr
            jump sprites_my_list_mi_swim_eng
        "Crysmile":
            show mi cry_smile swim far with dspr
            "mi cry_smile swim far"
            show mi cry_smile swim with dspr
            "mi cry_smile swim"
            show mi cry_smile swim close with dspr
            "mi cry_smile swim close"
            hide mi with dspr
            jump sprites_my_list_mi_swim_eng
        "Dislike":
            show mi dontlike swim far with dspr
            "mi dontlike swim far"
            show mi dontlike swim with dspr
            "mi dontlike swim"
            show mi dontlike swim close with dspr
            "mi dontlike swim close"
            hide mi with dspr
            jump sprites_my_list_mi_swim_eng
        "Grin":
            show mi grin swim far with dspr
            "mi grin swim far"
            show mi grin swim with dspr
            "mi grin swim"
            show mi grin swim close with dspr
            "mi grin swim close"
            hide mi with dspr
            jump sprites_my_list_mi_swim_eng
        "Happy":
            show mi happy swim far with dspr
            "mi happy swim far"
            show mi happy swim with dspr
            "mi happy swim"
            show mi happy swim close with dspr
            "mi happy swim close"
            hide mi with dspr
            jump sprites_my_list_mi_swim_eng
        "Laugh":
            show mi laugh swim far with dspr
            "mi laugh swim far"
            show mi laugh swim with dspr
            "mi laugh swim"
            show mi laugh swim close with dspr
            "mi laugh swim close"
            hide mi with dspr
            jump sprites_my_list_mi_swim_eng
        "Normal":
            show mi normal swim far with dspr
            "mi normal swim far"
            show mi normal swim with dspr
            "mi normal swim"
            show mi normal swim close with dspr
            "mi normal swim close"
            hide mi with dspr
            jump sprites_my_list_mi_swim_eng
        "Rage":
            show mi rage swim far with dspr
            "mi rage swim far"
            show mi rage swim with dspr
            "mi rage swim"
            show mi rage swim close with dspr
            "mi rage swim close"
            hide mi with dspr
            jump sprites_my_list_mi_swim_eng
        "Sad":
            show mi sad swim far with dspr
            "mi sad swim far"
            show mi sad swim with dspr
            "mi sad swim"
            show mi sad swim close with dspr
            "mi sad swim close"
            hide mi with dspr
            jump sprites_my_list_mi_swim_eng
        "Scared":
            show mi scared swim far with dspr
            "mi scared swim far"
            show mi scared swim with dspr
            "mi scared swim"
            show mi scared swim close with dspr
            "mi scared swim close"
            hide mi with dspr
            jump sprites_my_list_mi_swim_eng
        "Serious":
            show mi serious swim far with dspr
            "mi serious swim far"
            show mi serious swim with dspr
            "mi serious swim"
            show mi serious swim close with dspr
            "mi serious swim close"
            hide mi with dspr
            jump sprites_my_list_mi_swim_eng
        "Shocked":
            show mi shocked swim far with dspr
            "mi shocked swim far"
            show mi shocked swim with dspr
            "mi shocked swim"
            show mi shocked swim close with dspr
            "mi shocked swim close"
            hide mi with dspr
            jump sprites_my_list_mi_swim_eng
        "Shy":
            show mi shy swim far with dspr
            "mi shy swim far"
            show mi shy swim with dspr
            "mi shy swim"
            show mi shy swim close with dspr
            "mi shy swim close"
            hide mi with dspr
            jump sprites_my_list_mi_swim_eng
        "Smile":
            show mi smile swim far with dspr
            "mi smile swim far"
            show mi smile swim with dspr
            "mi smile swim"
            show mi smile swim close with dspr
            "mi smile swim close"
            hide mi with dspr
            jump sprites_my_list_mi_swim_eng
        "Surprised":
            show mi surprise swim far with dspr
            "mi surprise swim far"
            show mi surprise swim with dspr
            "mi surprise swim"
            show mi surprise swim close with dspr
            "mi surprise swim close"
            hide mi with dspr
            jump sprites_my_list_mi_swim_eng
        "Upset":
            show mi upset swim far with dspr
            "mi upset swim far"
            show mi upset swim with dspr
            "mi upset swim"
            show mi upset swim close with dspr
            "mi upset swim close"
            hide mi with dspr
            jump sprites_my_list_mi_swim_eng
        ">>Back<<":
            jump sprites_my_list_mi_eng

label sprites_my_list_us_eng:
    menu:
        "Pioneer Form":
            jump sprites_my_list_us_pioneer_eng
        "Dress":
            jump sprites_my_list_us_dress_eng
        "Sport uniform":
            jump sprites_my_list_us_sport_eng
        "Swimsuit":
            jump sprites_my_list_us_swim_eng
        ">>Back<<":
            jump sprites_my_list_eng

label sprites_my_list_us_pioneer_eng:
    menu:
        "Angry":
            show us angry pioneer far with dspr
            "us angry pioneer far"
            show us angry pioneer with dspr
            "us angry pioneer"
            show us angry pioneer close with dspr
            "us angry pioneer close"
            hide us with dspr
            jump sprites_my_list_us_pioneer_eng
        "Caml":
            show us calml pioneer far with dspr
            "us calml pioneer far"
            show us calml pioneer with dspr
            "us calml pioneer"
            show us calml pioneer close with dspr
            "us calml pioneer close"
            hide us with dspr
            jump sprites_my_list_us_pioneer_eng
        "Cry(1)":
            show us cry pioneer far with dspr
            "us cry pioneer far"
            show us cry pioneer with dspr
            "us cry pioneer"
            show us cry pioneer close with dspr
            "us cry pioneer close"
            hide us with dspr
            jump sprites_my_list_us_pioneer_eng
        "Cry(2)":
            show us cry2 pioneer far with dspr
            "us cry2 pioneer far"
            show us cry2 pioneer with dspr
            "us cry2 pioneer"
            show us cry2 pioneer close with dspr
            "us cry2 pioneer close"
            hide us with dspr
            jump sprites_my_list_us_pioneer_eng
        "Dislike":
            show us dontlike pioneer far with dspr
            "us dontlike pioneer far"
            show us dontlike pioneer with dspr
            "us dontlike pioneer"
            show us dontlike pioneer close with dspr
            "us dontlike pioneer close"
            hide us with dspr
            jump sprites_my_list_us_pioneer_eng
        "Fear":
            show us fear pioneer far with dspr
            "us fear pioneer far"
            show us fear pioneer with dspr
            "us fear pioneer"
            show us fear pioneer close with dspr
            "us fear pioneer close"
            hide us with dspr
            jump sprites_my_list_us_pioneer_eng
        "Grin":
            show us grin pioneer far with dspr
            "us grin pioneer far"
            show us grin pioneer with dspr
            "us grin pioneer"
            show us grin pioneer close with dspr
            "us grin pioneer close"
            hide us with dspr
            jump sprites_my_list_us_pioneer_eng
        "Laugh(1)":
            show us laugh pioneer far with dspr
            "us laugh pioneer far"
            show us laugh pioneer with dspr
            "us laugh pioneer"
            show us laugh pioneer close with dspr
            "us laugh pioneer close"
            hide us with dspr
            jump sprites_my_list_us_pioneer_eng
        "Laugh(2)":
            show us laugh2 pioneer far with dspr
            "us laugh2 pioneer far"
            show us laugh2 pioneer with dspr
            "us laugh2 pioneer"
            show us laugh2 pioneer close with dspr
            "us laugh2 pioneer close"
            hide us with dspr
            jump sprites_my_list_us_pioneer_eng
        "Normal":
            show us normal pioneer far with dspr
            "us normal pioneer far"
            show us normal pioneer with dspr
            "us normal pioneer"
            show us normal pioneer close with dspr
            "us normal pioneer close"
            hide us with dspr
            jump sprites_my_list_us_pioneer_eng
        "Sad":
            show us sad pioneer far with dspr
            "us sad pioneer far"
            show us sad pioneer with dspr
            "us sad pioneer"
            show us sad pioneer close with dspr
            "us sad pioneer close"
            hide us with dspr
            jump sprites_my_list_us_pioneer_eng
        "Shy(1)":
            show us shy pioneer far with dspr
            "us shy pioneer far"
            show us shy pioneer with dspr
            "us shy pioneer"
            show us shy pioneer close with dspr
            "us shy pioneer close"
            hide us with dspr
            jump sprites_my_list_us_pioneer_eng
        "Shy(2)":
            show us shy2 pioneer far with dspr
            "us shy2 pioneer far"
            show us shy2 pioneer with dspr
            "us shy2 pioneer"
            show us shy2 pioneer close with dspr
            "us shy2 pioneer close"
            hide us with dspr
            jump sprites_my_list_us_pioneer_eng
        "Smile":
            show us smile pioneer far with dspr
            "us smile pioneer far"
            show us smile pioneer with dspr
            "us smile pioneer"
            show us smile pioneer close with dspr
            "us smile pioneer close"
            hide us with dspr
            jump sprites_my_list_us_pioneer_eng
        "Surprised(1)":
            show us surp1 pioneer far with dspr
            "us surp1 pioneer far"
            show us surp1 pioneer with dspr
            "us surp1 pioneer"
            show us surp1 pioneer close with dspr
            "us surp1 pioneer close"
            hide us with dspr
            jump sprites_my_list_us_pioneer_eng
        "Surprised(2)":
            show us surp2 pioneer far with dspr
            "us surp2 pioneer far"
            show us surp2 pioneer with dspr
            "us surp2 pioneer"
            show us surp2 pioneer close with dspr
            "us surp2 pioneer close"
            hide us with dspr
            jump sprites_my_list_us_pioneer_eng
        "Surprised(3)":
            show us surp3 pioneer far with dspr
            "us surp3 pioneer far"
            show us surp3 pioneer with dspr
            "us surp3 pioneer"
            show us surp3 pioneer close with dspr
            "us surp3 pioneer close"
            hide us with dspr
            jump sprites_my_list_us_pioneer_eng
        "Upset":
            show us upset pioneer far with dspr
            "us upset pioneer far"
            show us upset pioneer with dspr
            "us upset pioneer"
            show us upset pioneer close with dspr
            "us upset pioneer close"
            hide us with dspr
            jump sprites_my_list_us_pioneer_eng
        ">>Back<<":
            jump sprites_my_list_us_eng

label sprites_my_list_us_dress_eng:
    menu:
        "Angry":
            show us angry dress far with dspr
            "us angry dress far"
            show us angry dress with dspr
            "us angry dress"
            show us angry dress close with dspr
            "us angry dress close"
            hide us with dspr
            jump sprites_my_list_us_dress_eng
        "Caml":
            show us calml dress far with dspr
            "us calml dress far"
            show us calml dress with dspr
            "us calml dress"
            show us calml dress close with dspr
            "us calml dress close"
            hide us with dspr
            jump sprites_my_list_us_dress_eng
        "Cry(1)":
            show us cry dress far with dspr
            "us cry dress far"
            show us cry dress with dspr
            "us cry dress"
            show us cry dress close with dspr
            "us cry dress close"
            hide us with dspr
            jump sprites_my_list_us_dress_eng
        "Cry(2)":
            show us cry2 dress far with dspr
            "us cry2 dress far"
            show us cry2 dress with dspr
            "us cry2 dress"
            show us cry2 dress close with dspr
            "us cry2 dress close"
            hide us with dspr
            jump sprites_my_list_us_dress_eng
        "Dislike":
            show us dontlike dress far with dspr
            "us dontlike dress far"
            show us dontlike dress with dspr
            "us dontlike dress"
            show us dontlike dress close with dspr
            "us dontlike dress close"
            hide us with dspr
            jump sprites_my_list_us_dress_eng
        "Fear":
            show us fear dress far with dspr
            "us fear dress far"
            show us fear dress with dspr
            "us fear dress"
            show us fear dress close with dspr
            "us fear dress close"
            hide us with dspr
            jump sprites_my_list_us_dress_eng
        "Grin":
            show us grin dress far with dspr
            "us grin dress far"
            show us grin dress with dspr
            "us grin dress"
            show us grin dress close with dspr
            "us grin dress close"
            hide us with dspr
            jump sprites_my_list_us_dress_eng
        "Laugh(1)":
            show us laugh dress far with dspr
            "us laugh dress far"
            show us laugh dress with dspr
            "us laugh dress"
            show us laugh dress close with dspr
            "us laugh dress close"
            hide us with dspr
            jump sprites_my_list_us_dress_eng
        "Laugh(2)":
            show us laugh2 dress far with dspr
            "us laugh2 dress far"
            show us laugh2 dress with dspr
            "us laugh2 dress"
            show us laugh2 dress close with dspr
            "us laugh2 dress close"
            hide us with dspr
            jump sprites_my_list_us_dress_eng
        "Normal":
            show us normal dress far with dspr
            "us normal dress far"
            show us normal dress with dspr
            "us normal dress"
            show us normal dress close with dspr
            "us normal dress close"
            hide us with dspr
            jump sprites_my_list_us_dress_eng
        "Sad":
            show us sad dress far with dspr
            "us sad dress far"
            show us sad dress with dspr
            "us sad dress"
            show us sad dress close with dspr
            "us sad dress close"
            hide us with dspr
            jump sprites_my_list_us_dress_eng
        "Shy(1)":
            show us shy dress far with dspr
            "us shy dress far"
            show us shy dress with dspr
            "us shy dress"
            show us shy dress close with dspr
            "us shy dress close"
            hide us with dspr
            jump sprites_my_list_us_dress_eng
        "Shy(2)":
            show us shy2 dress far with dspr
            "us shy2 dress far"
            show us shy2 dress with dspr
            "us shy2 dress"
            show us shy2 dress close with dspr
            "us shy2 dress close"
            hide us with dspr
            jump sprites_my_list_us_dress_eng
        "Smile":
            show us smile dress far with dspr
            "us smile dress far"
            show us smile dress with dspr
            "us smile dress"
            show us smile dress close with dspr
            "us smile dress close"
            hide us with dspr
            jump sprites_my_list_us_dress_eng
        "Surprised(1)":
            show us surp1 dress far with dspr
            "us surp1 dress far"
            show us surp1 dress with dspr
            "us surp1 dress"
            show us surp1 dress close with dspr
            "us surp1 dress close"
            hide us with dspr
            jump sprites_my_list_us_dress_eng
        "Surprised(2)":
            show us surp2 dress far with dspr
            "us surp2 dress far"
            show us surp2 dress with dspr
            "us surp2 dress"
            show us surp2 dress close with dspr
            "us surp2 dress close"
            hide us with dspr
            jump sprites_my_list_us_dress_eng
        "Surprised(3)":
            show us surp3 dress far with dspr
            "us surp3 dress far"
            show us surp3 dress with dspr
            "us surp3 dress"
            show us surp3 dress close with dspr
            "us surp3 dress close"
            hide us with dspr
            jump sprites_my_list_us_dress_eng
        "Upset":
            show us upset dress far with dspr
            "us upset dress far"
            show us upset dress with dspr
            "us upset dress"
            show us upset dress close with dspr
            "us upset dress close"
            hide us with dspr
            jump sprites_my_list_us_dress_eng
        ">>Back<<":
            jump sprites_my_list_us_eng

label sprites_my_list_us_sport_eng:
    menu:
        "Angry":
            show us angry sport far with dspr
            "us angry sport far"
            show us angry sport with dspr
            "us angry sport"
            show us angry sport close with dspr
            "us angry sport close"
            hide us with dspr
            jump sprites_my_list_us_sport_eng
        "Caml":
            show us calml sport far with dspr
            "us calml sport far"
            show us calml sport with dspr
            "us calml sport"
            show us calml sport close with dspr
            "us calml sport close"
            hide us with dspr
            jump sprites_my_list_us_sport_eng
        "Cry(1)":
            show us cry sport far with dspr
            "us cry sport far"
            show us cry sport with dspr
            "us cry sport"
            show us cry sport close with dspr
            "us cry sport close"
            hide us with dspr
            jump sprites_my_list_us_sport_eng
        "Cry(2)":
            show us cry2 sport far with dspr
            "us cry2 sport far"
            show us cry2 sport with dspr
            "us cry2 sport"
            show us cry2 sport close with dspr
            "us cry2 sport close"
            hide us with dspr
            jump sprites_my_list_us_sport_eng
        "Dislike":
            show us dontlike sport far with dspr
            "us dontlike sport far"
            show us dontlike sport with dspr
            "us dontlike sport"
            show us dontlike sport close with dspr
            "us dontlike sport close"
            hide us with dspr
            jump sprites_my_list_us_sport_eng
        "Fear":
            show us fear sport far with dspr
            "us fear sport far"
            show us fear sport with dspr
            "us fear sport"
            show us fear sport close with dspr
            "us fear sport close"
            hide us with dspr
            jump sprites_my_list_us_sport_eng
        "Grin":
            show us grin sport far with dspr
            "us grin sport far"
            show us grin sport with dspr
            "us grin sport"
            show us grin sport close with dspr
            "us grin sport close"
            hide us with dspr
            jump sprites_my_list_us_sport_eng
        "Laugh(1)":
            show us laugh sport far with dspr
            "us laugh sport far"
            show us laugh sport with dspr
            "us laugh sport"
            show us laugh sport close with dspr
            "us laugh sport close"
            hide us with dspr
            jump sprites_my_list_us_sport_eng
        "Laugh(2)":
            show us laugh2 sport far with dspr
            "us laugh2 sport far"
            show us laugh2 sport with dspr
            "us laugh2 sport"
            show us laugh2 sport close with dspr
            "us laugh2 sport close"
            hide us with dspr
            jump sprites_my_list_us_sport_eng
        "Normal":
            show us normal sport far with dspr
            "us normal sport far"
            show us normal sport with dspr
            "us normal sport"
            show us normal sport close with dspr
            "us normal sport close"
            hide us with dspr
            jump sprites_my_list_us_sport_eng
        "Sad":
            show us sad sport far with dspr
            "us sad sport far"
            show us sad sport with dspr
            "us sad sport"
            show us sad sport close with dspr
            "us sad sport close"
            hide us with dspr
            jump sprites_my_list_us_sport_eng
        "Shy(1)":
            show us shy sport far with dspr
            "us shy sport far"
            show us shy sport with dspr
            "us shy sport"
            show us shy sport close with dspr
            "us shy sport close"
            hide us with dspr
            jump sprites_my_list_us_sport_eng
        "Shy(2)":
            show us shy2 sport far with dspr
            "us shy2 sport far"
            show us shy2 sport with dspr
            "us shy2 sport"
            show us shy2 sport close with dspr
            "us shy2 sport close"
            hide us with dspr
            jump sprites_my_list_us_sport_eng
        "Smile":
            show us smile sport far with dspr
            "us smile sport far"
            show us smile sport with dspr
            "us smile sport"
            show us smile sport close with dspr
            "us smile sport close"
            hide us with dspr
            jump sprites_my_list_us_sport_eng
        "Surprised(1)":
            show us surp1 sport far with dspr
            "us surp1 sport far"
            show us surp1 sport with dspr
            "us surp1 sport"
            show us surp1 sport close with dspr
            "us surp1 sport close"
            hide us with dspr
            jump sprites_my_list_us_sport_eng
        "Surprised(2)":
            show us surp2 sport far with dspr
            "us surp2 sport far"
            show us surp2 sport with dspr
            "us surp2 sport"
            show us surp2 sport close with dspr
            "us surp2 sport close"
            hide us with dspr
            jump sprites_my_list_us_sport_eng
        "Surprised(3)":
            show us surp3 sport far with dspr
            "us surp3 sport far"
            show us surp3 sport with dspr
            "us surp3 sport"
            show us surp3 sport close with dspr
            "us surp3 sport close"
            hide us with dspr
            jump sprites_my_list_us_sport_eng
        "Upset":
            show us upset sport far with dspr
            "us upset sport far"
            show us upset sport with dspr
            "us upset sport"
            show us upset sport close with dspr
            "us upset sport close"
            hide us with dspr
            jump sprites_my_list_us_sport_eng
        ">>Back<<":
            jump sprites_my_list_us_eng

label sprites_my_list_us_swim_eng:
    menu:
        "Angry":
            show us angry swim far with dspr
            "us angry swim far"
            show us angry swim with dspr
            "us angry swim"
            show us angry swim close with dspr
            "us angry swim close"
            hide us with dspr
            jump sprites_my_list_us_swim_eng
        "Calm":
            show us calml swim far with dspr
            "us calml swim far"
            show us calml swim with dspr
            "us calml swim"
            show us calml swim close with dspr
            "us calml swim close"
            hide us with dspr
            jump sprites_my_list_us_swim_eng
        "Cry(1)":
            show us cry swim far with dspr
            "us cry swim far"
            show us cry swim with dspr
            "us cry swim"
            show us cry swim close with dspr
            "us cry swim close"
            hide us with dspr
            jump sprites_my_list_us_swim_eng
        "Cry(2)":
            show us cry2 swim far with dspr
            "us cry2 swim far"
            show us cry2 swim with dspr
            "us cry2 swim"
            show us cry2 swim close with dspr
            "us cry2 swim close"
            hide us with dspr
            jump sprites_my_list_us_swim_eng
        "Dislike":
            show us dontlike swim far with dspr
            "us dontlike swim far"
            show us dontlike swim with dspr
            "us dontlike swim"
            show us dontlike swim close with dspr
            "us dontlike swim close"
            hide us with dspr
            jump sprites_my_list_us_swim_eng
        "Fear":
            show us fear swim far with dspr
            "us fear swim far"
            show us fear swim with dspr
            "us fear swim"
            show us fear swim close with dspr
            "us fear swim close"
            hide us with dspr
            jump sprites_my_list_us_swim_eng
        "Grin":
            show us grin swim far with dspr
            "us grin swim far"
            show us grin swim with dspr
            "us grin swim"
            show us grin swim close with dspr
            "us grin swim close"
            hide us with dspr
            jump sprites_my_list_us_swim_eng
        "Laugh(1)":
            show us laugh swim far with dspr
            "us laugh swim far"
            show us laugh swim with dspr
            "us laugh swim"
            show us laugh swim close with dspr
            "us laugh swim close"
            hide us with dspr
            jump sprites_my_list_us_swim_eng
        "Laugh(2)":
            show us laugh2 swim far with dspr
            "us laugh2 swim far"
            show us laugh2 swim with dspr
            "us laugh2 swim"
            show us laugh2 swim close with dspr
            "us laugh2 swim close"
            hide us with dspr
            jump sprites_my_list_us_swim_eng
        "Normal":
            show us normal swim far with dspr
            "us normal swim far"
            show us normal swim with dspr
            "us normal swim"
            show us normal swim close with dspr
            "us normal swim close"
            hide us with dspr
            jump sprites_my_list_us_swim_eng
        "Sad":
            show us sad swim far with dspr
            "us sad swim far"
            show us sad swim with dspr
            "us sad swim"
            show us sad swim close with dspr
            "us sad swim close"
            hide us with dspr
            jump sprites_my_list_us_swim_eng
        "Shy(1)":
            show us shy swim far with dspr
            "us shy swim far"
            show us shy swim with dspr
            "us shy swim"
            show us shy swim close with dspr
            "us shy swim close"
            hide us with dspr
            jump sprites_my_list_us_swim_eng
        "Shy(2)":
            show us shy2 swim far with dspr
            "us shy2 swim far"
            show us shy2 swim with dspr
            "us shy2 swim"
            show us shy2 swim close with dspr
            "us shy2 swim close"
            hide us with dspr
            jump sprites_my_list_us_swim_eng
        "Smile":
            show us smile swim far with dspr
            "us smile swim far"
            show us smile swim with dspr
            "us smile swim"
            show us smile swim close with dspr
            "us smile swim close"
            hide us with dspr
            jump sprites_my_list_us_swim_eng
        "Surprised(1)":
            show us surp1 swim far with dspr
            "us surp1 swim far"
            show us surp1 swim with dspr
            "us surp1 swim"
            show us surp1 swim close with dspr
            "us surp1 swim close"
            hide us with dspr
            jump sprites_my_list_us_swim_eng
        "Surprised(2)":
            show us surp2 swim far with dspr
            "us surp2 swim far"
            show us surp2 swim with dspr
            "us surp2 swim"
            show us surp2 swim close with dspr
            "us surp2 swim close"
            hide us with dspr
            jump sprites_my_list_us_swim_eng
        "Surprised(3)":
            show us surp3 swim far with dspr
            "us surp3 swim far"
            show us surp3 swim with dspr
            "us surp3 swim"
            show us surp3 swim close with dspr
            "us surp3 swim close"
            hide us with dspr
            jump sprites_my_list_us_swim_eng
        "Upset":
            show us upset swim far with dspr
            "us upset swim far"
            show us upset swim with dspr
            "us upset swim"
            show us upset swim close with dspr
            "us upset swim close"
            hide us with dspr
            jump sprites_my_list_us_swim_eng
        ">>Back<<":
            jump sprites_my_list_us_eng

label sprites_my_list_mt_eng:
    menu:
        "Normal":
            jump sprites_my_list_mt_normal_eng
        "With panama":
            jump sprites_my_list_mt_panama_eng
        ">>Back<<":
            jump sprites_my_list_eng

label sprites_my_list_mt_normal_eng:
    menu:
        "Pioneer Form":
            jump sprites_my_list_mt_normal_pioneer_eng
        "Dress":
            jump sprites_my_list_mt_normal_dress_eng
        "Swimsuit":
            jump sprites_my_list_mt_normal_swim_eng
        ">>Back<<":
            jump sprites_my_list_mt_eng

label sprites_my_list_mt_normal_pioneer_eng:
    menu:
        "Cry":
            show mt cry pioneer far with dspr
            "mt cry pioneer far"
            show mt cry pioneer with dspr
            "mt cry pioneer"
            show mt cry pioneer close with dspr
            "mt cry pioneer close"
            hide mt with dspr
            jump sprites_my_list_mt_normal_pioneer_eng
        "Angry":
            show mt angry pioneer far with dspr
            "mt angry pioneer far"
            show mt angry pioneer with dspr
            "mt angry pioneer"
            show mt angry pioneer close with dspr
            "mt angry pioneer close"
            hide mt with dspr
            jump sprites_my_list_mt_normal_pioneer_eng
        "Grin":
            show mt grin pioneer far with dspr
            "mt grin pioneer far"
            show mt grin pioneer with dspr
            "mt grin pioneer"
            show mt grin pioneer close with dspr
            "mt grin pioneer close"
            hide mt with dspr
            jump sprites_my_list_mt_normal_pioneer_eng
        "Laugh":
            show mt laugh pioneer far with dspr
            "mt laugh pioneer far"
            show mt laugh pioneer with dspr
            "mt laugh pioneer"
            show mt laugh pioneer close with dspr
            "mt laugh pioneer close"
            hide mt with dspr
            jump sprites_my_list_mt_normal_pioneer_eng
        "Normal":
            show mt normal pioneer far with dspr
            "mt normal pioneer far"
            show mt normal pioneer with dspr
            "mt normal pioneer"
            show mt normal pioneer close with dspr
            "mt normal pioneer close"
            hide mt with dspr
            jump sprites_my_list_mt_normal_pioneer_eng
        "Rage":
            show mt rage pioneer far with dspr
            "mt rage pioneer far"
            show mt rage pioneer with dspr
            "mt rage pioneer"
            show mt rage pioneer close with dspr
            "mt rage pioneer close"
            hide mt with dspr
            jump sprites_my_list_mt_normal_pioneer_eng
        "Upset":
            show mt sad pioneer far with dspr
            "mt sad pioneer far"
            show mt sad pioneer with dspr
            "mt sad pioneer"
            show mt sad pioneer close with dspr
            "mt sad pioneer close"
            hide mt with dspr
            jump sprites_my_list_mt_normal_pioneer_eng
        "Scared":
            show mt scared pioneer far with dspr
            "mt scared pioneer"
            show mt scared pioneer with dspr
            "mt scared pioneer"
            show mt scared pioneer close with dspr
            "mt scared pioneer close"
            hide mt with dspr
            jump sprites_my_list_mt_normal_pioneer_eng
        "Shocked":
            show mt shocked pioneer far with dspr
            "mt shocked pioneer"
            show mt shocked pioneer with dspr
            "mt shocked pioneer"
            show mt shocked pioneer close with dspr
            "mt shocked pioneer"
            hide mt with dspr
            jump sprites_my_list_mt_normal_pioneer_eng
        "Smile":
            show mt smile pioneer far with dspr
            "mt smile pioneer far"
            show mt smile pioneer with dspr
            "mt smile pioneer"
            show mt smile pioneer close with dspr
            "mt smile pioneer close"
            hide mt with dspr
            jump sprites_my_list_mt_normal_pioneer_eng
        "Surprised":
            show mt surprise pioneer far with dspr
            "mt surprise pioneer far"
            show mt surprise pioneer with dspr
            "mt surprise pioneer"
            show mt surprise pioneer close with dspr
            "mt surprise pioneer close"
            hide mt with dspr
            jump sprites_my_list_mt_normal_pioneer_eng
        ">>Back<<":
            jump sprites_my_list_mt_normal_eng

label sprites_my_list_mt_normal_dress_eng:
    menu:
        "Angry":
            show mt angry dress far with dspr
            "mt angry dress far"
            show mt angry dress with dspr
            "mt angry dress"
            show mt angry dress close with dspr
            "mt angry dress close"
            hide mt with dspr
            jump sprites_my_list_mt_normal_dress_eng
        "Normal":
            show mt normal dress far with dspr
            "mt normal dress far"
            show mt normal dress with dspr
            "mt normal dress"
            show mt normal dress close with dspr
            "mt normal dress close"
            hide mt with dspr
            jump sprites_my_list_mt_normal_dress_eng
        "Rage":
            show mt rage dress far with dspr
            "mt rage dress far"
            show mt rage dress with dspr
            "mt rage dress"
            show mt rage dress close with dspr
            "mt rage dress close"
            hide mt with dspr
            jump sprites_my_list_mt_normal_dress_eng
        "Upset":
            show mt sad dress far with dspr
            "mt sad dress far"
            show mt sad dress with dspr
            "mt sad dress"
            show mt sad dress close with dspr
            "mt sad dress close"
            hide mt with dspr
            jump sprites_my_list_mt_normal_dress_eng
        "Scared":
            show mt scared dress far with dspr
            "mt scared dress"
            show mt scared dress with dspr
            "mt scared dress"
            show mt scared dress close with dspr
            "mt scared dress close"
            hide mt with dspr
            jump sprites_my_list_mt_normal_pioneer_eng
        "Shocked":
            show mt shocked dress far with dspr
            "mt shocked dress"
            show mt shocked dress with dspr
            "mt shocked dress"
            show mt shocked dress close with dspr
            "mt shocked dress"
            hide mt with dspr
            jump sprites_my_list_mt_normal_pioneer_eng
        "Smile":
            show mt smile dress far with dspr
            "mt smile dress far"
            show mt smile dress with dspr
            "mt smile dress"
            show mt smile dress close with dspr
            "mt smile dress close"
            hide mt with dspr
            jump sprites_my_list_mt_normal_dress_eng
        "Surprised":
            show mt surprise dress far with dspr
            "mt surprise dress far"
            show mt surprise dress with dspr
            "mt surprise dress"
            show mt surprise dress close with dspr
            "mt surprise dress close"
            hide mt with dspr
            jump sprites_my_list_mt_normal_dress_eng
        ">>Back<<":
            jump sprites_my_list_mt_normal_eng

label sprites_my_list_mt_normal_swim_eng:
    menu:
        "Angry":
            show mt angry swim far with dspr
            "mt angry swim far"
            show mt angry swim with dspr
            "mt angry swim"
            show mt angry swim close with dspr
            "mt angry swim close"
            hide mt with dspr
            jump sprites_my_list_mt_normal_swim_eng
        "Normal":
            show mt normal swim far with dspr
            "mt normal swim far"
            show mt normal swim with dspr
            "mt normal swim"
            show mt normal swim close with dspr
            "mt normal swim close"
            hide mt with dspr
            jump sprites_my_list_mt_normal_swim_eng
        "Rage":
            show mt rage swim far with dspr
            "mt rage swim far"
            show mt rage swim with dspr
            "mt rage swim"
            show mt rage swim close with dspr
            "mt rage swim close"
            hide mt with dspr
            jump sprites_my_list_mt_normal_swim_eng
        "Upset":
            show mt sad swim far with dspr
            "mt sad swim far"
            show mt sad swim with dspr
            "mt sad swim"
            show mt sad swim close with dspr
            "mt sad swim close"
            hide mt with dspr
            jump sprites_my_list_mt_normal_swim_eng
        "Scared":
            show mt scared swim far with dspr
            "mt scared swim"
            show mt scared swim with dspr
            "mt scared swim"
            show mt scared swim close with dspr
            "mt scared swim close"
            hide mt with dspr
            jump sprites_my_list_mt_normal_pioneer_eng
        "Shocked":
            show mt shocked swim far with dspr
            "mt shocked swim"
            show mt shocked swim with dspr
            "mt shocked swim"
            show mt shocked swim close with dspr
            "mt shocked swim"
            hide mt with dspr
            jump sprites_my_list_mt_normal_pioneer_eng
        "Smile":
            show mt smile swim far with dspr
            "mt smile swim far"
            show mt smile swim with dspr
            "mt smile swim"
            show mt smile swim close with dspr
            "mt smile swim close"
            hide mt with dspr
            jump sprites_my_list_mt_normal_swim_eng
        "Surprised":
            show mt surprise swim far with dspr
            "mt surprise swim far"
            show mt surprise swim with dspr
            "mt surprise swim"
            show mt surprise swim close with dspr
            "mt surprise swim close"
            hide mt with dspr
            jump sprites_my_list_mt_normal_swim_eng
        ">>Back<<":
            jump sprites_my_list_mt_normal_eng

label sprites_my_list_mt_panama_eng:
    menu:
        "Pioneer Form":
            jump sprites_my_list_mt_panama_pioneer_eng
        "Dress":
            jump sprites_my_list_mt_panama_dress_eng
        "Swimsuit":
            jump sprites_my_list_mt_panama_swim_eng
        ">>Back<<":
            jump sprites_my_list_mt_eng

label sprites_my_list_mt_panama_pioneer_eng:
    menu:
        "Angry":
            show mt angry panama pioneer far with dspr
            "mt angry panama pioneer far"
            show mt angry panama pioneer with dspr
            "mt angry panama pioneer"
            show mt angry panama pioneer close with dspr
            "mt angry panama pioneer close"
            hide mt with dspr
            jump sprites_my_list_mt_panama_pioneer_eng
        "Grin":
            show mt grin panama pioneer far with dspr
            "mt grin panama pioneer far"
            show mt grin panama pioneer with dspr
            "mt grin panama pioneer"
            show mt grin panama pioneer close with dspr
            "mt grin panama pioneer close"
            hide mt with dspr
            jump sprites_my_list_mt_panama_pioneer_eng
        "Laugh":
            show mt laugh panama pioneer far with dspr
            "mt laugh panama pioneer far"
            show mt laugh panama pioneer with dspr
            "mt laugh panama pioneer"
            show mt laugh panama pioneer close with dspr
            "mt laugh panama pioneer close"
            hide mt with dspr
            jump sprites_my_list_mt_panama_pioneer_eng
        "Normal":
            show mt normal panama pioneer far with dspr
            "mt normal panama pioneer far"
            show mt normal panama pioneer with dspr
            "mt normal panama pioneer"
            show mt normal panama pioneer close with dspr
            "mt normal panama pioneer close"
            hide mt with dspr
            jump sprites_my_list_mt_panama_pioneer_eng
        "Rage":
            show mt rage panama pioneer far with dspr
            "mt rage panama pioneer far"
            show mt rage panama pioneer with dspr
            "mt rage panama pioneer"
            show mt rage panama pioneer close with dspr
            "mt rage panama pioneer close"
            hide mt with dspr
            jump sprites_my_list_mt_panama_pioneer_eng
        "Upset":
            show mt sad panama pioneer far with dspr
            "mt sad panama pioneer far"
            show mt sad panama pioneer with dspr
            "mt sad panama pioneer"
            show mt sad panama pioneer close with dspr
            "mt sad panama pioneer close"
            hide mt with dspr
            jump sprites_my_list_mt_panama_pioneer_eng
        "Scared":
            show mt scared panama pioneer far with dspr
            "mt scared panama pioneer"
            show mt scared panama pioneer with dspr
            "mt scared panama pioneer"
            show mt scared panama pioneer close with dspr
            "mt scared panama pioneer close"
            hide mt with dspr
            jump sprites_my_list_mt_normal_pioneer_eng
        "Shocked":
            show mt shocked panama pioneer far with dspr
            "mt shocked panama pioneer"
            show mt shocked panama pioneer with dspr
            "mt shocked panama pioneer"
            show mt shocked panama pioneer close with dspr
            "mt shocked panama pioneer"
            hide mt with dspr
            jump sprites_my_list_mt_normal_pioneer_eng
        "Smile":
            show mt smile panama pioneer far with dspr
            "mt smile panama pioneer far"
            show mt smile panama pioneer with dspr
            "mt smile panama pioneer"
            show mt smile panama pioneer close with dspr
            "mt smile panama pioneer close"
            hide mt with dspr
            jump sprites_my_list_mt_panama_pioneer_eng
        "Surprised":
            show mt surprise panama pioneer far with dspr
            "mt surprise panama pioneer far"
            show mt surprise panama pioneer with dspr
            "mt surprise panama pioneer"
            show mt surprise panama pioneer close with dspr
            "mt surprise panama pioneer close"
            hide mt with dspr
            jump sprites_my_list_mt_panama_pioneer_eng

        ">>Back<<":
            jump sprites_my_list_mt_normal_eng

label sprites_my_list_mt_panama_dress_eng:
    menu:
        "Angry":
            show mt angry panama dress far with dspr
            "mt angry panama dress far"
            show mt angry panama dress with dspr
            "mt angry panama dress"
            show mt angry panama dress close with dspr
            "mt angry panama dress close"
            hide mt with dspr
            jump sprites_my_list_mt_panama_dress_eng
        "Normal":
            show mt normal panama dress far with dspr
            "mt normal panama dress far"
            show mt normal panama dress with dspr
            "mt normal panama dress"
            show mt normal panama dress close with dspr
            "mt normal panama dress close"
            hide mt with dspr
            jump sprites_my_list_mt_panama_dress_eng
        "Rage":
            show mt rage panama dress far with dspr
            "mt rage panama dress far"
            show mt rage panama dress with dspr
            "mt rage panama dress"
            show mt rage panama dress close with dspr
            "mt rage panama dress close"
            hide mt with dspr
            jump sprites_my_list_mt_panama_dress_eng
        "Upset":
            show mt sad panama dress far with dspr
            "mt sad panama dress far"
            show mt sad panama dress with dspr
            "mt sad panama dress"
            show mt sad panama dress close with dspr
            "mt sad panama dress close"
            hide mt with dspr
            jump sprites_my_list_mt_panama_dress_eng
        "Scared":
            show mt scared panama dress far with dspr
            "mt scared panama dress"
            show mt scared panama dress with dspr
            "mt scared panama dress"
            show mt scared panama dress close with dspr
            "mt scared panama dress close"
            hide mt with dspr
            jump sprites_my_list_mt_panama_dress_eng
        "Shocked":
            show mt shocked panama dress far with dspr
            "mt shocked panama dress"
            show mt shocked panama dress with dspr
            "mt shocked panama dress"
            show mt shocked panama dress close with dspr
            "mt shocked panama dress"
            hide mt with dspr
            jump sprites_my_list_mt_panama_dress_eng
        "Smile":
            show mt smile panama dress far with dspr
            "mt smile panama dress far"
            show mt smile panama dress with dspr
            "mt smile panama dress"
            show mt smile panama dress close with dspr
            "mt smile panama dress close"
            hide mt with dspr
            jump sprites_my_list_mt_panama_dress_eng
        "Surprised":
            show mt surprise panama dress far with dspr
            "mt surprise panama dress far"
            show mt surprise panama dress with dspr
            "mt surprise panama dress"
            show mt surprise panama dress close with dspr
            "mt surprise panama dress close"
            hide mt with dspr
            jump sprites_my_list_mt_panama_dress_eng
        ">>Back<<":
            jump sprites_my_list_mt_normal_eng

label sprites_my_list_mt_panama_swim_eng:
    menu:
        "Angry":
            show mt angry panama swim far with dspr
            "mt angry panama swim far"
            show mt angry panama swim with dspr
            "mt angry panama swim"
            show mt angry panama swim close with dspr
            "mt angry panama swim close"
            hide mt with dspr
            jump sprites_my_list_mt_panama_swim_eng
        "Normal":
            show mt normal panama swim far with dspr
            "mt normal panama swim far"
            show mt normal panama swim with dspr
            "mt normal panama swim"
            show mt normal panama swim close with dspr
            "mt normal panama swim close"
            hide mt with dspr
            jump sprites_my_list_mt_panama_swim_eng
        "Rage":
            show mt rage panama swim far with dspr
            "mt rage panama swim far"
            show mt rage panama swim with dspr
            "mt rage panama swim"
            show mt rage panama swim close with dspr
            "mt rage panama swim close"
            hide mt with dspr
            jump sprites_my_list_mt_panama_swim_eng
        "Upset":
            show mt sad panama swim far with dspr
            "mt sad panama swim far"
            show mt sad panama swim with dspr
            "mt sad panama swim"
            show mt sad panama swim close with dspr
            "mt sad panama swim close"
            hide mt with dspr
            jump sprites_my_list_mt_panama_swim_eng
        "Scared":
            show mt scared panama swim far with dspr
            "mt scared panama swim"
            show mt scared panama swim with dspr
            "mt scared panama swim"
            show mt scared panama swim close with dspr
            "mt scared panama swim close"
            hide mt with dspr
            jump sprites_my_list_mt_panama_swim_eng
        "Shocked":
            show mt shocked panama swim far with dspr
            "mt shocked panama swim"
            show mt shocked panama swim with dspr
            "mt shocked panama swim"
            show mt shocked panama swim close with dspr
            "mt shocked panama swim"
            hide mt with dspr
            jump sprites_my_list_mt_panama_swim_eng
        "Smile":
            show mt smile panama swim far with dspr
            "mt smile panama swim far"
            show mt smile panama swim with dspr
            "mt smile panama swim"
            show mt smile panama swim close with dspr
            "mt smile panama swim close"
            hide mt with dspr
            jump sprites_my_list_mt_panama_swim_eng
        "Surprised":
            show mt surprise panama swim far with dspr
            "mt surprise panama swim far"
            show mt surprise panama swim with dspr
            "mt surprise panama swim"
            show mt surprise panama swim close with dspr
            "mt surprise panama swim close"
            hide mt with dspr
            jump sprites_my_list_mt_panama_swim_eng
        ">>Back<<":
            jump sprites_my_list_mt_normal_eng

label sprites_my_list_uv_eng:
    menu:
        "Dislike":
            show uv dontlike far with dspr
            "uv dontlike far"
            show uv dontlike with dspr
            "uv dontlike "
            show uv dontlike close with dspr
            "uv dontlike close"
            hide uv with dspr
            jump sprites_my_list_uv_eng
        "Grin":
            show uv grin far with dspr
            "uv grin far"
            show uv grin with dspr
            "uv grin "
            show uv grin close with dspr
            "uv grin close"
            hide uv with dspr
            jump sprites_my_list_uv_eng
        "Guilty":
            show uv guilty far with dspr
            "uv guilty far"
            show uv guilty with dspr
            "uv guilty "
            show uv guilty close with dspr
            "uv guilty close"
            hide uv with dspr
            jump sprites_my_list_uv_eng
        "Laugh":
            show uv laugh far with dspr
            "uv laugh far"
            show uv laugh with dspr
            "uv laugh "
            show uv laugh close with dspr
            "uv laugh close"
            hide uv with dspr
            jump sprites_my_list_uv_eng
        "Normal":
            show uv normal far with dspr
            "uv normal far"
            show uv normal with dspr
            "uv normal "
            show uv normal close with dspr
            "uv normal close"
            hide uv with dspr
            jump sprites_my_list_uv_eng
        "Rage":
            show uv rage far with dspr
            "uv rage far"
            show uv rage with dspr
            "uv rage "
            show uv rage close with dspr
            "uv rage close"
            hide uv with dspr
            jump sprites_my_list_uv_eng
        "Sad":
            show uv sad far with dspr
            "uv sad far"
            show uv sad with dspr
            "uv sad "
            show uv sad close with dspr
            "uv sad close"
            hide uv with dspr
            jump sprites_my_list_uv_eng
        "Shocked":
            show uv shocked far with dspr
            "uv shocked far"
            show uv shocked with dspr
            "uv shocked "
            show uv shocked close with dspr
            "uv shocked close"
            hide uv with dspr
            jump sprites_my_list_uv_eng
        "Smile":
            show uv smile far with dspr
            "uv smile far"
            show uv smile with dspr
            "uv smile "
            show uv smile close with dspr
            "uv smile close"
            hide uv with dspr
            jump sprites_my_list_uv_eng
        "Surprised":
            show uv surprise far with dspr
            "uv surprise far"
            show uv surprise with dspr
            "uv surprise "
            show uv surprise close with dspr
            "uv surprise close"
            hide uv with dspr
            jump sprites_my_list_uv_eng
        "Surprised(2)":
            show uv surprise2 far with dspr
            "uv surprise2 far"
            show uv surprise2 with dspr
            "uv surprise2 "
            show uv surprise2 close with dspr
            "uv surprise2 close"
            hide uv with dspr
            jump sprites_my_list_uv_eng
        "Upset":
            show uv upset far with dspr
            "uv upset far"
            show uv upset with dspr
            "uv upset "
            show uv upset close with dspr
            "uv upset close"
            hide uv with dspr
            jump sprites_my_list_uv_eng
        ">>Back<<":
            jump sprites_my_list_eng

label sprites_my_list_mz_eng:
    menu:
        "Glasses":
            jump sprites_my_list_mz_glasses_eng
        "Without glasses":
            jump sprites_my_list_mz_normal_eng
        ">>Back<<":
            jump sprites_my_list_eng

label sprites_my_list_mz_glasses_eng:
    menu:
        "Angry":
            show mz angry glasses pioneer far with dspr
            "mz angry glasses pioneer far"
            show mz angry glasses pioneer with dspr
            "mz angry glasses pioneer"
            show mz angry glasses pioneer close with dspr
            "mz angry glasses pioneer close"
            hide mz with dspr
            jump sprites_my_list_mz_glasses_eng
        "Indifferent":
            show mz bukal glasses pioneer far with dspr
            "mz bukal glasses pioneer far"
            show mz bukal glasses pioneer with dspr
            "mz bukal glasses pioneer"
            show mz bukal glasses pioneer close with dspr
            "mz bukal glasses pioneer close"
            hide mz with dspr
            jump sprites_my_list_mz_glasses_eng
        "Laugh":
            show mz laugh glasses pioneer far with dspr
            "mz laugh glasses pioneer far"
            show mz laugh glasses pioneer with dspr
            "mz laugh glasses pioneer"
            show mz laugh glasses pioneer close with dspr
            "mz laugh glasses pioneer close"
            hide mz with dspr
            jump sprites_my_list_mz_glasses_eng
        "Normal":
            show mz normal glasses pioneer far with dspr
            "mz normal glasses pioneer far"
            show mz normal glasses pioneer with dspr
            "mz normal glasses pioneer"
            show mz normal glasses pioneer close with dspr
            "mz normal glasses pioneer close"
            hide mz with dspr
            jump sprites_my_list_mz_glasses_eng
        "Rage":
            show mz rage glasses pioneer far with dspr
            "mz rage glasses pioneer far"
            show mz rage glasses pioneer with dspr
            "mz rage glasses pioneer"
            show mz rage glasses pioneer close with dspr
            "mz rage glasses pioneer close"
            hide mz with dspr
            jump sprites_my_list_mz_glasses_eng
        "Shy":
            show mz shy glasses pioneer far with dspr
            "mz shy glasses pioneer far"
            show mz shy glasses pioneer with dspr
            "mz shy glasses pioneer"
            show mz shy glasses pioneer close with dspr
            "mz shy glasses pioneer close"
            hide mz with dspr
            jump sprites_my_list_mz_glasses_eng
        "Smile":
            show mz smile glasses pioneer far with dspr
            "mz smile glasses pioneer far"
            show mz smile glasses pioneer with dspr
            "mz smile glasses pioneer"
            show mz smile glasses pioneer close with dspr
            "mz smile glasses pioneer close"
            hide mz with dspr
            jump sprites_my_list_mz_glasses_eng
        ">>Back<<":
            jump sprites_my_list_mz_eng

label sprites_my_list_mz_normal_eng:
    menu:
        "Angry":
            show mz angry pioneer far with dspr
            "mz angry pioneer far"
            show mz angry pioneer with dspr
            "mz angry pioneer"
            show mz angry pioneer close with dspr
            "mz angry pioneer close"
            hide mz with dspr
            jump sprites_my_list_mz_normal_eng
        "Indifferent":
            show mz bukal pioneer far with dspr
            "mz bukal pioneer far"
            show mz bukal pioneer with dspr
            "mz bukal pioneer"
            show mz bukal pioneer close with dspr
            "mz bukal pioneer close"
            hide mz with dspr
            jump sprites_my_list_mz_normal_eng
        "Laugh":
            show mz laugh pioneer far with dspr
            "mz laugh pioneer far"
            show mz laugh pioneer with dspr
            "mz laugh pioneer"
            show mz laugh pioneer close with dspr
            "mz laugh pioneer close"
            hide mz with dspr
            jump sprites_my_list_mz_normal_eng
        "Normal":
            show mz normal pioneer far with dspr
            "mz normal pioneer far"
            show mz normal pioneer with dspr
            "mz normal pioneer"
            show mz normal pioneer close with dspr
            "mz normal pioneer close"
            hide mz with dspr
            jump sprites_my_list_mz_normal_eng
        "Rage":
            show mz rage pioneer far with dspr
            "mz rage pioneer far"
            show mz rage pioneer with dspr
            "mz rage pioneer"
            show mz rage pioneer close with dspr
            "mz rage pioneer close"
            hide mz with dspr
            jump sprites_my_list_mz_normal_eng
        "Shy":
            show mz shy pioneer far with dspr
            "mz shy pioneer far"
            show mz shy pioneer with dspr
            "mz shy pioneer"
            show mz shy pioneer close with dspr
            "mz shy pioneer close"
            hide mz with dspr
            jump sprites_my_list_mz_normal_eng
        "Smile":
            show mz smile pioneer far with dspr
            "mz smile pioneer far"
            show mz smile pioneer with dspr
            "mz smile pioneer"
            show mz smile pioneer close with dspr
            "mz smile pioneer close"
            hide mz with dspr
            jump sprites_my_list_mz_normal_eng
        ">>Back<<":
            jump sprites_my_list_mz_eng

label sprites_my_list_cs_eng:
    menu:
        "Normal":
            jump sprites_my_list_cs_normal_eng
        "Glasses":
            jump sprites_my_list_cs_glasses_eng
        "Stethoscope":
            jump sprites_my_list_cs_stethoscope_eng
        ">>Back<<":
            jump sprites_my_list_eng

label sprites_my_list_cs_normal_eng:
    menu:
        "Normal":
            show cs normal far with dspr
            "cs normal far"
            show cs normal with dspr
            "cs normal"
            show cs normal close with dspr
            "cs normal close"
            hide cs with dspr
            jump sprites_my_list_cs_normal_eng
        "Smile":
            show cs smile far with dspr
            "cs smile far"
            show cs smile with dspr
            "cs smile"
            show cs smile close with dspr
            "cs smile close"
            hide cs with dspr
            jump sprites_my_list_cs_normal_eng
        "Shy":
            show cs shy far with dspr
            "cs shy far"
            show cs shy with dspr
            "cs shy"
            show cs shy close with dspr
            "cs shy close"
            hide cs with dspr
            jump sprites_my_list_cs_normal_eng
        ">>Back<<":
            jump sprites_my_list_cs_eng

label sprites_my_list_cs_glasses_eng:
    menu:
        "Normal":
            show cs normal glasses far with dspr
            "cs normal glasses far"
            show cs normal glasses with dspr
            "cs normal glasses"
            show cs normal glasses close with dspr
            "cs normal glasses close"
            hide cs with dspr
            jump sprites_my_list_cs_glasses_eng
        "Smile":
            show cs smile glasses far with dspr
            "cs smile glasses far"
            show cs smile glasses with dspr
            "cs smile glasses"
            show cs smile glasses close with dspr
            "cs smile glasses close"
            hide cs with dspr
            jump sprites_my_list_cs_glasses_eng
        "Shy":
            show cs shy glasses far with dspr
            "cs shy glasses far"
            show cs shy glasses with dspr
            "cs shy glasses"
            show cs shy glasses close with dspr
            "cs shy glasses close"
            hide cs with dspr
            jump sprites_my_list_cs_glasses_eng
        ">>Back<<":
            jump sprites_my_list_cs_eng

label sprites_my_list_cs_stethoscope_eng:
    menu:
        "Normal":
            show cs normal stethoscope far with dspr
            "cs normal stethoscope far"
            show cs normal stethoscope with dspr
            "cs normal stethoscope"
            show cs normal stethoscope close with dspr
            "cs normal stethoscope close"
            hide cs with dspr
            jump sprites_my_list_cs_stethoscope_eng
        "Smile":
            show cs smile stethoscope far with dspr
            "cs smile stethoscope far"
            show cs smile stethoscope with dspr
            "cs smile stethoscope"
            show cs smile stethoscope close with dspr
            "cs smile stethoscope close"
            hide cs with dspr
            jump sprites_my_list_cs_stethoscope_eng
        "Shy":
            show cs shy stethoscope far with dspr
            "cs shy stethoscope far"
            show cs shy stethoscope with dspr
            "cs shy stethoscope"
            show cs shy stethoscope close with dspr
            "cs shy stethoscope close"
            hide cs with dspr
            jump sprites_my_list_cs_stethoscope_eng
        ">>Back<<":
            jump sprites_my_list_cs_eng

label sprites_my_list_el_eng:
    menu:
        "Fingal":
            show el fingal pioneer far with dspr
            "el fingal pioneer far"
            show el fingal pioneer with dspr
            "el fingal pioneer"
            show el fingal pioneer close with dspr
            "el fingal pioneer close"
            hide el with dspr
            jump sprites_my_list_el_eng
        "Angry":
            show el angry pioneer far with dspr
            "el angry pioneer far"
            show el angry pioneer with dspr
            "el angry pioneer"
            show el angry pioneer close with dspr
            "el angry pioneer close"
            hide el with dspr
            jump sprites_my_list_el_eng
        "Grin":
            show el grin pioneer far with dspr
            "el grin pioneer far"
            show el grin pioneer with dspr
            "el grin pioneer"
            show el grin pioneer close with dspr
            "el grin pioneer close"
            hide el with dspr
            jump sprites_my_list_el_eng
        "Laugh":
            show el laugh pioneer far with dspr
            "el laugh pioneer far"
            show el laugh pioneer with dspr
            "el laugh pioneer"
            show el laugh pioneer close with dspr
            "el laugh pioneer close"
            hide el with dspr
            jump sprites_my_list_el_eng
        "Normal":
            show el normal pioneer far with dspr
            "el normal pioneer far"
            show el normal pioneer with dspr
            "el normal pioneer"
            show el normal pioneer close with dspr
            "el normal pioneer close"
            hide el with dspr
            jump sprites_my_list_el_eng
        "Sad":
            show el sad pioneer far with dspr
            "el sad pioneer far"
            show el sad pioneer with dspr
            "el sad pioneer"
            show el sad pioneer close with dspr
            "el sad pioneer close"
            hide el with dspr
            jump sprites_my_list_el_eng
        "Scared":
            show el scared pioneer far with dspr
            "el scared pioneer far"
            show el scared pioneer with dspr
            "el scared pioneer"
            show el scared pioneer close with dspr
            "el scared pioneer close"
            hide el with dspr
            jump sprites_my_list_el_eng
        "Serious":
            show el serious pioneer far with dspr
            "el serious pioneer far"
            show el serious pioneer with dspr
            "el serious pioneer"
            show el serious pioneer close with dspr
            "el serious pioneer close"
            hide el with dspr
            jump sprites_my_list_el_eng
        "Shocked":
            show el shocked pioneer far with dspr
            "el shocked pioneer far"
            show el shocked pioneer with dspr
            "el shocked pioneer"
            show el shocked pioneer close with dspr
            "el shocked pioneer close"
            hide el with dspr
            jump sprites_my_list_el_eng
        "Smile":
            show el smile pioneer far with dspr
            "el smile pioneer far"
            show el smile pioneer with dspr
            "el smile pioneer"
            show el smile pioneer close with dspr
            "el smile pioneer close"
            hide el with dspr
            jump sprites_my_list_el_eng
        "Surprised":
            show el surprise pioneer far with dspr
            "el surprise pioneer far"
            show el surprise pioneer with dspr
            "el surprise pioneer"
            show el surprise pioneer close with dspr
            "el surprise pioneer close"
            hide el with dspr
            jump sprites_my_list_el_eng
        "Upset":
            show el upset pioneer far with dspr
            "el angry pioneer far"
            show el angry pioneer with dspr
            "el angry pioneer"
            show el angry pioneer close with dspr
            "el angry pioneer close"
            hide el with dspr
            jump sprites_my_list_el_eng
        ">>Back<<":
            jump sprites_my_list_eng

label sprites_my_list_sh_eng:
    menu:
        "Normal":
            jump sprites_my_list_sh_1_eng
        "Glases":
            jump sprites_my_list_sh_2_eng
        ">>Back<<":
            jump sprites_my_list_eng

label sprites_my_list_sh_1_eng:
    menu:
        "Cry":
            show sh cry far with dspr
            "sh cry far"
            show sh cry with dspr
            "sh cry"
            show sh cry close with dspr
            "sh cry close"
            hide sh with dspr
            jump sprites_my_list_sh_1_eng
        "Laugh":
            show sh laugh far with dspr
            "sh laugh far"
            show sh laugh with dspr
            "sh laugh"
            show sh laugh close with dspr
            "sh laugh close"
            hide sh with dspr
            jump sprites_my_list_sh_1_eng
        "Normal":
            show sh normal far with dspr
            "sh normal far"
            show sh normal with dspr
            "sh normal"
            show sh normal close with dspr
            "sh normal close"
            hide sh with dspr
            jump sprites_my_list_sh_1_eng
        "Normal Smile":
            show sh normal_smile far with dspr
            "sh normal_smile far"
            show sh normal_smile with dspr
            "sh normal_smile"
            show sh normal_smile close with dspr
            "sh normal_smile close"
            hide sh with dspr
            jump sprites_my_list_sh_1_eng
        "Rage":
            show sh rage far with dspr
            "sh rage far"
            show sh rage with dspr
            "sh rage"
            show sh rage close with dspr
            "sh rage close"
            hide sh with dspr
            jump sprites_my_list_sh_1_eng
        "Scared":
            show sh scared far with dspr
            "sh scared far"
            show sh scared with dspr
            "sh scared"
            show sh scared close with dspr
            "sh scared close"
            hide sh with dspr
            jump sprites_my_list_sh_1_eng
        "Serious":
            show sh serious far with dspr
            "sh serious far"
            show sh serious with dspr
            "sh serious"
            show sh serious close with dspr
            "sh serious close"
            hide sh with dspr
            jump sprites_my_list_sh_1_eng
        "Smile":
            show sh smile far with dspr
            "sh smile far"
            show sh smile with dspr
            "sh smile"
            show sh smile close with dspr
            "sh smile close"
            hide sh with dspr
            jump sprites_my_list_sh_1_eng
        "Surprised":
            show sh surprise far with dspr
            "sh surprise far"
            show sh surprise with dspr
            "sh surprise"
            show sh surprise close with dspr
            "sh surprise close"
            hide sh with dspr
            jump sprites_my_list_sh_1_eng
        "Upset":
            show sh upset far with dspr
            "sh upset far"
            show sh upset with dspr
            "sh upset"
            show sh upset close with dspr
            "sh upset close"
            hide sh with dspr
            jump sprites_my_list_sh_1_eng
        ">>Back<<":
            jump sprites_my_list_sh_eng

label sprites_my_list_sh_2_eng:
    menu:
        "Cry":
            show sh cry pioneer far with dspr
            "sh cry pioneer far"
            show sh cry pioneer with dspr
            "sh cry pioneer"
            show sh cry pioneer close with dspr
            "sh cry pioneer close"
            hide sh with dspr
            jump sprites_my_list_sh_2_eng
        "Laugh":
            show sh laugh pioneer far with dspr
            "sh laugh pioneer far"
            show sh laugh pioneer with dspr
            "sh laugh pioneer"
            show sh laugh pioneer close with dspr
            "sh laugh pioneer close"
            hide sh with dspr
            jump sprites_my_list_sh_2_eng
        "Normal":
            show sh normal pioneer far with dspr
            "sh normal pioneer far"
            show sh normal pioneer with dspr
            "sh normal pioneer"
            show sh normal pioneer close with dspr
            "sh normal pioneer close"
            hide sh with dspr
            jump sprites_my_list_sh_2_eng
        "Normal smile":
            show sh normal_smile pioneer far with dspr
            "sh normal_smile pioneer far"
            show sh normal_smile pioneer with dspr
            "sh normal_smile pioneer"
            show sh normal_smile pioneer close with dspr
            "sh normal_smile pioneer close"
            hide sh with dspr
            jump sprites_my_list_sh_2_eng
        "Rage":
            show sh rage pioneer far with dspr
            "sh rage pioneer far"
            show sh rage pioneer with dspr
            "sh rage pioneer"
            show sh rage pioneer close with dspr
            "sh rage pioneer close"
            hide sh with dspr
            jump sprites_my_list_sh_2_eng
        "Scared":
            show sh scared pioneer far with dspr
            "sh scared pioneer far"
            show sh scared pioneer with dspr
            "sh scared pioneer"
            show sh scared pioneer close with dspr
            "sh scared pioneer close"
            hide sh with dspr
            jump sprites_my_list_sh_2_eng
        "Serious":
            show sh serious pioneer far with dspr
            "sh serious pioneer far"
            show sh serious pioneer with dspr
            "sh serious pioneer"
            show sh serious pioneer close with dspr
            "sh serious pioneer close"
            hide sh with dspr
            jump sprites_my_list_sh_2_eng
        "Smile":
            show sh smile pioneer far with dspr
            "sh smile pioneer far"
            show sh smile pioneer with dspr
            "sh smile pioneer"
            show sh smile pioneer close with dspr
            "sh smile pioneer close"
            hide sh with dspr
            jump sprites_my_list_sh_2_eng
        "Surprised":
            show sh surprise pioneer far with dspr
            "sh surprise pioneer far"
            show sh surprise pioneer with dspr
            "sh surprise pioneer"
            show sh surprise pioneer close with dspr
            "sh surprise pioneer close"
            hide sh with dspr
            jump sprites_my_list_sh_2_eng
        "Upset":
            show sh upset pioneer far with dspr
            "sh upset pioneer far"
            show sh upset pioneer with dspr
            "sh upset pioneer"
            show sh upset pioneer close with dspr
            "sh upset pioneer close"
            hide sh with dspr
            jump sprites_my_list_sh_2_eng
        ">>Back<<":
            jump sprites_my_list_sh_eng

label sprites_my_list_pi_eng:
    menu:
        "Normal":
            show pi far with dspr
            "pi far"
            show pi with dspr
            "pi"
            show pi close with dspr
            "pi close"
            hide pi with dspr
            jump sprites_my_list_pi_eng
        "Smile":
            show pi smile far with dspr
            "pi smile far"
            show pi smile with dspr
            "pi smile"
            show pi smile close with dspr
            "pi smile close"
            hide pi with dspr
            jump sprites_my_list_pi_eng
        ">>Back<<":
            jump sprites_my_list_eng
