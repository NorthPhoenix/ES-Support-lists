init:
    image zoominout_code = "mods/mylist/image/zoominout.png"
    image qwe = ParameterizedText(style = "qwe_text")
    $ style.qwe_text = Style(style.default)
    $ style.qwe_text.color = "#FF4500"
    $ style.qwe_text.drop_shadow = [ (5, 5), (5, 5), (5, 5), (5, 5) ]
    $ style.qwe_text.drop_shadow_color = "#3D2897"
    $ style.qwe_text.italic = True
    $ style.qwe_text.bold = False
    $ style.qwe_text.size = 140

    define rc = DynamicCharacter(u"rc_name", color="#ffcc00", what_color="#f1d076")

init python:
    p = "images/avatars/sl/sl-"
    sl_avatar_set = {
                     'body':p+"body.png",
                     0     :p+"emo05.png"
                }
    class CardGameRivalSl(CardGameRival):
        def pick_my_card(self):
            x = random.randrange(0,n_cards)
            while cards_my[x].name == name_of_none or cards_my[x].interesting:
                x = random.randrange(0,n_cards)
            return x

        def pick_my_card_last(self):
            return self.pick_my_card()

#=========================================================================================================================================================================================================================================
#==========================================================================================================================================================================================================================================

label qweasdzxc:
    menu:
        "{i}Мини-Уроки{/i}"
        "Тесты":
            jump mqweasdzxc
        "№1\nПереходы":
            jump lesson_transition
        "\n>>Назад<<":
            jump start_my_list

label lesson_transition:
    show ss grin_smile casual at right with pixellate
    ss "Знали, что я так умею?"
    show ss normal casual at center with blinds
    ss "А так?"
    ss "Об этом и поговорим."
    ss "Надеюсь все уже знают про {i}dissolve, fade{/i} и {i}flash.{/i}{w} Если нет, вы можете найти уроки в другом похожем на этот моде."
    ss "Сегодня речь зайдёт о более специфичных переходах. "
    show ss at fright with move
    show sl smile pioneer at left with moveinleft
    extend "С этим мне поможет Славя."
    ss "Начнём с простых... "
    $ persistent.sprite_time = 'sunset'
    scene bg int_dining_hall_sunset
    show ss normal casual at fright
    show sl smile pioneer at left
    with pixellate
    extend "{i}with pixellate{/i}!"
    ss "Он превращает картинку сначала в пиксели, а потом обратно!"
    show sl smile pioneer at center with move
    ss "{i}...with move{/i}."
    ss "Он передвигает картинку из предыдущего положения в текущее."
    show sl angry pioneer at center with hpunch
    ss "{i}...with hpunch{/i}."
    show sl scared pioneer at center with vpunch
    ss "{i}...with vpunch{/i}."
    show ss shy casual
    show sl angry pioneer at left with move
    with dspr
    ss "Прости Славя..."
    hide sl
    hide ss
    scene bg black
    scene bg int_dining_hall_sunset
    show ss smile2 casual at fright
    with blinds
    ss "Она ушла...{w} {i}with blinds{/i}."
    ss "Ладно, позовём Алису... "
    show dv normal pioneer2 at cleft with squares
    extend "{i}with squares!{/i}"
    ss "Алиса поможет нам с новыми переходами."
    ss "Существует много переходов вида {i}move.{/i}"
    ss "Группа {i}movein (moveinright, moveinleft, moveintop, moveinbottom){/i} - двигают изображение извне экрана внутрь и {i}moveout (moveoutright, moveoutleft, moveouttop, moveoutbottom){/i} - двигают изображение за пределы экрана."
    hide dv with moveoutbottom
    show dv normal pioneer2 at cleft with moveinleft
    hide dv with moveoutleft
    show dv normal pioneer2 at cleft with moveintop
    hide dv with moveouttop
    show dv normal pioneer2 at cleft behind ss with moveinright
    hide dv with moveoutright
    show dv normal pioneer2 at cleft with moveinbottom
    ss "Есть также переходы вида {i}ease.{/i}{w} Они очень похожи на переходы вида {i}move,{/i} но протекают более плавно."
    ss "Группа {i}easein (easeinright, easeinleft, easeintop, easeinbottom){/i} и {i}easeout (easeoutright, easeoutleft, easeouttop, easeoutbottom){/i}"
    hide dv with easeoutbottom
    show dv normal pioneer2 at cleft with easeinleft
    hide dv with easeoutleft
    show dv normal pioneer2 at cleft with easeintop
    hide dv with easeouttop
    show dv normal pioneer2 at cleft behind ss with easeinright
    hide dv with easeoutright
    show dv normal pioneer2 at left with easeinbottom
    ss "Ну и просто {i}...with ease{/i}."
    hide ss with dspr
    show dv normal pioneer2 at fright with ease
    show dv normal pioneer2 as dv1 at fright behind dv
    ss "Здесь просто представленны {i}ease{/i} и {i}move{/i} для сравнения."
    show dv normal pioneer2 at fleft with move
    show dv normal pioneer2 as dv1 at fleft with ease
    hide dv with dissolve
    hide dv as dv1 with dissolve
    show ss normal casual at center with dissolve
    ss "Также существует группа переходов масштабирования изображения {i}zoomin, zoomout{/i} и {i}zoominout.{/i}"
    hide ss with zoomout
    show ss smile2 casual with zoomin
    show zoominout_code:
        anchor(0,0)
        pos(20,20)
    ss "{i}\"zoominout\"{/i} используется для удобства, когда вам нужно одновременно вывести и убрать с экрана некоторые изображения."

