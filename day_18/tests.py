"""
🧪 Tests for Pathfinding on a Grid

Run this file to check if your pathfinding is correct!

Usage:
    python tests.py
"""

from project import (
    create_grid,
    add_obstacle,
    is_valid_cell,
    get_neighbors,
    find_path_bfs,
    reconstruct_path,
    calculate_path_length,
    visualize_grid,
    count_reachable_cells,
)


# ============================================================
# CREATE GRID TESTS
# ============================================================

def test_create_grid_size():
    """Test: Grid has correct dimensions"""
    grid = create_grid(5, 3)
    assert len(grid) == 3, f"❌ Should have 3 rows"
    assert len(grid[0]) == 5, f"❌ Should have 5 columns"
    print("✅ Test 1 passed: Grid dimensions")


def test_create_grid_empty():
    """Test: Grid cells are initialized to 0"""
    grid = create_grid(3, 3)
    for row in grid:
        for cell in row:
            assert cell == 0, f"❌ Cells should be 0"
    print("✅ Test 2 passed: Grid empty")


# ============================================================
# OBSTACLE TESTS
# ============================================================

def test_add_obstacle():
    """Test: Obstacle added correctly"""
    grid = create_grid(5, 5)
    add_obstacle(grid, 2, 1)
    assert grid[1][2] == 1, f"❌ Cell (2,1) should be blocked"
    print("✅ Test 3 passed: Add obstacle")


# ============================================================
# VALID CELL TESTS
# ============================================================

def test_valid_cell_empty():
    """Test: Empty cell is valid"""
    grid = create_grid(5, 5)
    assert is_valid_cell(grid, 2, 2) == True, f"❌ Empty cell should be valid"
    print("✅ Test 4 passed: Empty cell valid")


def test_valid_cell_obstacle():
    """Test: Obstacle cell is invalid"""
    grid = create_grid(5, 5)
    add_obstacle(grid, 2, 2)
    assert is_valid_cell(grid, 2, 2) == False, f"❌ Obstacle should be invalid"
    print("✅ Test 5 passed: Obstacle invalid")


def test_valid_cell_out_of_bounds():
    """Test: Out of bounds is invalid"""
    grid = create_grid(5, 5)
    assert is_valid_cell(grid, -1, 0) == False, f"❌ Negative x invalid"
    assert is_valid_cell(grid, 0, -1) == False, f"❌ Negative y invalid"
    assert is_valid_cell(grid, 5, 0) == False, f"❌ x >= width invalid"
    assert is_valid_cell(grid, 0, 5) == False, f"❌ y >= height invalid"
    print("✅ Test 6 passed: Out of bounds invalid")


# ============================================================
# NEIGHBORS TESTS
# ============================================================

def test_neighbors_center():
    """Test: Center cell has 4 neighbors"""
    grid = create_grid(5, 5)
    neighbors = get_neighbors(grid, 2, 2)
    assert len(neighbors) == 4, f"❌ Center should have 4 neighbors"
    print("✅ Test 7 passed: Center neighbors")


def test_neighbors_corner():
    """Test: Corner cell has 2 neighbors"""
    grid = create_grid(5, 5)
    neighbors = get_neighbors(grid, 0, 0)
    assert len(neighbors) == 2, f"❌ Corner should have 2 neighbors"
    print("✅ Test 8 passed: Corner neighbors")


def test_neighbors_with_obstacle():
    """Test: Obstacle neighbors not included"""
    grid = create_grid(5, 5)
    add_obstacle(grid, 2, 1)  # Block cell above (2,2)
    neighbors = get_neighbors(grid, 2, 2)
    assert (2, 1) not in neighbors, f"❌ Obstacle shouldn't be neighbor"
    print("✅ Test 9 passed: Obstacle not neighbor")


# ============================================================
# PATHFINDING TESTS
# ============================================================

def test_path_straight():
    """Test: Find straight path"""
    grid = create_grid(5, 1)
    path = find_path_bfs(grid, (0, 0), (4, 0))
    assert len(path) == 5, f"❌ Path should be 5 cells long"
    assert path[0] == (0, 0), f"❌ Should start at (0,0)"
    assert path[-1] == (4, 0), f"❌ Should end at (4,0)"
    print("✅ Test 10 passed: Straight path")


