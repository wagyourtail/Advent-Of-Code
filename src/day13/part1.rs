use crate::Shared;

fn split_grids(raw: String) -> Vec<String> {
    // split on double newlines
    let mut grids = Vec::new();
    let mut grid = String::new();
    for line in raw.lines() {
        if line.len() == 0 {
            grids.push(grid);
            grid = String::new();
        } else {
            grid.push_str(line);
            grid.push('\n');
        }
    }
    grids.push(grid);
    return grids;
}

fn find_reflection_index(grid: String) -> i32 {
    // convert to 2d array
    let mut grid = grid.lines().map(|x| x.chars().collect::<Vec<char>>()).collect::<Vec<Vec<char>>>();
    // find the first row/col that works for reflection
    let mut row = find_reflection_index_row(grid.clone());
    let mut col = find_reflection_index_col(grid.clone());

    // if we can't find a row or col, return -1
    if row == -1 && col == -1 {
        return -1;
    }

    // if we can find both, return the smaller of the two
    if row != -1 && col != -1 {
        return if row < col {
            row * 100
        } else {
            col
        }
    }

    // if we can only find one, return that one
    if row != -1 {
        return row * 100;
    }
    return col;
}

fn find_reflection_index_row(grid: Vec<Vec<char>>) -> i32 {
    // find the first row that works for reflection
    for i in 1..grid.len() {
        // reflection is between rows, so must match
        let mut spread = 0;
        let mut matches = true;
        loop {
            if i + spread >= grid.len() || i - spread == 0 {
                break;
            }
            if grid[i + spread] != grid[i - spread - 1] {
                matches = false;
                break;
            }
            spread += 1;
        }
        if matches {
            return i as i32;
        }
    }
    return -1;
}

fn find_reflection_index_col(grid: Vec<Vec<char>>) -> i32 {
    // let's just rotate the grid and use the row function
    let mut grid = rotate_grid(grid);
    return find_reflection_index_row(grid);
}

fn rotate_grid(grid: Vec<Vec<char>>) -> Vec<Vec<char>> {
    let mut new_grid = Vec::new();
    for i in 0..grid[0].len() {
        let mut new_row = Vec::new();
        for j in 0..grid.len() {
            new_row.push(grid[j][i]);
        }
        new_grid.push(new_row);
    }
    return new_grid;
}


pub fn solve(shared: &mut Shared) -> String {
    let grids = split_grids(shared.1.clone());
    let mut total = 0;
    for grid in grids {
        let reflection_index = find_reflection_index(grid);
        if reflection_index != -1 {
            total += reflection_index;
        } else {
            panic!("No reflection index found");
        }
    }
    return total.to_string();
}