##    show sl normal dress at left
##    show dv surprised pioneer
##    hide el
##    with zoominout

    hide zoominout_code
    show bg black
    hide ss
    with dissolve
    jump qweasdzxc

#==========================================================================================================================================================================================================================================
#==========================================================================================================================================================================================================================================

label mqweasdzxc:
    scene black
    menu:
        "{b}{i}Выбор{/b}{/i}"
        "Текст":
            jump text
        "Карты":
            jump sl_play
        "Выбор имени":
            jump pick_name
        "Спрайты":
            jump sprite_test
        ">>Назад<<":
            jump qweasdzxc

label text:
    show qwe "Всевозможный текст" with dissolve:
        xcenter 0.5
        ycenter 0.5
    pause
    jump mqweasdzxc

label sl_play:
    python:
        dialogs = {
                        (0,"win","jump"):  "sl_play_win",
                        (0,"fail","jump"): "sl_play_fail",
                        (0,"draw","jump"): "sl_play_draw",
                    }
        generate_cards("bg hall",dialogs)
        rival = CardGameRivalSl(sl_avatar_set, translation["sl"][_preferences.language])
    jump cards_gameloop

label sl_play_win:
    scene black
    menu:
        "Вы выйграли!"
        "Играть ещё":
            jump sl_play
        ">>Назад<<":
            jump mqweasdzxc
label sl_play_fail:
    scene black
    menu:
        "Вы проиграли"
        "Играть ещё":
            jump sl_play
        ">>Назад<<":
            jump mqweasdzxc
label sl_play_draw:
    scene black
    menu:
        "Ничья"
        "Играть ещё":
            jump sl_play
        ">>Назад<<":
            jump mqweasdzxc

label pick_name:
    show sl normal pioneer at cright with dissolve
    sl "Привет, как тебя зовут?"
    $ rc_name = renpy.input("Меня зовут...")
    show sl smile pioneer with dspr
    sl "Приятно познакомиться %(rc_name)s."
    rc "Взаимно."
    jump mqweasdzxc

label sprite_test:
    window hide
    show un night with dissolve
    pause
    hide un with dissolve
    window show
    jump mqweasdzxc
