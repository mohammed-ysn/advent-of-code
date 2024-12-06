package main

import (
	"bufio"
	"fmt"
	"os"
	"sort"
	"strconv"
	"strings"
)

func main() {
	col1, col2, err := readInput("input.in")
	if err != nil {
		fmt.Println(err)
		os.Exit(1)
	}

	fmt.Println("Part 1:", part1(col1, col2))
	fmt.Println("Part 2:", part2(col1, col2))
}

func readInput(filename string) ([]int, []int, error) {
	file, err := os.Open(filename)
	if err != nil {
		return nil, nil, err
	}
	defer file.Close()

	var col1 []int
	var col2 []int

	scanner := bufio.NewScanner(file)
	for scanner.Scan() {
		line := scanner.Text()
		parts := strings.Fields(line)
		if len(parts) != 2 {
			return nil, nil, fmt.Errorf("invalid input: %s", line)
		}

		num1, err1 := strconv.Atoi(parts[0])
		num2, err2 := strconv.Atoi(parts[1])
		if err1 != nil || err2 != nil {
			return nil, nil, fmt.Errorf("invalid input: %s", line)
		}

		col1 = append(col1, num1)
		col2 = append(col2, num2)
	}

	if err := scanner.Err(); err != nil {
		return nil, nil, err
	}

	return col1, col2, nil
}

func part1(col1 []int, col2 []int) int {
	sort.Ints(col1)
	sort.Ints(col2)

	var sum int
	for i := 0; i < len(col1); i++ {
		sum += abs(col1[i], col2[i])
	}

	return sum
}

func abs(a, b int) int {
	if a > b {
		return a - b
	}
	return b - a
}

func part2(col1 []int, col2 []int) int {
	col2Counts := counts(col2)

	var sum int
	for i := 0; i < len(col1); i++ {
		val := col1[i]
		sum += val * col2Counts[val]
	}

	return sum
}

func counts(col []int) map[int]int {
	counts := make(map[int]int)
	for _, v := range col {
		counts[v]++
	}
	return counts
}
