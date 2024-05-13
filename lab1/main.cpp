#include <iostream>
#include <fstream>
#include <cmath>

class Cone {
private:
    double m, h0, x, v, h, ro, alpha, rozh, f, g;
public:
    Cone(double x, double v, double h, double ro, double alpha, double rozh, double f, double g): x(x), v(v), h(h), ro(ro), alpha(alpha), rozh(rozh), f(f), g(g) {
        m = (M_PI*ro/3)*pow(tan(alpha), 2)*pow(h, 3);
        h0 = h*cbrt(ro/rozh);
    }
    double calculated2xd2t( double x, double v) {
        return -g + ((M_PI*pow(tan(alpha), 2)*pow(h0-x, 2))/m)*((rozh*g/3)*(h0-x)-f*v/sin(alpha));
    }
    void moving(double dt) {
        double d2xd2t = calculated2xd2t(x, v);
        x += v*dt;
        v += d2xd2t*dt;
    }
    double getPosition() const { return x; }
    double getSpeed() const { return v; }
};


int main() {
    Cone cone(0.1, 0.0, 0.25, 500, 30*M_PI/180, 1000, 15, 9.8);
    std::ofstream file;
    file.open("output.csv");
    file << "Time,Position,Speed\n";
    const double dt = 0.001; 
    const double t_max = 10.0;

    for (double t = 0.0; t <= t_max; t += dt) {
        cone.moving(dt);
        file << t << "," << cone.getPosition() << "," << cone.getSpeed() << std::endl;
    }
    file.close();
    return 0;
}
