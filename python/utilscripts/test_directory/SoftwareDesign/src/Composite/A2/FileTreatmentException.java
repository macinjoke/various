package Composite.A2;

public class FileTreatmentException extends RuntimeException {      // RuntimeExceptionで正しいか？
    public FileTreatmentException() {
    }
    public FileTreatmentException(String msg) {
        super(msg);
    }
}
