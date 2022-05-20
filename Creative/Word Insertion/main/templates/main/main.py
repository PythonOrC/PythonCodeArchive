import os


def modify(f):
    f = "{% load static %}\n" + f
    for resource in resources:
        if resource in f:
            # print(resource)
            f = f.replace(resource, r"{% static '" + resource + "' %}")
    for file in files:
        rel_f = file.split("\\")[-1]
        f = f.replace(rel_f, "../" + rel_f.split(".")[0])
    return f


files = []
current_dir = os.path.dirname(os.path.realpath(__file__))

for (dirpath, dirnames, filenames) in os.walk(current_dir):
    for filename in filenames:
        if os.path.join(current_dir, filename) != os.path.realpath(__file__):
            files.append(dirpath + "\\" + filename)


current_dir = "\\".join(current_dir.split("\\")[:-2])
current_dir += "\\static"

resources = []
for (dirpath, dirnames, filenames) in os.walk(current_dir):
    for filename in filenames:
        resources.append(dirpath.replace(current_dir + "\\", "") + "/" + filename)

print("starting:")
succeeded = 0
failed = 0
for file in files:
    try:
        with open(file, "r", encoding="utf-8") as inf:
            text = inf.read()
        finished = modify(text)
        try:
            with open(file, "w", encoding="utf-8") as outf:
                outf.write(finished)
            print(f"{file} done")
            succeeded += 1
        except:
            print(f"{file} write failed")
            failed += 1
    except:
        print(f"{file} failed")
        failed += 1
print(f"{succeeded} succeeded, {failed} failed out of {len(files)}")
