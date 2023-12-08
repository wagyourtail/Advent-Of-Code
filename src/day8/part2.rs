use std::collections::HashMap;
use crate::Shared;

// https://rustp.org/number-theory/lcm/
fn gcd(mut a:i64, mut b:i64) -> i64{
    if a==b { return a; }
    if b > a {
        let temp = a;
        a = b;
        b = temp;
    }
    while b>0 {
        let temp = a;
        a = b;
        b = temp%b;
    }
    return a;
}

fn lcm(a:i64, b:i64) -> i64{
    // LCM = a*b / gcd
    return a * (b/gcd(a,b));
}

pub fn traverse(mut next: (String, String), path: &str, nodes: HashMap<String, (String, String)>) -> i32 {

    // get next node id
    let mut idx = 0;
    loop {
        let rt = idx % path.len() as i32;

        let next_key = if path.chars().nth(rt as usize).unwrap() == 'L' {
            next.0.clone()
        } else {
            next.1.clone()
        };

        if next_key.ends_with('Z') {
            return idx + 1;
        }

        next = nodes.get(&next_key).unwrap().clone();
        idx += 1;
    }
}

pub fn solve(shared: &mut Shared) -> String {
    let mut lines = shared.1.lines();
    // get path
    let path = lines.next().unwrap();

    let mut nodes: HashMap<String, (String, String)> = HashMap::new();
    lines.next();
    for line in lines {
        let mut parts = line.split("=");
        let key = parts.next().unwrap().trim();
        let mut values: Vec<&str> = parts.next().unwrap().trim().split(",").collect::<Vec<&str>>();
        // remove ()
        values[0] = &values[0][1..].trim();
        values[1] = &values[1][..values[1].len() - 1].trim();
        // insert
        let node = (values[0].to_string(), values[1].to_string());
        nodes.insert(key.to_string(), node);
    }

    let roots = nodes.keys().filter(|k| k.ends_with('A')).collect::<Vec<&String>>();
    let mut values = Vec::new();
    for root in roots {
        println!("root: {}", root);
        let root = nodes.get(root).unwrap();
        values.push(traverse(root.clone(), path, nodes.clone()));
    }

    let mut val = values[0] as i64;
    for i in 1..values.len() {
        val = lcm(val, values[i] as i64);
    }

    return val.to_string();
}