

public class bingoLirikKonstruktor {
    public static void main (String[] args){
        bingoLirik satu = new bingoLirik("B-I-N-G-O");
        bingoLirik dua = new bingoLirik("(clap)-I-N-G-O");
        bingoLirik tiga = new bingoLirik("(clap)-(clap)-N-G-O");
        bingoLirik empat = new bingoLirik("(clap)-(clap)-(clap)-G-O");
        bingoLirik lima = new bingoLirik("(clap)-(clap)-(clap)-(clap)-O");
        bingoLirik enam = new bingoLirik("(clap)-(clap)-(clap)-(clap)-(clap)");
        
        satu.lirikLagu();
        dua.lirikLagu();
        tiga.lirikLagu();
        empat.lirikLagu();
        lima.lirikLagu();
        enam.lirikLagu();
    }
}
