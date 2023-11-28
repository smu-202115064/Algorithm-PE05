#include <cstdio>

#define MAX_N 14
#define MAX_K 14

int memoize[MAX_N + 1][MAX_K + 1];
int T;
int n;
int k;

int main()
{
    /**
     * @brief Memoization 으로 풀이.
     * N과 K의 상한이 14로 크지 않으므로, 나올 수 있는 모든 (N, K) 쌍을 담을 배열을 선언할 공간이 존재한다.
     * 모든 경우의 수를 미리 구해두고 답을 출력만 하자.
     *
     * 문제의 이름을 '부녀회장' 앞 글자를 따서 BNHJ이라고 하자.
     * a층의 b호에 사는 사람의 수가 BNHJ(a, b) 일 때, 다음의 점화식을 세울 수 있다.
     *
     * if (a > 0)
     *  BNHJ(a, b) = BNHJ(a-1, 0) + BNHJ(a-1, 1) + ... + BNHJ(a-1, b-1) + BNHJ(a-1, b)
     * otherwise
     *  BNHJ(0, b) = b
     *
     * 만약 b가 1보다 크다면, BNHJ(a, b)는 다음과 같이 표현도 가능하다.
     *  BNHJ(a, b) = BNHJ(a-1, 0) + BNHJ(a-1, 1) + ... + BNHJ(a-1, b-1) + BNHJ(a-1, b)
     *             = BNHJ(a, b-1) + BNHJ(a-1, b)
     *
     * 그렇다면, a = 0 일 때와, b = 1일 때의 BNHJ(a, b)를 모두 구해놓고
     * 나머지는 BNHJ(a, b) = BNHJ(a, b-1) + BNHJ(a-1, b) 식으로 구한다면,
     * a와 b에 대한 2중 반복문으로 간단하게 모든 BNHJ(a, b)를 구할 수 있을 것이다.
     *
     *
     * 이 때, 시간 복잡도는 O(NK+T) 가 된다.
     * 최초에 미리 모든 문제의 답을 구하는 데에 O(NK) 가 걸리고,
     * 각 테스트케이스마다 미리 구해둔 값을 랜덤 액세스하여 읽어오기만 하면 되므로,
     * 상수시간에 풀이가 가능하여, O(T) 시간이 걸린다.
     */

    for (n = 1; n <= MAX_N; n++)
        memoize[0][n] = n;
    for (k = 1; k <= MAX_K; k++)
        memoize[k][1] = 1;

    for (k = 1; k <= MAX_K; k++) {
        for (n = 2; n <= MAX_N; n++) {
            memoize[k][n] = memoize[k][n-1] + memoize[k-1][n];
        }
    }

    for (scanf("%d", &T); T > 0; T--) {
        scanf("%d %d", &k, &n);
        printf("%d\n", memoize[k][n]);
    }

    return 0;
}
