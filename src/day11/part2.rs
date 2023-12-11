use crate::Shared;

const EXPANSION_FACTOR: i64 = 1_000_000;

#[derive(Eq, PartialEq, Clone)]
struct Pos {
    x: i64,
    y: i64
}

impl Pos {
    fn new(x: i64, y: i64) -> Pos {
        return Pos { x, y };
    }
}

fn parse_map(raw: &String) -> Vec<Vec<char>> {
    let mut lines: Vec<Vec<char>> = Vec::new();
    for line in raw.split("\n") {
        lines.push(line.chars().collect());
    }
    return lines;
}

fn star_pos(map: &Vec<Vec<char>>) -> Vec<Pos> {
    let mut result: Vec<Pos> = Vec::new();
    let mut y_offset: i64 = 0;
    for y in 0..map.len() {
        if !map[y].contains(&'#') {
            y_offset += EXPANSION_FACTOR - 1;
            continue;
        }
        let mut x_offset = 0;
        for x in 0..map[y].len() {
            let mut should_expand = true;
            for y0 in 0..map.len() {
                if map[y0][x] == '#' {
                    should_expand = false;
                    break;
                }
            };
            if should_expand {
                x_offset += EXPANSION_FACTOR - 1;
            }
            if map[y][x] == '#' {
                result.push(Pos::new(x as i64 + x_offset, y as i64 + y_offset));
            }
        }
    }
    return result;
}

fn manhattan_distance(a: &Pos, b: &Pos) -> i64 {
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