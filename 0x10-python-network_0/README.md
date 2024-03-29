
# 0x10. Python - Network #0

-   By:  Guillaume
-   Weight:  1
-   Project will start  Aug 18, 2022 12:00 AM, must end by  Aug 19, 2022 12:00 AM
-   will be  released at  Aug 18, 2022 12:00 PM
-   An auto review will be launched at the deadline

## Resources

**Read or watch**:

-   [HTTP (HyperText Transfer Protocol)](https://intranet.hbtn.io/rltoken/vNqPD0N8vIgqJL1LnWaldQ "HTTP (HyperText Transfer Protocol)")  (_except: “TRACE” Request Method, “CONNECT” Request Method, Language Negotiation and “Options MultiView” and Character Set Negotiation_)
-   [HTTP Cookies](https://intranet.hbtn.io/rltoken/ubO0VPV2T3D77jyfc0c1Xw "HTTP Cookies")

## Learning Objectives

At the end of this project, you are expected to be able to  [explain to anyone](https://intranet.hbtn.io/rltoken/8bj998Jl9ii97hl7x8JTkQ "explain to anyone"),  **without the help of Google**:

### General

-   What a URL is
-   What HTTP is
-   How to read a URL
-   The scheme for a HTTP URL
-   What a domain name is
-   What a sub-domain is
-   How to define a port number in a URL
-   What a query string is
-   What an HTTP request is
-   What an HTTP response is
-   What HTTP headers are
-   What the HTTP message body is
-   What an HTTP request method is
-   What an HTTP response status code is
-   What an HTTP Cookie is
-   How to make a request with cURL
-   What happens when you type google.com in your browser (Application level)

## Requirements

### General

-   Allowed editors:  `vi`,  `vim`,  `emacs`
-   - A  `README.md`  file, at the root of the folder of the project, is mandatory
-   All your scripts will be tested on Ubuntu 20.04 LTS
-   All your Bash scripts should be exactly 3 lines long (`wc -l file`  should print 3)
-   All your files should end with a new line
-   All your files must be executable
-   The first line of all your bash files should be exactly  `#!/bin/bash`
-   The second line of all your Bash scripts should be a comment explaining what is the script doing
-   All  `curl`  commands must have the option  `-s`  (silent mode)
-   All your files will be interpreted/compiled on Ubuntu 20.04 LTS using  `python3`  (version 3.8.5)
-   The first line of all your Python files should be exactly  `#!/usr/bin/python3`
-   Your code should use the pycodestyle (version  `2.8.*`)
-   All your modules should be documented:  `python3 -c 'print(__import__("my_module").__doc__)'`
-   All your classes should be documented:  `python3 -c 'print(__import__("my_module").MyClass.__doc__)'`
-   All your functions (inside and outside a class) should be documented:  `python3 -c 'print(__import__("my_module").my_function.__doc__)'`  and  `python3 -c 'print(__import__("my_module").MyClass.my_function.__doc__)'`
-   A documentation is not a simple word, it’s a real sentence explaining what’s the purpose of the module, class or method (the length of it will be verified)

### Quiz questions

**Great!**  You've completed the quiz successfully! Keep going!  (Show quiz)

## Tasks

### 0. cURL body size

mandatory

Write a Bash script that takes in a URL, sends a request to that URL, and displays the size of the body of the response

-   The size must be displayed in bytes
-   You have to use  `curl`

Please test your script in the sandbox provided, using the web server running on port 5000

```
guillaume@ubuntu:~/0x10$ ./0-body_size.sh 0.0.0.0:5000
10
guillaume@ubuntu:~/0x10$ 

```

**Repo:**

-   GitHub repository:  `holbertonschool-higher_level_programming`
-   Directory:  `0x10-python-network_0`
-   File:  `0-body_size.sh`

Done?  Help  Get a sandbox

### 1. cURL to the end

mandatory

Write a Bash script that takes in a URL, sends a  `GET`  request to the URL, and displays the body of the response

-   Display only body of a  `200`  status code response
-   You have to use  `curl`

Please test your script in the sandbox provided, using the web server running on port 5000

```
guillaume@ubuntu:~/0x10$ ./1-body.sh 0.0.0.0:5000/route_1 ; echo ""
Route 2
guillaume@ubuntu:~/0x10$ 

```

**Repo:**

-   GitHub repository:  `holbertonschool-higher_level_programming`
-   Directory:  `0x10-python-network_0`
-   File:  `1-body.sh`

Done?  Help  Get a sandbox

### 2. cURL Method

mandatory

Write a Bash script that sends a  `DELETE`  request to the URL passed as the first argument and displays the body of the response

-   You have to use  `curl`

Please test your script in the sandbox provided, using the web server running on port 5000

```
guillaume@ubuntu:~/0x10$ ./2-delete.sh 0.0.0.0:5000/route_3 ; echo ""
I'm a DELETE request
guillaume@ubuntu:~/0x10$ 

```

**Repo:**

-   GitHub repository:  `holbertonschool-higher_level_programming`
-   Directory:  `0x10-python-network_0`
-   File:  `2-delete.sh`

Done?  Help  Get a sandbox

### 3. cURL only methods

mandatory

Write a Bash script that takes in a URL and displays all HTTP methods the server will accept.

-   You have to use  `curl`

Please test your script in the sandbox provided, using the web server running on port 5000

```
guillaume@ubuntu:~/0x10$ ./3-methods.sh 0.0.0.0:5000/route_4
OPTIONS, HEAD, PUT
guillaume@ubuntu:~/0x10$ 

```

**Repo:**

-   GitHub repository:  `holbertonschool-higher_level_programming`
-   Directory:  `0x10-python-network_0`
-   File:  `3-methods.sh`

Done?  Help  Get a sandbox

### 4. cURL headers

mandatory

Write a Bash script that takes in a URL as an argument, sends a  `GET`  request to the URL, and displays the body of the response

-   A header variable  `X-HolbertonSchool-User-Id`  must be sent with the value  `98`
-   You have to use  `curl`

Please test your script in the sandbox provided, using the web server running on port 5000

```
guillaume@ubuntu:~/0x10$ ./4-header.sh 0.0.0.0:5000/route_5 ; echo ""
Hello Holberton School!
guillaume@ubuntu:~/0x10$ 

```

**Repo:**

-   GitHub repository:  `holbertonschool-higher_level_programming`
-   Directory:  `0x10-python-network_0`
-   File:  `4-header.sh`

Done?  Help  Get a sandbox

### 5. cURL POST parameters

mandatory

Write a Bash script that takes in a URL, sends a  `POST`  request to the passed URL, and displays the body of the response

-   A variable  `email`  must be sent with the value  `test@gmail.com`
-   A variable  `subject`  must be sent with the value  `I will always be here for PLD`
-   You have to use  `curl`

Please test your script in the sandbox provided, using the web server running on port 5000

```
guillaume@ubuntu:~/0x10$ ./5-post_params.sh 0.0.0.0:5000/route_6 ; echo ""
POST params:
    email: test@gmail.com
    subject: I will always be here for PLD
guillaume@ubuntu:~/0x10$ 

```

**Repo:**

-   GitHub repository:  `holbertonschool-higher_level_programming`
-   Directory:  `0x10-python-network_0`
-   File:  `5-post_params.sh`

Done?  Help
