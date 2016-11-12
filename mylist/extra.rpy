
label extra_my_list:
    menu:
        "Спрайты":
            jump extra_my_list_sprites
        ">>Назад<<":
            jump start_my_list

label extra_my_list_sprites:
    menu:
#        "Толян":
#            jump extra_my_list_sprites_tl
#        "QR":
#            jump extra_my_list_sprites_qr
#        "Кошмар":
#            jump extra_my_list_sprites_nightmare
#        "Uprt":
#            jump extra_my_list_sprites_uprt
        "Тело":
            jump extra_my_list_sprites_body
        ">>Назад<<":
            jump extra_my_list

label extra_my_list_sprites_tl:
    menu:
        "Обычный":
            show tl normal pioneer far with dspr
            "tl normal pioneer far"
            show tl normal pioneer with dspr
            "tl normal pioneer"
            show tl normal pioneer close with dspr
            "tl normal pioneer close"
            hide tl with dspr
            jump extra_my_list_sprites_tl
        "Злой":
            show tl rage pioneer far with dspr
            "tl rage pioneer far"
            show tl rage pioneer with dspr
            "tl rage pioneer"
            show tl rage pioneer close with dspr
            "tl rage pioneer close"
            hide tl with dspr
            jump extra_my_list_sprites_tl
        ">>Назад<<":
            jump extra_my_list_sprites

label extra_my_list_sprites_qr:
    menu:
        "Обычная":
            show qr normal with dspr
            "qr normal"
            hide qr with dspr
            jump extra_my_list_sprites_qr
        "Грязная":
            show qr dirty with dspr
            "qr dirty"
            hide qr with dspr
            jump extra_my_list_sprites_qr
        "Ня":
            show qr nya with dspr
            "qr nya"
            hide qr with dspr
            jump extra_my_list_sprites_qr
        ">>Назад<<":
            jump extra_my_list_sprites

label extra_my_list_sprites_nightmare:
    menu:
        "Виола":
            show cs dead with dspr
            "cs dead"
            show cs dead hat with dspr
            "cs dead hat"
            hide cs with dspr
            jump extra_my_list_sprites_nightmare
        "Алиса":
            show dv dead with dspr
            "dv dead"
            show dv dead neck with dspr
            "dv dead neck"
            hide dv with dspr
            jump extra_my_list_sprites_nightmare
        "Электроник":
            show el nohead with dspr
            "el nohead"
            hide el with dspr
            jump extra_my_list_sprites_nightmare
        "Мику":
            show mi nightmare with dspr
            "mi nightmare"
            hide mi with dspr
            jump extra_my_list_sprites_nightmare
        "Ольга Дмитриевна":
            show mt nightmare close with dspr
            "mt nightmare close"
            hide mt with dspr
            jump extra_my_list_sprites_nightmare
        "Женя":
            show mz burned with dspr
            "mz burned"
            show mz burned body1 with dspr
            "mz burned body1"
            show mz burned body2 with dspr
            "mz burned body2"
            show mz burned body3 with dspr
            "mz burned body3"
            show mz burned body4 with dspr
            "mz burned body4"
            hide mz with dspr
            jump extra_my_list_sprites_nightmare
        "Пионер":
            show pi blood with dspr
            "pi blood"
            hide pi with dspr
            jump extra_my_list_sprites_nightmare
        "Шурик":
            show sh dead with dspr
            "sh dead"
            show sh dead blood with dspr
            "sh dead blood"
            show sh dead hands with dspr
            "sh dead hands"
            hide sh with dspr
            jump extra_my_list_sprites_nightmare
        "Славя":
            show sl dead with dspr
            "sl dead"
            hide sl with dspr
            jump extra_my_list_sprites_nightmare
        "Лена":
            show un blood with dspr
            "un blood"
            hide un with dspr
            jump extra_my_list_sprites_nightmare
        "Ульяна":
            show us dead with dspr
            "us dead"
            show us dead elhead with dspr
            "us dead elhead"
            show us zombie with dspr
            "us zombie"
            hide us with dspr
            jump extra_my_list_sprites_nightmare
        ">>Назад<<":
            jump extra_my_list_sprites

