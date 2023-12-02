use crate::Shared;

pub fn solve(shared: &mut Shared) -> String {
    let mut value = 0;
    shared.p1_input.split('\n').for_each(|line| {
        let semi = line.chars().into_iter().position(|c| c == ':').unwrap();
        let key = line.get(5..semi).unwrap().parse::<i32>().unwrap();
        let mut else_ = true;
        for game in line.get(semi+1..line.len()).unwrap().split(';') {
            let mut red = 0;
            let mut blue = 0;
            let mut green = 0;
            for tile in game.split(',') {
                let mut t = tile.split(' ');
                t.next();
                let number = t.next().unwrap();
                let color = t.next().unwrap();
                match color {
                    "red" => red += number.parse::<i32>().unwrap(),
                    "blue" => blue += number.parse::<i32>().unwrap(),
                    "green" => green += number.parse::<i32>().unwrap(),
                    _ => (),
                }
            }
            if red > 12 || green > 13 || blue > 14 {
                else_ = false;
                break;
            }
        }
        if else_ {
            value += key;
        }
    });
    return value.to_string();
}