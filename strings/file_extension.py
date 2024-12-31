filename = 'python_notes.txt'
no_suffix = filename.removesuffix(".txt")
no_prefix = filename.removeprefix("python_notes")

print(f"{no_suffix}{no_prefix} \n{filename} ")
