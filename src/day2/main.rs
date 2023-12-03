use std::fs;

mod part1;
mod part2;

pub struct Shared {
    p1_input: String,
    p2_input: Option<String>,
}

fn main() {

    let part1 = fs::read_to_string("input/day2/part1.txt").expect("Error reading file");
    let part2 = {
        let metadata = fs::metadata("input/day2/part2.txt");
        if metadata.is_ok() && metadata.unwrap().is_file() {
            Some(fs::read_to_string("input/day2/part2.txt").expect("Error reading file"))
        } else {
            None
        }
    };

    let shared = &mut Shared {
        p1_input: part1,
        p2_input: part2,
    };

    println!("Day 2 - Part 1: {}", part1::solve(shared));
    println!("Day 2 - Part 2: {}", part2::solve(shared));

}