from modules.actions import lib_manager


while True:
    action = input(lib_manager.list_actions())
    if action != "0":
        lib_manager.execute(action)
    else:
        break

