use crate::Shared;

fn find_prev(mut sequence: Vec<i32>) -> i32 {
    let mut stack: Vec<i32> = Vec::new();
    while !sequence.iter().all(|&x| x == 0) {
        let mut next: Vec<i32> = Vec::new();
        for i in 1..sequence.len() {
            next.push(sequence[i] - sequence[i - 1]);
        }
        stack.push(sequence[0]);
        sequence = next;
    }
    let mut val = 0;
    while !stack.is_empty() {
        val = stack.pop().unwrap() - val;
    }
    return val;
}

pub fn solve(shared: &mut Shared) -> String {
    let mut result = 0;
    for line in shared.1.split("\n") {
        let sequence: Vec<i32> = line.split(" ").map(|x| x.parse::<i32>().unwrap()).collect();
        result += find_prev(sequence);
    }
    return result.to_string();
}