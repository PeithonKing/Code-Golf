#include <bits/stdc++.h>

using namespace std;

int main(){
	int t;
	cin >> t;
	while (t--){
		string f;
		cin >> f;
		string r = f;
		int n = f.length();
		for (int i = 0; i < n / 2; i++){
			r[n - 1 - i] = r[i];
		}

		if (r > f){
			cout << r << endl;
		}else{
			int mid = (n - 1) / 2;
			for (int i = mid; i >= 0; i--){
				if (r[i] != '9'){
					r[i] = r[i] + 1;
					break;
				}else{
					r[i] = '0';
				}
			}

			for (int i = n / 2; i < n; i++){
				r[i] = r[n - i - 1];
			}

			if (r[0] == '0'){
				r += '1';
				r[0] = '1';
			}
			cout << r << endl;
		}
	}
}