label extra_my_list_sprites_uprt:
    menu:
        "Славя":
            show sl uprt far with dspr
            "sl uprt"
            show sl uprt with dspr
            "sl uprt"
            show sl uprt close with dspr
            "sl uprt"
            hide sl with dspr
            jump extra_my_list_sprites_uprt
        ">>Назад<<":
            jump extra_my_list_sprites

label extra_my_list_sprites_body:
    menu:
        "Алиса":
            jump extra_my_list_sprites_body_dv
"""        "Мику":
            jump extra_my_list_sprites_body_mi
        "Ольга Дмитриевна":
            jump extra_my_list_sprites_body_mt
        "Славя":
            jump extra_my_list_sprites_body_sl
        "Лена":
            jump extra_my_list_sprites_body_un
        "Ульяна":
            jump extra_my_list_sprites_body_us"""
        ">>Назад<<":
            jump extra_my_list_sprites

label extra_my_list_sprites_body_dv:
    menu:
        "Хмурая":
            show dv angry body with dspr
            "dv angry body"
            show dv angry body close with dspr
            "dv angry body close"
            hide dv with dspr
            jump extra_my_list_sprites_body_dv
        "Плачущая":
            show dv cry body with dspr
            "dv cry body"
            show dv cry body close with dspr
            "dv cry body close"
            hide dv with dspr
            jump extra_my_list_sprites_body_dv
        "Усмешка":
            show dv grin body with dspr
            "dv grin body"
            show dv grin body close with dspr
            "dv grin body close"
            hide dv with dspr
            jump extra_my_list_sprites_body_dv
        "Виноватая":
            show dv guilty body with dspr
            "dv guilty body"
            show dv guilty body close with dspr
            "dv guilty body close"
            hide dv with dspr
            jump extra_my_list_sprites_body_dv
        "Смех":
            show dv laugh body with dspr
            "dv laugh body"
            show dv laugh body close with dspr
            "dv laugh body close"
            hide dv with dspr
            jump extra_my_list_sprites_body_dv
        "Обычная":
            show dv normal body with dspr
            "dv normal body"
            show dv normal body close with dspr
            "dv normal body close"
            hide dv with dspr
            jump extra_my_list_sprites_body_dv
        "Злость":
            show dv rage body with dspr
            "dv rage body"
            show dv rage body close with dspr
            "dv rage body close"
            hide dv with dspr
            jump extra_my_list_sprites_body_dv
        "Испуганная":
            show dv scared body with dspr
            "dv scared body"
            show dv scared body close with dspr
            "dv scared body close"
            hide dv with dspr
            jump extra_my_list_sprites_body_dv
        "Грустная":
            show dv sad body with dspr
            "dv sad body"
            show dv sad body close with dspr
            "dv sad body close"
            hide dv with dspr
            jump extra_my_list_sprites_body_dv
        "Шокированная":
            show dv shocked body with dspr
            "dv shocked body"
            show dv shocked body close with dspr
            "dv shocked body close"
            hide dv with dspr
            jump extra_my_list_sprites_body_dv
        "Стесняущаяся":
            show dv shy body with dspr
            "dv shy body"
            show dv shy body close with dspr
            "dv shy body close"
            hide dv with dspr
            jump extra_my_list_sprites_body_dv
        "Улыбка":
            show dv smile body with dspr
            "dv smile body"
            show dv smile body close with dspr
            "dv smile body close"
            hide dv with dspr
            jump extra_my_list_sprites_body_dv
        "Удивлённая":
            show dv surprise body with dspr
            "dv surprise body"
            show dv surprise body close with dspr
            "dv surprise body close"
            hide dv with dspr
            jump extra_my_list_sprites_body_dv
        ">>Назад<<":
            jump extra_my_list_sprites_body

