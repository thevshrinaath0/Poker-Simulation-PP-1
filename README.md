# Roulette Wheel Simulator 🎲

[![Python CI](https://github.com/thevshrinaath0/Poker-Simulation-PP-1/actions/workflows/CI.yml/badge.svg)](https://github.com/thevshrinaath0/Poker-Simulation-PP-1/actions/workflows/CI.yml)

A **command-line Python simulator** for a European roulette wheel, built as a portfolio project to demonstrate Python programming, CLI development, testing, and CI/CD practices.

---

## Table of Contents

- [About](#about)
- [Features](#features)
- [Installation](#installation)
- [Usage](#usage)
- [Testing](#testing)
- [Tech Stack](#tech-stack)
- [Contributing](#contributing)
- [License](#license)

---

## About

This project simulates spins of a European roulette wheel (numbers 0–36) and provides statistical outputs for the spins, including:

- Color distribution (red, black, green)  
- Counts of numbers per color  
- Top spun numbers  

It’s designed to be run from the command line using Python and `click` for easy CLI interaction. This project also integrates **continuous integration (CI)** via GitHub Actions to automatically run tests on every push.

---

## Features

- Simulate any number of roulette spins
- Filter results by color (red, black, green, or all)
- Display top spun numbers and color distributions
- Fully tested with `pytest`
- Automated CI using GitHub Actions

---

## Installation

Clone the repository:

```bash
git clone https://github.com/thevshrinaath0/Poker-Simulation-PP-1.git
cd Poker-Simulation-PP-1
