# GetTex
Py script to download the Configuration.tex from the OpenCorePkg repo.

```
usage: GetTex.py [-h] [-v VERSION] [-o OUTPUT_FOLDER]

GetTex - a py script to download OpenCore's Configuration.tex

options:
  -h, --help            show this help message and exit
  -v VERSION, --version VERSION
                        The OC version to get in X.Y.Z format - or pass
                        master, or latest for the latest version
  -o OUTPUT_FOLDER, --output-folder OUTPUT_FOLDER
                        The output folder for the Configuration.tex file
                        (defaults to ../ProperTree if it exists, falls back to
                        the current directory)
```