label extra_my_list_sprites_body_mi:
    menu:
        "Хмурая":
            show mi angry body far with dspr
            "mi angry body far"
            show mi angry body with dspr
            "mi angry body"
            show mi angry body close with dspr
            "mi angry body close"
            hide mi with dspr
            jump extra_my_list_sprites_body_mi
        "Плачущая":
            show mi cry body far with dspr
            "mi cry body far"
            show mi cry body with dspr
            "mi cry body"
            show mi cry body close with dspr
            "mi cry body close"
            hide mi with dspr
            jump extra_my_list_sprites_body_mi
        "Улыбка сквозь слёзы":
            show mi cry_smile body far with dspr
            "mi cry_smile body far"
            show mi cry_smile body with dspr
            "mi cry_smile body"
            show mi cry_smile body close with dspr
            "mi cry_smile body close"
            hide mi with dspr
            jump extra_my_list_sprites_body_mi
        "Неприязнь":
            show mi dontlike body far with dspr
            "mi dontlike body far"
            show mi dontlike body with dspr
            "mi dontlike body"
            show mi dontlike body close with dspr
            "mi dontlike body close"
            hide mi with dspr
            jump extra_my_list_sprites_body_mi
        "Усмешка":
            show mi grin body far with dspr
            "mi grin body far"
            show mi grin body with dspr
            "mi grin body"
            show mi grin body close with dspr
            "mi grin body close"
            hide mi with dspr
            jump extra_my_list_sprites_body_mi
        "Счастье":
            show mi happy body far with dspr
            "mi happy body far"
            show mi happy body with dspr
            "mi happy body"
            show mi happy body close with dspr
            "mi happy body close"
            hide mi with dspr
            jump extra_my_list_sprites_body_mi
        "Смех":
            show mi laugh body far with dspr
            "mi laugh body far"
            show mi laugh body with dspr
            "mi laugh body"
            show mi laugh body close with dspr
            "mi laugh body close"
            hide mi with dspr
            jump extra_my_list_sprites_body_mi
        "Обычная":
            show mi normal body far with dspr
            "mi normal body far"
            show mi normal body with dspr
            "mi normal body"
            show mi normal body close with dspr
            "mi normal body close"
            hide mi with dspr
            jump extra_my_list_sprites_body_mi
        "Злость":
            show mi rage body far with dspr
            "mi rage body far"
            show mi rage body with dspr
            "mi rage body"
            show mi rage body close with dspr
            "mi rage body close"
            hide mi with dspr
            jump extra_my_list_sprites_body_mi
        "Грустная":
            show mi sad body far with dspr
            "mi sad body far"
            show mi sad body with dspr
            "mi sad body"
            show mi sad body close with dspr
            "mi sad body close"
            hide mi with dspr
            jump extra_my_list_sprites_body_mi
        "Испуганная":
            show mi scared body far with dspr
            "mi scared body far"
            show mi scared body with dspr
            "mi scared body"
            show mi scared body close with dspr
            "mi scared body close"
            hide mi with dspr
            jump extra_my_list_sprites_body_mi
        "Серьёзная":
            show mi serious body far with dspr
            "mi serious body far"
            show mi serious body with dspr
            "mi serious body"
            show mi serious body close with dspr
            "mi serious body close"
            hide mi with dspr
            jump extra_my_list_sprites_body_mi
        "Шокированная":
            show mi shocked body far with dspr
            "mi shocked body far"
            show mi shocked body with dspr
            "mi shocked body"
            show mi shocked body close with dspr
            "mi shocked body close"
            hide mi with dspr
            jump extra_my_list_sprites_body_mi
        "Стесняущаяся":
            show mi shy body far with dspr
            "mi shy body far"
            show mi shy body with dspr
            "mi shy body"
            show mi shy body close with dspr
            "mi shy body close"
            hide mi with dspr
            jump extra_my_list_sprites_body_mi
        "Улыбка":
            show mi smile body far with dspr
            "mi smile body far"
            show mi smile body with dspr
            "mi smile body"
            show mi smile body close with dspr
            "mi smile body close"
            hide mi with dspr
            jump extra_my_list_sprites_body_mi
        "Удивлённая":
            show mi surprise body far with dspr
            "mi surprise body far"
            show mi surprise body with dspr
            "mi surprise body"
            show mi surprise body close with dspr
            "mi surprise body close"
            hide mi with dspr
            jump extra_my_list_sprites_body_mi
        "Расстроенная":
            show mi upset body far with dspr
            "mi upset body far"
            show mi upset body with dspr
            "mi upset body"
            show mi upset body close with dspr
            "mi upset body close"
            hide mi with dspr
            jump extra_my_list_sprites_body_mi
        ">>Назад<<":
            jump extra_my_list_sprites_body

