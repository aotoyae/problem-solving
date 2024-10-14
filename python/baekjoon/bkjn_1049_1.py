import sys
sys.stdin = open('input.txt', 'r')
# input = sys.stdin.readline

N, M = map(int, input().split())
package_lst = []
piece_lst = []

for _ in range(M):
    package, piece = map(int, input().split())
    package_lst.append(package)
    piece_lst.append(piece)

package = min(package_lst)
piece = min(piece_lst)

money = min(N // 6 * package + N % 6 * piece, (N // 6 + 1) * package, N * piece)


print(money)
