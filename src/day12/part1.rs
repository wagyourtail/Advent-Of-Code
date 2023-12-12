use crate::Shared;
use regex::Regex;

fn parse_groups(line: &str) -> String {
    let nums = line.split(",").map(|x| x.parse::<i32>().unwrap()).collect::<Vec<i32>>();
    let mut regex = Vec::new();
    for num in nums {
        regex.push(format!("#{{{}}}", num));
        regex.push("\\.+".to_string());
    }
    regex.remove(regex.len() - 1);
    return regex.join("");
}

fn mutations(line: &str, groups: String) -> i32 {
    if !line.contains("?") {
        return 1;
    }
    let mut total: i32 = 1;
    for char in line.chars() {
        if char == '?' {
            total <<= 1;
        }
    }

    print!("{} -> ", total.ilog2());

    let group_matcher = Regex::new(&format!("^\\.*{}\\.*$", groups)).unwrap();
    let mut matches = 0;
    for i in 0..total {
        let mut j = i;
        // map bitwise to ?'s
        let mut new_line = String::new();
        for char in line.chars() {
            if char == '?' {
                if j & 1 == 1 {
                    new_line.push('#');
                } else {
                    new_line.push('.');
                }
                j >>= 1;
            } else {
                new_line.push(char);
            }
        }
        if group_matcher.is_match(&new_line) {
            matches += 1;
        }
    }
    return matches;
}

pub fn solve(shared: &mut Shared) -> String {
    let mut total = 0;
    let mut line_num = 0;
    let lines = shared.1.lines();
    let line_count = lines.clone().count();
    for line in lines {
        line_num += 1;
        println!("{} / {}", line_num, line_count);
        let mut parts = line.split_ascii_whitespace();
        let line = parts.next().unwrap();
        let group_matcher = parse_groups(parts.next().unwrap());
        total += mutations(line, group_matcher);
    }
    return total.to_string();
}