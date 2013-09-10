import static org.junit.Assert.*;

import org.junit.Test;


public class GiaiPTB1Test {
	/**
	 * Test GiaiPTB1 voi a=1, b=1
	 * Ket qua mong muon x=-1
	 */
	@Test
	public void test1() {
		GiaiPTB1 num = new GiaiPTB1();
		assertEquals(-1, num.GiaiPTB1(1,1), 0);
	}
	
	/**
	 * Test GiaiPTB1 voi a=-10, b=90
	 * Ket qua mong muon x=9
	 */
	@Test
	public void test2() {
		GiaiPTB1 num = new GiaiPTB1();
		assertEquals(9, num.GiaiPTB1(-10,90), 0);
	}

}
