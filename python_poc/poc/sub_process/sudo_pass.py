#!/usr/bin/env python
#!/usr/bin/env python
from subprocess import Popen, PIPE

def execute(c_list):
	command = Popen(
		c_list,
		stdout=PIPE,
		stderr=PIPE,
	)
	
	output = command.communicate()[0].decode("utf-8")
	error = command.communicate()[1].decode("utf-8")

	return output, error

if __name__ == "__main__":

    pwd = ""
    cmd = ["echo", "ls", "|", "sudo", "-S", pwd]

    output, error = execute(cmd)
    print(output)
    print(error)

