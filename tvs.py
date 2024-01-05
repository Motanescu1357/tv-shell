__author__ = "Rares Miclaus Stoian"
__version__ = "0.1"
class tvshell:
    """
    Use main or set tvsinput to None to use default configuration.
    \nSet tvs input to input(whatever) where whatever is a string to change the prompt or set it to a string value to run a command.
    """
    def __init__(self, tvsinput: str | None):
        import os
        super().__init__()
        if tvsinput is None:
            self.main()
        installpackagepath = tvsinput.replace("tvs install", "")
        uninstallpackagename = tvsinput.replace("tvs uninstall", "")
        package_name = installpackagepath.replace(installpackagepath, os.path.basename(installpackagepath)).replace(" ", "")
        try:
            with open(f"{package_name} config.txt", "x") as config:
                config.write("py binary=")
        except Exception as e:
            if e is KeyboardInterrupt:
                raise e
            else:
                pass
        if tvsinput == "tvs_py":
            print("Entering py mode.")
            while True:
                tvsinput = input(">>>")
                if tvsinput == "tvs_py_quit":
                    break
                eval(tvsinput)
            print("Exiting py mode.")
        elif tvsinput == "help":
            print("Commands are:"
                  "    \nhelp -the helper command"
                  "    \ntvs_py -the python interpreter"
                  "    \ntvs_py_quit -exit the python interpreter"
                  "    \ntvs package_name -run an installed package with name of package_name"
                  "    \ntvs install package_path -install package from .tvspackage file"
                  "    \ntvs uninstall package_name -uninstall package with name package_name")
        elif tvsinput == f"tvs {tvsinput.replace('tvs', '')}":
            with open(f"{package_name} config.txt", "r") as setconfig:
                if setconfig.read(1) == "py binary=True":
                    eval(f"{package_name}.py")
        elif tvsinput.replace(installpackagepath, "") == "tvs install":
            try:
                with open(package_name) as package:
                    package_text = package.readlines()
                    py_start_index = package_text.index('#start_py\n')
                    py_end_index = package_text.index("#end_py")
                    try:
                        py_end_dependencies = package_text.index("#end_dependencies\n")
                    except ValueError:
                        py_end_dependencies = -1
                    try:
                        try:
                            os.remove(f"{package_name.replace('.tvspackage','')}.py")
                        except FileNotFoundError:
                            pass
                        with open(f"{package_name.replace('.tvspackage', '')}.py", "x") as py:
                            # print(str(package_text).replace("[", "").replace("]", "").replace(",", "").replace('#start_py', '').replace("#end dependencies", "#").replace("#end_py", "").replace("'", "").replace(r"\n", "").replace(" ", ""))
                            py.write(str(package_text).replace("[", "").replace("]", "").replace(",", "").replace('#start_py', '').replace("#end dependencies", "#").replace("#end_py", "").replace("'", "").replace(r"\n", "").replace(" ", ""))
                        with open(f"{package_name.replace('.tvspackage', '')} config.txt", "w") as config:
                            config.write("py binary=True")
                        if py_end_dependencies != -1:
                            os.system(
                                f'pip install {str(package.readlines(py_end_dependencies)).replace("[", "").replace("]", "")}')
                    except Exception as e:
                        raise e
            except ValueError as e:
                raise e
        elif tvsinput == f"tvs uninstall {uninstallpackagename}":
            os.remove(f"{uninstallpackagename}.py")
            os.remove(f"{uninstallpackagename} config.txt")
            os.remove(f"{uninstallpackagename}.tvspackage .py")
            os.remove(f"{uninstallpackagename}.tvspackage config.txt")


    def main(self):
        while True:
            tvshell(tvsinput=input("Enter command:"))

if __name__ == '__main__':
    tvshell(None).main()
