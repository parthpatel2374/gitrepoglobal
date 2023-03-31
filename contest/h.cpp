#include<bits/stdc++.h>
using namespace std;
int main(){

    int times;
    cin >> times;

    for(int i=0; i<times; i++){
        int len;
        cin >> len;

        int arr[len];
        for(int i=0; i<len; i++){
            arr[i] = i+1;
        }
        int k=len;
        for(int i=0; i<k; i++){
            int min=arr[0], max=arr[k];
            int dif = max-min;
            for(int i=0; i<k; i++){
                arr[i]=arr[i+1];
            }
            arr[]
            k--;
        }
    }
}