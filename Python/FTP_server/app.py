from ftp_shell import FtpShell
from core.file_service import FileService
from local_ftp_client import LocalFtpClient


if __name__ == '__main__':
    file_service = FileService('../data')
    ft_client = LocalFtpClient(file_service)
    FtpShell(ft_client).cmdloop()
