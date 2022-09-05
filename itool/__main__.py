import argparse
import os
import pathlib
import subprocess


def rm_tree(p):
    pth = pathlib.Path(p)
    for child in pth.glob('MODEL_CHUNKED.*'):
        if child.is_file():
            child.unlink()
        else:
            rm_tree(child)
    pth.rmdir()


def main(t: str, src: str, dest: str, cs: int):
    src_path = pathlib.Path(src)
    dest_path = pathlib.Path(dest)
    assert src_path.exists() and src_path.is_dir(), "Source argument provided is not a directory"
    dest_path.mkdir(parents=True, exist_ok=True)
    if dest_path.exists() and len(list(dest_path.glob("MODEL_CHUNKED.*"))) > 0:
        # Clean rubbish from previous call otherwise it won't work.
        rm_tree(dest_path)
        dest_path.mkdir(parents=True, exist_ok=True)
    bp = pathlib.Path(os.getcwd()) / "bin"
    if t == "chunkify":
        command = ["bash", str(bp / "chunkify.sh"), str(src_path), str(dest_path / "MODEL_CHUNKED.zip"), str(cs) + "m"]
    subprocess.run(command)


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description='TOOL parser')

    parser.add_argument("-t", "--task", type=str, help="Task to complete", default=None, dest='task')
    parser.add_argument("-s", "--src", type=str, required=True, dest="src")
    dest_dir = pathlib.Path(os.getcwd()) / "output"
    parser.add_argument("-d", "--dest", type=str, required=False, dest="dest", default=str(dest_dir))
    parser.add_argument("-cs", "--chunksize", type=int, required=False, default=30, dest="cs")
    args = parser.parse_args()
    main(args.task, args.src, args.dest, args.cs)
