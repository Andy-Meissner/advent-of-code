import argparse
import tools
from importlib.util import spec_from_file_location, module_from_spec

import sys
from pathlib import Path


def load_and_run(path: Path):
    spec = spec_from_file_location(path.stem, path)
    if not spec:
        raise RuntimeError(f"No spec found for {path}")
    module = module_from_spec(spec)
    sys.modules[path.stem] = module

    if not spec.loader:
        raise RuntimeError(f"No spec laoder found for {path}")
    spec.loader.exec_module(module)

    if not hasattr(module, "main"):
        raise RuntimeError("No main() function found")

    return module.main()


def main():
    parser = argparse.ArgumentParser(
        prog="advent-of-code", description="Solves advent-of-code problems"
    )
    sub = parser.add_subparsers(required=True, dest="command")
    _ = sub.add_parser("download")
    parser.add_argument("--number", required=True, type=int)
    parser.add_argument("--year", default=2025, type=int)

    _ = sub.add_parser("solve")
    arguments = parser.parse_args()

    if arguments.command == "download":
        tools.download(arguments.year, arguments.number)
    if arguments.command == "solve":
        puzzle_script = (
            Path(__file__).resolve().parent
            / str(arguments.year)
            / f"p{arguments.number}.py"
        )
        load_and_run(puzzle_script)


if __name__ == "__main__":
    main()
