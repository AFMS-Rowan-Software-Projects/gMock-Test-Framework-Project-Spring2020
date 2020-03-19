#include<iostream>
using namespace std;

#include"Service.h"

Service * first = new Service();

int getCommand(){
    cout<<"Choose one of the following commands: "<<endl;
    cout<<"1. Add new service"<<endl;
    cout<<"2. Add new subservice"<<endl;
    cout<<"3. Add parent to a service"<<endl;
    cout<<"4. Delete a service(and it's subservices)"<<endl;
    cout<<"Your Choice: ";
    int c;
    cin>>c;
    return c;
}
void addService(){
    first->add();
}

void addSubService(){
    cout<<"Let's choose the parent first: "<<endl;
    int * one = new int;
    *one = 1;
    first->print(one,0);
    cout<<"0. here."<<endl<<"> ";
    int id;
    cin>>id;
    Service * f = first->find(one,id);

}

void addParentToService(){

}

void doCommand(int c){
    switch(c){
    case 1:
        addService();
        break;
    case 2:
        addSubService();
        break;
    case 3:
        addParentToService();
        break;
    case 4:
        //deleteService();
        break;
    }
}