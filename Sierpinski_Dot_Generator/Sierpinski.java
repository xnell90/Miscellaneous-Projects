import java.util.Scanner;

public class Sierpinski {

  public static double[] midpoint(double x1, double y1, double x2, double y2) {
    double[] midPoint = new double[2];

    midPoint[0] = (double)(x1 + x2) / 2.0;
    midPoint[1] = (double)(y1 + y2) / 2.0;

    return midPoint;
  }

  public static void main(String[] args) {
    Scanner input = new Scanner(System.in);

    System.out.println("*******************Sierpinksi Generator************************");
    System.out.print("Enter Scale: ");
    double scale = input.nextDouble();

    System.out.print("Enter Number of Iterations: ");
    int iterations = input.nextInt();
    System.out.println("***************************************************************");

    StdDraw.setXscale(-scale - 1, scale + 1);
    StdDraw.setYscale(-scale - 1, scale + 1);
    StdDraw.clear(StdDraw.WHITE);
    StdDraw.enableDoubleBuffering();

    StdDraw.setPenColor(StdDraw.BLACK);
    StdDraw.setPenRadius(0.0125);
    //Draw Three Points (0,scale), (-scale, -scale), (scale, -scale)
    StdDraw.point(0, scale);
    StdDraw.point(-scale, -scale);
    StdDraw.point(scale, -scale);
    StdDraw.show();

    //Draw Initial Point (0,0)
    double[] current = {0, 0};
    StdDraw.point(current[0], current[1]);

    for(int i = 1; i <= iterations; i++) {
      double rand = Math.random();

      if(rand < 0.33333) {
        current = midpoint(current[0], current[1], 0, scale);
      }
      else if(rand < 0.66666) {
        current = midpoint(current[0], current[1], -scale, -scale);
      }
      else {
        current = midpoint(current[0], current[1], scale, -scale);
      }
      StdDraw.point(current[0], current[1]);
      System.out.printf("Current Position at iteration %d: (%.2f, %.2f)\n", i, current[0], current[1]);

      StdDraw.show();
      StdDraw.pause(40);

    }
  }

}
