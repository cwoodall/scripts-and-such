module grey_code_counter_TEST();
   reg clk;
   wire [2:0] count;

   grey_code_counter Counter(clk, count);

   initial begin
	  $dumpvars;
	  
	  $display(" clk | count ");
	  $monitor(" %b | %b ", clk, count);
	  
	  clk = 0;
	  #100
		repeat (20) begin
		   #10 clk <= ~clk;
		end
   end
endmodule // u_test

module grey_code_counter(clk, count);
   input clk; // Input clock line
   output [2:0] count;

   wire 		clk;
   reg [2:0] 	i_count; // Internal count register 	
   reg [2:0] 	count;   // what the outside world sees

   initial
	 begin
		count <= 3'b000;
	 end

   always @ (posedge clk)
	 begin
		case (count)
		  3'b000: count = 3'b001;
		  3'b001: count = 3'b011;
		  3'b010: count = 3'b110;
		  3'b011: count = 3'b010;
		  3'b100: count = 3'b000;
		  3'b101: count = 3'b100;
		  3'b110: count = 3'b111;
		  3'b111: count = 3'b101;
		  default: count = 3'bxxx;
		endcase // case (count)
	 end // always @ (posedge clk)
   
endmodule // grey_code_counter
