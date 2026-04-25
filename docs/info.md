<!---
This file is used to generate your project datasheet. Please fill in the information below and delete any unused
sections.

You can also include images in this folder and reference them in the markdown. Each image must be less than
512 kb in size, and the combined size of all images must be less than 1 MB.
-->

## How it works

This design implements a simple **parity generator**.  
It takes the lower 4 input bits (`ui[0]`–`ui[3]`) and computes their **even parity** using XOR logic.  
The parity bit is then driven on output pin `uo[0]`.  

- If the number of 1s in the inputs is even → parity output = 0  
- If the number of 1s in the inputs is odd → parity output = 1  

All unused pins are tied to zero to avoid warnings.

## How to test

1. Drive values on `ui[0]`–`ui[3]`.  
2. Observe the parity bit on `uo[0]`.  
3. Verify that the output matches the XOR of the four input bits.  

For example:  
- Input `0000` → Output parity = 0  
- Input `0001` → Output parity = 1  
- Input `0110` → Output parity = 0  
- Input `1111` → Output parity = 0  

You can run the provided Cocotb testbench (`test/test.py`) to automatically check all 16 input combinations.

## External hardware

No external hardware is required.  
The design is purely combinational and self‑contained.
