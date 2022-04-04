def group_by_owners(file_list):
    file_by_owners = {}
    for file in file_list:
        owner = file_list[file]
        if owner in file_by_owners:
            file_by_owners[owner].append(file)
        else:
            file_by_owners[owner] = [file]

    return file_by_owners


print(group_by_owners({
    'Input.txt': 'Randy',
    'Code.py': 'Stan',
    'Output.txt': 'Randy'
}))
