port(
  clk,x: in std_logic;
  y:    out std_logic
);
architecture

type states  is (a,b,c,d);
signal actuSt, nextSt: states;

processWhat: process (actuSt,x) begin

  case actuSt is
    when a => 
      if x = '0' then
        nextSt <= d;
      else 
        nextSt <= b;

    when b => 
      if x = '0' then
        nextSt <= d;
      else 
        nextSt <= c;

    when c =>
      if x = '0' then
        nextSt <= d
        

end process processWhat;

end;