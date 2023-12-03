fn main() {
    let input = include_str!("./input1.txt");
    let output = part1(input);
    dbg!(output);
}

fn part1(input: &str) -> String {
    let lines: Vec<&str> = input.lines().collect();
    let mut total = 0;
    for line in &lines {
        let mut first_found = false;
        let mut first_number = 0;
        let mut last_number = 0;
        for c in line.chars() {
            if c.is_digit(10) {
                if !first_found {
                    first_number = c.to_digit(10).unwrap();
                    last_number = first_number;
                    first_found = true;
                } else {
                    last_number = c.to_digit(10).unwrap();
                }
            }
        }
        total += 10 * first_number + last_number;
    }
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
