#include<bits/stdc++.h>
using namespace std;
const int MAX = 2 * 1e5 + 5;
int t , n , q;
int a[MAX];
set<int> S;

int Digit_Sum(int x)
{
    int ret = 0;
    while (x)
    {
        ret += x % 10;
        x /= 10;
    }
    return ret;
}

void Solve()
{
    // 한자릿수는 자릿수의 합을 계속해도 값이 똑같다.
    // a_i 값의 자릿수의 합이 가장 큰 경우는 999,999,999 이다.
    // 이때 자릿수의 합은 81이고 한 번 더 시행하면 최대는 16, 그리고 한 번 더 시행하면 최대 9이다
    // 따라서 자릿수의 합 연산을 3번 시행하면 무조건 한자릿수가 된다.
    // 즉 한자릿수가 아닌 값의 인덱스를 set 에 넣고 연산을 진행하면서 필요한 연산만 시행하게 한다.
    // 만약 set 이 아닌 배열을 사용하여 갱신을 진행하면 필요없는 연산이 생기지만
    // set 으로 한자릿수가 아닌 값들만 계속해서 넣고, 제거하는 연산을 계속하면
    // 꼭 필요한 연산만 발생하므로 시간복잡도를 효율적으로 관리할 수 있다.
    cin >> n >> q;
    for (int i = 0;i < n;i++)
    {
        cin >> a[i];
        if (a[i] > 9)
            S.insert(i);
    }
    while (q--)
    {
        int type; cin >> type;
        if (type == 1)
        {
            int l , r; cin >> l >> r; l-- , r--;
            int lst = l;
            while (!S.empty())
            {
                auto itr = S.lower_bound(lst);
                // 만약 검색 실패하거나, r를 넘어선 경우 탈출한다.
                if (itr == S.end() || *itr > r)
                    break;
                // 자릿수의 합으로 변경
                a[*itr] = Digit_Sum(a[*itr]);
                // tmp
                int nxt = *itr;
                // 이제 삭제
                S.erase(itr);
                // 만약 아직도 9보다 크다면 set에 삽입
                if (a[nxt] > 9)
                    S.insert(nxt);
                lst = nxt + 1;
            }
        }
        else
        {
            int x; cin >> x; x--;
            cout << a[x] << "\n";
        }
    }
}


int main()
{
    ios::sync_with_stdio(false);
    cin.tie(nullptr); cout.tie(0);
    cin >> t;
    while (t--)
        Solve();
}