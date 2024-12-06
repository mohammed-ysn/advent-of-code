package main

import "testing"

func TestPart1(t *testing.T) {
	col1, col2, err := readInput("test.in")
	if err != nil {
		t.Fatal(err)
	}

	want := 11
	got := part1(col1, col2)

	if got != want {
		t.Errorf("got %d, want %d", got, want)
	}
}

func TestPart2(t *testing.T) {
	col1, col2, err := readInput("test.in")
	if err != nil {
		t.Fatal(err)
	}

	want := 31
	got := part2(col1, col2)

	if got != want {
		t.Errorf("got %d, want %d", got, want)
	}
}
