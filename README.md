# Code Golf 2022 - NISER

## About
This repository contains a suite of solutions submitted for the Code Golf 2022 hackathon, an event hosted by the Coding Club at NISER. The goal of these entries was to solve a set of competitive programming challenges with the shortest possible source code. The project showcases a mix of Python and C++ implementations, balancing raw algorithmic efficiency with the concise, often unconventional syntax typical of code golf.

## Technical Details
The project is organized into directories corresponding to the contest problems (A through E). The implementation focuses on minimizing the character count of each solution while ensuring correctness against the problem constraints.

Key technical components include:
- Base Conversion: A utility in `gcd.py` that performs conversions between arbitrary bases by using a decimal intermediate: $n\text{-base} \rightarrow 10 \rightarrow m\text{-base}$.
- PDF Server: A lightweight Flask application (`index.py`) designed to dynamically list and serve the contest problem statements (PDFs) from the root directory.
- Length Tracking: A script (`count.py`) used to quantify the "golf" score by calculating the exact character length of the source files.
- Algorithmic Logic: Solutions cover a range of problems including palindrome generation, modular arithmetic, and boolean logic optimizations.

## Execution
- Python Solutions: Execute any `.py` file using a standard Python 3 interpreter:
  `python "C. Appy/appy2.py"`
- C++ Solutions: Compile using `g++` and run the resulting binary:
  `g++ "A. Palindrome/palindrome.cpp" -o palindrome && ./palindrome`
- Local Server: To host the problem documents locally, run the Flask server:
  `python index.py`
  (Note: Requires `flask` installed via pip).
- Character Count: To check the length of a specific file, edit the path in `count.py` and run:
  `python count.py`