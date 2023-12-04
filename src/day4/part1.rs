use crate::Shared;

pub fn solve(shared: &mut Shared) -> String {
    let lines = shared.1.split('\n');
    let mut result = 0;

    for line in lines {
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
            result += 1 << (win_count - 1);
        }
    }

    return result.to_string();
}