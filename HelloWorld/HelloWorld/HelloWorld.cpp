#include "pch.h"
#include <iostream>
#include <algorithm>
#include <climits>
#include <vector>
#include <math.h>
#include <cmath>
#include <set>

using namespace std;

int minimum = INT_MAX;
vector<pair<int, int>> optimal;
set<pair<int, int>> possibleMoves;
vector<vector<bool>> visited(9, vector<bool> (9, false));

void DFS(int i, int j, int times, vector<pair<int, int>> path) {
	if (times > 6) return;

	if (i == 8 && j == 8) {
		minimum = min(minimum, times);

		if (minimum == times) {
			optimal = path;
		}
		return;
	}

	times++;
	path.push_back(make_pair(i, j));
	visited[i][j] = true;

	for (auto k : possibleMoves) {
		if (i + k.first < 1 || j + k.second < 1) continue;
		if (i + k.first >= 9 || j + k.second>= 9) continue;
		if (visited[i + k.first][j + k.second]) continue;

		DFS(i + k.first, j + k.second, times, path);
	}
} 

void start() {
	possibleMoves.insert(make_pair(1, 2));
	possibleMoves.insert(make_pair(-1, 2));
	possibleMoves.insert(make_pair(-2, 1));
	possibleMoves.insert(make_pair(2, 1));

	possibleMoves.insert(make_pair(1, -2));
	possibleMoves.insert(make_pair(-1, -2));
	possibleMoves.insert(make_pair(-2, -1));
	possibleMoves.insert(make_pair(2, -1));
}

int main() {
	start();
	vector<pair<int, int>> input;
	DFS(1, 1, 0, input);

	cout << minimum << endl;

	for (auto i : optimal) {
		cout << i.first << " " << i.second << endl;
	}

	cout << "8 8" << endl;
}
