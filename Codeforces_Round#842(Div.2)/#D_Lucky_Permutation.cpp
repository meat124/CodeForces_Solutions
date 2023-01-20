#include<bits/stdc++.h>
using namespace std;
const int MAX = 200005;
int t , n;
int p[MAX] , parent[MAX];
bool vis[MAX];

void Input()
{
    cin >> n;
    for (int i = 1;i <= n;i++)
        cin >> p[i];
}

void Solve()
{
    int cnt = 0;
    for (int i = 1;i <= n;i++)
    {
        int nxt = i;
        if (!vis[nxt]) cnt++;
        while (!vis[nxt])
        {
            vis[nxt] = true;
            parent[nxt] = i;
            nxt = p[nxt];
        }
    }
    int result = n - cnt + 1;
    for (int i = 1;i < n;i++)
        if (parent[i] == parent[i + 1])
        {
            result = n - cnt - 1;
            break;
        }
    cout << result << "\n";
}

void Reset()
{
    fill(parent , parent + n + 1 , 0);
    fill(vis , vis + n + 1 , false);
}

int main()
{
    ios::sync_with_stdio(false);
    cin.tie(nullptr);
    cin >> t;
    while (t--)
    {
        Input();
        Solve();
        Reset();
    }
}