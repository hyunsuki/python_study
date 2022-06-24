import re
import uuid
import socket
import getmac
from icecream import ic


class AddressManager:

    def getHostName(self):
        return socket.gethostname()

    def getInternalIp(self):
        return socket.gethostbyname(socket.gethostname())

    def getExternalIp(self):
        return socket.gethostbyname(socket.getfqdn())

    def getMacAddressUsingGetMac(self):
        return getmac.get_mac_address()

    def getMacAddressUsingUuid(self):
        return ':'.join(re.findall('..', '%012x' % uuid.getnode()))


def main():
    am = AddressManager()
    ic(am.getHostName())
    ic(am.getInternalIp())
    ic(am.getExternalIp())
    ic(am.getMacAddressUsingGetMac())
    ic(am.getMacAddressUsingUuid())


if __name__ == '__main__':
    main()
