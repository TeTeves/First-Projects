import java.util.Scanner;

public class CalculadoraIMC {

	public static void main(String[] args) {
		Scanner leia = new Scanner(System.in);
		
		//variaveis
		
		int peso, altura;
		int imc;
		
		//entrada de dados
		
		do {
			System.out.println("Digite sua altura");
			altura = leia.nextFloat();
		if (altura > 250 || altura <= 0) {
			System.err.println("A altura não pode ser igual ou inferior a 0 e nem superior à 250cm");	
		}
		}while (altura > 250 || altura <= 0);
		
		do {
			System.out.println("Digite o seu peso");
			peso = leia.nextFloat();
		if (peso <=0) {
			System.err.println("o peso deve ser maior que 0");
		}
		}while(peso <= 0);
		imc = peso / (altura * altura);
		
		// resultados
		System.out.println(" O seu IMC é: " +imc);
	}

}
