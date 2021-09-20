I've been using the Bryton 420 for almost a year and always had have problems when importing external .gpx files in the app for route creation.
After investigating the output files, I noticed that the Bryton active app inserts bugs in the .fit files (Bryton proprietary route format) generated based in .gpx files (routes created directly on their app work without problems).

Frustrated with this experience, I've analyzed the .fit files to understand how the route information is encoded and created python scripts to "translate" .gpx in .fit without errors.

This work is based on the idea and execution of two others designed for bryton units TBD

As far as my research goes, this is the first project to work with the bryton 420 unit, due to this (and the fact that it is the only one I own) this project is primarily focused on this model.
If you want to add functionalities for other units fell free to help, I just can't test and guarantee compatibility since I don't own others.

It's been a couple of year since I stopped programming professionally (my life is based on excel now) and even when I did, I only used C.
Considering also that this is my first big python project, I know there are a lot of improvements to be made in my code.
I'll try to refactor my functions as I learn more of the language, suggestions of improvements are also welcomed.

To run this script, navigate to the folder BrytonUtilities/source/ and run the following command in the terminal:
python main.py ABSOLUTE_PATH_TO_YOUR_INPUT_GPX
The script will generate an output in .fit format in the same path and with the same filename as your input .gpx

Currently the tool is in alpha, I already tested it sucessfully with a couple of routes, but can't guarantee the behavior for all inputs.

The worst case I found when inputting wrong files in my unit was it did not recognized the routes, anyway I don't take responsability for any damage that may happen to your gps unit due to issues in the generated files.

