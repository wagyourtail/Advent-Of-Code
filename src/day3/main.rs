use std::fs;

mod part1;
mod part2;

pub struct Shared {
    p0_input: String,
    p1_input: String,
    p2_input: String,
}

fn main() {
    let part0  = fs::read_to_string("input/day3/part0.txt").expect("Error reading file");
    let part1 = fs::read_to_string("input/day3/part1.txt").expect("Error reading file");
    let part2 = fs::read_to_string("input/day3/part2.txt").expect("Error reading file");

    let shared = &mut Shared {
        p0_input: part0,
        p1_input: part1,
        p2_input: part2,
    };

    println!("Day 3 - Part 1: {}", part1::solve(shared));
    println!("Day 3 - Part 2: {}", part2::solve(shared));

}