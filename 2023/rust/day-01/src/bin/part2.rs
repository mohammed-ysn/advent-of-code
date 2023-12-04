fn main() {
    let input = include_str!("./input2.txt");
    let output = part1(input);
    dbg!(output);
}

fn part1(input: &str) -> String {
    let total: u32 = input.lines().map(|line| process_line(line)).sum();

    total.to_string()
}

fn process_line(line: &str) -> u32 {
    let mut it = (0..line.len()).filter_map(|i| {
        let reduced_line = &line[i..];
        let result = if reduced_line.starts_with("one") {
            '1'
        } else if reduced_line.starts_with("two") {
            '2'
        } else if reduced_line.starts_with("three") {
            '3'
        } else if reduced_line.starts_with("four") {
            '4'
        } else if reduced_line.starts_with("five") {
            '5'
        } else if reduced_line.starts_with("six") {
            '6'
        } else if reduced_line.starts_with("seven") {
            '7'
        } else if reduced_line.starts_with("eight") {
            '8'
        } else if reduced_line.starts_with("nine") {
            '9'
        } else {
            reduced_line.chars().next().expect("no digit found")
        };

        result.to_digit(10)
    });
    let first = it.next().expect("no digits in line");
    match it.last() {
        Some(last) => 10 * first + last,
        None => 10 * first + first, // line contains only one digit
    }
}

#[cfg(test)]
mod tests {
    use super::*;

    #[test]
    fn test() {
        let result = part1(
            "two1nine
eightwothree
abcone2threexyz
xtwone3four
4nineeightseven2
zoneight234
7pqrstsixteen",
        );
        let expected = "281".to_string();
        assert_eq!(result, expected);
    }
}
