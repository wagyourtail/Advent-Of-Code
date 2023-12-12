use std::fs;

mod part1;
mod part2;

pub struct Shared(String, String, String);

#[async_std::main]
async fn main() {
    let part12  = fs::read_to_string("input/day12/part0.txt").expect("Error reading file");
    let part1 = fs::read_to_string("input/day12/part1.txt").expect("Error reading file");
    let part2 = fs::read_to_string("input/day12/part2.txt").expect("Error reading file");

    let shared = &mut Shared(part12, part1, part2);

    // println!("Day 12 - Part 1: {}", part1::solve(shared));
    println!("Day 12 - Part 2: {}", part2::solve(shared));

}