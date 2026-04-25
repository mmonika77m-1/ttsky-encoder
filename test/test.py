# SPDX-FileCopyrightText: © 2024 Tiny Tapeout
# SPDX-License-Identifier: Apache-2.0

import cocotb
from cocotb.clock import Clock
from cocotb.triggers import ClockCycles


@cocotb.test()
async def test_parity_generator(dut):
    dut._log.info("Starting Parity Generator Test...")

    # Start a clock (not strictly needed if design is purely combinational,
    # but included for consistency with TinyTapeout template)
    cocotb.start_soon(Clock(dut.clk, 10, units="ns").start())

    # Reset and enable
    dut.ena.value = 1
    dut.rst_n.value = 0
    await ClockCycles(dut.clk, 5)
    dut.rst_n.value = 1
    await ClockCycles(dut.clk, 5)

    # Test all 16 combinations of ui_in[3:0]
    for val in range(16):
        dut.ui_in.value = val
        await ClockCycles(dut.clk, 2)

        # Expected even parity: XOR of all 4 bits
        bits = [(val >> i) & 1 for i in range(4)]
        expected_parity = bits[0] ^ bits[1] ^ bits[2] ^ bits[3]

        actual_parity = int(dut.uo_out.value) & 1

        assert actual_parity == expected_parity, (
            f"Parity mismatch: input={val:04b}, "
            f"expected={expected_parity}, got={actual_parity}"
        )

        dut._log.info(
            f"Input={val:04b} -> Parity={actual_parity} [PASS]"
        )
