fn main() {
    let input = include_str!("./input1.txt");
    let output = part1(input);
    dbg!(output);
}

fn part1(input: &str) -> String {
    let total: u32 = input
        .lines()
        .map(|line| {
            // Use filter_map to extract digits from the line
            let digits: Vec<u32> = line.chars().filter_map(|c| c.to_digit(10)).collect();

            // Use pattern matching to get the first and last digits
            match digits.as_slice() {
                [] => 0,                                      // No digits found
                [num] => (10 * *num) + (*num),                // Only one digit found
                [first, .., last] => (10 * *first) + (*last), // More than one digit found
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
