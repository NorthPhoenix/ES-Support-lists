init :

    $ mods["my_list_refresher"]=u"How to make a mod{b}(persistent refresher){/b}"

label my_list_refresher:

    $persistent.meetss = False
    $persistent.music_warn = False

    show bg black

    if _preferences.language == None:
        "Переменные \"persistent.meetss\" и \"persistent.music_warn\" были обновлены."
    elif _preferences.language == "english":
        "Variables \"persistent.meetss\" и \"persistent.music_warn\" were refreshed."

    return
