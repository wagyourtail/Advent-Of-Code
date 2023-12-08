use std::collections::HashMap;
use crate::Shared;

pub fn traverse(next: (String, String), idx: i32, path: &str, nodes: HashMap<String, (String, String)>) -> i32 {

    // get next node id
    let rt = idx % path.len() as i32;

    let next_key = if path.chars().nth(rt as usize).unwrap() == 'L' {
        next.0
    } else {
        next.1
    };

    if next_key == "ZZZ" {
        return idx + 1;
    }

    let next_node = nodes.get(&next_key).unwrap();
    return traverse(next_node.clone(), idx + 1, path, nodes);
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

    let root = nodes.get("AAA").unwrap();

    return traverse(root.clone(), 0, path, nodes).to_string();
}