/*
 * Copyright (c) 2024 Your Name
 * SPDX-License-Identifier: Apache-2.0
 */

`default_nettype none

module tt_um_parity_generator (
    input  wire [7:0] ui_in,    // Dedicated inputs
    output wire [7:0] uo_out,   // Dedicated outputs
    input  wire [7:0] uio_in,   // IOs: Input path
    output wire [7:0] uio_out,  // IOs: Output path
    output wire [7:0] uio_oe,   // IOs: Enable path
    input  wire       ena,      // enable
    input  wire       clk,      // clock
    input  wire       rst_n     // reset_n
);

  // Generate even parity for ui_in[3:0]
  wire parity_bit = ui_in[0] ^ ui_in[1] ^ ui_in[2] ^ ui_in[3];

  // Drive parity bit on uo_out[0], rest tied to 0
  assign uo_out  = {7'b0000000, parity_bit};
  assign uio_out = 0;
  assign uio_oe  = 0;

  // Prevent unused warnings
  wire _unused = &{ena, clk, rst_n, uio_in, ui_in[7:4], 1'b0};

endmodule
