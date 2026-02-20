## Sequence and Series Analyzer

##Project Overview

This project aims to build a flexible python tool capable of analyzing sequences from either datasets or explicit formulas. The long term goal is to automatically detect patterns (arithmetic, geometric, and polynomial), then derive the corresponding equation when possible, and compute important values such as the Nth term and partial sums. 

##Current Version v1.0

The current implementation focuses on exact arithmetic and geometric sequence detection from user provided datasets. It validates input, handles large numbers with thousands of separators, and uses floating-point tolerant comparisons to ensure reliable detection. 

##Features

Parses datasets entered with spaces or commas

Supports thousands-formatted numbers (e.g., 1,000)

Detects arithmetic sequences (constant difference)

Detects geometric sequences (constant ratio)

Recognizes constant sequences (both arithmetic and geometric)

Computes nth term 𝑎𝑛
​
Computes partial sum 𝑆𝑛
​
Uses tolerance-based numeric comparisons


##Roadmap

Polynomial sequence detection via finite differences

Equation-input mode

Expanded model inference beyond exact arithmetic/geometric forms
