from __future__ import print_function
import time
import ynab
from ynab.rest import ApiException
from pprint import pprint
import json

def dumper(obj):
    try:
        return obj.toJSON()
    except:
        return obj.__dict__

# Configure API key authorization: bearer
configuration = ynab.Configuration()

try: 
    with open('api_key') as f:
        configuration.api_key['Authorization'] = f.read().rstrip("\n")
        print(configuration.api_key)
        f.close()
except FileNotFoundError as e:
    print("Exception %s" % e)

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
configuration.api_key_prefix['Authorization'] = 'Bearer'
# create an instance of the API class
api_instance = ynab.AccountsApi()
budgets_instance = ynab.BudgetsApi()

budget_id = 'budget_id_example' # str | The ID of the Budget.
account_id = 'account_id_example' # str | The ID of the Account.

#budgets = '{}' #json response
#
try:
    # Single account
    # api_response = api_instance.get_account_by_id(budget_id, account_id)
    budgets = budgets_instance.get_budgets()
    # pprint(api_response)
    pprint(budgets)
except ApiException as e:
    print("Exception when calling ynab budgets Api %s\n" % e)


try:
    #buddict = json.dumps(budgets, default=vars, indent=4)
    print(type(budgets))
    budgets_dict = json.dumps(budgets, default=dumper, indent=2)
    pprint(budgets_dict)
    pprint(type(budgets_dict))
except Exception as e:
    print("Exception %s\n" % e)
