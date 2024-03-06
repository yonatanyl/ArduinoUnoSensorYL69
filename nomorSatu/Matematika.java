public class Matematika {
    int hasilOperasi;
    double hasilBagi;

    public void pertambahan(int a, int b) {
        hasilOperasi = a + b;
        System.out.println("Pertambahan : " + a + " + " + b + " = " + hasilOperasi);
    }

    public void pengurangan(int a, int b) {
        hasilOperasi = a - b;
        System.out.println("Pengurangan : " + a + " - " + b + " = " + hasilOperasi);

    }

    public void perkalian(int a, int b) {
        hasilOperasi = a * b;
        System.out.println("Perkalian : " + a + " * " + b + " = " + hasilOperasi);

    }

    public void pembagian(int a, int b) {
        hasilBagi = a / b;
        System.out.println("Pembagian : " + a + " / " + b + " = " + hasilBagi);

    }
}
