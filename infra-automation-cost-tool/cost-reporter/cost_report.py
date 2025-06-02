import os
from azure.identity import DefaultAzureCredential
from azure.mgmt.costmanagement import CostManagementClient
from datetime import datetime, timedelta

def main():
    subscription_id = os.environ.get('AZURE_SUBSCRIPTION_ID')
    if not subscription_id:
        raise Exception('Set AZURE_SUBSCRIPTION_ID environment variable')

    credential = DefaultAzureCredential()
    client = CostManagementClient(credential)

    end_date = datetime.utcnow().date()
    start_date = end_date - timedelta(days=7)

    scope = f'/subscriptions/{subscription_id}'
    query = {
        'type': 'Usage',
        'timeframe': 'Custom',
        'timePeriod': {
            'from': str(start_date),
            'to': str(end_date)
        },
        'dataset': {
            'granularity': 'Daily',
            'aggregation': {
                'totalCost': {
                    'name': 'PreTaxCost',
                    'function': 'Sum'
                }
            }
        }
    }

    result = client.query.usage(scope, query)
    print('Cost report for last 7 days:')
    for row in result.rows:
        print(row)

if __name__ == '__main__':
    main()
