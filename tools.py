import requests


def download(year: int, puzzle_number: int):
    puzzle_url = f"https://adventofcode.com/{year}/day/{puzzle_number}/input"

    cookies = {
        "session": "53616c7465645f5f03825fb743e3317d7d25ecbab3ac0a1d0b33c3d385ee1ca2b87fc0f9f2e719d06ef1ff3bb3e68b9a4784905e911e643cc79ac8887eec7665"
    }
    headers = {"User-Agent": "andy_meissner"}
    response = requests.get(puzzle_url, cookies=cookies, headers=headers)
    response.raise_for_status()

    with open(f"{year}/p{puzzle_number}.txt", "w") as f:
        f.write(response.text)


def get_puzzle_input() -> list[str]:
    return []
