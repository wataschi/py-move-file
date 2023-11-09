import os


def move_file(command: str) -> None:
    get_command = command.split()
    if get_command[0] == "mv" and len(get_command) == 3:
        _, old_file_name, new_file_name = get_command
        directory = os.path.dirname(new_file_name)
        if directory:
            if not os.path.exists(directory):
                os.makedirs(directory, exist_ok=True)
            elif os.path.isfile(new_file_name):
                os.remove(new_file_name)

            with (open(old_file_name, "r") as file_old,
                  open(new_file_name, "w") as file_new):
                file_new.write(file_old.read())
            os.remove(old_file_name)
        else:
            if os.path.exists(new_file_name):
                os.remove(new_file_name)
            os.rename(old_file_name, new_file_name)
