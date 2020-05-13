import cmd
import os
from local_ftp_client import LocalFtpClient


class FtpShell(cmd.Cmd):
    prompt = f"$ "
    intro = "Welcome to MAMA-FT Server\nEnter a command: (?) for help"

    def __init__(self, client: LocalFtpClient):
        super().__init__(completekey='tab')
        self.ft_client = client

    # Save options
    def do_save(self, inp):
        src, out = inp.split()

        try:
            self.ft_client.save_file(src, out)
        except FileNotFoundError:
            print(f"The file can't be found or doesnt exist: {src}")

    @staticmethod
    def help_save():
        print("Saves a file onto the ft server")
        print("save {file_source} {file_output}")

    # Get file options
    def do_read(self, inp):
        try:
            print(self.ft_client.get_file_content(inp))
        except FileNotFoundError:
            print(f"The file doesnt exist: {inp}")

    @staticmethod
    def help_read():
        print("Reads the file to the shell")
        print("read {file_path}")

    # List dir options
    def do_ls(self, inp):
        try:
            print(" ".join(self.ft_client.get_dir_content(inp)))
        except FileNotFoundError:
            print(f"The dir doesnt exit: {inp}")

    @staticmethod
    def help_ls():
        print("Listing the content of given directory")
        print("ls [file_path]")

    # General utilities
    @staticmethod
    def do_exit(self):
        print("Exiting, See you soon")
        return True

    @staticmethod
    def help_exit(self):
        print("exit the application. Shorthand: 'exit', 'Ctrl-D'.")

    @staticmethod
    def do_cd(inp):
        if inp:
            os.chdir(inp)

    @staticmethod
    def help_cd():
        print("Navigate the file system")

    @staticmethod
    def do_pwd(self):
        print(os.getcwd())

    @staticmethod
    def help_pwd():
        print("Print the current working directory")

    @staticmethod
    def do_cls(self):
        os.system('clear')

    @staticmethod
    def help_cls():
        print("Clears the screen")

    def default(self, line):
        if line == 'q' or line == ':q':
            return self.do_exit(line)
        elif line == 'cls':
            return os.system('clear')
        else:
            return ''
