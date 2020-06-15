#include <iostream>
#include <stack>
using namespace std;

class MyQueue{
public:
int numItems,sizes;
stack<int> s1;
stack<int> s2;
MyQueue(){
    sizes=20;
    numItems=0;
}
string enqueue(int item){
    if(numItems==sizes){
        return "Overflow";
    }
    s1.push(item);
    numItems++;

}
string retpop(int id){
    if(id==0){
        cout<<"Empty"<<endl;

    }
}
int dequeue(){
    if(numItems==0){
        retpop(0);
        return 0;
    }
    while(!s1.empty()){
        s2.push(s1.top());
        s1.pop();

    }
    int result=s2.top();
    s2.pop();
    while(!s2.empty()){
        s1.push(s2.top());
        s2.pop();
    }
    cout<<result<<endl;
    return result;
}

};

int main(){
    MyQueue que;
    que.dequeue();
    que.enqueue(4);
    que.enqueue(5);
    que.dequeue();
}
