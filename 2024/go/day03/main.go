package main

import (
	"bufio"
	"fmt"
	"os"
	"regexp"
	"strconv"
	"strings"
)

func main() {
	line, err := readInput("input.in")
	if err != nil {
		fmt.Println(err)
		os.Exit(1)
	}

	fmt.Println("Part 1:", part1(line))
	fmt.Println("Part 2:", part2(line))
}

func readInput(filename string) (string, error) {
	file, err := os.Open(filename)
	if err != nil {
		return "", err
	}
	defer file.Close()

	var sb strings.Builder

	scanner := bufio.NewScanner(file)
	for scanner.Scan() {
		sb.WriteString(scanner.Text())
	}

	if err := scanner.Err(); err != nil {
		return "", err
	}

	return sb.String(), nil
}

func part1(line string) int {
	pattern := `mul\((\d+),(\d+)\)`

	re := regexp.MustCompile(pattern)

	matches := re.FindAllStringSubmatch(line, -1)

	var sum int
	for _, match := range matches {
		// match[0] is the full string mul(x,y)
		xStr := match[1]
		yStr := match[2]

		x, _ := strconv.Atoi(xStr)
		y, _ := strconv.Atoi(yStr)

		sum += x * y
	}

	return sum
}

func part2(line string) int {
	pattern := `mul\((\d+),(\d+)\)|do\(\)|don't\(\)`

	re := regexp.MustCompile(pattern)

	matches := re.FindAllStringSubmatch(line, -1)

	enabled := true
	sum := 0

	for _, match := range matches {
		switch {
		case enabled && strings.HasPrefix(match[0], "m"):
			xStr := match[1]
			yStr := match[2]

			x, _ := strconv.Atoi(xStr)
			y, _ := strconv.Atoi(yStr)

			sum += x * y
		case match[0] == "do()":
			enabled = true
		case match[0] == "don't()":
			enabled = false
		}

	}

	return sum
}
