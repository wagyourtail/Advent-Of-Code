use crate::Shared;

fn find_next(mut sequence: Vec<i32>) -> i32 {
    let mut next_val = 0;
    while !sequence.iter().all(|&x| x == 0) {
        let mut next: Vec<i32> = Vec::new();
        for i in 1..sequence.len() {
            next.push(sequence[i] - sequence[i - 1]);
        }
        next_val += sequence[sequence.len() - 1];
        sequence = next;
    }
    return next_val;
}

pub fn solve(shared: &mut Shared) -> String {
    let mut result = 0;
    for line in shared.1.split("\n") {
        let sequence: Vec<i32> = line.split(" ").map(|x| x.parse::<i32>().unwrap()).collect();
        result += find_next(sequence);
    }
    return result.to_string();
}