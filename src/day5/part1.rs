use std::ops::Range;
use crate::Shared;

struct RangeMap {
    from: Range<i64>,
    to: Range<i64>
}

struct Almanac {
    seeds: Vec<i64>,
    ranges: Vec<Vec<RangeMap>>
}

fn parse_almanac(almanac: &String) -> Almanac {
    let mut seeds: Vec<i64> = Vec::new();
    let mut ranges: Vec<Vec<RangeMap>> = Vec::new();

    let mut lines = almanac.split('\n');
    // first line is the seeds

    // parse seeds
    lines.next().unwrap().split(':').skip(1).next().unwrap().split_ascii_whitespace().for_each(|seed| {
        seeds.push(seed.parse::<i64>().unwrap());
    });

    // parse ranges
    for line in lines {
        // is section header
        if line.contains(":") {
            ranges.push(Vec::new());
        } else if line.len() > 0 {
            let mut parts = line.split_ascii_whitespace();
            let to = parts.next().unwrap().parse::<i64>().unwrap();
            let from = parts.next().unwrap().parse::<i64>().unwrap();
            let len = parts.next().unwrap().parse::<i64>().unwrap();
            ranges.last_mut().unwrap().push(RangeMap {
                from: from..from+len,
                to: to..to+len,
            });
        }
    }

    return Almanac {
        seeds,
        ranges
    };
}

pub fn solve(shared: &mut Shared) -> String {
    let almanac = parse_almanac(&shared.1);
    // parsing done

    let mut results: Vec<i64> = Vec::new();

    // find lowest end map for seeds
    for seed in almanac.seeds {
        // map to last section
        let mut seed = seed;
        for range_list in almanac.ranges.iter() {
            for range in range_list {
                // if range contains seed
                if seed >= range.from.start && seed < range.from.end {
                    // map seed to new range
                    seed = range.to.start + (seed - range.from.start);
                    break;
                }
            }
        }
        results.push(seed);
    }

    return results.iter().reduce(|a, b| {
        if a < b {
            a
        } else {
            b
        }
    }).unwrap().to_string();
}