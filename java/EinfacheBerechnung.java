/* EinfacheBerechnung.java */

import java.util.Scanner;

public class EinfacheBerechnung {
	public static void main (String[] args) {
		System.out.println("Gib die erste Zahl ein: ");
		Scanner one = new Scanner(System.in);
		int zahl1 = one.nextInt();
		
		System.out.println("Gib den Operator (+, -, *, /) ein: ");
		Scanner op = new Scanner(System.in);
		String operator = op.nextLine();
		
		// System.out.println(operator);
		
		System.out.println("Gib die zweite Zahl ein: ");
		Scanner two = new Scanner(System.in);
		int zahl2 = two.nextInt();
		
		int ergebnis = 0;
		// String plus = "+";
		// String minus = "-";
		// String multiply = "*";
		// String divide = "/";
		
		if (operator == "+") {
			ergebnis = zahl1 + zahl2;
		} else if (operator == "-") {
			ergebnis = zahl1 - zahl2;
		} else if (operator == "*") {
			ergebnis = zahl1 * zahl2;
		} else if (operator == "/") {
			ergebnis = zahl1 / zahl2;
		} else {
			System.out.println("Es wurde kein gültiger Operator eingegeben.");
		}
		
		System.out.println("Das Ergebnis ist: " + ergebnis);
	}
}
