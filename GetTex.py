from Scripts import *
import os, sys, argparse

class GetTex:
    def __init__(self, **kwargs):
        self.dl = downloader.Downloader()
        self.u  = utils.Utils("Get Tex")
        self.version = kwargs.get("version","master")
        try:
            # Check if we got an X.Y.Z version value
            x,y,z = map(int,self.version.split("."))
            assert x < 10
            assert y < 10
            assert z < 10
        except:
            self.version = "master"
        if self.version.lower() in ("latest","master"):
            self.version = "master"
        self.output = kwargs.get("output",None)
        # Pass "master" for the latest - otherwise a valid OC version to get that specifically
        self.tex_url = "https://raw.githubusercontent.com/acidanthera/OpenCorePkg/{}/Docs/Configuration.tex".format(self.version)

    def process(self):
        # Actually work through the downloading process, and copy the target file over
        print("Attempting to download Configuration.tex from:")
        print(self.tex_url)
        # Let's make sure the output folder exists - if not, make it.
        # If it does and is a file - throw an error.
        if not self.output: # Check if ../ProperTree exists - if not use CD
            cd = os.path.abspath(os.path.dirname(__file__))
            pt = os.path.abspath(os.path.join(cd,"..","ProperTree"))
            self.output = pt if os.path.isdir(pt) else cd
        # Strip Configuration.tex from the name if needed
        if os.path.basename(self.output).lower() == "configuration.tex":
            self.output = self.output[:-len("configuration.tex")]
        print("Verifying output folder:")
        print(self.output)
        if os.path.exists(self.output):
            if os.path.isfile(self.output):
                print(" - Already exists, and is a file!  Aborting...")
                exit(1)
            print(" - Exists, and is a directory...")
        else:
            print(" - Does not exist, creating...")
            try: os.makedirs(self.output)
            except Exception as e:
                print(" --> Failed to create: {}".format(e))
                exit(1)
        print("Downloading Configuration.tex...")
        try:
            file_path = self.dl.stream_to_file(self.tex_url,os.path.join(self.output,os.path.basename(self.tex_url)))
        except Exception as e:
            print(" - Failed: {}".format(e))
            exit(1)
        if not file_path:
            print(" - File failed to download!")
            exit(1)
        print("Done.")

if __name__ == '__main__':
    # Setup the cli args
    parser = argparse.ArgumentParser(prog="GetTex.py", description="GetTex - a py script to download OpenCore's Configuration.tex")
    parser.add_argument("-v","--version",help="The OC version to get in X.Y.Z format - or pass master, or latest for the latest version")
    parser.add_argument("-o","--output-folder",help="The output folder for the Configuration.tex file (defaults to ../ProperTree if it exists, falls back to the current directory)")

    args = parser.parse_args()

    g = GetTex(version=args.version,output=args.output_folder)
    g.process()