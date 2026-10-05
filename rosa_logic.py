"""Calculation logic reused from 722_a1.ipynb (Part 2)."""

import numpy as np
from starter import delivery_times


def late_order_cost(costs):
    refund = costs["refund"]
    churn_orders = costs["churn_orders"]
    margin = costs["margin"]

    total_cost = refund + churn_orders * margin

    return total_cost


def best_promise(zone, time_block, promises, costs):

    best_time = None
    best_profit = float("-inf")

    for promise in promises:
        times = delivery_times(
            zone, time_block, promise, seed=1
        )

        number_of_orders = len(times)
        number_of_late_orders = np.sum(times > promise)

        order_profit = number_of_orders * costs["margin"]
        late_cost = number_of_late_orders * late_order_cost(costs)

        net_profit = order_profit - late_cost

        if net_profit > best_profit:
            best_profit = net_profit
            best_time = promise

    return best_time, best_profit
