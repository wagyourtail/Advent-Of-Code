use crate::Shared;

// numbers in string array var
const numbers: [&str; 10] = ["zero", "one", "two", "three", "four", "five", "six", "seven", "eight", "nine"];

pub fn solve(shared: &mut Shared) -> String {
    let mut result = 0;
    let s = shared.p1_input.clone();
    s.split("\n")
        .for_each(|line| {
            let mut first = false;
            let mut a = '0';
            let mut b = '0';
            for i in 0..line.len() {
                let c = line.chars().nth(i).unwrap();
                if c >= '0' && c <= '9' {
                    if !first {
                        a = c;
                        first = true;
                    }
                    b = c;
                }
                for j in 0..numbers.len() {
                    // length of entry
                    let len = numbers[j].len();
                    if (i + len) > line.len() {
                        continue;
                    }
                    if &line[i..i+len] == numbers[j] {
                        if !first {
                            a = (j as u8 + '0' as u8) as char;
                            first = true;
                        }
                        b = (j as u8 + '0' as u8) as char;
                    }
                }
            }
            // println!("{} {}", a, b);
            let mut str = String::new();
            str.push(a);
            str.push(b);
            result += str.parse::<i32>().unwrap();
        });
    return result.to_string();
}