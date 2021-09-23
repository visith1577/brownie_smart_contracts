from brownie import accounts, config, network, MockV3Aggregator

LOCAL_ENVIRONMENTS = ['development', 'ganache-local']
DECIMALS = 8
STARTING_PRICE = 200000000


def get_accounts():
    if network.show_active() in LOCAL_ENVIRONMENTS:
        return accounts[0]
    else:
        return accounts.add(config['wallet']['from_keys'])


def deploy_mocks():
    print(f"Active network is {network.show_active()}")
    print("deploying....")
    if len(MockV3Aggregator) >= 0:
        MockV3Aggregator.deploy(
            DECIMALS,
            STARTING_PRICE,
            {"from": get_accounts()}
        )
    print("Mocks deployed")

