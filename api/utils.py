def JSONListFormatter(name_ser, ser_data=None, name_obj=None):
    if not name_obj and ser_data:
        data = []
        for obj in ser_data:
            langs = obj[name_ser] # language list
            obj[name_ser] = {}
            for l in langs:
                print("WE are here: ", l)
                selected_lang = l['lang']['code']
                del l['lang']
                obj[name_ser][selected_lang] =  l
            data.append(obj)
        return data
    else:
        print(name_obj)
        langs = name_obj[name_ser] # language list
        name_obj[name_ser] = {}
        for l in langs:
            selected_lang = l['lang']['code']
            del l['lang']
            name_obj[name_ser][selected_lang] =  l
        print(name_obj)
        return name_obj
