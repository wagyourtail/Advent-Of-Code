use std::ops::Range;
use crate::Shared;


fn getDistanceGtForTime(max_time: i64, min_distance: i64) -> i64 {
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

    // merge remaining lines
    let mut time = "".to_string();
    let mut dist = "".to_string();
    while times.peek().is_some() {
        time.push_str(times.next().unwrap());
        dist.push_str(distance.next().unwrap());
    }

    let time = time.parse::<i64>().unwrap();
    let dist = dist.parse::<i64>().unwrap();
    return getDistanceGtForTime(time, dist).to_string();
}