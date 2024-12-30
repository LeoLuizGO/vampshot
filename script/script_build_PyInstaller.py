from shutil import rmtree
import os


def build():
    #   PySide6_path = os.path.dirname(PySide6.__file__)
    #   PySide6_plugins = os.path.join(PySide6_path, "plugins")

    try:
        rmtree("../build/jogo")
    except (PermissionError, FileNotFoundError):
        pass

    cmd = 'pyinstaller  '
    cmd += '"../jogoshooter.py" '
    cmd += '--clean '
    # cmd += '--onefile '
    # cmd += '--noconsole '
    # cmd += '--uac-admin '
    cmd += '--name "jogo" '
    # cmd += '--icon "../assets/icons/RISK2D.ico" '
    # cmd += f'--add-data "{PySide6_plugins}";"./PySide6/plugins" '
    # cmd += '--key "123" '
    # cmd += '--win-private-assemblies '
    cmd += '--distpath "../build"'

    os.system(cmd)

    try:
        rmtree("./build")
        os.remove("./jogo.spec")
    except (PermissionError, FileNotFoundError):
        pass


if __name__ == "__main__":
    build()
