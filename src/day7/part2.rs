use std::cmp::Ordering;
use std::collections::HashMap;
use crate::Shared;

#[derive(PartialEq, Eq, PartialOrd, Ord)]
enum Combo {
    HighCard,
    OnePair,
    TwoPair,
    ThreeOfAKind,
    FullHouse,
    FourOfAKind,
    FiveOfAKind
}

fn get_combo(value: String) -> Combo {
    let mut cards: HashMap<char, i32> = HashMap::new();
    for card in value.chars() {
        let mut count = cards.get(&card).unwrap_or(&0).clone();
        count += 1;
        cards.insert(card, count);
    }

    // remove jokers
    let count = cards.remove(&'J').unwrap_or(0);

    // get max count of a card
    let mut max_count = 0;
    for (_, count) in cards.clone() {
        if count > max_count {
            max_count = count;
        }
    }

    // add joker to max count
    max_count += count;

    match max_count {
        1 => Combo::HighCard,
        2 => {
            if cards.len() == 3 {
                Combo::TwoPair
            } else {
                Combo::OnePair
            }
        },
        3 => {
            if cards.len() == 2 {
                Combo::FullHouse
            } else {
                Combo::ThreeOfAKind
            }
        },
        4 => Combo::FourOfAKind,
        5 => Combo::FiveOfAKind,
        _ => panic!("Invalid card count")
    }
}

fn get_card_value(card: char) -> i32 {
    match card {
        'A' => 14,
        'K' => 13,
        'Q' => 12,
        'J' => 1,
        'T' => 10,
        _ => card.to_digit(10).unwrap() as i32
    }
}

fn sort_hands(a: &(Combo, String), b: &(Combo, String)) -> Ordering {
    let a_hand = a.1.split_ascii_whitespace().next().unwrap();
    let b_hand = b.1.split_ascii_whitespace().next().unwrap();

    return if a.0 != b.0 {
        a.0.cmp(&b.0)
    } else {
        // turn into numbers
        let a_hand_cards = a_hand.chars().map(|c| get_card_value(c)).collect::<Vec<i32>>();
        let b_hand_cards = b_hand.chars().map(|c| get_card_value(c)).collect::<Vec<i32>>();
        let val = a_hand_cards.cmp(&b_hand_cards);
        return val;
    }
}

pub fn solve(shared: &mut Shared) -> String {
    let values = shared.1.split("\n").collect::<Vec<&str>>();
    let mut v2 = values.iter().map(|v| (get_combo(v.split_ascii_whitespace().next().unwrap().to_string()), v.to_string())).collect::<Vec<(Combo, String)>>();
    v2.sort_by(|a, b| sort_hands(a, b));
    v2.reverse();
    let mut winning = 0;
    for (idx, value) in v2.iter().enumerate() {
        let rank = values.len() - idx;
        // get bid
        let bid = value.1.split_ascii_whitespace().last().unwrap().parse::<i32>().unwrap();
        winning += rank as i32 * bid;
    }

    return winning.to_string();
}