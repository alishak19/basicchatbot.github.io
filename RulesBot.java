import javax.swing.*;

// simple rules-based chatbot code in Java, followed an initial tutorial, customizing with knowledge of Java Swing 

public class RulesBot extends JFrame {

    public RulesBot() {
        JFrame frame = new JFrame(); 
        frame.setDefaultCloseOperation(WindowConstants.EXIT_ON_CLOSE);
        frame.setVisible(true);
        frame.setResizable(true);
        frame.setLayout(null);

        frame.setSize(501, 500);

    }

    public static void main(String[] args) {
        new RulesBot();

    }
}

