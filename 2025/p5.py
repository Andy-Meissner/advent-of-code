from pathlib import Path


def insert_range(all_ranges: list[tuple[int, int]], new_range: tuple[int, int]):
    for i, r in enumerate(all_ranges):
        # Go from left to right
        if r[1] < new_range[0] - 1:
            continue
        # newr_left is right of range right side
        if new_range[0] >= r[0]:
            if new_range[1] > r[1]:  # New is inside of existing but larger on the right
                r = (r[0], new_range[1])
            # new range is included inside the existing range
            return all_ranges
        if new_range[1] >= r[0] - 1:
            if new_range[1] > r[1]:
                r = (new_range[0], new_range[1])
            else:
                r = (new_range[0], r[1])
            return all_ranges
        all_ranges.insert(i, new_range)
        return all_ranges
    all_ranges.append(new_range)
    return all_ranges


def main():
    relative_dir = Path(__file__).resolve().parent
    with open(f"{relative_dir}/p5_test.txt") as f:
        lines = f.readlines()

    with open(f"{relative_dir}/p5.txt") as f:
        lines = f.readlines()

    fresh_ranges = []
    fresh_ids = []

    for current_range in lines:
        current_range = current_range.strip()
        if "-" in current_range:
            spl = current_range.split("-")
            new_range = (int(spl[0]), int(spl[1]))
            insert_range(fresh_ranges, new_range)
        else:
            if len(current_range) > 0:
                for existing_range in fresh_ranges:
                    i = int(current_range)
                    if existing_range[0] <= i and existing_range[1] >= i:
                        fresh_ids.append(i)
                        break

    print(f"Fresh Ids: {len(fresh_ids)}")

    ctr = 0
    for existing_range in fresh_ranges:
        ctr += existing_range[1] - existing_range[0] + 1

    print(f"All Fresh Ids: {ctr}")


if __name__ == "__main__":
    main()
