package main

import "testing"

func TestPart1(t *testing.T) {
	reports, err := readInput("test.in")
	if err != nil {
		t.Fatal(err)
	}

	want := 2
	got := part1(reports)

	if got != want {
		t.Errorf("got %d, want %d", got, want)
	}
}

func TestPart1Ext(t *testing.T) {
	reports := [][]int{
		{},
		{1},
		{1, 2},
		{2, 1},
		{1, 2, 4},
		// Not safe
		{1, 1},
		{1, 2, 1},
		{1, 4, 1},
		{5, 4, 5},
	}

	want := 5
	got := part1(reports)

	if got != want {
		t.Errorf("got %d, want %d", got, want)
	}
}

func TestPart2(t *testing.T) {
	reports, err := readInput("test.in")
	if err != nil {
		t.Fatal(err)
	}

	want := 4
	got := part2(reports)

	if got != want {
		t.Errorf("got %d, want %d", got, want)
	}
}