def test_path_around_obstacle():
    """Test: Path goes around obstacle"""
    grid = create_grid(3, 3)
    add_obstacle(grid, 1, 0)  # Block middle of top row
    add_obstacle(grid, 1, 1)  # Block middle
    path = find_path_bfs(grid, (0, 0), (2, 0))
    assert len(path) > 0, f"❌ Should find a path around"
    print("✅ Test 11 passed: Path around obstacle")


def test_path_no_solution():
    """Test: No path returns empty"""
    grid = create_grid(3, 3)
    # Block all paths
    add_obstacle(grid, 1, 0)
    add_obstacle(grid, 1, 1)
    add_obstacle(grid, 1, 2)
    path = find_path_bfs(grid, (0, 0), (2, 0))
    assert path == [], f"❌ Should return empty list when blocked"
    print("✅ Test 12 passed: No solution")


def test_path_same_start_goal():
    """Test: Start equals goal"""
    grid = create_grid(3, 3)
    path = find_path_bfs(grid, (1, 1), (1, 1))
    assert path == [(1, 1)], f"❌ Should return just the start/goal"
    print("✅ Test 13 passed: Same start and goal")


# ============================================================
# PATH LENGTH TESTS
# ============================================================

def test_path_length():
    """Test: Calculate path length"""
    path = [(0, 0), (1, 0), (2, 0), (2, 1)]
    length = calculate_path_length(path)
    assert length == 3, f"❌ Length should be 3 steps"
    print("✅ Test 14 passed: Path length")


# ============================================================
# VISUALIZE TESTS
# ============================================================

def test_visualize_basic():
    """Test: Basic visualization"""
    grid = create_grid(3, 3)
    add_obstacle(grid, 1, 1)
    viz = visualize_grid(grid)
    assert "#" in viz, f"❌ Should show obstacle as #"
    assert "." in viz, f"❌ Should show empty as ."
    print("✅ Test 15 passed: Basic visualization")


def test_visualize_with_path():
    """Test: Visualization shows path"""
    grid = create_grid(3, 3)
    path = [(0, 0), (1, 0), (2, 0)]
    viz = visualize_grid(grid, path)
    assert "*" in viz or "S" in viz or "G" in viz, \
        f"❌ Should show path markers"
    print("✅ Test 16 passed: Path visualization")


# ============================================================
# REACHABLE CELLS TESTS
# ============================================================

def test_count_reachable_all():
    """Test: All cells reachable in empty grid"""
    grid = create_grid(3, 3)
    count = count_reachable_cells(grid, (0, 0))
    assert count == 9, f"❌ All 9 cells should be reachable"
    print("✅ Test 17 passed: All reachable")


def test_count_reachable_blocked():
    """Test: Blocked cells not reachable"""
    grid = create_grid(3, 3)
    # Create a wall
    add_obstacle(grid, 1, 0)
    add_obstacle(grid, 1, 1)
    add_obstacle(grid, 1, 2)
    count = count_reachable_cells(grid, (0, 0))
    assert count == 3, f"❌ Only 3 cells reachable, got {count}"
    print("✅ Test 18 passed: Blocked not reachable")


def run_all_tests():
    """Run all tests and show results."""
    print("=" * 50)
    print("🤖 Running Pathfinding Tests")
    print("=" * 50)
    print()
    
    tests = [
        test_create_grid_size,
        test_create_grid_empty,
        test_add_obstacle,
        test_valid_cell_empty,
        test_valid_cell_obstacle,
        test_valid_cell_out_of_bounds,
        test_neighbors_center,
        test_neighbors_corner,
        test_neighbors_with_obstacle,
        test_path_straight,
        test_path_around_obstacle,
        test_path_no_solution,
        test_path_same_start_goal,
        test_path_length,
        test_visualize_basic,
        test_visualize_with_path,
        test_count_reachable_all,
        test_count_reachable_blocked,
    ]
    
    passed = 0
    failed = 0
    
    for test in tests:
        try:
            test()
            passed += 1
        except AssertionError as e:
            print(str(e))
            failed += 1
        except TypeError as e:
            print(f"❌ {test.__doc__.split(':')[0]}: Function not implemented yet")
            failed += 1
        except Exception as e:
            print(f"❌ {test.__name__} crashed: {e}")
            failed += 1
    
    print()
    print("=" * 50)
    print(f"Results: {passed} passed, {failed} failed")
    if failed == 0:
        print("🎉 All tests passed! Pathfinding ready!")
    else:
        print("💪 Keep coding, find that path!")
    print("=" * 50)


if __name__ == "__main__":
    run_all_tests()

