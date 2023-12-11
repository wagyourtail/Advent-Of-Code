use crate::Shared;

#[derive(Eq, PartialEq, Clone)]
struct Pos {
    x: i32,
    y: i32
}

impl Pos {
    fn new(x: i32, y: i32) -> Pos {
        return Pos { x, y };
    }
}

fn parse_map(raw: &String) -> Vec<Vec<char>> {
    let mut lines: Vec<Vec<char>> = Vec::new();
    for line in raw.split("\n") {
        lines.push(line.chars().collect());
    }
    // apply expansion
    let mut x_expanded: Vec<Vec<char>> = Vec::new();
    for y in 0..lines.len() {
        let mut new_line: Vec<char> = Vec::new();
        x_expanded.push(new_line);
    }
    // x expansion
    for x in 0..lines[0].len() {
        let mut has_hash = false;
        for y in 0..lines.len() {
            if lines[y][x] == '#' {
                has_hash = true;
            }
            x_expanded[y].push(lines[y][x]);
        }
        if !has_hash {
            for y in 0..lines.len() {
                x_expanded[y].push('.')
            }
        }
    }
    // y expansion
    let mut xy_expanded: Vec<Vec<char>> = Vec::new();
    for y in 0..x_expanded.len() {
        let new_line: Vec<char> = x_expanded[y].clone();
        xy_expanded.push(new_line);
        if !x_expanded[y].contains(&'#') {
            let new_line: Vec<char> = x_expanded[y].clone();
            xy_expanded.push(new_line);
        }
    }
    return xy_expanded;
}

fn star_pos(map: &Vec<Vec<char>>) -> Vec<Pos> {
    let mut result: Vec<Pos> = Vec::new();
    for y in 0..map.len() {
        for x in 0..map[y].len() {
            if map[y][x] == '#' {
                result.push(Pos::new(x as i32, y as i32));
            }
        }
    }
    return result;
}

fn manhattan_distance(a: &Pos, b: &Pos) -> i32 {
    return (a.x - b.x).abs() + (a.y - b.y).abs();
}

fn pairs(stars: &Vec<Pos>) -> Vec<(Pos, Pos)> {
    let mut result: Vec<(Pos, Pos)> = Vec::new();
    for i in 0..stars.len() {
        for j in i+1..stars.len() {
            result.push((stars[i].clone(), stars[j].clone()));
        }
    }
    return result;
}

pub fn solve(shared: &mut Shared) -> String {
    let starmap = parse_map(&shared.1);
    let stars = star_pos(&starmap);
    let pairs = pairs(&stars);
    let mut result = 0;
    for pair in pairs {
        result += manhattan_distance(&pair.0, &pair.1);
    }
    return result.to_string();
}