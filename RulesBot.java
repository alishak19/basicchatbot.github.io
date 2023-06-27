import javax.swing.*;

// basic rules-based chatbot code in Java, followed an initial tutorial and customized with knowledge of Java Swing library and basic ML mechanics

public class RulesBot extends JFrame {

    public RulesBot() {
        JFrame frame = new JFrame();
        frame.setDefaultCloseOperation(WindowConstants.EXIT_ON_CLOSE);
        frame.setVisible(true);
        frame.setResizable(true);
        frame.setLayout(null);

        frame.setSize(600, 600);

    }

    public static void main(String[] args) {
        new RulesBot();

    }
}

