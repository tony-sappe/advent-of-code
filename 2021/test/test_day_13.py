from day_13 import Sample_Input, parse_input, place_dots, count_dots, step_1, fold_paper


def test_input_parser():
    """Test the input parser output behavior"""
    points, folds = parse_input(Sample_Input)
    assert folds == [("y", 7), ("x", 5)]
    assert points == [
        (6, 10),
        (0, 14),
        (9, 10),
        (0, 3),
        (10, 4),
        (4, 11),
        (6, 0),
        (6, 12),
        (4, 1),
        (0, 13),
        (10, 12),
        (3, 4),
        (3, 0),
        (8, 4),
        (1, 10),
        (2, 14),
        (8, 10),
        (9, 0),
    ]


def test_dot_placement():
    points, _ = parse_input(Sample_Input)
    grid = place_dots(points)
    expected = [
        "...#..#..#.",
        "....#......",
        "...........",
        "#..........",
        "...#....#.#",
        "...........",
        "...........",
        "...........",
        "...........",
        "...........",
        ".#....#.##.",
        "....#......",
        "......#...#",
        "#..........",
        "#.#........",
    ]

    for p, e in zip(grid, expected):
        assert "".join(p) == e


def test_counting():
    points, _ = parse_input(Sample_Input)
    grid = place_dots(points)
    assert count_dots(grid) == 18


def test_provided_step_1():
    """Ensure the sample puzzle input matches the provided answer for step 1"""
    points, folds = parse_input(Sample_Input)
    assert step_1(points, folds) == 17


def test_provided_step_2():
    """Ensure the sample puzzle input matches the provided answer for step 2"""
    expected = [
        "#####",
        "#...#",
        "#...#",
        "#...#",
        "#####",
        ".....",
        ".....",
    ]
    points, folds = parse_input(Sample_Input)
    grid = place_dots(points)
    for fold in folds:
        grid = fold_paper(grid, fold)

    for p, e in zip(grid, expected):
        assert "".join(p) == e
