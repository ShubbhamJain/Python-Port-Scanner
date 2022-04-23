import socket
from common_ports import ports_and_services


def get_open_ports(target: str, port_range: list, verbose: bool = False):
    start, end = port_range
    open_ports = []

    if target[0].isdigit():
        ip = True
    else:
        ip = False

    try:
        for port in range(start, end + 1, 1):
            s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            s.settimeout(5)
            result = s.connect_ex((target, port))
            s.close()
            if result == 0:
                print("Port is open")
                open_ports.append(port)

        if ip == False:
            site = target + f" ({socket.gethostbyname(target)})"
        else:
            try:
                site = socket.gethostbyaddr(target)[0] + f" ({target})"
            except socket.herror:
                site = target

        if verbose == True:
            formattedOutput = f"Open ports for {site}\nPORT     SERVICE\n"
            for i in open_ports:
                spaces = (9 - len(str(i))) * " "
                formattedOutput += f"{i}{spaces}{ports_and_services[i]}\n"
            formattedOutput = formattedOutput.rstrip()
            open_ports = formattedOutput

        return open_ports
    except socket.gaierror:
        if ip == True:
            return "Error: Invalid IP address"
        else:
            return "Error: Invalid hostname"
