use cached::proc_macro::cached;
use cached::UnboundCache;
use crate::Shared;

#[cached(
    type = "UnboundCache<String, i64>",
    create = "{ UnboundCache::new() }",
    convert = r#"{ format!("{}{}{}", known, nums.iter().map(|x| x.to_string()).collect::<Vec<String>>().join(","), consumed) }"#
)]
fn get_possible(known: &str, nums: &Vec<i64>, consumed: bool) -> i64 {
    if known.len() == 0 {
        return if nums.len() == 0 || (nums.len() == 1 && nums[0] == 0) {
            1
        } else {
            0
        }
    }
    let item = known.chars().nth(0).unwrap();
    if item == '?' {
        return get_possible(&format!("#{}", &known[1..]), nums, consumed) + get_possible(&format!(".{}", &known[1..]), nums, consumed);
    } else if item == '#' {
        if nums.len() == 0 {
            return 0;
        }
        return if nums[0] >= 1 {
            let mut new_nums = nums.clone();
            new_nums[0] -= 1;
            get_possible(&known[1..], &new_nums, true)
        } else {
            0
        }
    } else if item == '.' {
        if nums.len() == 0 {
            return get_possible(&known[1..], nums, false);
        }
        return if nums[0] == 0 {
            get_possible(&known[1..], &nums[1..].to_vec(), false)
        } else if !consumed {
            get_possible(&known[1..], nums, false)
        } else {
            0
        }
    }
    return 0;
}

pub fn solve(shared: &mut Shared) -> String {
    let mut total = 0;
    let mut line_num = 0;
    let lines = shared.1.lines();
    let line_count = lines.clone().count();
    for line in lines {
        line_num += 1;
        println!("{} / {}", line_num, line_count);
        let mut line = line.split(" ");
        let line_part = line.next().unwrap().to_string();
        let known = (0..5).map(|_| line_part.clone()).collect::<Vec<String>>().join("?");
        let nums = line.next().unwrap().split(",").map(|x| x.parse::<i64>().unwrap()).collect::<Vec<i64>>().repeat(5);
        total += get_possible(&known, &nums, false);
    }
    return total.to_string();
}