label extra_my_list_sprites_body_mt:
    menu:
        "Обычная":
            jump extra_my_list_sprites_body_mt_normal
        "С панамой":
            jump extra_my_list_sprites_body_mt_panama
        ">>Назад<<":
            jump extra_my_list_sprites_body

label extra_my_list_sprites_body_mt_panama:
    menu:
        "Хмурая":
            show mt angry panama body far with dspr
            "mt angry panama body far"
            show mt angry panama body with dspr
            "mt angry panama body"
            show mt angry panama body close with dspr
            "mt angry panama body close"
            hide mt with dspr
            jump extra_my_list_sprites_body_mt_panama
        "Усмешка":
            show mt grin panama body far with dspr
            "mt grin panama body far"
            show mt grin panama body with dspr
            "mt grin panama body"
            show mt grin panama body close with dspr
            "mt grin panama body close"
            hide mt with dspr
            jump extra_my_list_sprites_body_mt_panama
        "Смех":
            show mt laugh panama body far with dspr
            "mt laugh panama body far"
            show mt laugh panama body with dspr
            "mt laugh panama body"
            show mt laugh panama body close with dspr
            "mt laugh panama body close"
            hide mt with dspr
            jump extra_my_list_sprites_body_mt_panama
        "Обычная":
            show mt normal panama body far with dspr
            "mt normal panama body far"
            show mt normal panama body with dspr
            "mt normal panama body"
            show mt normal panama body close with dspr
            "mt normal panama body close"
            hide mt with dspr
            jump extra_my_list_sprites_body_mt_panama
        "Злость":
            show mt rage panama body far with dspr
            "mt rage panama body far"
            show mt rage panama body with dspr
            "mt rage panama body"
            show mt rage panama body close with dspr
            "mt rage panama body close"
            hide mt with dspr
            jump extra_my_list_sprites_body_mt_panama
        "Расстроенная":
            show mt sad panama body far with dspr
            "mt sad panama body far"
            show mt sad panama body with dspr
            "mt sad panama body"
            show mt sad panama body close with dspr
            "mt sad panama body close"
            hide mt with dspr
            jump extra_my_list_sprites_body_mt_panama
        "Испуганная":
            show mt scared panama body far with dspr
            "mt scared panama body"
            show mt scared panama body with dspr
            "mt scared panama body"
            show mt scared panama body close with dspr
            "mt scared panama body close"
            hide mt with dspr
            jump extra_my_list_sprites_body_mt_panama
        "Шокированная":
            show mt shocked panama body far with dspr
            "mt shocked panama body"
            show mt shocked panama body with dspr
            "mt shocked panama body"
            show mt shocked panama body close with dspr
            "mt shocked panama body"
            hide mt with dspr
            jump extra_my_list_sprites_body_mt_panama
        "Улыбка":
            show mt smile panama body far with dspr
            "mt smile panama body far"
            show mt smile panama body with dspr
            "mt smile panama body"
            show mt smile panama body close with dspr
            "mt smile panama body close"
            hide mt with dspr
            jump extra_my_list_sprites_body_mt_panama
        "Удивлённая":
            show mt surprise panama body far with dspr
            "mt surprise panama body far"
            show mt surprise panama body with dspr
            "mt surprise panama body"
            show mt surprise panama body close with dspr
            "mt surprise panama body close"
            hide mt with dspr
            jump extra_my_list_sprites_body_mt_panama
        ">>Назад<<":
            jump extra_my_list_sprites_body_mt

