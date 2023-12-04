use std::collections::HashMap;
use crate::Shared;

pub fn solve(shared: &mut Shared) -> String {
    let lines = shared.1.split('\n').collect::<Vec<&str>>();

    let mut extra_count: HashMap<usize, i32> = HashMap::new();

    for (idx, line) in lines.iter().enumerate() {
        let mut card = line.split(':');
        card.next();
        let mut parts = card.next().unwrap().split('|');
        let winning = parts.next().unwrap().split_ascii_whitespace();
        let have = parts.next().unwrap().split_ascii_whitespace().collect::<Vec<&str>>();
        let mut win_count = 0;
        for num in winning {
            if have.contains(&num) {
                win_count += 1;
            }
        }
        if win_count > 0 {
            // add current's extra_count to extra_count for each subsequent in range ..win_count
            let current_extra = *extra_count.get(&idx).unwrap_or(&0) + 1;
            for i in idx+1..idx+1+win_count {
                let mut extra = *extra_count.get(&i).unwrap_or(&0);
                extra += current_extra;
                extra_count.insert(i, extra);
            }
        }
    }

    let mut result = lines.len() as i32;
    for value in extra_count.values() {
        result += *value;
    }

    return result.to_string();
}