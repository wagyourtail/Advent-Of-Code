use std::collections::HashMap;
use crate::Shared;

#[derive(Eq, Hash, PartialEq)]
struct Pos {
    x: i32,
    y: i32,
}

pub fn solve(shared: &mut Shared) -> String {
    let mut value = 0;
    let lines = shared.p1_input.split('\n').collect::<Vec<&str>>();
    let mut gear_map: HashMap<Pos, Vec<String>> = HashMap::new();
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
                find_sym(&lines, line_num, line, &mut nums, line_idx, &mut gear_map);
                nums.clear()
            }
        }
        find_sym(&lines, line_num, line, &mut nums, line.len(), &mut gear_map);
        nums.clear();
    }
    // search for gear
    for key in gear_map.keys() {
        let nums = gear_map.get(key).unwrap();
        if nums.len() != 2 { continue; }
        // multiply nums
        let mut result = 1;
        for num in nums {
            result *= num.parse::<i32>().unwrap();
        }
        value += result;
    }
    return value.to_string();
}

fn find_sym(lines: &Vec<&str>, line_num: usize, line: &str, nums: &mut String, line_idx: usize, gear_map: &mut HashMap<Pos, Vec<String>>) {
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
                if test == '*' {
                    let pos = Pos { x: line_num as i32 + l, y: pos_j as i32 + m };
                    if gear_map.contains_key(&pos) {
                        let mut nums2 = gear_map.get(&pos).unwrap().clone();
                        nums2.push(nums.to_string());
                        gear_map.insert(pos, nums2);
                    } else {
                        gear_map.insert(pos, vec![nums.to_string()]);
                    }
                    return;
                }
            }
        }
    }
}