label extra_my_list_sprites_body_mt_normal:
    menu:
        "Хмурая":
            show mt angry body far with dspr
            "mt angry body far"
            show mt angry body with dspr
            "mt angry body"
            show mt angry body close with dspr
            "mt angry body close"
            hide mt with dspr
            jump extra_my_list_sprites_body_mt_normal
        "Усмешка":
            show mt grin body far with dspr
            "mt grin body far"
            show mt grin body with dspr
            "mt grin body"
            show mt grin body close with dspr
            "mt grin body close"
            hide mt with dspr
            jump extra_my_list_sprites_body_mt_normal
        "Смех":
            show mt laugh body far with dspr
            "mt laugh body far"
            show mt laugh body with dspr
            "mt laugh body"
            show mt laugh body close with dspr
            "mt laugh body close"
            hide mt with dspr
            jump extra_my_list_sprites_body_mt_normal
        "Обычная":
            show mt normal body far with dspr
            "mt normal body far"
            show mt normal body with dspr
            "mt normal body"
            show mt normal body close with dspr
            "mt normal body close"
            hide mt with dspr
            jump extra_my_list_sprites_body_mt_normal
        "Злость":
            show mt rage body far with dspr
            "mt rage body far"
            show mt rage body with dspr
            "mt rage body"
            show mt rage body close with dspr
            "mt rage body close"
            hide mt with dspr
            jump extra_my_list_sprites_body_mt_normal
        "Расстроенная":
            show mt sad body far with dspr
            "mt sad body far"
            show mt sad body with dspr
            "mt sad body"
            show mt sad body close with dspr
            "mt sad body close"
            hide mt with dspr
            jump extra_my_list_sprites_body_mt_normal
        "Испуганная":
            show mt scared body far with dspr
            "mt scared body"
            show mt scared body with dspr
            "mt scared body"
            show mt scared body close with dspr
            "mt scared body close"
            hide mt with dspr
            jump extra_my_list_sprites_body_mt_normal
        "Шокированная":
            show mt shocked body far with dspr
            "mt shocked body"
            show mt shocked body with dspr
            "mt shocked body"
            show mt shocked body close with dspr
            "mt shocked body"
            hide mt with dspr
            jump extra_my_list_sprites_body_mt_normal
        "Улыбка":
            show mt smile body far with dspr
            "mt smile body far"
            show mt smile body with dspr
            "mt smile body"
            show mt smile body close with dspr
            "mt smile body close"
            hide mt with dspr
            jump extra_my_list_sprites_body_mt_normal
        "Удивлённая":
            show mt surprise body far with dspr
            "mt surprise body far"
            show mt surprise body with dspr
            "mt surprise body"
            show mt surprise body close with dspr
            "mt surprise body close"
            hide mt with dspr
            jump extra_my_list_sprites_body_mt_normal
        ">>Назад<<":
            jump extra_my_list_sprites_body_mt

