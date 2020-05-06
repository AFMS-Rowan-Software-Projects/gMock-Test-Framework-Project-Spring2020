import argparse, os.path, re, subprocess

# global variables
bash_profile = os.path.expanduser('~/.bash_profile')
alias_regex = r'alias gwiz="python3 \S*?"\n?'


# Adds or updates the gwiz alias in the current user's .bash_profile
# Raises RuntimeError if gwiz.py is not in the current working directory
def update():
    gwiz_path = os.path.abspath('gwiz.py')
    if not os.path.exists(gwiz_path):
        raise RuntimeError('gwiz.py must be in the current working directory')

    alias_new = f'alias gwiz="python3 {gwiz_path}"\n'
    contents = read()

    if re.search(alias_regex, contents) is None:
        contents = f'{contents}{alias_new}'
    else:
        contents = re.sub(alias_regex, alias_new, contents)

    write(contents)


# Removes the gwiz alias in the current user's .bash_profile
def remove():
    contents = read()
    contents = re.sub(alias_regex, '', contents)
    write(contents)


# Returns a string containing the contents of .bash_profile
# String is empty if the file doesn't exist
def read():
    if os.path.exists(bash_profile):
        with open(bash_profile, mode='r') as bp:
            file_contents = bp.read()
    else:
        file_contents = ''
    return file_contents


# Overwrites the contents of .bash_profile with the passed string
# Creates the file if it doesn't exist
def write(file_contents):
    with open(bash_profile, mode='w') as bp:
        bp.write(file_contents)


# Returns an argument parser for the alias module
# Can be used alone or added as a subparser
def create_parser():
    parser = argparse.ArgumentParser(
        description='Enables an easy way to add and remove an alias for the gwiz python program. The alias will allow the user to call the program from anywhere in their user directory tree by simply typing "gwiz [arguments]".',
        epilog='This script edits the .bash_profile of the current user. It simply adds, updates, or removes the following line to manage the alias; alias gwiz="python3 absolute_path_to_gwiz.py". The current working directory is used to find the absolute file path of gwiz.py and can not be done in an efficient manner otherwise.')
    parser.add_argument('-s', '--show_file', action='store_true',
                        help='Prints the contents of .bash_profile after it has been edited.')
    group = parser.add_mutually_exclusive_group()
    group.add_argument('-c', '--create', action='store_true',
                       help='Creates the alias. The gwiz.py file must be in the current working directory.')
    group.add_argument('-r', '--remove', action='store_true', help='Removes the alias.')
    return parser


# This block is executed when this module is run as a script and not when imported
if __name__ == '__main__':
    parser = create_parser()
    args = parser.parse_args()
    if args.create:
        try:
            update()
            print('Alias Updated')
        except RuntimeError:
            print('Your current working directory must have the gwiz modules in it.')
            print('Please navigate to them and recall the command.')
    elif args.remove:
        remove()
        print('Alias Removed')
    elif not args.show_file:
        parser.print_usage()

    if args.show_file:
        print('\ncat .bash_profile')
        subprocess.run(f'cat {bash_profile}', shell=True)
