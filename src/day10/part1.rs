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
    let mut result = 1;
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
        result += 1;
        // find next
        let pos = nexts.clone();
        let new_nexts = (find_next(lasts.0, pos.0, &map), find_next(lasts.1, pos.1, &map));
        lasts = nexts;
        nexts = new_nexts;
        // check if they crossed
        nexts.0 != nexts.1
    } {}
    return result.to_string();
}