label extra_my_list_sprites_body_sl:
    menu:
        "Злость":
            show sl angry body far with dspr
            "sl angry body far"
            show sl angry body with dspr
            "sl angry body"
            show sl angry body close with dspr
            "sl angry body close"
            hide sl with dspr
            jump extra_my_list_sprites_body_sl
        "Счастье":
            show sl happy body far with dspr
            "sl happy body far"
            show sl happy body with dspr
            "sl happy body"
            show sl happy body close with dspr
            "sl happy body close"
            hide sl with dspr
            jump extra_my_list_sprites_body_sl
        "Смех":
            show sl laugh body far with dspr
            "sl laugh body far"
            show sl laugh body with dspr
            "sl laugh body"
            show sl laugh body close with dspr
            "sl laugh body close"
            hide sl with dspr
            jump extra_my_list_sprites_body_sl
        "Обычная":
            show sl normal body far with dspr
            "sl normal body far"
            show sl normal body with dspr
            "sl normal body"
            show sl normal body close with dspr
            "sl normal body close"
            hide sl with dspr
            jump extra_my_list_sprites_body_sl
        "Грустная":
            show sl sad body far with dspr
            "sl sad body far"
            show sl sad body with dspr
            "sl sad body"
            show sl sad body close with dspr
            "sl sad body close"
            hide sl with dspr
            jump extra_my_list_sprites_body_sl
        "Испуганная":
            show sl scared body far with dspr
            "sl scared body far"
            show sl scared body with dspr
            "sl scared body"
            show sl scared body close with dspr
            "sl scared body close"
            hide sl with dspr
            jump extra_my_list_sprites_body_sl
        "Серьёзная":
            show sl serious body far with dspr
            "sl serious body far"
            show sl serious body with dspr
            "sl serious body"
            show sl serious body close with dspr
            "sl serious body close"
            hide sl with dspr
            jump extra_my_list_sprites_body_sl
        "Стесняущаяся":
            show sl shy body far with dspr
            "sl shy body far"
            show sl shy body with dspr
            "sl shy body"
            show sl shy body close with dspr
            "sl shy body close"
            hide sl with dspr
            jump extra_my_list_sprites_body_sl
        "Улыбка":
            show sl smile body far with dspr
            "sl smile body far"
            show sl smile body with dspr
            "sl smile body"
            show sl smile body close with dspr
            "sl smile body close"
            hide sl with dspr
            jump extra_my_list_sprites_body_sl
        "Улыбка(2)":
            show sl smile2 body far with dspr
            "sl smile2 body far"
            show sl smile2 body with dspr
            "sl smile2 body"
            show sl smile2 body close with dspr
            "sl smile2 body close"
            hide sl with dspr
            jump extra_my_list_sprites_body_sl
        "Удивлённая":
            show sl surprise body far with dspr
            "sl surprise body far"
            show sl surprise body with dspr
            "sl surprise body"
            show sl surprise body close with dspr
            "sl surprise body close"
            hide sl with dspr
            jump extra_my_list_sprites_body_sl
        "Нежность":
            show sl tender body far with dspr
            "sl tender body far"
            show sl tender body with dspr
            "sl tender body"
            show sl tender body close with dspr
            "sl tender body close"
            hide sl with dspr
            jump extra_my_list_sprites_body_sl
        ">>Назад<<":
            jump extra_my_list_sprites_body

