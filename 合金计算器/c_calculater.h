#include <iostream>
#include <string>
using namespace std;

#ifndef _Calculater
#define _Calculater

struct Metal
{
    string name;
    int content;
    int quantity;
    float lowerLimit;
    float upperLimit;
};


'class Metal
{
private:
    string name;
    int content;
    int quantity;

public:
    Metal(istream &is);
    Metal(const string &n, const int &c, const int &q);
    Metal()
    {
        name = "";
        content = 0;
        quantity = 0;
    }
    void Init(const string &n, const int &c, const int &q)
    {
        name = n;
        content = c;
        quantity = q;
    }
    string nameIs() const { return name; }
    int contentIs() const { return content; }
    int quantityIs() const { return quantity; }
}'

#endif