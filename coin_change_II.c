#include <stdio.h>
#include <stdlib.h>

int change(int amount, int* coins, int coinsSize) {
    int** dp = (int**)malloc((coinsSize + 1) * sizeof(int*));
    for (int i = 0; i <= coinsSize; i++) {
        dp[i] = (int*)calloc(amount + 1, sizeof(int));
    }
    // base case: Amount --> 0
    for (int i = 0; i < coinsSize; i++) dp[i][0] = 1;

    for (int i = coinsSize - 1; i >= 0; i--) {
        for (int amt = 1; amt <= amount; amt++) {
            // Not take current index
            int not_take = dp[i + 1][amt];

            // if I take current index
            int take = 0;
            if (coins[i] <= amt)
                take = dp[i][amt - coins[i]];

            dp[i][amt] = (take + not_take);
        }
    }
    int result = dp[0][amount];
    for (int i = 0; i <= coinsSize; i++) free(dp[i]);
    free(dp);
    return result;
}