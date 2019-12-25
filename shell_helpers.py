def get_folder(arg=1):
    folder = sys.argv[arg]
    if folder.endswith('/'):
        return folder
    else:
        return folder+'/'
