use std::fs;

mod part1;
mod part2;

pub struct Shared(String, String, String);

fn main() {
    let part0  = fs::read_to_string("input/day9/part0.txt").expect("Error reading file");
    let part1 = fs::read_to_string("input/day9/part1.txt").expect("Error reading file");
    let part2 = fs::read_to_string("input/day9/part2.txt").expect("Error reading file");

    let shared = &mut Shared(part0, part1, part2);

    println!("Day 9 - Part 1: {}", part1::solve(shared));
    println!("Day 9 - Part 2: {}", part2::solve(shared));

}