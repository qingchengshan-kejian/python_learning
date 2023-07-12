import subprocess

out_bytes = subprocess.check_output('netstat', '-a')

out_text = out_bytes.decode('utf-8')

try:
    out_bytes = subprocess.check_output(['cmd', 'arg1', 'arg2'])
except subprocess.CalledProcessError as e:
    out_bytes = e.output
    code = e.returncode
