import requests
import pyjson5 as json
import os
import zipfile
import shutil

# If desired mc version is 1.18.2, only type 1.18
# If an other mc version is released, you can always
# download the latest version with get_latest_mc_version set to True,
# thus making the version variable ignorable, do that at your own risks,
# as this could break your server
# create your curseforge api key here:
# https://console.curseforge.com/

def githubFormat(element):
    foo = element.split("/")
    print(f"{foo[4]} ...")
    string = ""
    for i in range(5):
        if i == 2:
            string += f"api.{foo[i]}/repos/"
        elif i != 5:
            string += foo[i] + "/"
        else:
            string += foo[i]
    return string + "releases/latest"

def removeZeros(text):
    if text[0] == "0":
        return removeZeros(text[1:])
    else:
        return text

settings = json.load(open("settings.json"))

api = "https://papermc.io/api/v2"
version = settings["version"]
filename = settings["filename"]
get_latest_mc_version = settings["get_latest_mc_version"]
curseforge_api_key = settings["curseforge_api_key"]

# get the build number of the most recent build
if get_latest_mc_version:
    version = json.loads(requests.get(f"{api}/projects/paper").content.decode("utf-8"))["version_groups"][-1]

latest_build = json.loads(requests.get(f"{api}/projects/paper/version_group/{version}/builds").content.decode("utf-8"))["builds"][-1]
if len(latest_build["version"].split(".")) > 2:
    version_suffix = "." + latest_build["version"].split(".")[-1]
else:
    version_suffix = ""
latest_build = latest_build["build"]
if settings["update_paper"]:
    print(f"paper version : {latest_build}")

if version_suffix == ".0":
    version_suffix = ""

print(f"mc version : {version}{version_suffix}")

if settings["update_paper"]:
    # construct download URL
    download_url = f"{api}/projects/paper/versions/{version}{version_suffix}/builds/{latest_build}/downloads/paper-{version}{version_suffix}-{latest_build}.jar"
    print(f"url : {download_url}")

    # download file
    print("downloading file ...")
    response = requests.get(download_url)
    open(filename, "wb").write(response.content)

#creates paths if they don't already exist
paths = ["./plugins", "./world", "./world/datapacks"]
if settings["mods"]["curseforge"]:
    paths.append("./mods")
for path in paths:
    if not os.path.exists(path):
        os.makedirs(path)

print("downloading plugins from github:")

for i in settings["plugins"]["github"]:
    foo = i.split("/")
    string = githubFormat(i)
    #getting the link of the file
    download_url = json.loads(requests.get(string).content.decode("utf_8"))["assets"][0]["browser_download_url"]
    #downloading the file
    response = requests.get(download_url)
    open(f"./plugins/{foo[4]}.jar", "wb").write(response.content)

print("downloading plugins from bukkit:")

for i in settings["plugins"]["bukkit"]:
    #formating
    nom = i.split("/")
    print(f"{nom[4]} ...")
    if len(nom) == 4:
        i += "/files/latest/"
    else:
        i += "files/latest/"
    #downloading the file
    response = requests.get(i)
    open(f"./plugins/{nom[4]}.jar", "wb").write(response.content)

if settings["plugins"]["custom"]:
    for url in settings["plugins"]["custom"]:
        print("downloading plugins from custom sources:")
        #formating
        nom = url.split("/")[-1]
        nom = nom.split(".")[0]
        print(f"{nom} ...")
        #downloading the file
        response = requests.get(url)
        open(f"./plugins/{nom}.jar", "wb").write(response.content)

if settings["plugins"]["essentials"]["core"]:
    print("downloading essentials plugins:")
    i = 0
    string = "https://api.github.com/repos/EssentialsX/Essentials/releases/latest"
    for key, value in settings["plugins"]["essentials"].items():
        if value:
            print(f"{key} ...")
            download_url = json.loads(requests.get(string).content.decode("utf_8"))["assets"][i]["browser_download_url"]
            response = requests.get(download_url)
            open(f"./plugins/essentials_{key}.jar", "wb").write(response.content)
        i += 1

if settings["plugins"]["luckperms"]:
    print("downloading luckperms ...")
    os.makedirs("./temp")
    #gets the latest release of luckperms
    response = requests.get("https://ci.lucko.me/view/LuckPerms/job/LuckPerms//lastSuccessfulBuild/artifact/*zip*/archive.zip")
    open("./temp/luckperms.zip", "wb").write(response.content)
    #unzips the archive
    with zipfile.ZipFile("./temp/luckperms.zip", 'r') as zip_ref:
        zip_ref.extractall("./temp")
    #moves the bukkit release to the plugins folder and deletes the temporary folder
    directory = "./temp/archive/bukkit/loader/build/libs/"
    if not os.path.exists("./plugins/luckperms.jar"):
        os.rename(f"{directory}{os.listdir(directory)[0]}","./plugins/luckperms.jar")
    else:
        os.remove("./plugins/luckperms.jar")
        os.rename(f"{directory}{os.listdir(directory)[0]}","./plugins/luckperms.jar")
    shutil.rmtree("./temp")

if settings["plugins"]["geyser"]:
    print("downloading geyser ...")
    response = requests.get("https://ci.opencollab.dev//job/GeyserMC/job/Geyser/job/master/lastSuccessfulBuild/artifact/bootstrap/spigot/target/Geyser-Spigot.jar")
    open("./plugins/geyser.jar", "wb").write(response.content)
    
    print("downloading floodgate ...")
    response = requests.get("https://ci.opencollab.dev/job/GeyserMC/job/Floodgate/job/master/lastSuccessfulBuild/artifact/spigot/build/libs/floodgate-spigot.jar")
    open("./plugins/floodgate.jar", "wb").write(response.content)
elif settings["plugins"]["floodgate"]:
    print("can't download floodgate without geyser, skipping plugin")


print("downloading datapacks from github:")

for element in settings["datapacks"]["github"]:
    name = element.split("/")[4]
    element = githubFormat(element)
    #getting the link of the file
    download_url = json.loads(requests.get(element).content.decode("utf_8"))["assets"][0]["browser_download_url"]
    #downloading the file
    response = requests.get(download_url)
    open(f"./world/datapacks/{name}.zip", "wb").write(response.content)

if settings["mods"]["curseforge"]:
    print("downloading mods from curseforge:")
    #using the cursforge api

    headers = {
    'Accept': 'application/json',
    'x-api-key': f"{curseforge_api_key}"
    }

    for id in settings["mods"]["curseforge"]:
        r = json.loads(requests.get(f"https://api.curseforge.com/v1/mods/{id}", headers = headers).content.decode("utf_8"))
        name = r["data"]["name"]
        print(f"{name} ...")
        download = True
        #searches through available versions to find the latest matching version
        for i in range(len(r["data"]["latestFilesIndexes"])):
            if r["data"]["latestFilesIndexes"][i]["gameVersion"] == version + version_suffix:
                break
        if i == len(r["data"]["latestFilesIndexes"]) - 1:
            print("no matching version found, skipping mod")
            download = False
        if download:
            fileId = str(r["data"]["latestFilesIndexes"][i]["fileId"])[:4] + "/" + removeZeros(str(r["data"]["latestFilesIndexes"][i]["fileId"])[4:])
            filename = r["data"]["latestFilesIndexes"][i]["filename"]
            download_url = f"https://mediafiles.forgecdn.net/files/{fileId}/{filename}"
            response = requests.get(download_url)
            open(f"./mods/{name}.jar", "wb").write(response.content)