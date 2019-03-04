#include "pch.h"
#include <map>
#include <vector>
#include <iostream>
#include <algorithm>

using namespace std;
vector<int> arr;
vector<int> answer;
map<int, int> sameValues;

int findIndex(int i) { // O(N)
	int count = 0;

	for (int j = 0; j < (int)arr.size(); j++) {
		if (i == j) continue;

		if (arr[i] > arr[j]) {
			count++;
		}
	}

	return count;
}

int main(){
	int N;
	cin >> N;
	arr.assign(N, 0);
	answer.assign(N, 0);
	vector<int> index(N);

	for (int i = 0; i < N; i++) {
		cin >> arr[i];
		sameValues[arr[i]]++;
	}

	for (int i = 0; i < N; i++) { //calls N O(N) functions
		index[i] = findIndex(i);
	}

	for (int i = 0; i < N; i++) {
		answer[index[i]] = arr[i];

		if (sameValues[arr[i]] > 1) {
			for (int j = 1; j < sameValues[arr[i]]; j++) {
				answer[index[i] + j] = arr[i];
			}
		}
	}

	for (int i : answer) {
		cout << i << " ";
	}
	cout << endl;

	return 0;
}

// Run program: Ctrl + F5 or Debug > Start Without Debugging menu
// Debug program: F5 or Debug > Start Debugging menu

// Tips for Getting Started: 
//   1. Use the Solution Explorer window to add/manage files
//   2. Use the Team Explorer window to connect to source control
//   3. Use the Output window to see build output and other messages
//   4. Use the Error List window to view errors
//   5. Go to Project > Add New Item to create new code files, or Project > Add Existing Item to add existing code files to the project
//   6. In the future, to open this project again, go to File > Open > Project and select the .sln file
