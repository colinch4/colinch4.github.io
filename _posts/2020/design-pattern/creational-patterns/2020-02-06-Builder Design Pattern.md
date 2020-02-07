---
layout: post
title: "Builder Design Pattern"
description: "Separate the construction of a complex object from its representation so that the same construction process can create different representations. Parse a complex representation, create one of several targets."
date: 2020-02-06 13:04
tags: [디자인패턴]
comments: true
share: true
---

/ [Design Patterns](../2020-02-06-Design%20Patterns.md) / [Creational patterns](./2020-02-06-Creational%20patterns.md)

### Intent

-   Separate the construction of a complex object from its representation so that the same construction process can create different representations.
-   Parse a complex representation, create one of several targets.

### Problem

An application needs to create the elements of a complex aggregate. The specification for the aggregate exists on secondary storage and one of many representations needs to be built in primary storage.

### Discussion

Separate the algorithm for interpreting (i.e. reading and parsing) a stored persistence mechanism (e.g. RTF files) from the algorithm for building and representing one of many target products (e.g. ASCII, TeX, text widget). The focus/distinction is on creating complex aggregates.

The "director" invokes "builder" services as it interprets the external format. The "builder" creates part of the complex object each time it is called and maintains all intermediate state. When the product is finished, the client retrieves the result from the "builder".

Affords finer control over the construction process. Unlike creational patterns that construct products in one shot, the Builder pattern constructs the product step by step under the control of the "director".

### Structure

The Reader encapsulates the parsing of the common input. The Builder hierarchy makes possible the polymorphic creation of many peculiar representations or targets.

