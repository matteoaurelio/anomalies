import subprocess
from utils import find_and_summarize_error

# Define the command to run the script as a plain string
command = 'python test_1.py'

# Run the script in the shell and capture the standard error output
result = subprocess.run(command, shell=True, text=True, capture_output=True)

# The standard error (including any Python errors) will be in result.stderr
error_output = result.stderr

# If there are errors in the script
if result.returncode != 0:
    summary = find_and_summarize_error(text=error_output,
                             keyword='error',
                             context_size=3)
    
    with open('error_log.txt', 'w') as f:
        f.write(summary)
else:
    script_name = command.split()[1]
    print(f'Success running {script_name}')



