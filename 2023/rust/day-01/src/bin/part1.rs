fn main() {
    let input = include_str!("./input1.txt");
    let output = part1(input);
    dbg!(output);
}

fn part1(input: &str) -> String {
    let total: u32 = input
        .lines()
        .map(|line| {
            let mut it = line.chars().filter_map(|c| c.to_digit(10));
            let first = it.next().expect("no digits in line");
            match it.last() {
                Some(last) => 10 * first + last,
                None => 10 * first + first, // line contains only one digit
            }
        })
        .sum();

    total.to_string()
}

#[cfg(test)]
mod tests {
    use super::*;

    #[test]
    fn test() {
        let result = part1(
            "1abc2
pqr3stu8vwx
a1b2c3d4e5f
treb7uchet",
        );
        let expected = "142".to_string();
        assert_eq!(result, expected);
    }
}
