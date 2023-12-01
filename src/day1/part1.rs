use crate::Shared;

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
            }
            // println!("{} {}", a, b);
            let mut str = String::new();
            str.push(a);
            str.push(b);
            result += str.parse::<i32>().unwrap();
        });
    return result.to_string();
}