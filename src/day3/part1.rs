use crate::Shared;

pub fn solve(shared: &mut Shared) -> String {
    let mut value = 0;
    let lines = shared.p1_input.split('\n').collect::<Vec<&str>>();
    for line_num in 0..lines.len() {
        let line = lines[line_num];
        // find non . or num symbols on line
        let mut nums = String::new();
        for line_idx in 0..line.len() {
            let char = line.chars().nth(line_idx).unwrap();
            if char >= '0' && char <= '9' {
                nums.push(char);
            } else if nums.len() > 0 {
                // check if num is adjacent to non . char
                find_sym(&mut value, &lines, line_num, line, &mut nums, line_idx);
                nums.clear()
            }
        }
        find_sym(&mut value, &lines, line_num, line, &mut nums, line.len());
        nums.clear();
    }
    return value.to_string();
}

fn find_sym(value: &mut i32, lines: &Vec<&str>, line_num: usize, line: &str, nums: &mut String, line_idx: usize) {
    for offset in 1..nums.len() + 1 {
        let pos_j = line_idx - offset;
        // search around pos for non . char
        for l in -1..2 {
            for m in -1..2 {
                if l == -1 && line_num == 0 { continue; }
                if m == -1 && pos_j == 0 { continue; }
                if l == 1 && line_num == lines.len() - 1 { continue; }
                if m == 1 && pos_j == line.len() - 1 { continue; }
                let test = lines[(line_num as i32 + l) as usize].chars().nth((pos_j as i32 + m) as usize).unwrap();
                if test != '.' && (test < '0' || test > '9') {
                    *value += nums.parse::<i32>().unwrap();
                    // println!("{}", nums.to_string());
                    return;
                }
            }
        }
    }
}