label extra_my_list_sprites_body_un:
    menu:
        "Злость":
            show un angry body far with dspr
            "un angry body far"
            show un angry body with dspr
            "un angry body"
            show un angry body close with dspr
            "un angry body close"
            hide un with dspr
            jump extra_my_list_sprites_body_un
        "Хмурая":
            show un angry2 body far with dspr
            "un angry2 body far"
            show un angry2 body with dspr
            "un angry2 body"
            show un angry2 body close with dspr
            "un angry2 body close"
            hide un with dspr
            jump extra_my_list_sprites_body_un
        "Улыбка сквозь слёзы":
            show un cry_smile body far with dspr
            "un cry_smile body far"
            show un cry_smile body with dspr
            "un cry_smile body"
            show un cry_smile body close with dspr
            "un cry_smile body close"
            hide un with dspr
            jump extra_my_list_sprites_body_un
        "Плачущая":
            show un cry body far with dspr
            "un cry body far"
            show un cry body with dspr
            "un cry body"
            show un cry body close with dspr
            "un cry body close"
            hide un with dspr
            jump extra_my_list_sprites_body_un
        "Дьявольская улыбка":
            show un evil_smile body far with dspr
            "un evil_smile body far"
            show un evil_smile body with dspr
            "un evil_smile body"
            show un evil_smile body close with dspr
            "un evil_smile body close"
            hide un with dspr
            jump extra_my_list_sprites_body_un
        "Усмешка":
            show un grin body far with dspr
            "un grin body far"
            show un grin body with dspr
            "un grin body"
            show un grin body close with dspr
            "un grin body close"
            hide un with dspr
            jump extra_my_list_sprites_body_un
        "Смех":
            show un laugh body far with dspr
            "un laugh body far"
            show un laugh body with dspr
            "un laugh body"
            show un laugh body close with dspr
            "un laugh body close"
            hide un with dspr
            jump extra_my_list_sprites_body_un
        "Обычная":
            show un normal body far with dspr
            "un normal body far"
            show un normal body with dspr
            "un normal body"
            show un normal body close with dspr
            "un normal body close"
            hide un with dspr
            jump extra_my_list_sprites_body_un
        "Ярость":
            show un rage body far with dspr
            "un rage body far"
            show un rage body with dspr
            "un rage body"
            show un rage body close with dspr
            "un rage body close"
            hide un with dspr
            jump extra_my_list_sprites_body_un
        "Грустная":
            show un sad body far with dspr
            "un sad body far"
            show un sad body with dspr
            "un sad body"
            show un sad body close with dspr
            "un sad body close"
            hide un with dspr
            jump extra_my_list_sprites_body_un
        "Испуганная":
            show un scared body far with dspr
            "un scared body far"
            show un scared body with dspr
            "un scared body"
            show un scared body close with dspr
            "un scared body close"
            hide un with dspr
            jump extra_my_list_sprites_body_un
        "Серьёзная":
            show un serious body far with dspr
            "un serious body far"
            show un serious body with dspr
            "un serious body"
            show un serious body close with dspr
            "un serious body close"
            hide un with dspr
            jump extra_my_list_sprites_body_un
        "Шокированная":
            show un shocked body far with dspr
            "un shocked body far"
            show un shocked body with dspr
            "un shocked body"
            show un shocked body close with dspr
            "un shocked body close"
            hide un with dspr
            jump extra_my_list_sprites_body_un
        "Застенчивая":
            show un shy body far with dspr
            "un shy body far"
            show un shy body with dspr
            "un shy body"
            show un shy body close with dspr
            "un shy body close"
            hide un with dspr
            jump extra_my_list_sprites_body_un
        "Улыбка(1)":
            show un smile body far with dspr
            "un smile body far"
            show un smile body with dspr
            "un smile body"
            show un smile body close with dspr
            "un smile body close"
            hide un with dspr
            jump extra_my_list_sprites_body_un
        "Улыбка(2)":
            show un smile2 body far with dspr
            "un smile2 body far"
            show un smile2 body with dspr
            "un smile2 body"
            show un smile2 body close with dspr
            "un smile2 body close"
            hide un with dspr
            jump extra_my_list_sprites_body_un
        "Улыбка(3)":
            show un smile3 body far with dspr
            "un smile3 body far"
            show un smile3 body with dspr
            "un smile3 body"
            show un smile3 body close with dspr
            "un smile3 body close"
            hide un with dspr
            jump extra_my_list_sprites_body_un
        "Удивлённая":
            show un surprise body far with dspr
            "un surprise body far"
            show un surprise body with dspr
            "un surprise body"
            show un surprise body close with dspr
            "un surprise body close"
            hide un with dspr
            jump extra_my_list_sprites_body_un
        ">>Назад<<":
            jump extra_my_list_sprites_body

