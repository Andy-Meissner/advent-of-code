import argparse
import tools


def main():
    parser = argparse.ArgumentParser(
        prog="advent-of-code", description="Solves advent-of-code problems"
    )
    sub = parser.add_subparsers(required=True, dest="command")
    download = sub.add_parser("download")
    download.add_argument("--number", required=True, type=int)
    download.add_argument("--year", default=2025, type=int)
    arguments = parser.parse_args()

    if arguments.command == "download":
        tools.download(arguments.year, arguments.number)


if __name__ == "__main__":
    main()
