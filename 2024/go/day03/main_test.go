package main

import "testing"

func TestPart1(t *testing.T) {
	line, err := readInput("test1.in")
	if err != nil {
		t.Fatal(err)
	}

	want := 161
	got := part1(line)

	if got != want {
		t.Errorf("got %d, want %d", got, want)
	}
}

func TestPart2(t *testing.T) {
	line, err := readInput("test2.in")
	if err != nil {
		t.Fatal(err)
	}

	want := 48
	got := part2(line)

	if got != want {
		t.Errorf("got %d, want %d", got, want)
	}
}
