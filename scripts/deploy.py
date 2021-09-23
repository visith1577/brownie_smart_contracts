from brownie import FundMe, network, config, MockV3Aggregator
from scripts.helpful_scripts import get_accounts, deploy_mocks, LOCAL_ENVIRONMENTS


def deploy_fund_me():
    account = get_accounts()
    if network.show_active() not in LOCAL_ENVIRONMENTS:
        price_feed_address = config['networks'][network.show_active()]['eth_usd_price_feed']

    else:
        deploy_mocks()
        price_feed_address = MockV3Aggregator[-1].address
    fund_me = FundMe.deploy(
        price_feed_address,
        {"from": account},
        publish_source=config['networks'][network.show_active()].get("verify")
    )
    print(f"FundMe deployed to {fund_me.address}")


def main():
    deploy_fund_me()