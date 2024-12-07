package main

import (
	"bufio"
	"fmt"
	"os"
	"strconv"
	"strings"

	"github.com/mohammed-ysn/advent-of-code/2024/go/utils"
)

func main() {
	reports, err := readInput("input.in")
	if err != nil {
		fmt.Println(err)
		os.Exit(1)
	}

	fmt.Println("Part 1:", part1(reports))
	fmt.Println("Part 2:", part2(reports))
}

func readInput(filename string) ([][]int, error) {
	file, err := os.Open(filename)
	if err != nil {
		return nil, err
	}
	defer file.Close()

	var reports [][]int

	scanner := bufio.NewScanner(file)
	for scanner.Scan() {
		line := scanner.Text()
		parts := strings.Fields(line)

		var report []int
		for _, part := range parts {
			num, err := strconv.Atoi(part)
			if err != nil {
				return nil, err
			}
			report = append(report, num)
		}
		reports = append(reports, report)
	}

	if err := scanner.Err(); err != nil {
		return nil, err
	}

	return reports, nil
}

func part1(reports [][]int) int {
	var count int
	for _, report := range reports {
		if reportIsSafe(report) {
			count++
		} else {
		}
	}
	return count
}

func part2(reports [][]int) int {
	var count int
	for _, report := range reports {
		if reportIsSafe(report) || reportIsSafeTolerate(report) {
			count++
		}
	}
	return count
}

func reportIsSafe(report []int) bool {
	if len(report) <= 1 {
		return true
	}

	var isGoingUp bool
	if report[1] > report[0] {
		isGoingUp = true
	} else if report[1] < report[0] {
		isGoingUp = false
	} else {
		// Neither increase nor decrease - invalid
		return false
	}

	for i := 0; i < len(report)-1; i++ {
		diff := utils.AbsDiff(report[i], report[i+1])
		if diff < 1 || diff > 3 {
			return false
		}

		if isGoingUp {
			if report[i+1] < report[i] {
				return false
			}
		} else {
			if report[i+1] > report[i] {
				return false
			}
		}
	}

	return true
}

func reportIsSafeTolerate(report []int) bool {
	for i := 0; i < len(report); i++ {
		reportWithDel := append([]int{}, report[:i]...)
		reportWithDel = append(reportWithDel, report[i+1:]...)
		if reportIsSafe(reportWithDel) {
			return true
		}
	}
	return false
}
