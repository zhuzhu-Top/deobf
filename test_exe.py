import traceback

if __name__ == '__main__':
    file_name = r"C:\Users\zhuzhu\AppData\Roaming\Binary Ninja\plugins\deobf\test.py"
    global_namespace = globals()
    local_namespace = locals()
    file = open(file_name, "r")

    try:
        exec(compile(file.read(), file_name, "exec"), global_namespace, local_namespace)
        print(f" ==> {aaa}")
    except BaseException as e:
        print(traceback.format_exc())
    print(f" ==> {aaa}")