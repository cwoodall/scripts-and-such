VERILOGEX = .v # Verilog file extension

VERILOG_CMD = iverilog # iverilog config
VVP_CMD = VVP # VVP (iverilog runtime engine)
WAVEFORM_VIEWER = gtkwave

test :
	$(VERILOG_CMD) *.v
	$(VVP_CMD) *.out
	$(WAVEFORM_VIEWER) dump.vcd