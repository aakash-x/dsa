#include<iostream>
using namespace std;

class Node{
    public:
        int val;
        Node *prev;
        Node *next;
        Node(int val){
            this->val = val;
            prev = nullptr;
            next = nullptr;
        }
};

class LinkedList{
    public: 
        Node *head;
        Node *tail;
        LinkedList(){
            head = nullptr;
            tail = nullptr;
        }
        void add(int val){
            Node* new_node = new Node(val);
            if(!head ){
                head = new_node;
                tail = new_node;
                return;
            }
            head->prev = new_node;
            new_node->next = head;
            head = new_node;
        }
        void remove(Node *node){
            // removing from head
            if(node == head){
                head = head->next;
                if(head) head->prev = nullptr;
                else tail = nullptr;
            }
            // remove from tail
            else if(node == tail){
                tail = tail->prev;
                tail->next = nullptr;
            }
            // remove from the middle
            else{
                node->prev->next = node->next;
                node->next->prev = node->prev;
            }
            delete node;
        }
        // Print forward
        void displayForward() {
            Node* temp = head;
            cout << "Forward: ";
            while (temp) {
                cout << temp->val << " ";
                temp = temp->next;
            }
            cout << "\n";
        }

        // Print backward
        void displayBackward() {
            Node* temp = tail;
            cout << "Backward: ";
            while (temp) {
                cout << temp->val << " ";
                temp = temp->prev;
            }
            cout << "\n";
        }        
};

int main(int argc, char const *argv[])
{
    /* code */
    LinkedList ll;
    ll.add(2);
    ll.add(3);
    ll.displayForward();
    ll.displayBackward();
    ll.add(4);
    ll.remove(ll.head->next); // remove 3
    ll.displayForward();
    ll.displayBackward();
    return 0;
}
