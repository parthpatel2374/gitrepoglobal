public class overloadingdemo{
	public static void main(String args[]){
		System.out.println("Sum of two integers   ");
		sum(10, 20);
		System.out.println("Sum of two double numbers   ");
		sum(10.5, 20.4);
		System.out.println("Sum of two three integers   ");
		sum(10, 20, 30);
	}
	public static void sum(int num1, int num2){
		int ans;
		ans = num1+num2;
		System.out.println(ans);
	}
	public static void sum(double num1, double num2){
		double ans;
		ans = num1+num2;
		System.out.println(ans);
	}
	public static void sum(int num1, int num2, int num3){
		int ans;
		ans = num1+num2+num3;
		System.out.println(ans);
	}
}