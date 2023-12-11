use crate::Shared;

#[derive(Eq, PartialEq, Clone, Hash)]
struct Pos {
    x: i32,
    y: i32
}

impl Pos {
    fn new(x: i32, y: i32) -> Pos {
        return Pos { x, y };
    }
}

fn get_connected(pos: &Pos, map: &Vec<Vec<char>>) -> Option<(Pos, Pos)> {
    // get char at pos
    let c = map[pos.y as usize][pos.x as usize];
    // find next
    return Some(match c {
        '|' => (Pos::new(pos.x, pos.y + 1), Pos::new(pos.x, pos.y - 1)), // top-bottom
        '-' => (Pos::new(pos.x + 1, pos.y), Pos::new(pos.x - 1, pos.y)), // left-right
        'L' => (Pos::new(pos.x + 1, pos.y), Pos::new(pos.x, pos.y - 1)), // top-right
        'J' => (Pos::new(pos.x - 1, pos.y), Pos::new(pos.x, pos.y - 1)), // top-left
        '7' => (Pos::new(pos.x - 1, pos.y), Pos::new(pos.x, pos.y + 1)), // bottom-left
        'F' => (Pos::new(pos.x + 1, pos.y), Pos::new(pos.x, pos.y + 1)), // bottom-right
        '.' => return None,
        'S' => {
            // iterate over all directions
            // find ones that point back
            let mut result: Vec<Pos> = Vec::new();
            for dir in vec![Pos::new(0, 1), Pos::new(1, 0), Pos::new(0, -1), Pos::new(-1, 0)] {
                if (pos.x == 0 && dir.x == -1) || (pos.y == 0 && dir.y == -1) { continue; } // skip out of bounds
                if (pos.x == map[0].len() as i32 - 1 && dir.x == 1) || (pos.y == map.len() as i32 - 1 && dir.y == 1) { continue; } // skip out of bounds
                let next = Pos::new(pos.x + dir.x, pos.y + dir.y);
                let connected = get_connected(&next, map);
                if connected.is_none() { continue; }
                let unwrapped = connected.unwrap();
                if unwrapped.0 == *pos || unwrapped.1 == *pos {
                    result.push(next);
                }
            }
            assert_eq!(result.len(), 2, "Expected 2 pipes, found {}", result.len());
            return Some((result[0].clone(), result[1].clone()));
        },
        _ => return None,
    });
}

fn find_next(last: Pos, pos: Pos, map: &Vec<Vec<char>>) -> Pos {
    // get char at pos
    let values = get_connected(&pos, map).unwrap();
    assert!(values.0 == last || values.1 == last, "Expected last to be one of the values, broken pipe!");
    // find value not equal last
    return if values.0 != last {
        values.0
    } else {
        values.1
    }
}

fn parse_map(map: &String) -> Vec<Vec<char>> {
    let mut result: Vec<Vec<char>> = Vec::new();
    for line in map.split("\n") {
        result.push(line.chars().collect());
    }
    return result;
}

fn find_start(map: &Vec<Vec<char>>) -> Pos {
    for y in 0..map.len() {
        for x in 0..map[y].len() {
            if map[y][x] == 'S' {
                return Pos::new(x as i32, y as i32);
            }
        }
    }
    panic!("No start found");
}

fn max(a: f32, b: f32) -> f32 {
    return if a > b { a } else { b };
}

pub fn solve(shared: &mut Shared) -> String {
    let map = parse_map(&shared.1);
    // let mut new_map: Vec<Vec<char>> = Vec::new();
    // // insert ground
    // for y in 0..map.len() {
    //     new_map.push(map[y].clone().iter().map(|_| '.').collect());
    // }
    let start = find_start(&map);
    let mut lasts = (start.clone(), start.clone());
    let mut nexts = get_connected(&start, &map).unwrap();
    let mut vertexes: Vec<Pos> = Vec::new();
    vertexes.push(start.clone());
    vertexes.insert(0, nexts.0.clone());
    vertexes.push(nexts.1.clone());
    while {
        // // insert nexts into new_map
        // new_map[nexts.0.y as usize][nexts.0.x as usize] = map[nexts.0.y as usize][nexts.0.x as usize];
        // new_map[nexts.1.y as usize][nexts.1.x as usize] = map[nexts.1.y as usize][nexts.1.x as usize];
        // // print new_map
        // println!("###########");
        // for line in new_map.clone() {
        //     for c in line {
        //         print!("{}", c);
        //     }
        //     println!();
        // }
        // increment result
        // find next
        let pos = nexts.clone();
        let new_nexts = (find_next(lasts.0, pos.0, &map), find_next(lasts.1, pos.1, &map));
        lasts = nexts;
        nexts = new_nexts;
        vertexes.insert(0, nexts.0.clone());
        vertexes.push(nexts.1.clone());
        // check if they crossed
        nexts.0 != nexts.1
    } {}

    // shoelace formula
    let mut area = 0.0;
    for i in 0..vertexes.len() - 1 {
        area += vertexes[i].x as f32 * vertexes[i + 1].y as f32;
        area -= vertexes[i].y as f32 * vertexes[i + 1].x as f32;
    }
    area = max(area, -area) / 2.0;
    // because 1/2 of vertexes are going to be the inner and half are outer, because of how right angle polygons work,
    // we can just subtract half the number of vertexes to get the inner area
    // but for some reason add 1??? idk, it works
    return (area - ((vertexes.len() - 1) / 2) as f32 + 1.0).to_string();
}