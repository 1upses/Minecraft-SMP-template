This template is currently still running on 1.18.2 because some plugins still haven't been updated to 1.19.1, but you can still join in 1.19.1 if you want to. When all plugins will be updated, make sure to switch the version in ```settings.json``` before running ```update_files.py``` for the changes to take place

# Requirements

- [Java 17](https://www.oracle.com/java/technologies/downloads/#jdk17-windows)
- [Python](https://www.python.org/downloads/)
- [pip](https://pip.pypa.io/en/stable/)
- [pyjson5](https://pypi.org/project/pyjson5/)

# Installation

- launch ```update_files.py```
```bash
python "./udpate_files.py"
```
- start the server (Take a look at the Usage tab)

- Windows
```bash
del "./eula.txt"
echo eula=true > eula.txt
```

- Linux
```bash
rm ./eula.txt
echo eula=true > eula.txt
```

- Start the server and join it

- Once the server is launched, type the following command in the console to get admin perms
```
lp user {your username} parent set admin
```

- To set the world spawn location, use the command ```/setworldspawn``` where you want it to be. people will then be able to teleport there using ```/spawn``` 

- This template uses a diamond based economy, to initialize it, type the following commands where you want the bank to be
```
/schem load bank
```
```
//paste
```
if you messed up the location, you can type ```//undo``` to then type ```//paste``` again but this time at the correct location

- To protect the bank from potential griefers, you'll need to define a protected region, so execute ```//wand``` to get a wooden axe, and using this axe, make a 2 points 3D selection of the bank: left click is for the 1st point, and right click is for the 2nd one. And then, you can type the command ```/rg define bank```. If you messed up the selection area, you can redefine the region using ```/rg redefine bank```

# Usage

- Windows -> double click on ```run.bat```
- Linux -> ```bash run.sh```
- To stop the server -> type ```stop``` in the console
- Take a look on how to use [ChestShop](https://youtu.be/Zap3snBb5Fw) and [Blocklocker](https://youtu.be/EaCHTiPNGiQ)
- Regularly run the ```update_files.py``` script to stay up to date, make sure the server is closed before doing so

There are plenty of existing resources online to help you with deploying your server

If you want to modify the plugins, you can do so by editing ```settings.json```, deleting the plugins in the plugins folder, and running the ```update_files.py``` script again

You can also copy ```settings.json``` and ```update_files.py``` to your personnal server, to then modify ```settings.json``` to your liking, and get a script that will update everything in your server all by itself when executed -> also works with modded servers

## Contributing

Pull requests are welcome. For major changes, please open an issue first to discuss what you would like to change
