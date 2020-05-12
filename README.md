# b593shell
A python script to exploit the ping vulnerability in the Huawei B593 Router, resulting in remote code execution

The Script requires three arguments that need to be passed via the command line. These are as follows:

1. Host
2. Password
3. Command_to_execute

Thus the command to run the script will look somethin like:

  python b593shell.py 192.168.1.1 "my pass" "cat /var/sshusers.cfg"

Note: If your username/cmd_to_execute contains a space, then you need to encase it in double quotes.