![Scheme of Builder](https://sourcemaking.com/files/v2/content/patterns/Builder.png)

### Example

The Builder pattern separates the construction of a complex object from its representation so that the same construction process can create different representations. This pattern is used by fast food restaurants to construct children's meals. Children's meals typically consist of a main item, a side item, a drink, and a toy (e.g., a hamburger, fries, Coke, and toy dinosaur). Note that there can be variation in the content of the children's meal, but the construction process is the same. Whether a customer orders a hamburger, cheeseburger, or chicken, the process is the same. The employee at the counter directs the crew to assemble a main item, side item, and toy. These items are then placed in a bag. The drink is placed in a cup and remains outside of the bag. This same process is used at competing restaurants.

![Example of Builder](https://sourcemaking.com/files/v2/content/patterns/Builder_example1.png)

### Check list

1.  Decide if a common input and many possible representations (or outputs) is the problem at hand.
2.  Encapsulate the parsing of the common input in a Reader class.
3.  Design a standard protocol for creating all possible output representations. Capture the steps of this protocol in a Builder interface.
4.  Define a Builder derived class for each target representation.
5.  The client creates a Reader object and a Builder object, and registers the latter with the former.
6.  The client asks the Reader to "construct".
7.  The client asks the Builder to return the result.

### Rules of thumb

-   Sometimes creational patterns are complementary: Builder can use one of the other patterns to implement which components get built. Abstract Factory, Builder, and Prototype can use Singleton in their implementations.
-   Builder focuses on constructing a complex object step by step. Abstract Factory emphasizes a family of product objects (either simple or complex). Builder returns the product as a final step, but as far as the Abstract Factory is concerned, the product gets returned immediately.
-   Builder often builds a Composite.
-   Often, designs start out using Factory Method (less complicated, more customizable, subclasses proliferate) and evolve toward Abstract Factory, Prototype, or Builder (more flexible, more complex) as the designer discovers where more flexibility is needed.


### Code 

#### Before

In this example we render a tabular data read from a file into a GUI table. The requirement of this job is to be able to pick a different GUI implementation in run time.

This is the code BEFORE we applied the Builder pattern.

Note: for the sake of simplicity of comparison between BEFORE and AFTER, we have made all important classes internal, so that they can live together in one file. This is not a pattern limitation.

```java
public class TableBuilderDemo {

    public static void main(String[] args) {
        (new TableBuilderDemo()).demo(args);
    }

    /**
     * Client code perspective.
     */
    public void demo(String[] args) {
        // Name of the GUI table class can be passed to the app parameters.
        String class_name = args.length > 0 ?  args[0] : "JTable_Table";

        // Then we read the tabular data from file...
        String file_name = getClass().getResource("../BuilderDemo.dat").getFile();
        String[][] matrix = read_data_file(file_name);

        // ..and pass it to specific GUI creator, which knows what GUI
        // component to create and how to initialize it.
        Component comp;
        if (class_name.equals("GridLayout_Table")) {
            comp = new GridLayout_Table(matrix).get_table();
        } else if (class_name.equals("GridBagLayout_Table")) {
            comp = new GridBagLayout_Table(matrix).get_table();
        } else {
            comp = new JTable_Table(matrix).get_table();
        }

        // Finally, create a GUI window and put there our table component.
        JFrame frame = new JFrame("BuilderDemo - " + class_name);
        frame.setDefaultCloseOperation(JFrame.EXIT_ON_CLOSE);
        frame.getContentPane().add(comp);
        frame.pack();
        frame.setVisible(true);
    }

    class JTable_Table {
        private JTable m_table;

        public JTable_Table(String[][] matrix) {
            m_table = new JTable(matrix[0].length, matrix.length);

            TableModel model = m_table.getModel();
            for (int i = 0; i < matrix.length; ++i)
                for (int j = 0; j < matrix[i].length; ++j)
                    model.setValueAt(matrix[i][j], j, i);
        }

        public Component get_table() {
            return m_table;
        }
    }

    class GridLayout_Table {
        private JPanel m_table = new JPanel();

        public GridLayout_Table(String[][] matrix) {
            m_table = new JPanel();
            m_table.setLayout(new GridLayout(matrix[0].length, matrix.length));
            m_table.setBackground(Color.white);

            for (int i = 0; i < matrix[i].length; ++i)
                for (int j = 0; j < matrix.length; ++j)
                    m_table.add(new Label(matrix[j][i]));
        }

        public Component get_table() {
            return m_table;
        }
    }

    class GridBagLayout_Table {
        private JPanel m_table = new JPanel();

        public GridBagLayout_Table(String[][] matrix) {
            GridBagConstraints c = new GridBagConstraints();

            m_table.setLayout(new GridBagLayout());
            m_table.setBackground(Color.white);

            for (int i = 0; i < matrix.length; ++i)
                for (int j = 0; j < matrix[i].length; ++j) {
                    c.gridx = i;
                    c.gridy = j;
                    m_table.add(new Label(matrix[i][j]), c);
                }
        }

        public Component get_table() {
            return m_table;
        }
    }

    public static String[][] read_data_file(String file_name) {
        String[][] matrix = null;
        try {
            BufferedReader br = new BufferedReader(new FileReader(file_name));
            String line;
            String[] cells;

            if ((line = br.readLine()) != null) {
                cells = line.split("\\t");
                int width = Integer.parseInt(cells[0]);
                int height = Integer.parseInt(cells[1]);
                matrix = new String[width][height];
            }

            int row = 0;
            while ((line = br.readLine()) != null) {
                cells = line.split("\\t");
                for (int i = 0; i < cells.length; ++i) {
                    matrix[i][row] = cells[i];
                }
                row++;France
            }
            br.close();
        } catch (Exception ex) {
            ex.printStackTrace();
        }
        return matrix;
    }
}
```
  
  

#### After

The  `main()`  creates a reader/parser, and configures it with a builder (an object that implements a standard interface and knows how to create one of many possible "results". The reader reads and parses the common input and delegates the construction to the configured builder.

This implementation demonstrates the spirit of the Builder pattern, but it is more intricate, and probably cannot be justified for this fairly limited context.

```java
public class TableBuilderDemo {

    public static void main(String[] args) {
        (new TableBuilderDemo()).demo(args);
    }

    /**
     * Client code perspective.
     */
    public void demo(String[] args) {
        // Name of the GUI table class can be passed to the app parameters.
        String class_name = args.length > 0 ? args[0] : "JTable_Builder";

        Builder target = null;
        try {
            target = (Builder) Class.forName(getClass().getName() + "$" + class_name)
                    .getDeclaredConstructor().newInstance();
        } catch (Exception ex) {
            ex.printStackTrace();
        }

        String file_name = getClass().getResource("../BuilderDemo.dat").getFile();
        TableDirector director = new TableDirector(target);
        director.construct(file_name);
        Component comp = target.get_result();

        JFrame frame = new JFrame("BuilderDemo - " + class_name);
        frame.setDefaultCloseOperation(JFrame.EXIT_ON_CLOSE);
        frame.getContentPane().add(comp);
        frame.pack();
        frame.setVisible(true);
    }

    interface Builder {
        void set_width_and_height(int width, int height);

        void start_row();

        void build_cell(String value);

        Component get_result();
    }

    public static class JTable_Builder implements Builder {
        private JTable m_table;
        private TableModel m_model;
        private int x = 0, y = 0;

        public void set_width_and_height(int width, int height) {
            m_table = new JTable(height, width);
            m_model = m_table.getModel();
        }

        public void start_row() {
            x = 0;
            ++y;
        }

        public void build_cell(String value) {
            m_model.setValueAt(value, y, x++);
        }

        public Component get_result() {
            return m_table;
        }
    }

    public static class GridLayout_Builder implements Builder {
        private JPanel m_panel = new JPanel();

        public void set_width_and_height(int width, int height) {
            m_panel.setLayout(new GridLayout(height, width));
            m_panel.setBackground(Color.white);
        }

        public void start_row() {
        }

        public void build_cell(String value) {
            m_panel.add(new Label(value));
        }

        public Component get_result() {
            return m_panel;
        }
    }

    public static class GridBagLayout_Builder implements Builder {
        private JPanel m_panel = new JPanel();
        private GridBagConstraints c = new GridBagConstraints();
        private int x = 0, y = 0;

        public void set_width_and_height(int width, int height) {
            m_panel.setLayout(new GridBagLayout());
            m_panel.setBackground(Color.white);
        }

        public void start_row() {
            x = 0;
            ++y;
        }

        public void build_cell(String value) {
            c.gridx = x++;
            c.gridy = y;
            m_panel.add(new Label(value), c);
        }

        public Component get_result() {
            return m_panel;
        }
    }

    class TableDirector {
        private Builder m_builder;

        public TableDirector(Builder b) {
            m_builder = b;
        }

        public void construct(String file_name) {
            try {
                BufferedReader br = new BufferedReader(new FileReader(file_name));
                String line;
                String[] cells;

                if ((line = br.readLine()) != null) {
                    cells = line.split("\\t");
                    int width = Integer.parseInt(cells[0]);
                    int height = Integer.parseInt(cells[1]);
                    m_builder.set_width_and_height(width, height);
                }

                while ((line = br.readLine()) != null) {
                    cells = line.split("\\t");
                    for (int col = 0; col < cells.length; ++col) {
                        m_builder.build_cell(cells[col]);
                    }
                    m_builder.start_row();
                }

                br.close();
            } catch (Exception ex) {
                ex.printStackTrace();
            }
        }
    }
}
```