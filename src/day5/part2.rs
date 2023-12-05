use std::cmp::min;
use std::ops::Range;
use crate::Shared;

struct RangeMap {
    from: Range<i64>,
    to: Range<i64>
}

struct Almanac {
    seeds: Vec<Range<i64>>,
    ranges: Vec<Vec<RangeMap>>
}

fn parse_almanac(almanac: &String) -> Almanac {
    let mut seeds: Vec<Range<i64>> = Vec::new();
    let mut ranges: Vec<Vec<RangeMap>> = Vec::new();

    let mut lines = almanac.split('\n');
    // first line is the seeds

    // parse seeds
    let mut seed_iter = lines.next().unwrap().split(':').skip(1).next().unwrap().split_ascii_whitespace().into_iter().peekable();
    while seed_iter.peek().is_some() {
        let from = seed_iter.next().unwrap().parse::<i64>().unwrap();
        let len = seed_iter.next().unwrap().parse::<i64>().unwrap();
        seeds.push(from..from+len);
    }

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

    let mut result: i64 = i64::MAX;

    // find lowest end map for seeds
    for seed_orig in almanac.seeds {
        // map to last section
        let mut seed = Vec::new();
        let seed_len = seed_orig.end - seed_orig.start;
        seed.push(seed_orig);
        let mut seed_stack = Vec::new();
        seed_stack.push(seed.clone());


        for range_list in almanac.ranges.iter() {
            let mut seed_out = Vec::new();
            while !seed.is_empty() {
                let seed_range = seed.pop().unwrap();
                let mut else_ = true;
                for range in range_list {
                    // if range contains part of seed range
                    // contains start
                    if seed_range.start >= range.from.start && seed_range.start < range.from.end {
                        // push remainder of seed range
                        if seed_range.end > range.from.end {
                            seed.push(range.from.end..seed_range.end);
                        }
                        // get length of overlap
                        let overlap_len = min(seed_range.end - seed_range.start, range.from.end - seed_range.start);
                        let overlap_offset = seed_range.start - range.from.start;
                        // map seed to new range
                        seed_out.push(range.to.start + overlap_offset..range.to.start + overlap_offset + overlap_len);
                        else_ = false;
                        break;
                    }
                    // contains end
                    else if seed_range.end > range.from.start && seed_range.end <= range.from.end {
                        // push remainder of seed range
                        // this will always happen, or the first case would've been true
                        if seed_range.start < range.from.start {
                            seed.push(seed_range.start..range.from.start);
                        }
                        // get length of overlap
                        let overlap_len = min(seed_range.end - seed_range.start, seed_range.end - range.from.start);
                        let overlap_offset = seed_range.end - overlap_len - range.from.start;
                        // map seed to new range
                        seed_out.push(range.to.start + overlap_offset..range.to.start + overlap_offset + overlap_len);
                        else_ = false;
                        break;
                    }
                }
                // wasn't found in any range
                if else_ {
                    seed_out.push(seed_range);
                }
            }

            // check that length of output is the same as input
            let mut seed_out_len = 0;
            for seed_range in seed_out.iter() {
                seed_out_len += seed_range.end - seed_range.start;
            }

            if seed_out_len != seed_len {
                panic!("Seed length mismatch");
            }

            seed = seed_out.clone();
            seed_stack.push(seed.clone());
            seed_out.clear();
        }

        // find lowest end
        for seed_range in seed {
            if seed_range.start < result {
                result = seed_range.start;
            }
        }

    }

    return result.to_string();
}