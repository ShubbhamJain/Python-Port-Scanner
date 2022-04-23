### Python Port Scanner

Project uses Python to build a port scanner.

We have `port_scanner.py` file with a function called `get_open_ports` that takes a `target` argument and a `port_range` argument. `target` can be a URL or IP address. `port_range` is a list of two numbers indicating the first and last numbers of the range of ports to check.

Here are examples of how the function may be called:
```
get_open_ports("209.216.230.240", [440, 445])
get_open_ports("www.stackoverflow.com", [79, 82])
```

The function returns a list of open ports in the given range.

The `get_open_ports` function also takes an optional third argument of `True` to indicate "Verbose" mode. If this is set to true, the function returns a descriptive string instead of a list of ports.

Here is the format of the string that should be returned in verbose mode (text inside `{}` indicates the information that should appear):
```
Open ports for {URL} ({IP address})
PORT     SERVICE
{port}   {service name}
{port}   {service name}
```
We use the dictionary in `common_ports.py` to get the correct service name for each port.

For example, if the function is called like this:
```
port_scanner.get_open_ports("scanme.nmap.org", [20, 80], True)
```
It should return the following:
```
Open ports for scanme.nmap.org (45.33.32.156)
PORT     SERVICE
22       ssh
80       http
```

If the URL passed into the `get_open_ports` function is invalid, the function returns the string: "Error: Invalid hostname".

If the IP address passed into the `get_open_ports` function is invalid, the function returns the string: "Error:  Invalid IP address".

### Development

For development we are using `port_scanner.py` to write the function. We use `main.py` to test the function.

### Testing 

The unit tests for this project are in `test_module.py`. We imported the tests from `test_module.py` to `main.py` for our convenience. The tests will run automatically whenever we run the code written in `main.py`.
