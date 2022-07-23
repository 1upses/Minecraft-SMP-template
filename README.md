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

- Once the server is launched, type the following command in the console to get admin perms
```
lp user {your username} parent set admin
```

- To set the world spawn, use the command ```/setworldspawn``` where you want to set the world spawn location

- This template uses a diamond based economy, to initialize it, type the following commands where you want the bank to be
```
/schem load bank
```
```
//paste
```
if you messed up the location, you can type ```//undo``` to then type ```//paste``` again but at the correct location

- To protect the bank from potential griefers, you'll need to protect it, so execute ```//wand``` to get a wooden axe, and using this axe, make 2 points 3D selection of the bank: left click is for the 1st point, and right click is for the 2nd one. And then, you can type the command ```/rg define bank```. If you messed up the selection area, you can redefine the region using ```/rg redefine bank```

# Usage

- Windows -> double click on ```run.bat``` and enjoy
- Linux -> ```bash run.sh```
- To stop the server -> type ```stop``` in the console

If you want to modify the plugins, you can do so by editing ```settings.json```, deleting the plugins in the plugins folder, and running the ```update_files.py``` script again

You can also copy ```settings.json``` and ```update_files.py``` to your personnal server, to then modify ```settings.json``` to your liking, and get a script that will update everything in your server all by itself -> also works with modded servers

## Contributing

Pull requests are welcome. For major changes, please open an issue first to discuss what you would like to change
