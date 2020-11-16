#include "c_calculater.h"
#include <string>
string targetMetal;
int kindOfMetal;
Metal metalList[10];

void inputInformation(){
    cout << "How many kinds of metal:";
    cin >> kindOfMetal;
    cout << "Now input the submetals and please input the most important metal at first(eg. MetalName MetalContent MetalQuantity MetalLowerLimit MetalUpperLimit)" << endl;
    for (int i = 0; i < kindOfMetal; i++)
    {
        cout << "The metal " << i << ':';
        cin >> metalList[i].name >> metalList[i].content >> metalList[i].quantity >> metalList[i].lowerLimit >> metalList[i].upperLimit;
    }
}

void calculate(){
    switch(kindOfMetal){
        case 2:
        {
            int total = 0;
            int m1 = metalList[0].quantity;
            int m2 = metalList[1].quantity;
            
            for (int i = 0; i < metalList[0].quantity; i++)
                for(int j = 0; j < metalList[1].quantity; j++)
                {
                    int tot = i * metalList[0].content + j * metalList[1].content;
                    float part1 = i * metalList[0].content;
                    float part2 = j * metalList[1].content;
                    float percent1 = part1 / tot;
                    float percent2 = part2 / tot;
                    if(percent1 <= metalList[0].upperLimit && percent1 >= metalList[0].lowerLimit && percent2 <= metalList[1].upperLimit && percent2 >= metalList[1].lowerLimit && i < m1 && tot > total){
                        m1 = i;
                        m2 = j;
                    }
                }
                cout << "The best answer is:\n" 
                     << metalList[1].name << ": " << m1 << endl
                     << metalList[2].name << ": " << m2 << endl;
                break;
        }
        case 3:
        {
            break;
        }
        case 4:
        {
            break;
        }
    }
}

int main()
{
    inputInformation();
    calculate();
    return 0;
}