label extra_my_list_sprites_body_us:
    menu:
        "Хмурая":
            show us angry body far with dspr
            "us angry body far"
            show us angry body with dspr
            "us angry body"
            show us angry body close with dspr
            "us angry body close"
            hide us with dspr
            jump extra_my_list_sprites_body_us
        "Спокойная":
            show us calml body far with dspr
            "us calml body far"
            show us calml body with dspr
            "us calml body"
            show us calml body close with dspr
            "us calml body close"
            hide us with dspr
            jump extra_my_list_sprites_body_us
        "Плачущая(1)":
            show us cry body far with dspr
            "us cry body far"
            show us cry body with dspr
            "us cry body"
            show us cry body close with dspr
            "us cry body close"
            hide us with dspr
            jump extra_my_list_sprites_body_us
        "Плачущая(2)":
            show us cry2 body far with dspr
            "us cry2 body far"
            show us cry2 body with dspr
            "us cry2 body"
            show us cry2 body close with dspr
            "us cry2 body close"
            hide us with dspr
            jump extra_my_list_sprites_body_us
        "Неприязнь":
            show us dontlike body far with dspr
            "us dontlike body far"
            show us dontlike body with dspr
            "us dontlike body"
            show us dontlike body close with dspr
            "us dontlike body close"
            hide us with dspr
            jump extra_my_list_sprites_body_us
        "Страх":
            show us fear body far with dspr
            "us fear body far"
            show us fear body with dspr
            "us fear body"
            show us fear body close with dspr
            "us fear body close"
            hide us with dspr
            jump extra_my_list_sprites_body_us
        "Усмешка":
            show us grin body far with dspr
            "us grin body far"
            show us grin body with dspr
            "us grin body"
            show us grin body close with dspr
            "us grin body close"
            hide us with dspr
            jump extra_my_list_sprites_body_us
        "Смех(1)":
            show us laugh body far with dspr
            "us laugh body far"
            show us laugh body with dspr
            "us laugh body"
            show us laugh body close with dspr
            "us laugh body close"
            hide us with dspr
            jump extra_my_list_sprites_body_us
        "Смех(2)":
            show us laugh2 body far with dspr
            "us laugh2 body far"
            show us laugh2 body with dspr
            "us laugh2 body"
            show us laugh2 body close with dspr
            "us laugh2 body close"
            hide us with dspr
            jump extra_my_list_sprites_body_us
        "Обычная":
            show us normal body far with dspr
            "us normal body far"
            show us normal body with dspr
            "us normal body"
            show us normal body close with dspr
            "us normal body close"
            hide us with dspr
            jump extra_my_list_sprites_body_us
        "Грустная":
            show us sad body far with dspr
            "us sad body far"
            show us sad body with dspr
            "us sad body"
            show us sad body close with dspr
            "us sad body close"
            hide us with dspr
            jump extra_my_list_sprites_body_us
        "Стесняущаяся(1)":
            show us shy body far with dspr
            "us shy body far"
            show us shy body with dspr
            "us shy body"
            show us shy body close with dspr
            "us shy body close"
            hide us with dspr
            jump extra_my_list_sprites_body_us
        "Стесняущаяся(2)":
            show us shy2 body far with dspr
            "us shy2 body far"
            show us shy2 body with dspr
            "us shy2 body"
            show us shy2 body close with dspr
            "us shy2 body close"
            hide us with dspr
            jump extra_my_list_sprites_body_us
        "Улыбка":
            show us smile body far with dspr
            "us smile body far"
            show us smile body with dspr
            "us smile body"
            show us smile body close with dspr
            "us smile body close"
            hide us with dspr
            jump extra_my_list_sprites_body_us
        "Удивлённая(1)":
            show us surp1 body far with dspr
            "us surp1 body far"
            show us surp1 body with dspr
            "us surp1 body"
            show us surp1 body close with dspr
            "us surp1 body close"
            hide us with dspr
            jump extra_my_list_sprites_body_us
        "Удивлённая(2)":
            show us surp2 body far with dspr
            "us surp2 body far"
            show us surp2 body with dspr
            "us surp2 body"
            show us surp2 body close with dspr
            "us surp2 body close"
            hide us with dspr
            jump extra_my_list_sprites_body_us
        "Удивлённая(3)":
            show us surp3 body far with dspr
            "us surp3 body far"
            show us surp3 body with dspr
            "us surp3 body"
            show us surp3 body close with dspr
            "us surp3 body close"
            hide us with dspr
            jump extra_my_list_sprites_body_us
        "Расстроенная":
            show us upset body far with dspr
            "us upset body far"
            show us upset body with dspr
            "us upset body"
            show us upset body close with dspr
            "us upset body close"
            hide us with dspr
            jump extra_my_list_sprites_body_us
        ">>Назад<<":
            jump extra_my_list_sprites_body
