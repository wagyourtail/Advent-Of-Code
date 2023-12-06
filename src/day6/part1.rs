use std::ops::Range;
use crate::Shared;


fn getDistanceGtForTime(max_time: i32, min_distance: i32) -> i32 {
    // each second, speed doubles, starting at 0 for time 0
    // then remaining time is distance
    let mut count = 0;
    for time in 1..max_time {
        let distance = time * (max_time - time);
        if distance > min_distance {
            count += 1;
        }
    }
    return count;
}

pub fn solve(shared: &mut Shared) -> String {
    let mut values = shared.1.split("\n");
    let mut times = values.next().unwrap().split_ascii_whitespace().into_iter().peekable();
    let mut distance = values.next().unwrap().split_ascii_whitespace();

    // pop headers
    times.next();
    distance.next();

    let mut count = 1;
    while times.peek().is_some() {
        let time = times.next().unwrap().parse::<i32>().unwrap();
        let distance = distance.next().unwrap().parse::<i32>().unwrap();
        count *= getDistanceGtForTime(time, distance);
    }
    return count.to_string();
}