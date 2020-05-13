from shell import FtpShell, LocalFtpClient
from services.ftp_core import FileService


if __name__ == '__main__':
    file_service = FileService('../data')
    ft_client = LocalFtpClient(file_service)
    FtpShell(ft_client).cmdloop()
