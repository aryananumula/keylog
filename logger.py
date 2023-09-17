import keyboard

recorded = keyboard.record(until='esc+command')
d = layout_specific_keys = {
    # NOT COMPLETE - ALL KEY CODES AT https://eastmanreference.com/complete-list-of-applescript-key-codes
                            18:"1",
                            19:"2",
                            20:"3",
                            21:"4",
                            23:"5",
                            22:"6",
                            26:"7",
                            28:"8",
                            25:"9",
                            29:"0",
                            27:"-",
                            24:"=",
                            12:"q",
                            13:"w",
                            14:"e",
                            15:"r",
                            17:"t",
                            16:"y",
                            32:"u",
                            34:"i",
                            31:"o",
                            35:"p",
                            0:"a",
                            1:"s",
                            2:"d",
                            3:"f",
                            5:"g",
                            4:"h",
                            38:"j",
                            40:"k",
                            37:"l",
                            6:"z",
                            7:"x",
                            8:"c",
                            9:"v",
                            11:"b",
                            45:"n",
                            46:"m"
                            }
for i in range(len(recorded)):
    try:
        recorded[i] = d.get(int(str(recorded[i])[22:-6].strip()))+" down"
        pass
    except Exception as e:
        try:
            recorded[i] = d.get(int(str(recorded[i])[22:-4].strip()))+" up"
            pass
        except Exception as er:
            recorded[i] = str(recorded[i])[14:-1].strip()
            pass

recorded = "\n".join(recorded)

print(recorded, file = open("/Users/Aryan/Documents/logged.txt", "w"), end = "")
