/* EinfacheBerechnung.java */

import java.util.Scanner;

public class EinfacheBerechnung {
	public static void main (String[] args) {
		Scanner nums = new Scanner(System.in);
		
		System.out.print("Gib die erste Zahl ein: ");
		int zahl1 = nums.nextInt();
		
		System.out.print("Gib den Operator (+, -, *, /) ein: ");
		Scanner op = new Scanner(System.in);
		String operator = op.nextLine();
		
		// System.out.println(operator);
		
		System.out.print("Gib die zweite Zahl ein: ");
		int zahl2 = nums.nextInt();
		
		int ergebnis = 0;
		
		if (operator.equals("+")) {
			ergebnis = zahl1 + zahl2;
		} else if (operator.equals("-")) {
			ergebnis = zahl1 - zahl2;
		} else if (operator.equals("*")) {
			ergebnis = zahl1 * zahl2;
		} else if (operator.equals("/")) {
			ergebnis = zahl1 / zahl2;
		} else {
			System.out.println("Es wurde kein gültiger Operator eingegeben.");
		}
		
		System.out.println("Das Ergebnis ist: " + ergebnis);
	}
}
