// Christopher Woodall
// MIT License
// October 7, 2011
//

module tester_tb();

   wire GT, LT, EQ;

   reg signed [2:0]	A, B;

   initial begin
	  $display(" A  | B  | GT | LT | EQ ");
	  
	  $monitor(" %d | %d | %b | %b | %b ", A, B, GT, LT, EQ);

	  A = 3'b000;
	  B = 3'b000;

	  #10
	  A = 3'b100;
	  B = 3'b000;

	  #10
		A = 3'b001;
	  B = 3'b001;

	  #10
		A = 3'b001;
	  B = 3'b010;

	  #10 A = 3'b001;
	  B = 3'b000;

	  #10 
		A = 3'b101;
	  B = 3'b110;

	  #10 B = 3'b100;
	  
	  #10 $finish;
   end // initial begin

   comparator_3bit_b U_Comparator(A, B, GT, LT, EQ);

endmodule // tester_tb



module comparator_3bit(A, B, GT, LT, EQ);
   input [2:0] A;
   input [2:0] B;
   output GT, LT, EQ;

   // Inputs
   wire [2:0] A;
   wire [2:0] B;
   
   // Temporary Wires
   wire [2:0] gt_t;
   wire [2:0] lt_t;
   wire [2:0] eq_t;

   wire [1:0] lt_w;
   wire [1:0] gt_w;
   
   // Outputs
   wire 		  GT, LT, EQ;

   comparator comp1(A[2], B[2], lt_t[2], gt_t[2], eq_t[2]);
   comparator comp2(A[1], B[1], gt_t[1], lt_t[1], eq_t[1]);
   comparator comp3(A[0], B[0], gt_t[0], lt_t[0], eq_t[0]);

   and(EQ, eq_t[2], eq_t[1], eq_t[0]);
   and(gt_w[1], eq_t[2], gt_t[1]);
   and(gt_w[0], eq_t[2], eq_t[1], gt_t[0]);
   or(GT, gt_w[1], gt_w[0], gt_t[2]);
   and(lt_w[1], eq_t[2], lt_t[1]);
   and(lt_w[0], eq_t[2], eq_t[1], lt_t[0]);
   or(LT, lt_t[2], lt_w[1], lt_w[0]);
   
endmodule // comparator_3bit

module comparator(a, b, gt, lt, eq);
   input a, b;
   output gt, lt, eq;

   wire   a, b, not_a, not_b; // Input wires
   wire 	  gt, lt, eq; // output wires

   // Negate Inputs
   not( not_a, a );
   not( not_b, b );
   
   // A == B
   xnor( eq, a, b );

   // A > B
   and( gt, a, not_b );

   // A < B
   and (lt, not_a, b);
endmodule //comparator