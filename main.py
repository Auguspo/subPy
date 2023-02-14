import os
import shutil

mainDir = "Z:\HDD"
folderArray = []
unsub = []


def getFolder():
    return os.listdir(mainDir)


def checkSub(folderArray, unsub):
    for el in folderArray:
        if not (
            os.path.isfile(mainDir + "\\" + el + "\\" + el + ".mp4")
            and os.path.isfile(mainDir + "\\" + el + "\\" + el + ".srt")
        ):
            if not (
                os.path.isfile(mainDir + "\\" + el + "\\" + el + ".mkv")
                or len(os.listdir(mainDir + "\\" + el)) >= 5
            ):
                print(mainDir + "\\" + el + "\\" + el + " no tiene subs")
                unsub.append(mainDir + "\\" + el)


def copySub():
    print(unsub)
    for el in unsub:
        for subEl in os.listdir(el):
            print(subEl)
            if subEl == "Subs":
                shutil.copy(
                    el + "\\" + subEl + "\\" + os.listdir(el + "\\" + subEl)[0],
                    el + "\\" + os.path.basename(el) + ".srt",
                )


folderArray = getFolder()
checkSub(folderArray, unsub)
copySub()
